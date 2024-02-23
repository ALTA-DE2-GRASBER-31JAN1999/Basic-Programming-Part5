def muncul_sekali(angka):
    unique_numbers = []
    for num in angka:
        if angka.count(num) == 1 and int(num) not in unique_numbers:
            unique_numbers.append(int(num))
    return unique_numbers

if __name__ == '__main__':
    print(muncul_sekali("1234123")) # [4]
    print(muncul_sekali("76523752")) # [6, 3]
    print(muncul_sekali("12345")) # [1, 2, 3, 4, 5]
    print(muncul_sekali("1122334455")) # []
    print(muncul_sekali("0872504")) # [8, 7, 2, 5, 4]