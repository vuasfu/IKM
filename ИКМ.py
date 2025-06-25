class Stack:
    """Реализация стека с базовыми операциями"""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Добавление элемента на вершину стека"""
        self._items.append(item)

    def pop(self):
        """Извлечение элемента с вершины стека"""
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустого стека")
        return self._items.pop()

    def peek(self):
        """Просмотр верхнего элемента без извлечения"""
        if self.is_empty():
            raise IndexError("Попытка просмотра пустого стека")
        return self._items[-1]

    def is_empty(self):
        """Проверка на пустоту"""
        return len(self._items) == 0

    def size(self):
        """Количество элементов в стеке"""
        return len(self._items)


class ExpressionCalculator:
    """Калькулятор выражений с операциями min и max"""

    def __init__(self):
        self._operations = {'m': min, 'M': max}

    def _apply_operation(self, stack):
        """Применяет операцию к аргументам из стека"""
        args = []
        # Собираем аргументы (они в стеке в обратном порядке)
        while stack.peek() != '(':
            args.append(stack.pop())
        stack.pop()  # Удаляем '('

        if len(args) != 2:
            raise ValueError(f"Ожидалось 2 аргумента, получено {len(args)}")

        operation_char = stack.pop()
        if operation_char not in self._operations:
            raise ValueError(f"Неизвестная операция: {operation_char}")

        return self._operations[operation_char](args[1], args[0])

    def calculate(self, expression):
        """Вычисляет значение выражения"""
        stack = Stack()
        i = 0
        n = len(expression)

        while i < n:
            char = expression[i]

            if char in self._operations:
                stack.push(char)
                i += 1
            elif char == '(':
                stack.push(char)
                i += 1
            elif char == ')':
                result = self._apply_operation(stack)
                stack.push(result)
                i += 1
            elif char.isdigit():
                num_str = []
                while i < n and expression[i].isdigit():
                    num_str.append(expression[i])
                    i += 1
                stack.push(int(''.join(num_str)))
            elif char == ',' or char == ' ':
                i += 1  # Игнорируем разделители
            else:
                raise ValueError(f"Недопустимый символ: '{char}'")

        if stack.size() != 1:
            raise ValueError("Неполное выражение")

        return stack.pop()


def main():
    """Основной интерфейс программы"""
    calculator = ExpressionCalculator()

    # Приветственное сообщение
    print("╔══════════════════════════════════════╗")
    print("║   КАЛЬКУЛЯТОР MIN/MAX ВЫРАЖЕНИЙ     ║")
    print("╚══════════════════════════════════════╝")

    print("\nИнструкция:")
    print("• m(a,b) - минимум из a и b")
    print("• M(a,b) - максимум из a и b")
    print("• Примеры:")
    print("  m(5,10) → 5")
    print("  M(15,m(16,8)) → 15")
    print("  m(M(2,5),M(3,8)) → 5")
    print("\nВведите 'выход' для завершения")

    while True:
        try:
            user_input = input("\n> Введите выражение: ").strip()

            if user_input.lower() in ('выход', 'exit', 'quit'):
                print("До свидания!")
                break

            if not user_input:
                print("⚠ Пустой ввод. Попробуйте снова.")
                continue

            result = calculator.calculate(user_input)
            print(f"✔ Результат: {result}")

        except Exception as e:
            print(f"✘ Ошибка: {str(e)}")
            print("Правильный формат: m(число1,число2) или M(число1,число2)")
            print("Пример корректного ввода: M(m(2,5),M(3,8))")


if __name__ == "__main__":
    main()