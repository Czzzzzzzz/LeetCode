import heapq

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for char in s:
            if char in dic:
                dic[char] = dic[char] + 1
            else:
                dic[char] = 1
        
        sorted_dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)        
        
        sortedChars = ""
        for key, num in sorted_dic:
            sortedChars += key * num
            
        return sortedChars
    
if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("tree"))
    