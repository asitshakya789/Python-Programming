# def ispalindrome (s):
#     return s == s [::-1]

# s = "asit"
# ans = ispalindrome(s)
# if ans :
#     print("yes")
# else:
#     print("no")
    


num = 761
rev = int(str(num)[::-1])
if num==rev:
    print("yes")
else:
    print("no")