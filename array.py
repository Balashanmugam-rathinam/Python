# num = [1,2,1]

# for i in num.copy():
#     num.append(i)
# print(num)
# from typing import List
# def getarr(x,nums: List[int]) -> List[int]:
#     ans = []
#     for i in range(x):
#         for n in nums:
#             ans.append(n)
#     return ans

# print(getarr(3,[1,2,3]))
# def pos(n):
#     ## Write the code
#     for i in range(n+1):
#         if n == 0:
#             return "already Zero"
#         elif n > 0:
#             n -= 1
#         print(n,end=' ')
# pos(3)
def pos(n):
    ## Write the code
        if n == 0:
            print("already Zero")
        while n > 0:
            n -= 1
            print(n,end=' ')
def neg(n):
    ##Write the code
        if n == 0:
            print("already Zero")
        while n < 0:
            n += 1
            print(n,end=' ')
            
pos(4)