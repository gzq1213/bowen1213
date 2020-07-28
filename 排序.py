a=eval(input('请输入一个列表:'))
n=len(a)
for i in range(n-1):
   for j in range(n-1-i):
      if a[j]>a[j+1]:
         a[j],a[j+1]=a[j+1],a[j]
print(a)
