def pascals_triangle(n):
    pt = []
    for i in range(n + 1):
        row = [1]
        for j in range(1, i):
            row.append(pt[i - 1][j - 1] + pt[i - 1][j])
        if i != 0:
            row.append(1)
        pt.append(row)
    return pt


if __name__ == '__main__':
    """
                        1
                    1       1
                1       2       1
            1       3       3       1
        1       4       6       4       1
    1       5       10      10      5       1
    """

    print(pascals_triangle(5))
