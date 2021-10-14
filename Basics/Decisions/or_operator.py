# making beep follow paths

print("What type of adventure should I have?")

journey = str(input())

if (journey == 'scary') or (journey == 'short'):
    print('Entering the dark forest!')
elif (journey == 'safe') or (journey == 'long'):
    print('Not sure which route to take.')
else:
    print("Not sure which route to take.")
