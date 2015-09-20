class Solution(object):
    digits_letter_map = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def _bleach_one(self, string):
        bleached = ""
        for char in string:
            if char == "1":
                continue
            else:
                bleached += char
        return bleached

    def _combine(self, list1, list2):
        if len(list1) == 0:
            return list2
        if len(list2) == 0:
            return list1
        combined_list = []
        for items1 in list1:
            for items2 in list2:
                combined_list.append(items1 + items2)
        return combined_list

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        bleached = self._bleach_one(digits)
        if len(bleached) == 0:
            return []
        cache = {}
        max_cache_len = 0
        i = 0
        current_string = ""
        while i < len(bleached):
            if max_cache_len == 0:
                cache[bleached[i]] = self.digits_letter_map[bleached[i]]
                max_cache_len = 1
                current_string = bleached[i]
                i += 1
            else:
                j = min(i + max_cache_len, len(bleached))
                while j > i and not cache.get(bleached[i:j]):
                    j -= 1

                if j == i:
                    new_combination = self._combine(cache[current_string], self.digits_letter_map[bleached[i]])
                    current_string += bleached[i]
                    cache[current_string] = new_combination
                    i += 1
                else:
                    new_combination = self._combine(cache[current_string], cache[bleached[i:j]])
                    current_string += bleached[i:j]
                    cache[current_string] = new_combination
                    i = j
        return cache[current_string]
