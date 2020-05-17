"""
    Universrity of the Aegean - Polytechnic Shcoolg
    Department: Information & Communications Systems Engineering
    Lesson: Cryptography
    Nikolaos Chaikalis
        icsd12200
    Homework_2018 Exercise 4
"""
import functools


# Euclidean extended algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        d, x, y = egcd(b % a, a)
        return d, y - (b // a) * x, x


"""
    Functions whcih calculate the CRT (
    return x in ' x = a mod n'.
"""


def chinese_remainder(a, n):
    modulus = functools.reduce(lambda a, b: a * b, n)
    multipliers = []
    for N_i in n:
        N = modulus / N_i
        gcd, inverse, y = egcd(N, N_i)
        multipliers.append(inverse * N % modulus)

    result = 0
    for multi, a_i in zip(multipliers, a):
        result = (result + multi * a_i) % modulus
    return result


n = [7, 6, 5]
a = [6, 2, 0]
print("Chinese remainder:", chinese_remainder(a, n))
