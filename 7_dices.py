import random
import matplotlib.pyplot as plt
import pandas as pd

def roll_dice():
    """Функція для кидка двох кубиків і повернення їх суми."""
    return random.randint(1, 6) + random.randint(1, 6)

def simulate_rolls(num_rolls):
    """Функція для симуляції великої кількості кидків кубиків."""
    results = [roll_dice() for _ in range(num_rolls)]
    return results

def calculate_probabilities(results):
    """Функція для підрахунку ймовірностей кожної можливої суми."""
    counts = {sum_: 0 for sum_ in range(2, 13)}
    for result in results:
        counts[result] += 1
    
    probabilities = {sum_: count / len(results) for sum_, count in counts.items()}
    return probabilities

num_rolls = 100000  # Кількість симульованих кидків кубиків
results = simulate_rolls(num_rolls)
probabilities = calculate_probabilities(results)
    
data = {'Сума': list(probabilities.keys()), 'Ймовірність': list(probabilities.values())}
df = pd.DataFrame(data)
    
print(df)
    

plt.figure(figsize=(10, 6))
plt.bar(df['Сума'], df['Ймовірність'])
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.xticks(range(2, 13))
plt.grid(axis='y')
plt.show()