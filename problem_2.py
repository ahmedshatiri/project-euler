# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
sum = 2
firstTerm = 1
secondTerm = 2
while secondTerm < 4000000:
    temp = secondTerm
    secondTerm += firstTerm
    firstTerm = temp
    if secondTerm % 2 == 0:
        sum += secondTerm
print(sum)
