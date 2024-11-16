print('Итоговое практическое задание по модулю 1')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #множество
students=set({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}) #множество в список
lst_st=list(students)
print(lst_st)
res=lst_st.sort() #преобразованное множество в список выполняем соритровку по алфавиту
print(lst_st)
#промежуточные вычисления
a=[5, 3, 3, 5, 4]
b=[2, 2, 2, 3]
c=[4, 5, 5, 2]
d=[4, 4, 3]
e=[5, 5, 5, 4, 5]
a=round(sum(a)/len(a),1)
b=round(sum(b)/len(b),1)
c=round(sum(c)/len(c),1)
d=round(sum(d)/len(d),1)
e=round(sum(e)/len(e),1)
grades=[a,b,c,d,e]
#создание словаря
res =zip(lst_st,grades) #объединение списка студентов и списка оценок из последовательностей
book_teacher=dict(res)#преобразование нового списка в словарь
print(book_teacher)




