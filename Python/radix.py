order = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def join_buckets(buckets):
    ret = []
    for radix in order:
        for el in buckets[radix]:
            ret.append(el)
    return ret

def createEmptyBuckets():
    ret = {}
    for radix in order:
        ret[radix] = []
    return ret

def turnToStr(arr):
    ret = []
    for el in arr:
        ret.append(str(el))
    return ret

def get_biggest_length(arr):
    biggest = 0
    for el in arr:
        if biggest < len(el):
            biggest = len(el)
    return biggest

def fill_array(arr, size):
    ret = []
    for el in arr:
        temp = order[0] * (size - len(el)) + el
        ret.append(temp)
    return ret

def turnToInt(arr):
    ret = []
    for el in arr:
        ret.append(int(el))
    return ret

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