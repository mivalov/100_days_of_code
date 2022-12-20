# Day 8: Affirmation generator

print("Hi! Welcome to your daily affirmation generator.")
name = input("What is your name? ")

if name.lower() in ['mark', 'john', 'peter', 'mia', 'sofia', 'norah']:
    day = input("What day of the week is it today? ").lower()
    if day == 'monday':
        print(name, "it's time to solve the Monday's challenges!")
    elif day == 'tuesday':
        print(
            name,
            ", you're strong enough to handle "
            "anything Tuesday throws your way.",
            sep=''
        )
    elif day == 'wednesday':
        print('Some miracle will touch your life this Wednesday,', name)
    elif day == 'thursday':
        print(name, ', your Thursday looks promising!', sep='')
    elif day == 'friday':
        print('Congratulations ', name,
              '! You finally reached Friday!', sep='')
else:
    print("I do not know your name, but I hope you are having a great day!")
