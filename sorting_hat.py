#house names to capture score
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#Question 1

print('Q1) Do you like Dusk or Dawn?')
print('   1) Dawn')
print('   2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input.')

#Question 2

print('Q2) When I\'m dead, I want people to remember me as: ')
print('   1) The Good')
print('   2) The Great')
print('   3) The Wise')
print('   4) The Bold')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    hufflepuff += 1
elif answer == 2:
    slytherin += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:    
    gryffindor += 1
else:
    print('Wrong input.')

#Question 3

print('Q3) Which kind of instrument most pleases your ear? ')
print('   1) The violin')
print('   2) The trumpet')
print('   3) The piano')
print('   4) The drum')

answer = int(input('Enter answer (1-4): '))

if answer == 1:
    slytherin += 1
elif answer == 2:
    hufflepuff += 1
elif answer == 3:
    ravenclaw += 1
elif answer == 4:    
    gryffindor += 1
else:
    print('Wrong input.')

#Points Summary

print(str('Gryffindor: ') + str(gryffindor))
print(str('Ravenclaw: ') + str(ravenclaw))
print(str('Hufflepuff: ') + str(hufflepuff))
print(str('Slytherin: ') + str(slytherin))

#Sorting Ceremony: Final House

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if gryffindor == most_points:
  print('The Sorting Hat calls 🦁 Gryffindor!')
elif ravenclaw == most_points:
  print('The Sorting Hat calls 🦅 Ravenclaw!')
elif hufflepuff == most_points:
  print('The Sorting Hat calls 🦡 Hufflepuff!')
else:
  print('The Sorting Hat calls 🐍 Slytherin!')