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

# a=[3,5,-6,-9]
# sum1=0
# sum2=0
# sum3=0
# m1=float('-inf')
# m2=float('inf')
# for i in a:
#     sum1=sum1+i
#     m1=max(sum1,m1)
#     if(sum1<0):#required if sum becomes -ve
#         sum1=0
# e=(m1)
# for i in a:
#     sum2=sum2+i
#     m2=min(sum2,m2)
#     if(sum2>0):#required if sum becomes -ve
#         sum2=0
# (m2)
# for i in a:
#     sum3=sum3+i
# d=(sum3+(-m2))
# if sum3==m2:
#     print(m1)
 
# else:
#     print(max(d,e))



#maximum sum of array subarray with fixed size


#o=[1,2,3,4,5,6,7]
# N=2
# i=0
# j=i+N
# s=[]

# while(j<=len(o)):
#     sum=0
#     for p in range(i,j):
#         sum=sum+o[p]
#         s.append(sum)
#     sum

#     i=i+1
#     j=i+N
# print(max(s))


#Palindrome String 

# a="keokek"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# print(b)
# if(a==b):
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")


#or

# i=0
# j=len(a)-1
# flag=1
# while(i<=j):

#     if a[i]==a[j]:
#         i=i+1
#         j=j-1
#         flag=1
#     else:
#         flag=0
#         break
# if(flag==1):
#     print("it is palindrome")
# else:
#     print("it is not a palandrome")
    
    

#palindromic substrings
# def countSubstrings(s):
#         ans = 0
#         for i in range (len(s)):
#             ans = ans+ grow(s,i,i)
#             ans = ans + grow(s,i,i+1)
#         print(ans)

# def grow(str,left,right):
#     count  =0
#     while(left>=0 and right<len(str)):
#         if(str[left]==str[right]):
#             count+=1
#             left-=1
#             right+=1
#         else:
#             break
        

#     return count

# str = "aaa" 
# countSubstrings(str)


##custom problem take it  as an assignment 
# def reverser(s,i,j):
#     str1=""
#     if i>j:
#         return 0
#     else:
#         for i in range(j,-1,-1):
#             str1=str1+s[i]
#         print(str1)
# num=[2,2]
# string="vwxyz"
# limit1=len(string)+num[0]+1
# limit2=len(string)+num[1]+1
# reverser(string,2,limit1)

#the sum divisiable by 5 
#by brute force method 

        










