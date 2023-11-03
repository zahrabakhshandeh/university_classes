# Strings "", ''
str1 = "hi python"
# index 012345678
#             -3-2-1
print(str1)
print(str1[0])
print(str1[-1])
#print(str1[10]) IndexError
# Slicing
str1 = "hi python!"
#index  0123456789
sub_str = str1[3:9] # 3, 4, 5, 6, 7, 8
print(sub_str)
sub_str = str1[3:9:2] # 3, 5, 7
print(sub_str)
# [start:stop:step]
# start : def ===> 0 (start of str)
# stop : def ===> end of str
# step : def ===> 1
str1 = "hi python!"
"""print(str1[:])
print(str1[::3])
print(str1[::-1])"""
# Points
str1 = "hi python!"
# index 0123456789
# length ===> len()
l = len(str1)
#print(l)
# +, *
# + ====> all of them be str
print("-"*50)
st1 = "hi "
st2 = "python"
st3 = "3"
new_st = st1 + st2 + st3
print(new_st)
# * ===> must be int and str
st1 = "python \n"
new_st = st1 * 3
print(new_st)