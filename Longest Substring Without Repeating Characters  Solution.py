class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #一個字一個字加到list若有重複 index + 1
        list = []
        max_length = 0
        for x in s:
            if x in list:
                list = list[list.index(x)+1:]   # sliding windows
            list.append(x)     # else not in 1不重複就append
            max_length = max(max_length, len(list))
           
        return max_length
        
        
        '''
s = "pwwkew"

['p']
['p', 'w']
['w']
['w', 'k']
['w', 'k', 'e']
['k', 'e', 'w']

        '''
