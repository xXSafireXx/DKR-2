a=str(input())
b=1
c=len(a)//2
for i in range(c):
 if ord(a[i])==ord(a[-i-1]) or ord(a[i])==ord(a[-i-1])-32 or ord(a[i])-32==ord(a[-i-1]) :
    b=1
 else:
     b=0
     break
if b==1:
    print('палиндром')
else:
    print('не палиндром')
