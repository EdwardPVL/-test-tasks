number = int(input("Введите число: "))
length = int(input("Введите длину интервала: "))

 
c=1
path = []

while True:
    path.append(str(c))
    
    c=(c+length-2)%number+1
    
    if not c != 1:
     break 
    
result = ''.join(path)
print(result)
