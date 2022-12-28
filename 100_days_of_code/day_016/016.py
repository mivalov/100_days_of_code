# Day 16: Endless loop

print('Fill in the black lyrics!')
print(25 * '=')

print('Type in the blank lyrics and see if you are as cool as me.')
print()

counter = 0
while True:
    counter += 1
    print('Never gonna _______ you up.')
    word = input().strip().lower()
    if word == 'give':
        break
    else:
        print('Nope, try again. (:')

print(f'You did it! It only took you {counter} attempts.')
