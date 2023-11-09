#Area is x=550 by y=300
#reversed_list
pain = 0
WYSI = 162#Variable used for later (positioning of the pixels)

#Gradiants
gradiant = [['11111111', '11111111', '11111111'], ['11101011', '11111010', '11101011'], ['11010110', '11110101', '11010110'], ['11000010', '11110000', '11000010'], ['10101101', '11101011', '10101101'], ['10011001', '11100110', '10011001'], ['10000101', '11100000', '10000101'], ['01110000', '11011011', '01110000'], ['01011100', '11010110', '01011100'], ['01000111', '11010001', '01000111'], ['00110011', '11001100', '00110011'], ['00101110', '10111000', '00101110'], ['00101001', '10100011', '00101001'], ['00100100', '10001111', '00100100'], ['00011111', '01111010', '00011111'], ['00011001', '01100110', '00011001'], ['00010100', '01010010', '00010100'], ['00001111', '00111101', '00001111'], ['00001010', '00101001', '00001010'], ['00000101', '00010100', '00000101'], ['00000000', '00000000', '00000000']]

flagofNetherlands1=[['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'],['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0'], ['10001011', '0', '0']]
flagofNetherlands2=[['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'], ['11010011', '11010011', '11010011'],['11010011', '11010011', '11010011']] 
flagofNetherlands3=[['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111'],['00000000', '00000000', '11111111'],['00000000', '00000000', '11111111'],['00000000', '00000000', '11111111'],['00000000', '00000000', '11111111'], ['00000000', '00000000', '11111111']]


import turtle #Turtle module
t=turtle.Turtle()
t.hideturtle()
turtle.colormode(255) #Colormode 255 for RGB
decimal_numbers = []# Empty lists for later
combined_list = []
nested_list = []
print('Enter A to access Part One')
print('Enter B to access Part Two (Flag)')
response = input()
turtle.penup()
def BinarytoDecimal(binary): #Binary to Decimal code (last assignment)
  for sublist in binary:
    decimal_sublist = []
    for binary in sublist:
      decimal_sublist.append(int(binary, 2))
    decimal_numbers.append(decimal_sublist)

def LastDelete(binary): #Removes a bit from each
  for sublist in binary:
      for i, item in enumerate(sublist): #Separates the last character
          sublist[i] = item[:-1]


def AddBit(binary): #Adds "01" to each element of the list
  inner_list = []
  for inner_list in binary:
    for item in inner_list:
      combined_list.append(item)
  for i in range(len(combined_list)):
    combined_list[i] = combined_list[i] + '01'

if response == 'A' or response == 'a': #Nested selection for code
  print('Enter 1 to draw the original gradiant.')
  print('Enter 2 to remove one bit from each byte in the RGB.')
  print('Enter 3 to add 01 to each byte in the RGB.')
  print('Enter 4 to convert to RG Dichrome Palette.')
  print('Enter 5 to convert to GB Dichrome Palette.')
  print('Enter 6 to convert to RB Dichrome Palette.')
  response = input()
  count = 0
  if response == '1':
    print(gradiant)
    BinarytoDecimal(gradiant)#Converts binary to decimal
    turtle.goto(-210, WYSI)#Posistions at the top left
    
    while count < 17:#Loops until it goes all the way down the screen
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2])#Takes the RGB from the converted Binary code
        turtle.shape('square')#Shapes as a square to look like a pixel
        turtle.stamp()#Stamps current posistion
        turtle.forward(20)#Moves forward
      count = count + 1#Depends on how large screen is, but adds 1 to iteration for while loop
      WYSI -= 20#Subtract 20 for the Y, so it can go down 20 units
      turtle.goto(-210, WYSI)#Return to original posistion, 20 units down.
          
  elif response == '2':
    LastDelete(gradiant) #Deletes a bit function
    print(gradiant)#Same as seen in "If response == 1"
    BinarytoDecimal(gradiant)
    turtle.goto(-210, WYSI)
    while count < 17:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

  
  elif response == '3':
    AddBit(gradiant) #Adds '01' to the end of each element
    new_list = ''.join(combined_list) #Joins all list into 1
    longlist = new_list
    n = 8
    elements = [longlist[i:i+n] for i in range(0, len(longlist), n)] #Separates the string every 8 characters
    n = 3
    sublists = [elements[i:i+n] for i in range(0, len(elements), n)] #Separates the string every 3 elements
    gradiantV2 = sublists
    gradiantV3 = gradiantV2[:-3] 
    del gradiantV3[-3:]#Removes the last 3 elements from the list, to avoid errors
    print(gradiantV3)
    BinarytoDecimal(gradiantV3) #Same as first one
    turtle.goto(-210, WYSI)
    delete = 0
    while count < 17:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)


  elif response == '4':
    BinarytoDecimal(gradiant)#Same as first one, except for one change referenced later.
    turtle.goto(-210, WYSI)
    while count < 17:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2]**0)#Multiplies the B by 0, making it 0
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)
  elif response == '5':
    BinarytoDecimal(gradiant)#Same as first one, except for one change referenced later
    turtle.goto(-210, WYSI)
    while count < 17:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0]**0, decimal_numbers[i][1],decimal_numbers[i][2])#Multiplies the R in RGB by 0, making it 0
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)
  elif response == '6': 
    BinarytoDecimal(gradiant) #Same as first one, except for one changed referenced later
    turtle.goto(-210, WYSI)
    while count < 17:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1]**0,decimal_numbers[i][2])#Multiplies G in RGB by 0, making it 0.
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)
  else:
    print('You have made a typing error, please rerun the program')#Returns if invalid response


    
