import re

try:
    from ansible.errors import AnsibleFilterError
except ImportError:
    AnsibleFilterError = Exception


class FilterModule(object):
    def filters(self):
        return {
            'to_iso8601': self.to_iso8601,
            'shell_escape': self.shell_escape,
            'get_checksum': self.get_checksum
        }


    def to_iso8601(self, str_date):
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        try:
            (month, year) = str_date.split(' ')
            month = month.lower()
            year = int(year)
            assert len(month) >= 3
            month = next((i for i, value in enumerate(months) if value.startswith(month)))
            if month == 11:
                month = 1
                year += 1
            else:
                month += 2
        except Exception as e:
            raise AnsibleFilterError(
                "Date string '%s' does not respect compact form (e.g. 'Oct 1974')"
                % str_date)
        return f"{year}-{month:02}-00T00:00:00Z"


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
        if filename:
            lines = [
                line for line in lines
                if re.search(r'\b' + filename + r'\b', line)]
        if len(lines) == 0:
            raise AnsibleFilterError("No checksum found")
        if len(lines) != 1:
            raise AnsibleFilterError("Multiple checksums found")
        re_chk = [
            re.compile(r'\w+\s+\(\S+\)\s+=\s+([0-9a-fA-F]+)'),  # BSD
            re.compile(r'([0-9a-fA-F]+)\s+\S+'),  # GNU
            re.compile(r'([0-9a-fA-F]+)')
        ]
        checksum = None
        for chk in re_chk:
            if match := chk.fullmatch(lines[0]):
                return match.group(1)
        raise AnsibleFilterError("Uknown checksum format")
