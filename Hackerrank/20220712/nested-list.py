if __name__ == '__main__':
    first = 100
    second = 100
    record = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
        if score == first:
            continue
        elif score < first:
            second = first 
            first = score
        elif score < second:
            second = score

    names = []
    for nt in record:
        if nt[1] == second:
            names.append(nt[0])

    names.sort()
    for t in names:
        print(t)