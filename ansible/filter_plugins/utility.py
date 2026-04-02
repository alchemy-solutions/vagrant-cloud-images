import re
import urllib.request
import urllib.parse

from datetime import datetime
from html.parser import HTMLParser
from typing import NamedTuple

try:
    from ansible.errors import AnsibleFilterError
except ImportError:
    AnsibleFilterError = Exception


class SemanticVersion:
    version = []
    build = None

    def __init__(self, text, sep='.', build_sep='-'):
        assert isinstance(text, str), "Initial value of wrong type"
        version, self.build, *_ = text.split(build_sep) + [None]
        self.version = [int(number) for number in version.split(sep)]
        while len(self.version) < 3:
            self.version.append(0)

    def __repr__(self):
        version = '.'.join([str(number) for number in self.version])
        if self.build is None:
            return version
        else:
            return f"{version}-{self.build}"


class AnchorLinkExtractor(HTMLParser):
    def __init__(self, base_url, pattern):
        super().__init__()
        self.base_url = base_url
        self.links = set()
        try:
            self.regex = re.compile(pattern)
        except re.error as e:
            raise AnsibleFilterError(f"Invalid regex: {e}")

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            for attr, value in attrs:
                if attr.lower() == "href":
                    if self.regex.search(value):
                        self.links.add(value)


class FilterModule(object):
    def filters(self):
        return {
            'is_expired': self.is_expired,
            'shell_escape': self.shell_escape,
            'get_checksum': self.get_checksum,
            'get_links': self.get_links,
            'get_latest_version': self.get_latest_version,
            'semantic_version': self.semantic_version
        }

    def is_expired(self, str_date=None):
        if not str_date:
            return False
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        try:
            (month, year) = str_date.split(' ')
            month = month.lower()
            year = int(year)
            assert len(month) >= 3
            month = next((i+1 for i, value in enumerate(months) if value.startswith(month)))
        except Exception as e:
            raise AnsibleFilterError(f"Date string '{str_date}' does not respect compact form 'MMM YYYY' (e.g. 'Oct 1974')")
        return f"{year}-{month:02}" < datetime.today().strftime('%Y-%m')

    def shell_escape(self, shell_string):
        escaped_string = ''
        for char in shell_string:
            if char in ['\\', '"']:
                escaped_string += '\\'
            escaped_string += char
        return escaped_string

    def get_checksum(self, text, filename=None, algorithm=''):
        # TODO: GPG check
        algorithms = ['md5', 'sha1', 'sha256', 'sha512']
        if algorithm and algorithm not in algorithms:
            raise AnsibleFilterError(f"Checksum algorithm '{algorithm}' not supported")
        lines = text.splitlines()
        lines = [line for line in lines if not line.startswith('#')]
        re_chk = [
            re.compile(r'\w+\s+\(\S+\)\s+=\s+([0-9a-fA-F]+)'),  # BSD
            re.compile(r'([0-9a-fA-F]+)\s+\S+'),  # GNU
            re.compile(r'([0-9a-fA-F]+)')
        ]
        if len(lines) > 1 and filename:
            lines = [
                line for line in lines
                if re.search(r'\b' + filename + r'\b', line)]
        if len(lines) == 0:
            raise AnsibleFilterError("No checksum found"+(f" for {filename}" if filename else ""))
        #if len(lines) != 1:
        #    raise AnsibleFilterError("Multiple checksums found")
        for chk in re_chk:
            if match := chk.fullmatch(lines[0]):
                return match.group(1)
        raise AnsibleFilterError("Uknown checksum format")

    def get_links(self, url, pattern=''):
        try:
            with urllib.request.urlopen(url) as response:
                content_type = response.headers.get("Content-Type", "")
                if "text/html" not in content_type:
                    raise AnsibleFilterError("Error: URL does not contain HTML content.")
                html = response.read().decode("utf-8", errors="ignore")
                parser = AnchorLinkExtractor(url, pattern)
                parser.feed(html)
                return sorted(parser.links)
        except Exception as e:
            raise AnsibleFilterError(f"Error: {e}")

    def get_latest_version(self, url, pattern=''):
        try:
            with urllib.request.urlopen(url) as response:
                content_type = response.headers.get("Content-Type", "")
                if "text/html" not in content_type:
                    raise AnsibleFilterError("Error: URL does not contain HTML content.")
                html = response.read().decode("utf-8", errors="ignore")
                parser = AnchorLinkExtractor(url, pattern)
                parser.feed(html)
                last = sorted(parser.links)[-1]
                version = parser.regex.search(last)
                return {k: v for k, v in version.groupdict().items() if v is not None}
        except Exception as e:
            raise AnsibleFilterError(f"Error: {e}")

    def semantic_version(self, text, major=None, minor=None, patch=None, build=None):
        ver = SemanticVersion(text)
        try:
            if major is not None:
                ver.version[0] = int(major)
            if minor is not None:
                ver.version[1] = int(minor)
            if patch is not None:
                ver.version[2] = int(patch)
        except Exception as e:
            raise AnsibleFilterError(f"Not integer components: {e}")
        if build is not None:
            ver.build = build
        return f"{ver}"
