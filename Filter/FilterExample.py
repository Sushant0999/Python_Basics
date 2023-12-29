age = [19, 82, 34, 84, 45, 22, 26, 20, 10]

mid = list(filter(lambda age: age % 10 == 0, age))

print(mid)
