class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        one = 0
        two = 0
        for i in range(len(a)):
            if a[i] == 0:
                zero += 1
            elif a[i] == 1:
                one += 1
            else:
                two += 1
        index = 0
        while zero > 0:
            a[index] = 0
            index += 1
            zero -= 1
        while one > 0:
            a[index] = 1
            index += 1
            one -= 1
        while two > 0:
            a[index] = 2
            index += 1
            two -= 1