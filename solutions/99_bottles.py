<<<<<<< HEAD
def Print_Lyrics(number: int):
    if number != 0 & number != 1:
        print(str(number) + " bottles of beers on the wall, " + str(number) + 
              " bottles of beers.\n" +
              "Take one down and pass it around, " + 
              str((number - 1)) + 
              " bottles of beer on the wall.\n")
    elif number == 1:
         print(str(number) + " bottle of beer on the wall, " + str(number) + 
              " bottle of beers.\n" +
              "Take one down and pass it around, " + 
              str((number - 1)) + 
              " No more bottles of beer on the wall.\n")
    else:
        print("No more bottles of beer on the wall, " +  
              "No more bottles of beers.\n" +
              "Go to the store and buy some more, " + 
              "99" + 
              " bottles of beer on the wall.\n")

for number in range(99, -1, -1):
    Print_Lyrics(number)
=======
def Print_Lyrics(number: int):
    if number != 0 & number != 1:
        print(str(number) + " bottles of beers on the wall, " + str(number) + 
              " bottles of beers.\n" +
              "Take one down and pass it around, " + 
              str((number - 1)) + 
              " bottles of beer on the wall.\n")
    elif number == 1:
         print(str(number) + " bottle of beer on the wall, " + str(number) + 
              " bottle of beers.\n" +
              "Take one down and pass it around, " + 
              str((number - 1)) + 
              " No more bottles of beer on the wall.\n")
    else:
        print("No more bottles of beer on the wall, " +  
              "No more bottles of beers.\n" +
              "Go to the store and buy some more, " + 
              "99" + 
              " bottles of beer on the wall.\n")

for number in range(99, -1, -1):
    Print_Lyrics(number)
>>>>>>> 81ea21cc94d5f32a0644d1b800ba999bf5b14184
