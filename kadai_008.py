# 変数varが3の倍数の場合はFizz、5の倍数の場合はBuzz、
# 3と5の倍数の場合はFizzBuzz、それ以外の場合は変数varを出力する条件式を記述して
# ください。
# ただし、変数varは正の整数とします。

var = int(30)

if  var%3 == 0 and var%5 == 0:
    print("FizzBazz")
elif var % 3 ==0:
    print("Fizz")
elif var % 5 ==0:
    print("Buzz")
else:
    print(var)
