"""Game: Guess the number"""

import numpy as np

number = np.random.randint(1, 101) # Случайное число от 1 до 100

# Количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100: '))
    
    if predict_number > number:
        print('Число должно быть меньше')
        
    elif predict_number < number:
        print('Число должно быть больше')
        
    else:
        print(f'Вы угадали число {number} за {count} попыток!')
        break #выход из цикла
    #rrrr