i=0
j=len(a)-1
flag=1
while(i<=j):

    if a[i]==a[j]:
        i=i+1
        j=j-1
        flag=1
    else:
        flag=0
        break
if(flag==1):
    print("it is palindrome")
else:
    print("it is not a palandrome")
    