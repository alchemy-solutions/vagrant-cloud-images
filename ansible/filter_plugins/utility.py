import re
import urllib.request
import urllib.parse

from datetime import datetime
from html.parser import HTMLParser

try:
    from ansible.errors import AnsibleFilterError
except ImportError:
    AnsibleFilterError = Exception


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
            'get_latest_version': self.get_latest_version
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
            month = next((i for i, value in enumerate(months) if value.startswith(month)))
        except Exception as e:
            raise AnsibleFilterError(
                "Date string '%s' does not respect compact form 'MMM YYYY' (e.g. 'Oct 1974')"
                % str_date)
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
            raise AnsibleFilterError(
                "Checksum algorithm '%s' not supported" % algorithm)
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
            raise AnsibleFilterError("No checksum found")
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
                return version.groupdict()
        except Exception as e:
            raise AnsibleFilterError(f"Error: {e}")
