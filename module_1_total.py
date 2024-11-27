print('Итоговое практическое задание по модулю 1')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # множество
students = set({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})  # множество в список
lst_st = list(students)
print(lst_st)
res = lst_st.sort()  # преобразованное множество в список выполняем соритровку по алфавиту
print(lst_st)
# промежуточные вычисления
grades_average =  ( round(sum(grades[0]) / len(grades[0]), 1),
                    round(sum(grades[1]) / len(grades[1]), 1),
                    round(sum(grades[2]) / len(grades[2]), 1),
                    round(sum(grades[3]) / len(grades[3]), 1),
                    round(sum(grades[4]) / len(grades[4]), 1),)

# создание словаря
res = zip(lst_st, grades_average)  # объединение списка студентов и списка оценок из последовательностей
book_teacher = dict(res)  # преобразование нового списка в словарь
print(book_teacher)
