# Creating nested if for books

print("What type of cover does the book have?")

cover_type = str(input())

if cover_type == 'soft':
    print("Is the book perfect-bound?")
    perfect_bound = str(input())

    if perfect_bound == 'yes':
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")


elif cover_type == 'hard':
    print("Books with hard covers can be more expensive!")






