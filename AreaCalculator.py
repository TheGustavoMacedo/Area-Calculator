import math

print('=' * 18)
print('Area Calculator 📐')
print('=' * 18)

while True:
  choice = int(input('Choose a shape:\n1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\nType here: '))
  if choice == 1:
    print('')
    Base = int(input('Base: '))
    Height = int(input('Height: '))
    Area  = (Height * Base) / 2
    print('The area is:', Area)
    print('')
  elif choice == 2:
    print('')
    Length = int(input('Length: '))
    Width = int(input('Width: '))
    Area = Length * Width
    print('The area is:', Area)
    print('')
  elif choice == 3:
    print('')
    Side = int(input('Side: '))
    Area = Side**2
    print('The area is:', Area)
    print('')
  elif choice == 4:
    print('')
    Radius = int(input('Radius: '))
    Area = math.pi * Radius**2
    print('The area is:', Area)
    print('')
  elif choice == 5:
    print('')
    print('Quiting...')
    break
  else: ('Invalid choice, try again.')


