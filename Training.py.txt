#day one 12-03-24          
#problem 1  intersection of two sorted arrays

# arr1=[1,1,2,2,2,3,3,6]
# arr2=[2,2,3,4,5,5,8]
# a=[]
# i=0
# j=0
# while((i<=(len(arr1)-1)) and j<=(len(arr2)-1)):
#     if(arr1[i]<arr2[j]):
#         i=i+1
#     elif(arr1[i]>arr2[j]):
#         j=j+1
#     else:
#         a.append(arr1[i])
#         j=j+1
#         i=i+1
# print(a)


#problem 2 kadane's algo maximum subarray (o(n))

# a=[1,-2,3,-2]
# sum=0
# m=float('-inf')
# for i in a:
#     sum=sum+i
#     m=max(sum,m)
#     if(sum<0):#required if sum becomes -ve
#         sum=0
# e=(m)

#problem 3 circular list subarray sum 

a=[3,5,-6,-9]
sum1=0
sum2=0
sum3=0
m1=float('-inf')
m2=float('inf')
for i in a:
    sum1=sum1+i
    m1=max(sum1,m1)
    if(sum1<0):#required if sum becomes -ve
        sum1=0
e=(m1)
for i in a:
    sum2=sum2+i
    m2=min(sum2,m2)
    if(sum2>0):#required if sum becomes -ve
        sum2=0
(m2)
for i in a:
    sum3=sum3+i
d=(sum3+(-m2))
if sum3==m2:
    print(m1)
 
else:
    print(max(d,e))

