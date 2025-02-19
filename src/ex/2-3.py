# #2-3
# name = str(input("Type name: "))
# print(f"Hello {name}, would you like to learn some Python today?")

# #2-4
# name = str(input("Type name: "))
# print(f"{name.lower()}, {name.upper()} and {name.title()}")

# # 3-1 
# friends = ["Alex", "Damien", "Jinze"]
# print(f"{friends[0]}")
# print(f"{friends[1]}")
# print(f"{friends[2]}")

# # 3-2
# friends = ["Alex", "Damien", "Jinze"]
# print(f"{friends[0]} come stai?")
# print(f"Hi my name is {friends[1]}")
# print(f"{friends[2]} im chinese")

# 3-3

# # 3-4/ 3-5
# invited = ["LeBron", "Michael Jackson", "Kobe"]
# print(f"{invited[0]}, you are invited!")
# print(f"{invited[1]}, you are invited!")
# print(f"{invited[2]}, you are invited!")

# print(f"{invited[1]} can't make it.")

# invited[1] = "Gugu"
# # invited.remove(invited[1])

# print(f"{invited[0]}, you are invited!")
# print(f"{invited[1]}, you are invited!")

# # 3-8
# places = ["Madrid", "Rome", "Bern", "Paris"]
# print(places)

# x = sorted(places)
# print(x)
# print(places)

# y = sorted(places, reverse=True)
# print(y)
# print(places)

# places.reverse()
# print(places)

# places.reverse()
# print(places)

# places.sort()
# print(places)

# places.sort()
# places.reverse()
# print(places)

# lista = ["LeBron", "Gugu"]
# for item in lista:
#     print(f"{item} ur invited!")

# for i in range(1, 11):
#     if i%2==0:
#         continue
#     print(i)


# # 6-1 
# person:dict = {"first_name":"Alex", "last_name":"Samoila", "age": 19, "city": "Rome"}

# print(person["first_name"])
# print(person["last_name"])
# print(person["age"])
# print(person["city"])

# # 3-10
# mountains = {"India":["Kangchenjunga","Doddabetta Peak","Saltoro Kangri"], "Nepal":["Mount Everest"], "Pakistan":["K2"]}
# # print(mountains["India"][0]) # Access item inside list of a dict key
# # print(mountains["Pakistan"][0]) 

# # for key, value in mountains.items():
# #     for i in value:
# #         print(i)

# for i in mountains["India"]:
#     print(i)