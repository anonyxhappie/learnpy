def egg():
    print "Egg"

def milk():print "Milk"

def isPrime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1):
    while True:
        if isPrime(n): yield n
        n += 1

def aone():
    a = "one"
    print type(a), a

def swap():
    a, b = 0, 1
    s = "Less than" if a < b else "Not less than"
    a, b = b, a
    print a, b, s

def ifelse():
    a, b = 0, 1
    if a < b:
        print "a is less than b"
    elif a > b:
        print "b is less than a"
    else:
        print "a is equal to b"

def func(a = 7):
    import sys
    for x in range(a, 10):
        sys.stdout.write(str(x) + ' ')
        # for python3 - print(x, end=' ')
    print

class Device:
    def __init__(self, kind = "electronic"):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    print "This is prime.py file."
    egg()
    milk()
    for n in primes():
        if n > 100: break
#        print n
    aone()
    swap()
    ifelse()
    func(1)
    func()
    func(5)
    electronic = Device()
    mechanical = Device("mechanical")
    print mechanical.whatKind(), electronic.whatKind()

if __name__ == "__main__":
    main()
