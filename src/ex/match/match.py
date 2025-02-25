# while True:
#     n = int(input("Insert position: "))
#     if n == 1:
#         print(f"{n}st")
#     elif n == 2:
#         print(f"{n}nd")
#     elif n == 3:
#         print(f"{n}rd") 
#     else: 
#         print(f"{n}th") 

# n = int(input("Insert position: "))
# match n:
#     case 1:
#         print(f"{n}st")
#     case 2:
#         print(f"{n}nd")
#     case 3:
#         print(f"{n}rd")
#     case _:
#         print(f"{n}th")

http_status = 500
match http_status:
    case 200|201:
        print("Success")
    case 404:
        print("Not Found")
    case 500|501:
        print("Server Error")