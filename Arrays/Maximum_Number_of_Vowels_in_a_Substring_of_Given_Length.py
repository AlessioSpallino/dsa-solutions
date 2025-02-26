class Solution(object):
    def maxVowels(self, s, k):
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        vowel_n = 0

        for i in range(0, k):
            letter = s[i]
            right = i
            if letter in vowel_set:
                vowel_n+=1

        left = 0
        
        count = vowel_n
        for right in range(k, len(s)): 
            left_letter = s[left]
            right_letter = s[right]

            if left_letter in vowel_set:
                count-=1
            if right_letter in vowel_set:
                count+=1

            left+=1
            vowel_n = max(vowel_n, count)

        return vowel_n