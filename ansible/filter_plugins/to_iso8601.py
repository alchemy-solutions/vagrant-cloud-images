try:
    from ansible.errors import AnsibleFilterError
except ImportError:
    AnsibleFilterError = Exception

class FilterModule(object):
    def filters(self):
        return {
            'to_iso8601': self.to_iso8601
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
                "Date string '%s' does not respect compact form 'Month Year' (e.g. 'Oct 1974')"
                % str_date)
        return f"{year}-{month:02}-00T00:00:00Z"