elif response == 'B' or response == 'b':
  print('Enter 1 to draw the flag')
  print('Enter 2 to convert to RG Dichrome Palette.')
  print('Enter 3 to convert to GB Dichrome Palette.')
  print('Enter 4 to convert to RB Dichrome Palette.')
  response = input()
  if response == '1':#Changing it to RG, GB, and RB format is exactly the same as seen in part A, so i'll only annotate this part.
    BinarytoDecimal(flagofNetherlands1) #converts the first part of the flag to decimal
    turtle.goto(-210, WYSI)
    count=0
    while count < 6: #Fills up 6 lines with color assigned
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

    decimal_numbers.clear()#Clears the current color
    BinarytoDecimal(flagofNetherlands2) #Converts the second part of the flag to decimal (Uses same posistioning variable)
    count = 0
    turtle.goto(-210, WYSI)
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

    decimal_numbers.clear() #Clears current color
    BinarytoDecimal(flagofNetherlands3) #Converts the last part of the flag into decimal
    count = 0
    turtle.goto(-210, WYSI)
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)


    
  elif response == '2':
    BinarytoDecimal(flagofNetherlands1)
    turtle.goto(-210, WYSI)
    count=0
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2]**0)
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

    decimal_numbers.clear()
    BinarytoDecimal(flagofNetherlands2)
    count = 0
    turtle.goto(-210, WYSI)
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2]**0)
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

    decimal_numbers.clear()
    BinarytoDecimal(flagofNetherlands3)
    count = 0
    turtle.goto(-210, WYSI)
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1],decimal_numbers[i][2]**0)
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)
  
  elif response == '3':
    BinarytoDecimal(flagofNetherlands1)
    turtle.goto(-210, WYSI)
    count=0
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0]**0, decimal_numbers[i][1],decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

    decimal_numbers.clear()
    BinarytoDecimal(flagofNetherlands2)
    count = 0
    turtle.goto(-210, WYSI)
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0]**0, decimal_numbers[i][1],decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

    decimal_numbers.clear()
    BinarytoDecimal(flagofNetherlands3)
    count = 0
    turtle.goto(-210, WYSI)
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0]**0, decimal_numbers[i][1],decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

  
  
  
  elif response == '4':
    BinarytoDecimal(flagofNetherlands1)
    turtle.goto(-210, WYSI)
    count=0
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1]**0,decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

    decimal_numbers.clear()
    BinarytoDecimal(flagofNetherlands2)
    count = 0
    turtle.goto(-210, WYSI)
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1]**0,decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)

    decimal_numbers.clear()
    BinarytoDecimal(flagofNetherlands3)
    count = 0
    turtle.goto(-210, WYSI)
    while count < 6:
      for i in range(len(decimal_numbers)):
        turtle.color(decimal_numbers[i][0], decimal_numbers[i][1]**0,decimal_numbers[i][2])
        turtle.shape('square')
        turtle.stamp()
        turtle.forward(20)
      count = count + 1
      WYSI -= 20
      turtle.goto(-210, WYSI)
  else:
    print('You have made a typing error, please rerun the program.')


else:
  print('You have made a typing error, please rerun the program.')#Returns if invalid response

