# messages = ["Hi!","Hello!","How are you?"]
sent_messages = []

def show_messages(urlist):
    print("Showing all your messages: ")
    for elem in urlist:
        print(elem)

# show_messages(messages)


def send_messages(urlist):
    print(f"\nYour current messages: \n{urlist}")

    backuplist = list(urlist)
    full = len(urlist)

    for i in urlist:
        sent_messages.append(i)
    
    for i in range(full):
        urlist.pop(0)

    print(f"\nYour sent messages: \n{sent_messages}")
    print(f"\nYour current messages: \n{urlist}")
    print(f"\nYour old messages: \n{backuplist}")

# send_messages(messages)

