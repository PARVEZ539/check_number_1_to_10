def choise_num():
  choises = "Wrong"
  initial_value = [0,1,2,3,4,5,6,7,8,9,10]
  while choises.isdigit() == False:
    choise = input("Please enter a number(0-10): ")
    if choise.isdigit() == False:
      print("Sorry that is not a number")
    else:
      choises = choise
      if int(choises) not in initial_value:
        print("Sorry, you did not enter a number between 0 and 10")
        choises = "Wrong"
  return choises

print("You enter a right value "+choise_num() + " and it is a number. Thank you boss 🥰")