def bubble(s):
    n = len(s)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]


nordon = [1, 19999, 8, 12, 2, 39939, 0, -9, 8]
bubble(nordon)
print(nordon)

# print ("Sorted array is:")
# for i in range(len(nordon)):
#     print ("%d" %nordon[i]),