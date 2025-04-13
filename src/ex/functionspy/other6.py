def make_album(name:str, title:str, tracks:int = None):
    album: dict = {"Artist": name, "Title": title}
    if tracks:
        album["Tracks"] = tracks
    return album

# album = make_album("miao","bau")
# print(album["Artist"])

print(make_album("Kenia OS", "Malas Decisiones", 1))

print(make_album("KISS OF LIFE", "Sticky"))

print(make_album("Jordan Adetunji", "KEHLANI"))

print(make_album("Jordan Adetunji", "KEHLANI"))