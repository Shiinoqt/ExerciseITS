def make_album(name:str, title:str, tracks:int = None):
    album: dict = {"Artist": name, "Title": title}
    if tracks:
        album["Tracks"] = tracks
    return album

# album = make_album("miao","bau")
# print(album["Artist"])

while True:
    
    name = str(input("Enter artist name: "))
    
    if name == "quit":
        break

    title = str(input("Enter album title: "))

    print(make_album(name, title))

