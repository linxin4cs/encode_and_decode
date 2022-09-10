# count = 52
# for i in range(0, 10):
#   print('"' + str(i) + '"' + ": " + '"' + str(count) + '"', end = ", ")
#   count += 1

list = [1, 2, 3, 4]

for i in range(0, len(list), 3):
    for j in range(i, i + 3):
        print(list[j])
