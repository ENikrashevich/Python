//1234567890 +-*/ == 100 (убрать eval)
def find_expressions():
    """Основная функция для поиска выраженийБ дающих 100
    Returns:
        list: Список валидных выражений в строковом формате
    """
    digits = '1234567890'
    length = len(digits)
    results = []
    generate_combinations(0, [], length, results, digits)
    return results


def generate_combinations(index, path, length, results, digits):
    """Рекурсивно генерирует все комбинации чисел и операторов между цифрами
    Args:
        digits (str): Строка цифр для обработки
        results (list): Список для сохранения валидных выражений
    """
    if index == length:
        expression = ''.join(path)
        if expression[len(expression) - 2] == '/':
            return
        elif eval(expression) == 100:
            results.append(expression)
        return
    for i in range(index, length):
        if i != index and digits[index] == '0':
            break
        num = digits[index:i+1]
        if index == 0:
            generate_combinations(i+1, [num], length, results, digits)
        else:
            for op in '+-*/':
                generate_combinations(i + 1, path+[op, num], length, results, digits)


solutions = find_expressions()
for solution in solutions:
    print(solution)
