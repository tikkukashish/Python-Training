evensum=0
oddsum=0
counteven=0
countodd=0
for i in range(1,51):

    if i%2==0:
        print(i," is an even number")
        evensum+=i
        counteven+=1
    else:
        print(i, " is an odd number")
        oddsum+=i
        countodd+=1

print("Sum of even number: ",evensum)
print("sum of odd number: ",oddsum)
print("avg even: ",evensum/counteven)
print("avg odd: ",oddsum/countodd)
print("Sum of all: ",evensum+oddsum)
print("avg: ",(evensum+oddsum)/(counteven+countodd))