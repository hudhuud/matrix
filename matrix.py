matrix = []
S = []
m = int(input())  # строки
n = int(input())  # столбцы
for i in range(m):
    '''s = []
    for x in input().split():
        y = int(x)
        s.append(y)
    matrix.append(s)'''
    s=list(int(input()) for i in range(n))
    matrix.append(s)

#выводим матрицу
for i in range(len(matrix)):
    print(matrix[i])

#выводим сумму по строкам
for i in range(m):
    s1 = sum(matrix[i])
    S.append(s1)
print(S)
#выводим сумму по столбцам
s3 = [list(i) for i in zip(*matrix)]
#s4=[]
for i in s3:
    s4=[].append(sum(i))
print(s4)
#выводим сумму всей матрицы
print(sum(S))