# Finding out which direction the paint brush moves

print("Towards which direction should I paint (up, down, left or right)?")

direction = str(input())

if direction == "up":
    print("I am painting in the upward direction!")
elif direction == "down":
    print("I am painting in the downward direction!")
elif direction == "left":
    print("I am painting in the left direction!")
else:
    print("I am painting in the right direction!")