#user input for height and credits

height = int(input('What is your height in cm? '))
credits = int(input('How many credits do you have? '))
with_taller_person = str(input('Are you with a taller person? (Enter True or False) '))

if credits < 10:
    print('You dont have enough credits to ride the Cyclone')
elif height >= 137 and credits >= 10:
    print('Enjoy the ride!')
elif height < 137:
    if height < 100 or not with_taller_person:
        print('You are not tall enough for the Cyclone yet.')
    elif height >= 100 and with_taller_person:
        print('Enjoy the ride, folks!')
else:
    print('Invalid data.')