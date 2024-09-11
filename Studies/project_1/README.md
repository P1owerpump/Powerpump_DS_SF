# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](#описание-проекта)  
[2. Какой кейс решаем?](#какой-кейс-решаем)  
[3. Этапы работы над проектом](#этапы-работы-над-проектом)  
[4. Результат](#результаты)    
[5. Выводы](#выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное количество попыток.

:arrow_up:[Перейти к оглавлению](#оглавление)


### Какой кейс решаем?    
Написать программу, которая угадывает загаданное компьютером число число за минимальное количество попыток.

**Условия задания:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.
- Программа находит числа в среднем меньше чем за 20 попыток. 

**Метрика качества**     
- Результаты оцениваются по среднему количеству попыток при 10000 повторений. Необходимо добиться минимального количества попыток.

**Что практикуем**     
- Учимся писать хороший код на Python.
- Учимся работать с IDE.
- Учимся работать с GitHub.


### Этапы работы над проектом  
1. Анализ задачи.
2. Выбор оптимального алгоритма для минимизации количества попыток.
3. Написание кода и выявление ошибок.
4. Тестирование.
5. Документирование.
6. Зафиксировать версии библиотеки, которые использовались в проекте.
7. Публикация на GitHub.

:arrow_up:[Перейти к оглавлению](#оглавление)


### Результаты:  
Программа угадывает число в среднем за 5 попыток.  
Тест проводился по списку из 10000 случайных чисел загаданных компьютером.

:arrow_up:[Перейти к оглавлению](#оглавление)


### Выводы:  
В процессе выбора алгоритма для решения задачи был выбран алгоритм "бинарный поиск", но т.к. при целочисленном делении переменная, которая хранит в себе частное делимого числа приходит к нулю, было решено добавить коррекцию +-1, если переменная равна нулю.

:arrow_up:[Перейти к оглавлению](#оглавление)