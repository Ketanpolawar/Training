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

# def rev(a):
#     b=""
#     for i in range(len(a)-1,-1,-1):
#         b=b+a[i]
#     return(b)


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


# def rev(a):
#     b=""
#     for i in range(len(a)-1,-1,-1):
#         b=b+a[i]
#     return(b)


# def func(s,num):
#     s1 = s[len(s) - num:]
#     str=""
#     str1=""
#     limit=len(s)-num+1
#     if limit<num-1:
#          return -1
#     for i in range(num,limit-1):
#         str=str+s[i]
#     str2=rev(str)
#     for i in range (num):
#         str1=str1+s[i]
#     str1=str1+str2
#     x=len(s)-len(str1)
#     for i in range(x):
#         str1=str1+s1[i]
#     return(str1)

# num=[2,2]
# s="ketanPolawar"
# sout=func(s,2)
# sin=func(sout,2)
# print(sin)





#the sum divisiable by 5 
#by brute force method 

        
#printing all the substrings with sum k
# a=[1,2,3,4,5,6]
# l=[]
# k=5
# i=0
# j=0
# for i in range(0,len(a)-1):
#     sum=0
#     for j in range(i,len(a)-1):
#             sum=sum+a[j]
#             if sum==k :
#                l.append(sum)     
# print(l)
    



# nums=[4,5,0,-2,-3,1]
# k=5
# prefix=[0]
# rem={}
# count=0
# for i in nums:
#     prefix.append(prefix[-1]+i)
# for i in prefix:
#     if i%k in rem:
#         count=count+rem[i%k]
#         value=rem[i%k]+1
#         rem.update({i%k:value})
#     else:
#         #adding the key value pair in the dictonary
#         rem[i%k]=1+
# print(count)



# nums=[4,5,0,-2,-3,1]
# k=5
# prefix=[0]
# rem={}
# count=0
# for i in nums:
#     prefix.append(prefix[-1]+i)
# for i in prefix:
#     if i%k in rem:
#         count=count+rem[i%k]
#         value=rem[i%k]+1
#         rem.update({i%k:value})
#     else:
#         #adding the key value pair in the dictonary
#         rem[i%k]=1
# print(count)


# Recurssion 
# def func(num):
#     if num==1:
#         print(num)
#         num=5
#         return 1
#     else:
#         print(num)
#         return(func(num-1))
# func(5)
#Recurssion
# def print1(start,end):
#     if(start>end):
#         return
#     print(start)
#     print1(start+1,end)
#     print(start)
# print1(1,5)
#Recurrsion
# def print2(start,end):
#     if(start>end):
#         return
#     print(end)
#     print2(start,end-1)
#     print(end)

# print2(1,5)


#Recurssion
# def coinprint(coin,str):
#     if(coin==0):
#         print(str)
#         return
#     coinprint(coin-1,str+"T")
#     coinprint(coin-1,str+"H")

# coinprint(3,"")

#Day 15-03-24


# def partykartehai(s1,s2,i):
#     if(i>=len(s1)):
#         print(s2)
#         return
#     partykartehai(s1,s2+s1[i],i+1)
#     partykartehai(s1,s2,i+1)



# partykartehai("ab","",0)

# def partykartehai(s1,s2,i):
#     if(i>=len(s1)):
#         print(s2)
#         return
#     partykartehai(s1,s2+s1[i],i+1)
#     partykartehai(s1,s2,i+1)
#     partykartehai(s1,s2+str(ord(s1[i])),i+1)

# partykartehai("ab","",0)

#
# def jump(s,j):
#     if(j==0):
#         print(s)
#         return
#     elif(j<0):
#         return#return statement returns the control to the previous 

#     jump(s+"1",j-1)
#     jump(s+"2",j-2)
#     jump(s+"3",j-3)

# jump("",5)


# def jump1(s,j,a):
#     if(j==0):
#         print(s)
#         return
#     elif(j<0):
#         return#return statement returns the control to the previous 
#     for i in range(0,len(a)):
#         jump1(s+str(a[i]),j-(i+1),a)
# jump1("",5,[1,2,3])



# def reach(fr,fc,s,ir,ic):
#     if(ir>fr)or(ic>fc):
#         return
#     elif(fr==ir and fc==ic):
#         print(s)
#         return
#     reach(fr,fc,s+"R",ir,ic+1)
#     reach(fr,fc,s+"D",ir+1,ic)

# reach(2,2,"",0,0)


# def febo(i):
#     if(i==0 ):
#         return 0
#     elif(i==1):
#         return 1
#     else:
#         return(febo(i-1)+febo(i-2))
    
# f=febo(9)
# print(f)


# def check(n,temp,open,close,list):
#     if(open == close == n):
#         list.append(temp)
#         print(temp)
#         return
#     if(open>n or close>open):
#         return
    
#     check(n,temp +"(",open+1,close,list)
#     check(n,temp +")",open,close+1,list)
    
# check(3,"",0,0,[])



