from Sorter import Sorter

order = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#PL - Pobranie danych od użytkownika z konsoli
def get_input_from_console():
    print('Please enter array as non-negative integers seperated by only a single space:')
    raw_input = input()
    listed_input = raw_input.split(' ')
    parsed_input = []
    for element in listed_input:
        try:
            temp_integer = int(element)
        except ValueError:
            print('Couldn\'t parse "{}"'.format(element))
            return
        if temp_integer < 0:
            print('{} is not a non-negative integer'.format(temp_integer))
            return
        parsed_input.append(temp_integer)
    return parsed_input

#PL - Program główny w którym wykonane są wszystkie powyższe Funkcje
def main():
    arr = get_input_from_console()
    sorter = Sorter(arr, order = order)
    sorter.sort()
    print(sorter.working_array)

if __name__ == '__main__':
    main()