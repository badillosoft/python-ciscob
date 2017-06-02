# _*_ coding: utf-8 _*_

def statistics(numbers):
    sum = 0 # with the sum obtain average
    sum2 = 0
    n = len(numbers)

    for x in numbers:
        sum += x
        sum2 += x ** 2

    avr = float(sum) / n # Integer / Integer => Integer Ex. 1 / 2 => 0
    # Covert at least one number to float and get a float division

    return {
        "sum": sum,
        "sum2": sum2,
        "average": avr
    }

print statistics([1, 3, 5, 7, 9, 11, 13])
print statistics([2, 4, 5, 7, 9])