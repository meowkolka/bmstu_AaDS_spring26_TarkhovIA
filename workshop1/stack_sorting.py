from __future__ import annotations
from typing import Any, Optional


# В лекции на портале говорилось о способах реализации 
# стека. Реализовал на односвязном списке
class SinglyNode: 
    def __init__(self, value: Any) -> SinglyNode:
        self.value: Any = value
        self.next: Optional[SinglyNode] = None


# Свой стек реализовал, но потом сказали, что можно писать
# на обычном питоновском списке, но стек решил оставить
class Stack:
    def __init__(self) -> None:
        self.head: Optional[SinglyNode] = None
        self.size: int = 0

    def __len__(self) -> int:
        return self.size
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def push(self, value: Any) -> None:
        new_node = SinglyNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self) -> Any:
        value: Any = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value
    
    def peek(self) -> Any:
        return self.head.value
    

def sort_stack(initial_stack: Stack) -> None:
    # Комментарии скорее для себя писал, прошу прощения

    # По "подсказкам / разрешению" можно использовать 
    # вспомогательный стек и вспомогательную переменную
    buf_stack: Stack = Stack()

    while initial_stack.is_empty() is False:
        # Суть в том, что мы на каждом шаге во временный стек
        # кладём элементы так, что у нас во временном точно 
        # отсортированный набор
        # Во время сортировки во временный стек идут такие элементы
        # которые точно больше "верхнего" в буфферном стеке
        temp: Any = initial_stack.pop()

        while buf_stack.is_empty() is False and buf_stack.peek() > temp:
            initial_stack.push(buf_stack.pop())

        buf_stack.push(temp)

    while buf_stack.is_empty() is False:
        initial_stack.push(buf_stack.pop())


def main() -> int:

    stack_to_test: Stack = Stack()

    for val in [4, 1, 3, 2]:
        stack_to_test.push(val)

    # В первой задаче был тест через assert, здесь через print()
    # с дополгнительной проверкой на отсортированность 
    # (но не всего стека, а по парам элементов)
    temp_stack: Stack = Stack()
    print("Стек до того, как его начали сортировать")
    # до начала тестирования
    while stack_to_test.is_empty() is False:
        val = stack_to_test.pop()
        temp_stack.push(val)
        print(f"{val} ", end=' ')
    while temp_stack.is_empty() is False:
        stack_to_test.push(temp_stack.pop())
    
    print('\nСтек после того, как его отсортировали')

    sort_stack(stack_to_test)

    prev: Any = None
    while stack_to_test.is_empty() is False:
        val = stack_to_test.pop()
        temp_stack.push(val)
        if prev is not None:
            assert prev <= val, "Сортировка не выполнена"
        print(f"{val} ", end=' ')
        prev = val
    while temp_stack.is_empty() is False:
        stack_to_test.push(temp_stack.pop())

    for val in [3, 1, 4, 1, 5, 2]:
        stack_to_test.push(val)
    temp_stack: Stack = Stack()
    print("Стек до того, как его начали сортировать")
    while stack_to_test.is_empty() is False:
        val = stack_to_test.pop()
        temp_stack.push(val)
        print(f"{val} ", end=' ')
    while temp_stack.is_empty() is False:
        stack_to_test.push(temp_stack.pop())
    
    print('\nСтек после того, как его отсортировали')

    sort_stack(stack_to_test)

    prev: Any = None
    while stack_to_test.is_empty() is False:
        val = stack_to_test.pop()
        temp_stack.push(val)
        if prev is not None:
            assert prev <= val, "Сортировка не выполнена"
        print(f"{val} ", end=' ')
        prev = val
    while temp_stack.is_empty() is False:
        stack_to_test.push(temp_stack.pop())


if __name__ == "__main__":
    main()
