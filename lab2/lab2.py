import unittest
def diap(d1,d2):
    massive = []
    for i in range(min(d1,d2), max(d1,d2)+1):
        massive.append(i)
    return massive

def find(key, mass):
    left, right = 0, len(mass)
    guess = 0
    while left < right:
        mid = (right + left) // 2
        if mass[mid] == key:
            return mass[mid], guess
        else:
            guess += 1
            if mass[mid] < key:
                left = mid
            else:
                right = mid

# number = int(input('введите число '))
# dd1 = int(input('1 граница интервала '))
# dd2 = int(input('2 граница интервала '))
# diapp = diap(dd1,dd2)
# print(find(number, diapp))