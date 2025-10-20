class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        """Добавляет элемент на вершину стека"""
        new_node = StackNode(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Извлекает элемент с вершины стека"""
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        """Возвращает элемент с вершины стека без удаления"""
        if self.is_empty():
            raise IndexError("Попытка просмотра пустого стека")
        return self.top.value

    def is_empty(self):
        """Проверяет наличие в стеке данных"""
        return self.top is None

    def get_size(self):
        """Возвращает размер стека"""
        return self.size


class ExpressionCalculator:
    """Калькулятор min и max"""

    def __init__(self):
        self.operations = {'m': min, 'M': max}

    def apply_operation(self, stack):
        """Применяет операцию к аргументам из стека"""
        # Извлекаем второй аргумент
        if stack.is_empty():
            raise ValueError("Недостаточно аргументов")
        arg2 = stack.pop()

        # Проверяем наличие первого аргумента
        if stack.is_empty() or stack.peek() == '(':
            raise ValueError("Недостаточно аргументов")
        arg1 = stack.pop()

        # Проверяем открывающую скобку
        if stack.is_empty() or stack.pop() != '(':
            raise ValueError("Несбалансированные скобки")

        # Проверяем наличие операции
        if stack.is_empty():
            raise ValueError("Не найдена операция")

        operation_char = stack.pop()
        if operation_char not in self.operations:
            raise ValueError(f"Неизвестная операция: '{operation_char}'")

        return self.operations[operation_char](arg1, arg2)

    def calculate(self, expression):
        """Вычисляет значение выражения"""
        expression = expression.replace(' ', '')

        if not expression:
            raise ValueError("Пустое выражение")

        stack = Stack()
        i = 0
        n = len(expression)

        while i < n:
            char = expression[i]

            if char in self.operations:
                stack.push(char)
                i += 1
            elif char == '(':
                stack.push(char)
                i += 1
            elif char == ')':
                result = self.apply_operation(stack)
                stack.push(result)
                i += 1
            elif char.isdigit():
                num_str = []
                while i < n and expression[i].isdigit():
                    num_str.append(expression[i])
                    i += 1
                stack.push(int(''.join(num_str)))
            elif char == ',':
                i += 1
            else:
                raise ValueError(f"Недопустимый символ: '{char}'")

        if stack.get_size() != 1:
            raise ValueError("Неполное выражение")

        return stack.pop()


def main():
    calculator = ExpressionCalculator()

    print("КАЛЬКУЛЯТОР MIN/MAX ВЫРАЖЕНИЙ")
    print("\nИнструкция:")
    print("• m(a,b) - минимум из a и b")
    print("• M(a,b) - максимум из a и b")
    print("• Примеры: m(5,10) → 5, M(15,m(16,8)) → 15")
    print("\nВведите 'выход' для завершения")

    while True:
        user_input = input("\n> Введите выражение: ").strip()

        if user_input.lower() == 'выход':
            print("До свидания!")
            break

        try:
            result = calculator.calculate(user_input)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {str(e)}")
            print("Формат: m(число1,число2) или M(число1,число2)")


if __name__ == "__main__":
    main()

