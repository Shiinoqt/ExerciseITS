animals:list[str] = ["dog","cat","horse"]

# for elem in animals:
#     if i == animals[0]:
#         print(f"A {i} would be an amazing pet!")
#     elif i == animals[1]:
#         print(f"A {i} is also an amazing pet!!")
#     else:
#         print(f"A {i} is also an amazing pet!!!")   

'''This uses the range function, useful when we use two lists.'''
# for i in range(0,len(animals)): 
#     print(animals[i])

for i in animals:
    print(f"There is a {i}.")
print("Each of them is a mammals!")


    