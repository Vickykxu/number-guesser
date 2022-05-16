
possibleNums = []
higherOrLower = []
multipleOf = []
temp = []

validAns = False

for i in range(1,101):
    possibleNums.append(i)


def isEven(list):
  temp = []
  listLength = len(possibleNums) + 1
  for num in range(listLength):
    if num%2 == 0:
      temp.append(num)
  return temp
def isOdd(list):
  temp = []
  listLength = len(possibleNums) + 1
  for num in range(listLength):
    if num%2 != 0:
      temp.append(num)
  return temp
  

def multipleOf4(list):
  temp = []
  validAns3 = False
  while validAns3 == False:
    userAns3 = input("Is it a multiple of 4? ").lower()
    if userAns3 == "yes":
      for num in list:
        if num%4 == 0:
          temp.append(num)
          validAns3 = True
    elif userAns3 == "no":
      for num in list:
        if num%4 != 0:
          temp.append(num)
          validAns3 = True
  return temp      
def multipleOf3(list):
  temp = []
  validAns3 = False
  while validAns3 == False:
    userAns3 = input("Is it a multiple of 3? ").lower()
    if userAns3 == "yes":
      for num in list:
        if num%3 == 0:
          temp.append(num)
          validAns3 = True
    elif userAns3 == "no":
      for num in list:
        if num%3 != 0:
          temp.append(num)
          validAns3 = True
  return temp  

def greaterOrLess(list):
  temp = []
  validAns6 = False
  while validAns6 == False:
    listLen = len(list)//2
    midPoint = list[listLen]
    userAns6 = input("Is it greater or equal to " + str(midPoint) +"\n--> ").lower()
    if userAns6 == "yes":
      for num in list:
        if num >= midPoint:
          temp.append(num)
          validAns6 = True 
    elif userAns6 == "no":
      for num in list:
        if num < midPoint:
          temp.append(num)
          validAns6 = True
  return temp
# Fourth
def check(list):
  global validAns
  if len(list) == 1:
    print("Your number is", list[0],"!")
    validAns = True

def evenRoute():
  isEvenRes = isEven(possibleNums)
  print(isEvenRes)
  isGreater = greaterOrLess(isEvenRes)
  print(isGreater)
  finalList = multipleOf4(isGreater)
  print("multiple of" ,finalList)
  while len(finalList) > 1:
    finalList = greaterOrLess(finalList)
    print(finalList)
    check(finalList)
def oddRoute():
  isOddRes = isOdd(possibleNums)
  print(isOddRes)
  isGreater = greaterOrLess(isOddRes)
  print(isGreater)
  finalList = multipleOf3(isGreater)
  print("multiple of" ,finalList)
  while len(finalList) > 1:
    finalList = greaterOrLess(finalList)
    print(finalList)
    check(finalList)
print("Pick a number between 1-100 \nKeep this number in mind and let me try to guess it!")


while validAns == False:
  print(validAns)
  userAns1 = input("Is your number even or odd?\n--> ").lower()
  if userAns1 == "even":
    evenRoute()
  elif userAns1 == "odd":
    oddRoute()