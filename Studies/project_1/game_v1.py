import numpy as np

def game_core_v3(number: int = 1) -> int:
    """За какое число попыток программа угадывает число
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    
    count = 0 # Количество попыток
    predict = 50 # Предсказываемое число
    mid_number = 50 # Число с помощью которого будем коректировать
    
    # Угадывается число с помощью бинарного поиска
    while number != predict:
        count += 1
        
        if predict > number:
            if mid_number != 0:
                mid_number //= 2
                predict -= mid_number
            else:
                predict -= 1
                
        elif predict < number:
            if mid_number != 0:
                mid_number //= 2
                predict += mid_number
            else:
                predict += 1
        
        # Если число угадано, возращаем переменной переменной для коррекции стартовое значение    
        else:
            mid_number = 50
            
    # Ваш код заканчивается здесь

    return count

def score_game(correction_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # Cписок для сохранения количества попыток
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(correction_predict(number))
    
    score = int(np.mean(count_ls)) # Среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

# Проверяем работу программы
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)

if __name__ == '__main__':
    score_game(game_core_v3)