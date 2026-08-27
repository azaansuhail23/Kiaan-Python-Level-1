N=int(input("Enter the first N. natural no. that you want to calculate the sum "))

#Approach 1: Mathematical Formula
sum1=N*(N+1)//2

print(sum1)

print("--------")

#Approach 2 : Loop Approach
sum=0
i=1

while(i<=N):
    sum =sum+i
    
    i+=1

print(sum)