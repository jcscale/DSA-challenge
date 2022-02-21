class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        number = nums[:]
        count = 0
        try:
            # hi = number.index(target)-1
            # low = number.index(target)

            while number[0] != target:
                num_pop = number.pop(0)
                number.append(num_pop)
                count += 1
            return count
        except:
            return -1
