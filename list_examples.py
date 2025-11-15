#1
number=[]
for i in range(5):
  num=int(input("enter the number"))
  number.append(num)
print(number)
#2
list=[1,2,3,4,5]
total=sum(list)
average=total/len(list)
#3
list=[1,2,4,5,6,8]
print("the largest number is",max(list))
print("the smallest number is",min(list))
#4
list=[1,2,3,4]
print(list.count(2))
#5
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=list[::-1]
print(b)
#6
list=[1,2,3,4,5,6]
for num in list:
  if num%2==0:
    print(num,"it is even")
#7
list=[1,2,3,4]
list.append(5)
list.remove(1)
print(list)
#8
list=[5,4,6,7,8,3,2,1]
list.sort()
print("ascending order",list)
