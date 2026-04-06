def count_less_equal_elements(matrix: list[list[int]], value: int) -> int:
    """
    По сути, эта функция реализует то, о чём рассказывали - ищем количество
    элементов, не превышающих value. Так как матрица отсортирована, то
    все элементы выше в этом столбца меньше значения, и можем перейти к
    следующей строке матрицы. Также идём направо по матрице - определяем 
    количество элементов меньше в других столбцах
    """
    row: int = len(matrix) - 1
    col: int = 0
    counter: int = 0

    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] <= value:
            counter += row + 1
            col += 1
        else:
            row -= 1
    return counter


def kth_smallest(matrix: list[list[int]], k: int) -> int:
    """
    Как я понял. На каждом шаге решаем "подзадачу": сколько элементов
    исходной матрицы меньше значения mid - здесь используется бинарный поиск.
    Так как у нас матрица отсортирована, то стартуем с левого нижнего угла
    (функция count_less_equal_elements)
    """

    rows: int = len(matrix)
    cols: int = len(matrix[0])

    left: int = matrix[0][0]
    right: int = matrix[rows - 1][cols - 1]

    while left < right:
        mid: int = (left + right) // 2
        if count_less_equal_elements(matrix, mid) < k:
            left = mid + 1
        else:
            right = mid
    return left


def main() -> int:

    # Тест из условия с воркшопа
    matrix_1: list[list[int]] = [
        [1, 5, 9, 11],
        [2, 6, 10, 12],
        [3, 7, 13, 14],
        [4, 8, 15, 16],
    ]

    assert kth_smallest(matrix_1, 7) == 7

    # Тесты из головы
    matrix_2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    # Проверим граничные случаи
    assert kth_smallest(matrix_2, 1) == 1
    assert kth_smallest(matrix_2, 9) == 9

    assert kth_smallest(matrix_2, 5) == 5

    matrix_3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    # А вдруг матрица прямоугольная?
    assert kth_smallest(matrix_3, 1) == 1
    assert kth_smallest(matrix_3, 5) == 5


if __name__ == '__main__':
    main()