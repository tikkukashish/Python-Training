str=input("Enter a sentence: ")
count = 0
consonentcount=0
for i in str:
    if i.isalpha(): 
        if i.lower() in 'aeiou':
            count+=1
        else:
            consonentcount+=1
    
    if i==" ":
        continue
    if i=='!':
        break
print("Number of vowels in the sentence: ",count)
print("Number of consonents in the sentence: ",consonentcount)