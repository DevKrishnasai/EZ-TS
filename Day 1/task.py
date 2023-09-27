# TASK 1
# Magical primes = if reverse of the given number and the given number are primes then their are called magical primes
# Ex: 19 and 91 are magical primes
# Neon numbers = if sum of digits of the number square = again given number then the given number is neon number
# Ex: 9
#    square = 9*9 = 81
#    sum = 8 + 1
#    sum = 9 which is again the same number 9
#    so the given number is neon number

# Neon number and Magical primes using class
class parent:
    pass

class child1(parent):
    def __init__(self, a):
        self.a = a

    def magicalPrimes(self):
        num = str(self.a)
        num = int(num[::-1])
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


class child2(parent):
    def __init__(self, a):
        self.a = a

    def neonNumbers(self):
        sq = str(self.a**2)
        s = 0
        for i in sq:
            s += int(i)
        if s == self.a:
            return True
        else:
            return False


c = child1(41)
result = c.magicalPrimes()
if result:
    print("The number is magical primes")
else:
    print("The number is not magical primes")


d = child2(9)
result = d.neonNumbers()
if result:
    print("The number is neon number")
else:
    print("The number is not neon number")
