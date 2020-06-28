list = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
with open('words.txt') as f:
    for line in f:
        line=line[:-1]
        list[len(line)].append(line)
a=input('Enter the letters in small letters without space: ')
num=int(input('Enter the number of empty spaces: '))
alpha='abcdefghijklmnopqrstuvwxyz'
b=[]
index=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for ind in range(0,26):
    # if alpha[ind] in a :
    #     pass
    # else:
    #     b.append(alpha[ind])
    for ind2 in range(0,len(a)):
        if alpha[ind]==a[ind2]:
            index[ind]+=1
for ind in range(0,26):
    if index[ind]==0:
        b.append(alpha[ind])
print ('The excluded letters are: ',b)
c=[]
d=[]
count2=0
for i in range(0,len(list[num])):#select each word in the list
    index2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    count1 = 0
    for j in range(0,len(b)):#select each letter from excluded list
        if b[j] in list[num][i]:#check if excluded letter is in the selected word
            count1+=1
    if count1==0 :#if no excluded letters are present in the word
      
        for ind in range(0,26):#select a number from 0 to 26
            count2=0#initialise count2 to zero
            for ind2 in range(0,len(list[num][i])):#select a number in the index of the word
                if alpha[ind]==list[num][i][ind2]:#check if the alphabet is present in the word
                    index2[ind]+=1#if present 
        for ind in range(0,26):    
            if index2[ind]>index[ind]:
                    count2+=1
        
        if count2==0:
            c.append(list[num][i])
        else:
            d.append(list[num][i])
    else:
        d.append(list[num][i])
print ("There are 1,09,583 words available in our program's database")
print ("And out of them, the available ",num," letter words are ",len(list[num]))
print ("\nTotal number of excluded letters is ",len(b))
print ("Total number of excluded words is ", len(d))
print ("Total number of required words is ",len(c))
print ("\nThe list is ",c)
