def generate_combinations(template, start=0):
    # Находим первую открывающую скобку
    start_idx = template.find('{', start)

    # Базовый случай: если скобок нет, возвращаем текущий вариант строки
    if start_idx == -1:
        return [template]

    # Находим закрывающую скобку для текущей открывающей
    end_idx = template.find('}', start_idx)

    # Извлекаем варианты из скобок и разбиваем их по запятой
    options = template[start_idx + 1:end_idx].split(',')

    # Список для хранения всех возможных комбинаций
    combinations = []

    # Для каждого варианта генерируем новую строку, заменяя текущие скобки на этот вариант,
    # и рекурсивно вызываем функцию для поиска следующих скобок
    for option in options:
        # Заменяем текущие скобки на вариант и вызываем рекурсию
        new_template = template[:start_idx] + option.strip() + template[end_idx + 1:]
        combinations += generate_combinations(new_template, start_idx + len(option))

    return combinations


# Исходная строка с фигурными скобками
template = "Какое {наибольшое,наименьшее} число на клетке {красного, желтого, оранжевого, зеленого, синего, фиолетового} цвета ? "

template = input()
# Генерация всех возможных комбинаций
combinations = generate_combinations(template)

# Вывод комбинаций
for combination in combinations:
    print(combination)
