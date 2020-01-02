def sumOfNum(nums):
    x = 0
    def GetVal(number):
        try:
            int(number)
            if int(number) % 2 == 1:
                return int(number)**2
            return 0
        except:
            return 0
    if type(nums) is list:
        for n in nums:
           x += GetVal(n)
        return x
    else:
        return "Invalid input"
print(sumOfNum([1,5,-3,5,9,8,4]))
