def mini_max_sum(arr: list):
    liste = []
    total = sum(arr)
    for item in arr:
        som = total - item
        liste.append(som)
    print(min(liste), max(liste))


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    mini_max_sum(arr)
