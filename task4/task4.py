
def readfile():
   file_name=input('Введите имя файла: ')
   f = open(file_name)
   lines = f.readlines()
   nums = [int(line.rstrip('\n'))for line in lines]
   f.close()
   return nums


def minMoves(nums):
      
      nums.sort() 
      mid=len(nums) //2
      res=0
     
      for n in nums:
       res+=abs(n-nums[mid])
      print(res)


minMoves(readfile())






















# def read2list(file):
#     # открываем файл в режиме чтения utf-8
#     file = open(file, 'r', encoding='utf-8')
#     # читаем все строки и удаляем переводы строк
#     lines = file.readlines()
#     lines = [line.rstrip('\n') for line in lines]
#     file.close()
#     return lines



# lines = read2list('file.txt')
# print(lines)