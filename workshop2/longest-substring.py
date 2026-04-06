def longest_substring(string: str) -> int:
    """
    Как я понял идею алгоритма: проходимся по строке
    скользящим окном, которое расширяется вправо до тех пор,
    пока символ не окажется в ключах словаря. Как только дубликат
    оказался ключах, то мы удаляем обновляем индекс его последнего вхождения;
    сужаем окно: левая граница смещается вправо, перепрыгивая символ, для которого
    нашли повторение. Словарь использую потому, что он реализован как хэш-таблица, 
    чтобы для поиска элементов, уже увиденных ранее, не сводиться к O(n)
    """
    seen_characters: dict[str, int] = dict()
    left_ptr: int = 0
    max_length: int = 0

    for right_ptr in range(len(string)):
        while string[right_ptr] in seen_characters and seen_characters[string[right_ptr]] >= left_ptr:
            left_ptr = seen_characters[string[right_ptr]] + 1
        seen_characters[string[right_ptr]] = right_ptr
        max_length = max(max_length, right_ptr - left_ptr + 1)

    return max_length


def main() -> int:
    
    # Тест из условия с воркшопа
    assert longest_substring("abcdebcfgh") == 7

    # Тесты "из головы"
    assert longest_substring("aaaaaaaa") == 1

    # ответ 14 - 14 символов подряд из алфавита
    assert longest_substring("abcdefghijklmn") == 14

    # Тест, в котором подходит сразу несколько подстрок
    # abcd bcda cdab dabc
    assert longest_substring("abcdabccba") == 4

    return 0


if __name__ == "__main__":
    main()