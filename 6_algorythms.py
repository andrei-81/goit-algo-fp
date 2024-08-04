def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості
    items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for item, details in items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.items())
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_name, details = item_list[i - 1]
            if details['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - details['cost']] + details['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items = []
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, details = item_list[i - 1]
            selected_items.append(item_name)
            w -= details['cost']

    return selected_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_cost, total_calories = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_items)
print("Загальна вартість:", total_cost)
print("Загальна калорійність:", total_calories)

selected_items, total_calories = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Вибрані страви:", selected_items)
print("Загальна калорійність:", total_calories)
