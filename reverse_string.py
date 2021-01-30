# розворот рядка
# reverse string

some_string = "Oleksandr Chakalov!"


def reverse_string(s):
    chars = list(s)  # рядок -> символи

    for i in range(len(s) // 2):
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp

    return ''.join(chars)


print(some_string)
print(reverse_string(some_string))