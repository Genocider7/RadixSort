default_order = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Sorter:
    def __init__(self, array, order = default_order):
        self.order = order
        self.buckets = []
        self.working_array = array
    
    #PL - Łączenie Kubełków z danymi w oparciu o order
    def join_buckets(self):
        ret = []
        for radix in self.order:
            for el in self.buckets[radix]:
                ret.append(el)
        return ret

    #PL - Tworzy pusty kubełek
    def create_empty_buckets(self):
        ret = {}
        for radix in self.order:
            ret[radix] = []
        return ret

    #PL - Konwersja zawartośni na stringi
    def turn_to_str(self):
        ret = []
        for el in self.working_array:
            ret.append(str(el))
        return ret

    #PL - Odanezienie wartości z największą liczbą znaków i zwrócenie tego jako wartość liczbowa
    def get_biggest_length(self):
        biggest = 0
        for el in self.working_array:
            if biggest < len(el):
                biggest = len(el)
        return biggest

    #PL - Dopisanie 0 z przodu w celu wyrównania ilości znaków w każdym elemencie
    def fill_array(self):
        size = self.get_biggest_length()
        ret = []
        for el in self.working_array:
            temp = self.order[0] * (size - len(el)) + el
            ret.append(temp)
        return ret

    #PL - Konwersja zmiennej do wartości całkowitej
    def turn_to_int(self):
        ret = []
        for el in self.working_array:
            ret.append(int(el))
        return ret
    
    def sort(self):
        self.working_array = self.turn_to_str()
        self.fill_array()
        for i in range(1, self.get_biggest_length() + 1):
            self.buckets = self.create_empty_buckets()
            for el in arr:
                self.buckets[el[-1 * i]].append(el)
            arr = self.join_buckets(self.buckets)
        self.working_array = self.turn_to_int()