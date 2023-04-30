# marks = []

# noofsubject = int(input("enter the number of subject:"))

# n = noofsubject

# while noofsubject>0:

#     mark = int(input("enter the subject marks:"))

#     marks.append(mark)

#     noofsubject = noofsubject-1

# sum =0

# for index in range(n):
#     sum = sum+marks[index]
    

# average = sum/n

# if( average> 90) :
#     print("grade A")

# elif(average>80) :
#     print("grade B")

# elif(average>70) :
#     print("grade c")

# elif(average>60) :
#     print("grade d")


# elif(average>50) :
#     print("grade d")

# else :
#     print("failed")





















marks =[]
noofsubject  = int( input( " enter the numberof subject of marks"))

n = noofsubject

while (noofsubject>0):
    mark = int(input( " enter the marks of subject"))
    marks.append(mark)
    noofsubject = noofsubject-1

sum =0
for index in range (n) :
    sum = sum +marks[index]


average = sum/n

if average>90:
    print("grade A")

elif average>80:
    print("grade B")

elif average>70:
    print("grade D")

elif average>60:
    print("grade E")

else:
   print(" fail")



