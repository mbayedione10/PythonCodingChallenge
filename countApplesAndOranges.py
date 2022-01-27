def countApplesAndOranges(s, t, a, b, apples: list, oranges: list):
    """
    :param s: starting point of Sam's house location
    :param t: ending location of Sam's house location
    :param a: location of the Apple tree
    :param b: location of the Orange tree
    :param apples: distances at which each apple falls from the tree
    :param oranges: distances at which each orange falls from the tree
    :return: [number of apples that fall on Sam's house, number of oranges that fall on Sam's house]
    """
    cpt_apple, cpt_orange = 0, 0
    for index, value in enumerate(apples):
        apples[index] = a + value
        if s <= apples[index] <= t:
            cpt_apple += 1
    for index, value in enumerate(oranges):
        oranges[index] = b + value
        if s <= oranges[index] <= t:
            cpt_orange += 1
    return [cpt_apple, cpt_orange]


if __name__ == '__main__':
    start = 7
    end = 10
    apple_tree = 4
    orange_tree = 12
    apple = [1, 3, -4]
    orange = [3, -2, -4]
    print(countApplesAndOranges(start, end, apple_tree, orange_tree, apple, orange))
