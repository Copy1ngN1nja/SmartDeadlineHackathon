# Примерные данные
plan = 8  # Запланированные часы
worked = 7  # Затраченные часы

# Функция для вычисления оценки
def calculate_score(plan, worked):
    return plan - worked  # Чем больше разница, тем лучше

# Функция для обновления worked в зависимости от change
def update_worked(worked, change):
    return float(input())

# Функция тернарного поиска
def ternary_search(plan, worked, low=0.0, high=10.0, epsilon=1e-1):
    while high - low > epsilon:
        mid1 = low + (high - low) / 3
        mid2 = high - (high - low) / 3
        
        score1 = calculate_score(plan, update_worked(worked, mid1))
        score2 = calculate_score(plan, update_worked(worked, mid2))
        
        if score1 < score2:
            low = mid1  # Максимум находится в правой части
        else:
            high = mid2  # Максимум находится в левой части
            
    optimal_change = (low + high) / 2
    max_score = calculate_score(plan, update_worked(worked, optimal_change))
    
    return optimal_change, max_score

optimal_change, max_score = ternary_search(plan, worked)
print(f'Оптимальное значение change: {optimal_change:.5f}, Максимальная оценка: {max_score:.5f}')
