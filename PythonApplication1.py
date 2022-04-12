number1=input("enter number1: ")
number2=input("input number2: ")

if number1.find(".")==-1:
    number1+='.0'
if number2.find(".")==-1:
    number2+='.0'

number1List=[*number1]
number2List=[*number2]



tonumber1=0

tonumber2=0

for i in number1List:
    if i=='.':
        break

    tonumber1+=1



for i in number2List:
    if i=='.':
        break

    tonumber2+=1


#######################3
if tonumber1>tonumber2:
    for i in range(tonumber1-tonumber2):
         number2='0'+number2
    
if tonumber1<tonumber2:
    for i in range(tonumber2-tonumber1):
         number1='0'+number1



if len(number1)>len(number2):
    for i in range(len(number1)-len(number2)):
        number2+='0'
        

if len(number1)<len(number2):
    for i in range(len(number2)-len(number1)):
        number1+='0'

#####################



sumHolder=0
sum=''
sumLoop=0
#print(number1)
#print(number2)

dubnum1=number1.replace('.','')
dubnum2=number2.replace('.','')

#############  main action starts from here           
for index in range(1,len(dubnum1)+1):

    sumLoop=int(dubnum1[-index]) + int(dubnum2[-index]) + sumHolder
    if index==len(dubnum1):
         sum=str(sumLoop)+sum
         sumHolder=0
    elif sumLoop <10:
        sum=str(sumLoop)+sum
        sumHolder=0
    elif sumLoop>=10:
        sumHolder=int(str(sumLoop)[0])
        sum=str(sumLoop)[-1]+sum
    
    
floatdot=0
for i in number1:
    floatdot+=1
    if i=='.':
        floatdot=0


#print("dot:",floatdot)


sum=sum[0:-(floatdot)]+'.'+sum[-floatdot:]

       
        
print("Adding:",sum)
##########

#######Cixma

antisum=''
for i in range(len(number1)):
    if number1[i]=='.':
        antisum+='.'
        continue
    antisum+=str(int(number1[i])-int(number2[i]))
    
    
    

antisum=antisum.replace('-','')


#print(antisum)

antiList=[*antisum]
#print(antiList)


for i in range(len(antiList)):

    if antiList[i] =='.' or antiList[i] != '0':
        break
    elif antiList[i]=='0' and antiList[i+1]=='0' :
        
        del antiList[i]    
#print(antiList)
for i in range(1,len(antiList)):
    if antiList[-i] =='.' or antiList[-i] != '0':
        break
    elif antiList[-i]=='0' :
        
        del antiList[-i]    


#print(antiList)
antisum=''

for i in antiList:
    antisum+=i

print("Cikarama",antisum)



