def checknum(num1, num2):
  if num1^num2!=0:
    print("The numbers are not equal")
  else:
    print("Both numbers are equal")
    
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 1st number: "))
checknum(num1,num2)

def OddOccuring(arr):
  res=0                 #[2,2,3,4,4]
  for element in arr:   #res=000 XOR 010 , res=010 XOR 010 , res=010 XOR 011 
    res = res ^ element     #So, res=010 , res=010x , res=001
  return res

arr=[]
size=int(input("Enter array size: "))
while (size):
  num=int(input("Enter number: "))
  arr.append(num)
  size=size-1

print("Odd Occuring number is ", OddOccuring(arr))

def TwoOdd(arr,size):
  xorof2=arr[0]
  x=0
  y=0
  SetBit=0
  
  for i in range(1, size):
    xorof2=xorof2 ^ arr[i]
  SetBit=xorof2 & ~(xorof2-1)
  
  for i in range(size):
    if (arr[i]&SetBit):
      x = x ^ arr[i]
    else:
      y = y ^ arr[i]
  print("TwoOdd element are", x,"&",y)
  
arr=[]
arr_size=int(input("Enter the size of the array: "))
for i in range(0, arr_size):
  z=int(input("Enter element: "))
  arr.append(z)
  
TwoOdd(arr,arr_size)
  