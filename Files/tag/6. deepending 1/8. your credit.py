#sys.stdin.readline()

from array import array

import sys

sumCredit = 0.0
result = 0

for _ in range(20):
    jubject, credit, grade = map(str, sys.stdin.readline().strip().split())

    credit = float(credit)
    sumCredit += float(credit)

    if grade == "A+" : result += 4.5*credit
    elif grade == "A0" : result += 4*credit
    elif grade == "B+": result += 3.5*credit
    elif grade == "B0":result += 3*credit
    elif grade == "C+":result += 2.5*credit
    elif grade == "C0":result += 2*credit
    elif grade == "D+":result += 1.5*credit
    elif grade == "D0":result += 1.0*credit
    elif grade == "F":result += 0
    elif grade == "P":sumCredit -= credit

print(result/sumCredit)