class Solution:
    def isValid(self, word: str) -> bool:

        def len_check(s):
            return len(s) >= 3

        def char_check(s):
            words = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
            for x in range(len(s)):
                if s[x] in words:
                    continue
                else:
                    return False

            return True

        def vowel_check(s):
            words = 'aeiouAEIOU'
            for x in range(len(s)):
                if s[x] in words:
                    return True
            return False

        def consonant_check(s):
            words = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
            for x in range(len(s)):
                if s[x] in words:
                    return True

            return False


        return len_check(word) and char_check(word) and vowel_check(word) and consonant_check(word)
        
