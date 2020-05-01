# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Formula to find all pythagorean triplets
# a = k * (m**2 - n**2)
# b = k * (2m*n)
# c = k * (m + n)2
# where  m,  n and k — natural numbers,  m>n,   m-n odd,  m и n mutually simple


def compute():
    Perimetr = 1000

    for C in range(999,1,-1):
        for B in range(Perimetr-C,1,-1):
            A = Perimetr - C - B
            if A**2 + B**2 == C**2:
                print(A,B,C)
                print(A*B*C)

if __name__=="__main__":
    print(compute())
