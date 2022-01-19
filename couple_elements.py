import random

# NioulBoy


def find_couple(liste: list, number):
    couple = []
    # Calculate each item with the others if it's equal number
    for i in liste:
        for j in liste:
            if i + j == number:
                cple = [i, j]
                # Check if the couple or its reverse are present in the final list
                if cple in couple or cple[::-1] in couple:
                    pass
                else:
                    couple.append(cple)
    return couple


# Elias
def find_n_pairs_sum_k(numbers, k):
    complementaries, pairs = set(), []
    for number in numbers:
        remainder = k - number
        if remainder in complementaries:
            pairs.append((number, remainder))
        # A set is useful because it contains unique elements
        complementaries.add(number)
    print([complementaries])
    return pairs


if __name__ == '__main__':
    # Create a random list
    random_list = [random.randint(1, 9) for _ in range(10)]
    print("Liste: ", random_list)
    print(find_couple(random_list, 11))
    print('-'*40)
    print("Elias")
    # Elias
    print(find_n_pairs_sum_k(random_list, 11))
    print(find_n_pairs_sum_k(random_list, 6))
