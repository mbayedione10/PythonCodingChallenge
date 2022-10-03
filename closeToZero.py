from ast import main
# https://www.codingame.com/ide/puzzle/temperatures


def closeToZero(ts):
    """Retourner la temperature la plus proche de zero

    Args:
        ts (list): liste de relever de temperatures
    """
    if len(ts) == 0:
        return 0
    else:
        mini_p, mini_n = max(ts), min(ts)
        for index, value in enumerate(ts):
            if value > 0 and value < mini_p:
                mini_p = value
            elif value < 0 and value > mini_n:
                mini_n = value
        if abs(mini_n) < abs(mini_p):
            return (mini_n)
        else:
            return (mini_p)


if __name__ == '__main__':
    ts = [7, -10, 13, 8, 4, -7.2, -12, -3.7, 3.5, -9.6, 6.5, -1.7, -6.2, 7]
    print(ts)
    result = closeToZero(ts)
    print("result: ", result)
