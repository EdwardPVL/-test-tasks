 
def read_file_circle():
   file_name=input('Введите имя файла 1: ')
   f = open(file_name).read().split()
   array=list(map(int, f))
   return array
  

arr_circle = read_file_circle()

def read_file_points():
   file_name = input(' Введите имя файла 2: ')
   f = open(file_name).read().split()
   array= list(map(int, f))
   points=[]
  
   for i in range(0,len(array),2):
     points.append([array[i], array[i+1]])
   return points

arr_points = read_file_points()
 

for item in arr_points:
   d=pow(pow((item[0]-arr_circle[0]),2)+pow((item[1]-arr_circle[1]),2),0.5)
   
   if  arr_circle[2]==d:
      print ("0")
   elif arr_circle[2]<d:
      print ("2")
   else:
      print ("1")

