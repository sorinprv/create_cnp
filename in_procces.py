import math
import random

from cnp import constant

choice = random.randint(1, 8)


def S(var):
    var = str(var)
    return var


S = S(choice)
print(f" S={S}")

"""AA=>00-99"""
aa = random.randint(00, 99)


def check(var):
    list_check = []
    if var < 10:
        list_check.append(var)
        while len(list_check) < 2:
            list_check.append(0)
        var = str(list_check[-1]) + str(list_check[0])
    else:
        var = str(var)
    return var


AA = check(aa)
print(f"AA={AA}")
"""LL=>01-12"""
ll = random.randint(1, 12)


def check(var):
    list_check = []
    if var < 10:
        list_check.append(var)
        while len(list_check) < 2:
            list_check.append(0)
        var = str(list_check[-1]) + str(list_check[0])
    else:
        var = str(var)
    return var


LL = check(ll)
print(f"LL={LL}")

"""ZZ=>01-28"""
zz = random.randint(1, 28)


def check(var):
    list_check = []
    if var < 10:
        list_check.append(var)
        while len(list_check) < 2:
            list_check.append(0)
        var = str(list_check[-1]) + str(list_check[0])
    else:
        var = str(var)
    return var


ZZ = check(zz)
print(f"ZZ={ZZ}")

"""JJ=>01-48 + 51 52"""


def choice():
    jj = 1
    jj_list = [51, 52]
    while jj <= 48:
        jj_list.append(jj)
        jj += 1

    jj_choice = random.choice(jj_list)
    return jj_choice


def check(var):
    list_check = []
    if var < 10:
        list_check.append(var)
        while len(list_check) < 2:
            list_check.append(0)
        var = str(list_check[-1]) + str(list_check[0])
    else:
        var = str(var)
    return var


JJ = check(choice())
print(f"JJ={JJ}")

"""NNN=>000-999"""
nnn = random.randint(1, 999)


def check(var):
    list_check = []
    if var < 10:
        list_check.append(var)
        while len(list_check) < 3:
            list_check.append(0)
        var = str(list_check[1]) + str(list_check[-1]) + str(list_check[0])
    elif 10 <= var <= 99:
        list_check.append(var)
        while len(list_check) < 2:
            list_check.append(0)
        var = str(list_check[-1]) + str(list_check[0])
    else:
        var = str(var)
    return var


NNN = check(nnn)

print(f"NNN={NNN}")


def CNP(v1, v2, v3, v4, v5, v6):
    cnp = v1 + v2 + v3 + v4 + v5 + v6
    cnp = list(cnp)
    cnp_good = []
    for i in cnp:
        i = int(i)
        cnp_good.append(i)
    return cnp_good


cnp = CNP(S, AA, LL, ZZ, JJ, NNN)
print(f"cnp fara a 13 valoarea: {cnp}")

"""C"""

k = constant
security = []
for i in range(0, len(cnp)):
    security.append(cnp[i] * k[i])
s = 0
for i in security:
    s = s + i
s = s / 11
ss = (s - math.floor(s)) * 100
ss = math.floor(ss)
if ss < 10:
    cnp.append(ss)
elif ss >= 10:
    cnp.append(1)
print(f"cnp complet             {cnp}")
