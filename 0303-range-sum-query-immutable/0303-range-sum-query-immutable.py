class NumArray(object):

    def __init__(self, nums):
        self.prefix = [0]

        for number in nums:
            self.prefix.append(self.prefix[-1] + number)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]