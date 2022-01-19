def binary_search(target: int, liste: list):
    """Search an element in sorted list.
    return index of value
    :param target: item we looking for
    :param liste: list of sorted items
    :return:
    """
    left = 0
    right = len(liste) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == liste[middle]:
            print("Left: ", left)
            print("Right: ", right)

            return middle
        elif target < liste[middle]:
            right = middle - 1
        elif target > liste[middle]:
            left = middle + 1
    return False


if __name__ == '__main__':
    liste_ = [5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15,
              16, 17, 18, 19, 20,
              21, 22, 23, 24, 25,
              26, 27, 28, 29, 30]
    print(binary_search(13, liste_))
    print(binary_search(143, liste_))
