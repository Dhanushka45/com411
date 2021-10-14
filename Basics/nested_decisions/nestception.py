# Creating a complicated if statement


print("Where should I look?")

place = str(input())

if place == "room":
    print("Where in the bedroom should I look?")
    in_room = str(input())
    if in_room == 'under the bed':
        print("Found some shoes but no battery.")
    else:
        print("Found some mess but no battery.")
elif place == 'bathroom':
    print("Where in the bathroom should I look?")
    in_bathroom = str(input())
    if in_bathroom == 'bathtub':
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")
elif place == 'lab':
    print("Where in lab should I look?")
    in_lab = str(input())
    if in_lab == 'table':
        print('Yes! I found my battery!')
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking.")


