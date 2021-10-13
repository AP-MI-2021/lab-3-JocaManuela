'''
 Toate numerele sunt divizibile cu k (citit)
'''

def div_k(k,nr):
    '''
    Verifică dacă un număr dat este divizibil cu un număr k citit
    :param k: numărul cu care este verificat
    :param nr: numărul care este verifcat
    :return:True, dacă este divizibil
            False, dacă nu este divizibil
    '''

    if nr % k == 0:
        return True
    return False

def get_longest_div_k(list,k):
    '''
    Determină cea mai lungă subsecvență de numere divizibile cu k
    :param list:int, lista de numere întregi
    :param k:int, un număr întreg cu care este verificat fiecare număr din lista dată
    :return: cea mai lungă subsecvență de numere divizibile cu k din listă
    '''
    max_start = 0
    max_len = 0
    length = 0
    for i in range(len(list)):
        if div_k(k, list[i]):
            length += 1
        else:
            length = 0
        if length > max_len:
            max_len = length
            max_start = i - max_len + 1
    return max_start, max_start + max_len - 1

def show_longest_div_k(list,k):
    show_list = get_longest_div_k(list,k)
    print("Subsecvența de numere divizibile cu k din listă este:", show_list)

def test_div_k():
    assert div_k(3,21) == True
    assert div_k(3, 40) == False
    assert div_k(3, 12) == True
    assert div_k(3, 5) == False
    assert div_k(3, 7) == False

def test_get_longest_div_k():
    assert get_longest_div_k([4, 8, 10, 17, 24],2) == (0,2)
    assert get_longest_div_k([27, 7, 81, 9, 15], 3) == (2,4)

test_get_longest_div_k()


''' 
Toate numerele se pot scrie ca x**k ,k citit, x întreg pozitiv
'''

def powers_of_k(x,k):
    '''
    Verifică dacă un număr poate fi scris ca putere de k
    :param x:int, numărul care se verifică dacă poate fi scris ca putere de k
    :param k:int, număr întreg citit
    :return:True, dacă se poate scrie ca putere de k
            False, dacă se nu poate scrie ca putere de k
    '''

    i=2
    while(pow(i,k)<=x):
        if pow(i,k) == x:
            return True
        i = i+1
    return False

def get_longest_powers_of_k(list,k):
    '''
    Determină cea mai lungă subsecvență de numere ce se pot scrie ca x**k
    :param list:int, lista de numere întregi
    :param k:număr întreg citit
    :return:cea mai lungă subsecvență de numere ce se pot scrie ca x**k
    '''
    max_start = 0
    max_len = 0
    length = 0
    for i in range(len(list)):
        if powers_of_k(list[i], k):
            length += 1
        else:
            length = 0
        if length > max_len:
            max_len = length
            max_start = i - max_len + 1

    return max_start, max_start + max_len - 1

def show_longest_powers_of_k(list,k):
    show_list = get_longest_powers_of_k(list,k)
    print("Subsecvența de numere ce se pot scrie ca x**k din listă este:", show_list)

def test_powers_of_k():
    assert powers_of_k(4,2)==True
    assert powers_of_k(81, 4) == True
    assert powers_of_k(81, 2) == True
    assert powers_of_k(81, 5) == False
    assert powers_of_k(8, 3) == True

def test_get_longest_powers_of_k():
    assert get_longest_powers_of_k([4, 9, 10, 81, 5],2) == (0,1)
    assert get_longest_powers_of_k([27, 8, 64, 7, 125], 3) == (0,2)

test_get_longest_powers_of_k()


''' 
Numerele sunt ordonate crescător
'''
def sorted_asc(a,b):
    '''
    Verifică dacă numerele date sunt ordonate crescător
    :param a: int, primul număr,care se verifică dacă e mai mic decât al doilea
    :param b: int, al doilea număr, care se verifică dacă e mai mare decât primul
    :return:True,dacă numerele sunt ordonate crescător
            False,dacă numerele nu sunt ordonate crescător
    '''
    if a < b:
        return True
    return False

def get_longest_sorted_asc(list):
    '''
    Determină cea mai lungă subsecvență de numere ordonate crescător
    :param list: int,lista de numere întregi
    :return: cea mai lungă subsecvență de numere ordonate crescător
    '''
    max_start = 0
    max_len = 0
    length = 0
    for i in range(len(list)):
        if sorted_asc(list[i-1],list[i]):
            length += 1
        else:
            length = 0
        if length > max_len:
            max_len = length
            max_start = i - max_len + 1
    return max_start, max_start + max_len - 1

def show_longest_sorted_asc(list):
    show_list = get_longest_sorted_asc(list)
    print("Subsecvența de numere ordonate crescător este:",show_list )

def test_sorted_asc():
    assert sorted_asc(3,5)==True
    assert sorted_asc(8,25) == True
    assert sorted_asc(6, 2) == False
    assert sorted_asc(11,12) == True
    assert sorted_asc(30,19) == False

def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([6, 9, 10, 3]) == (0,2)
    assert get_longest_sorted_asc([7, 8, 10, 9, 25, 2]) == (0,2)


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
        list.append(float(input("dați al {}-lea numar: ".format(i+1))))
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
