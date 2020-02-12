natural_number=int(input("put hear your some 4 natural numbers: "))
a=natural_number % 10
b=(natural_number // 10) %10
c=((natural_number // 10) //10) %10
d=(((natural_number // 10) //10) //10) %10
summ = a + b + c + d
number_sort = [a, b , c, d]

print("Summ of numbers :", summ)
print("Sorted numbers a,b,c,d :", sorted(number_sort))
print("Reversing of numbers :", a,b,c,d)


