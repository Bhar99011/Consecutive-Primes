import math
import time
start=time.time()
num1=int(input("Start : "))
num2=int(input("stop : "))
primes=[]
sums=[]
#To find the Prime Numbers
for num in range(num1,num2):
        #Here all() gives Bool Value So that the Prime value will be added to List        
        if all(num%i != 0 for i in range(2, int(math.sqrt(num)+1))):
                primes.append(num)
sum=0
count=0
#The list of prime numbers are packed in "primes"
for i in primes:
     if i > 1:           
        sum+=i
        count+=1
        # This if statement will filter the values,We can also provide num2 instead of hardcode value
        if sum < 100000:
            #Here is a list of sum of consecutive prime numbers,that is added again to a List called "sums"             
            sums.append(sum)
            c=count
#We choose Highest Ending number < 100000 by Reverse Indexing Method from "sums" List          
print("Prime Number : ",sums[-1])
# Total Sum of prime Numbers took for addition of largest prime Number Below 100000
print("On counsecutive count of : ",c)
# Time taken is Optional
print("Time Taken: {t}".format(t=str(time.time()-start)))
                            
                             
                             
