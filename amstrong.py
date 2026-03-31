digit=int(input("enter the number"))
sum=0
while(digit>0):
    digits= digit%10
    sum+=digits**3
    digit//=10
if(sum==digit):
    print("amstrong")
else:
    print("not amstrong")   