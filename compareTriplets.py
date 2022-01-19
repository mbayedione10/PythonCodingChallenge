def compareTriplets(a: [], b: []):
    """
    comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2]
    :param a: rating points for a
    :param b: rating points for b
    :return: return their respective comparison points in a list
    """
    score_a = 0
    score_b = 0
    for i in range(len(a)):
        if 1 < a[i] < 100 and 1 < b[i] < 100:
            if a[i] > b[i]:
                score_a = 1 + score_a
            elif a[i] < b[i]:
                score_b = 1 + score_b
        else:
            print("Value of {} not between ! and 100".format(i))
    liste = [score_a, score_b]
    return liste


if __name__ == '__main__':
    a = [3, 60, 10]
    b = [5, 6, 7]
    c = [17, 28, 30]
    d = [99, 16, 8]
    resultab = compareTriplets(a, b)
    resultcd = compareTriplets(c, d)
    resultac = compareTriplets(a, c)
    resultbd = compareTriplets(b, d)

    print("%12s%15s" % ("scoreA", "scoreB"))
    print("%12d%15d" % (resultab[0], resultab[1]))
    print("%28s" % ("=" * 24))
    print("%12s%15s" % ("scoreC", "scoreD"))
    print("%12d%15d" % (resultcd[0], resultcd[1]))
    print("%28s" % ("=" * 24))
    print("%12s%15s" % ("scoreA", "scoreC"))
    print("%12d%15d" % (resultac[0], resultac[1]))
    print("%28s" % ("=" * 24))
    print("%12s%15s" % ("scoreB", "scoreD"))
    print("%12d%15d" % (resultbd[0], resultbd[1]))
