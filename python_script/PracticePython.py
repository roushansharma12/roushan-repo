#Palindrome Number Validation
def palindromeNum():
  num = int(input("Enter Number: "))
  tempNum = num
  sumNum = 0
  while(num > 0):
    r = num % 10
    sumNum = (sumNum*10)+r
    num = num//10
  if sumNum == tempNum:
    return str(tempNum)+" is palindrome number"
  else:
    return str(tempNum)+" is not palindrome number"

#Palindrome String Validation
def palindromeStr():
  strInput = str(input("Enter Text: "))
  reverse = strInput[::-1]
  if strInput.lower() == reverse.lower():
    return strInput+" is palindrome number"
  else:
    return strInput+" is not palindrome number"

#Factorial Number Generate
def factNum():
  num = int(input("Enter Number: "))
  facNum = 1
  for n in range(1,num+1):
    facNum = facNum * n
  return "Factorial Number of "+str(num)+" is: "+str(facNum)

#Fibonacci Serise Generate
def favSeries(x):
  if x == 1:
    return 1
  elif x == 0:
    return 0
  else:
    return favSeries(x-1)+favSeries(x-2)
#Fibonacci Serise Generate Call
def generateFib():
  numFib = int(input("Enter Number: "))
  return "Fibonacci Serise of "+str(numFib)+" is: "+str(favSeries(numFib))



switchFunc = {
  1: generateFib,
  2: factNum,
  3: palindromeNum,
  4: palindromeStr
}

while(True):
  print("===========================================")
  print("1. Generate Fibonacci Serise.")
  print("2. Generate Factorial Number.")
  print("3. Palindrome Number Validation.")
  print("4. Palindrome Text Validation.")
  print("0. For exit.")
  print("===========================================")
  numInput = int(input("Enter Selection: "))
  if numInput == 0:
    break
  elif int(len(switchFunc)) >= numInput:
    funC = switchFunc[numInput]
    print(funC())
  else:
    print("Please Enter valid number.")