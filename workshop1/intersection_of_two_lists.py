from __future__ import annotations
from typing import Optional, Any


class SinglyNode:

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Optional[SinglyNode] = None


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head: Optional[SinglyNode] = None
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    # Позволил себе добавить вывод в строке, чтобы 
    # было более приятно смотреть на результат теста
    def __repr__(self) -> str:
        nodes: list[str] = []
        current: Optional[SinglyNode] = self.head
        while current:
            nodes.append(str(current.value))
            current = current.next
        return " - ".join(nodes) + " - None"

    def addNewTail(self, value: Any) -> None:
        new_node: SinglyNode = SinglyNode(value)

        if self.head is None:
            self.head = new_node
        else:
            current: SinglyNode = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node 

        self.size += 1

    def attach_node(self, node: SinglyNode) -> None:
        if self.head is None:
            self.head = node
        else:
            current: SinglyNode = self.head
            while current.next is not None:
                current = current.next
            current.next = node


def find_intersection_of_two_lists(
    headA: SinglyNode, 
    headB: SinglyNode,
) -> Optional[SinglyNode] | None:
    """
    Если не пересекаются, возвращаем None, 
    если пересекаются - возвращаем узел, 
    начиная с которого списки пересекаются
    """

    # 
    if headA is None or headB is None:
        return None

    buff_nodeA: Optional[SinglyNode] = headA
    buff_nodeB: Optional[SinglyNode] = headB

    # Здесь как бы сравниваем идентичность узлов списка - вдруг
    # получится ситуация, когда у нас значения одинаковые, а 
    # сами узлы - разные. 
    while buff_nodeA.value is not buff_nodeB.value:
        buff_nodeA = buff_nodeA.next if buff_nodeA is not None else headB
        buff_nodeB = buff_nodeB.next if buff_nodeB is not None else headA

    return buff_nodeA


def main() -> int:

    # Тут тест из условия задачи
    shared_8: SinglyNode = SinglyNode(8)
    shared_4: SinglyNode = SinglyNode(4)
    shared_5: SinglyNode = SinglyNode(5)
    shared_8.next = shared_4
    shared_4.next = shared_5

    list_a: SinglyLinkedList = SinglyLinkedList()
    list_a.addNewTail(4)
    list_a.addNewTail(1)
    # Просто написал дополнительный метод, так как
    # у нас есть изначально общий "участок" у списков
    # Как бы просто, чтобы не добавлять большим количеством кода
    # узлы в конец списка, одним методом добавляем целый список в конец другого
    list_a.attach_node(shared_8)

    list_b: SinglyLinkedList = SinglyLinkedList()
    list_b.addNewTail(5)
    list_b.addNewTail(6)
    list_b.attach_node(shared_8)

    # Просто вывести списки, чтобы удобнее проверять было
    print(f"listA: {list_a}")
    print(f"listB: {list_b}")

    result_1 = find_intersection_of_two_lists(list_a.head, list_b.head)
    assert result_1 is shared_8, f"Тест 1 провален: {result_1}"

    return 0


if __name__ == "__main__":
    main()
