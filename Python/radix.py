order = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


#PL - Łączenie Kubełków z danymi w oparciu o order
def join_buckets(buckets: list):
    ret = []
    for radix in order:
        for el in buckets[radix]:
            ret.append(el)
    return ret

#PL - Tworzy pusty kubełek
def createEmptyBuckets():
    ret = {}
    for radix in order:
        ret[radix] = []
    return ret

#PL - Konwersja zawartośni na stringi
def turnToStr(arr: list):
    ret = []
    for el in arr:
        ret.append(str(el))
    return ret

#PL - Odanezienie wartości z największą liczbą znaków i zwrócenie tego jako wartość liczbowa
def get_biggest_length(arr: list):
    biggest = 0
    for el in arr:
        if biggest < len(el):
            biggest = len(el)
    return biggest

#PL - Dopisanie 0 z przodu w celu wyrównania ilości znaków w każdym elemencie
def fill_array(arr: list, size: int):
    ret = []
    for el in arr:
        temp = order[0] * (size - len(el)) + el
        ret.append(temp)
    return ret

#PL - Konwersja zmiennej do wartości całkowitej
def turnToInt(arr: list):
    ret = []
    for el in arr:
        ret.append(int(el))
    return ret

#PL - Program główny w którym wykonane są wszystkie powyższe Funkcje
def main():
    arr = [505, 103, 87, 20, 325, 211, 134, 8]
    arr = turnToStr(arr)
    size = get_biggest_length(arr)
    arr = fill_array(arr, size)
    for i in range(1, size + 1):
        buckets = createEmptyBuckets()
        for el in arr:
            buckets[el[-1*i]].append(el)
        arr = join_buckets(buckets)
    print(turnToInt(arr))

if __name__ == '__main__':
    main()