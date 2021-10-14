'''
 Toate numerele sunt divizibile cu k (citit)
'''

def div_k(list,k):
    '''
    Verifică dacă toate numerele din lista dată sunt divizibile cu un număr k citit
    :param list:int, lista de numere întregi
    :param k: numărul cu care este verificat fiecare element al listei date
    :return:True, dacă toate numerele din listă sunt divizibile cu k
            False,dacă nu sunt numerele divizibile cu k
    '''
    for x in list:
        if x % k != 0:
            return False
    return True

def get_longest_div_k(list,k):
    '''
    Determină cea mai lungă subsecvență de numere divizibile cu k
    :param list:int, lista de numere întregi
    :param k:int, un număr întreg cu care este verificat fiecare element al listei date
    :return: cea mai lungă subsecvență de numere divizibile cu k din listă
    '''

    subsecventa_max = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if div_k(list[i:j + 1],k) and len(list[i:j + 1]) > len(subsecventa_max):
                subsecventa_max = list[i:j + 1]
    return subsecventa_max

def show_longest_div_k(list,k):
    show_list = get_longest_div_k(list,k)
    print("Subsecvența de numere divizibile cu k din listă este:", show_list)

def test_div_k():
    assert div_k([4, 6, 8, 12], 2) == True
    assert div_k([10, 4, 5], 10) == False
    assert div_k([12, 20, 44], 4) == True
    assert div_k([3, 9, 27], 3) == True
    assert div_k([10, 13, 15, 21], 5) == False

def test_get_longest_div_k():
    assert get_longest_div_k([4, 8, 10, 17, 24], 2) == [4, 8, 10]
    assert get_longest_div_k([27, 7, 81, 9, 15], 3) == [81, 9, 15]

test_get_longest_div_k()


''' 
Toate numerele se pot scrie ca x**k ,k citit, x întreg pozitiv
'''

def powers_of_k(list,k):
    '''
    Verifică daca toate numerele din lista data pot fi scrise ca putere de k
    :param list:int, lista de numere întregi
    :param k:int, un număr întreg
    :return:True, dacă toate numerele din lista se pot scrie ca putere de k
            False, dacă nu se pot scrie ca putere de k
    '''

    for i in range(len(list)):
        ok = False
        for j in range(list[i]):
            if j ** k == list[i]:
                ok = True
        if not ok:
            return False
    return True


def get_longest_powers_of_k(list,k):
    '''
    Determină cea mai lungă subsecvență de numere ce se pot scrie ca x**k
    :param list:int, lista de numere întregi
    :param k:un număr întreg
    :return:cea mai lungă subsecvență de numere ce se pot scrie ca x**k
    '''

    subsecventa_max = []

    for i in range(len(list)):
        for j in range(i, len(list)):
            if powers_of_k(list[i: j + 1], k) and len(list[i: j + 1]) > len(subsecventa_max):
               subsecventa_max = list[i: j + 1]
    return subsecventa_max

def show_longest_powers_of_k(list,k):
    show_list = get_longest_powers_of_k(list,k)
    print("Subsecvența de numere ce se pot scrie ca x**k din listă este:", show_list)

def test_powers_of_k():
    assert powers_of_k([4, 9, 16,64], 2) == True
    assert powers_of_k([8, 27, 125], 3) == True
    assert powers_of_k([1, 32, 243], 5) == True
    assert powers_of_k([2, 4, 9, 12], 2) == False

def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([27, 8, 64, 7, 125], 3) == [27, 8, 64]
    assert get_longest_powers_of_k([4, 36, 12, 25], 2) == [4, 36]
    assert get_longest_powers_of_k([16, 18, 27], 2) == [16]

test_get_longest_powers_of_k()


''' 
Numerele sunt ordonate crescător
'''
def sorted_asc(list):
    '''
    Verifică dacă numerele din lista data sunt ordonate crescator
    :param list: int,lista de numere întregi
    :return:True,dacă numerele din lista sunt ordonate crescător
            False,dacă numerele din lista nu sunt ordonate crescător
    '''
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

def get_longest_sorted_asc(list):
    '''
    Determină cea mai lungă subsecvență de numere ordonate crescător
    :param list: int,lista de numere întregi
    :return: cea mai lungă subsecvență de numere ordonate crescător
    '''

    subsecventa_max = []
    for i in range(len(list) - 1):
        for j in range(i, len(list)):
            if sorted_asc(list[i:j + 1]) and len(list[i:j + 1]) > len(subsecventa_max):
               subsecventa_max = list[i:j + 1]
    return subsecventa_max

def show_longest_sorted_asc(list):
    show_list = get_longest_sorted_asc(list)
    print("Subsecvența de numere ordonate crescător este:",show_list )

def test_sorted_asc():
    assert sorted_asc([2, 5, 7, 9]) == True
    assert sorted_asc([9, 2, 7, 5]) == False
    assert sorted_asc([3, 6, 7, 8]) == True
    assert sorted_asc([7, 8, 10, 27]) == True

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([6, 9, 10, 3]) == [6, 9, 10]
    assert get_longest_sorted_asc([7, 8, 10, 9, 25, 2]) == [7, 8, 10]


test_get_longest_sorted_asc()



def show_menu():
    print("1.Citire listă")
    print("2.Citire k")
    print("3.Determină cea mai lungă subsecvență de numere divizibile cu k")
    print("4.Determină cea mai lungă subsecvență de numere ce se pot scrie ca x**k")
    print("5.Determină cea mai lungă subsecvență de numere ordonate crescător")
    print("x.Ieșire")

def read_list():
    list = []
    nr = int(input("Câte numere doriți: "))
    for i in range(nr):
        list.append(int(input("dați al {}-lea numar: ".format(i+1))))
    return list

def read_k():
    '''Citește k dat
        Input:k-numărul dat
        Output:k-numărul dat
    '''
    k = int(input("k dat: "))
    return k

def main():
    list = []
    while True:
        show_menu()
        op = input("Opțiune: ")
        if op == "1":
            list = read_list()
        elif op == "2":
            k = read_k()
        elif op == "3":
            show_longest_div_k(list,k)
        elif op == "4":
            show_longest_powers_of_k(list,k)
        elif op == "5":
            show_longest_sorted_asc(list)
        elif op == "x":
            break
        else:
            print("Opțiune invalidă")
main()