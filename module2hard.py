def rasschet():
    n = int(input("Введите число от 3 до 20: "))
    if n < 3 or n > 20:
        print("Данное число не входит в указанный интервал (ОТ 3 ДО 20)!!!")
    result = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0 and i+j==n:
                result.append(f"{i} {j}")
    print(result)


rasschet()
