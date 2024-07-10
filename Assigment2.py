# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#        print(j,end="")
#     print()

# # *
# # **
# # ***
# # ****
# # *****
# # ******

# for i in range(1,7):
#      for j in range(1,i+1):
#         print('*',end="")
#      print()

#>>>>>>>>>>>>>>>>Question 3
ls=[2,-7,-55,45,32,66,77,4,1,77,9,98]

max=-9678698687
min=9687268767

for i in ls:
    if i>max:
        max=i
    elif i<min:
        min=i
print(min)
print(max)

