class Solution(object):
    unit_strs = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    decade_strs = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundred_strs = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousand_strs = ["", "M", "MM", "MMM"]

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousand = num / 1000
        hundred = (num % 1000) / 100
        decade = (num % 100) / 10
        unit = num % 10
        return "%s%s%s%s" % (
            self.thousand_strs[thousand],
            self.hundred_strs[hundred],
            self.decade_strs[decade],
            self.unit_strs[unit]
        )
