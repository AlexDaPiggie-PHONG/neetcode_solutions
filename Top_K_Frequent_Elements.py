class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        final_lst = []
        result = []
        sorted_lst = []
        doodoo ={}
        for num in nums:
            if num not in doodoo:
                doodoo[num] = 1
            else:
                doodoo[num] += 1
        
        # print ("DEBUG: Final Dictionary:", doodoo)
        for i in range (1, len(nums) + 1):
            sub_list = []
            for key in doodoo.keys():
                if doodoo[key] == i:
                    sub_list.append(key)
            if len(sub_list) != 0:
                sorted_lst.append(sub_list)
    
        # print ("DEBUG: Sorted List:", sorted_lst)
        for sub_element in sorted_lst:
            for element in sub_element:
                final_lst.append(element)
        
        for i in range (k):
            result.append(final_lst[-i-1])
        
        return result

solulu = Solution()
nums=[7,7]
k=1
print (solulu.topKFrequent(nums, k))
        