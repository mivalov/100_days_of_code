# Day 5: If statements

print(10 * '=', 'Marvel Movie Character Creator', 10 * '=')
print(52 * '-')
positive_answers = ['yes', 'yep', 'yeah', 'y', 'of course']

hanging_around = input("Do you like a 'hanging around'? ")
if hanging_around.lower() in positive_answers:
    print('You are Spider Man!')
else:
    print("Then you're not Spider-man")

    gravelly_voice = input("Do you like a 'hanging around'? ")
    if gravelly_voice.lower() in positive_answers:
        print("You are Korg")
    else:
        print("Aww, then you're not Korg")

        marvelous = input("Do you often feel 'Marvelous'? ")
        if marvelous.lower() in positive_answers:
            print("Aha! You're Captain Marvel! Hi!")
        else:
            print('Who are you?')
