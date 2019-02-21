import math


def columnar_encrypt(key, plaintext):
    columns = len(key)
    rows = math.ceil(len(plaintext) / columns)
    cipher = ''

    arr = [['' for x in range(rows)]for y in range(columns)]
    order = {
        val: num for num, val in enumerate(key)
    }

    row_count = 0
    col_count = 0
    for ch in plaintext:
        if (ch == " "):
            continue
        else:
            arr[col_count][row_count] = ch
            if (col_count == columns - 1):
                row_count += 1
                col_count = 0
            else:
                col_count += 1

    for index in sorted(order.keys()):
        cipher += ''.join(arr[order[index]])
    return cipher


def columnar_decrypt(key, encrypted):
    columns = len(key)
    rows = math.ceil(len(encrypted) / columns)
    plaintext = ''
    arr = ['' for y in range(columns)]

    order = {
        val: num for num, val in enumerate(key)
    }

    padding = len(encrypted) % columns
    count = 0

    if (padding != 0):
        for index in sorted(order.keys()):
            if (order[index] < padding):
                arr[order[index]] = encrypted[count:count+rows]
                count += rows
            else:
                arr[order[index]] = encrypted[count:count+rows-1]
                count += rows-1
    else:
        for index in sorted(order.keys()):
            arr[order[index]] = encrypted[count:count+rows]
            count += rows
    count = 0
    for i in range(len(encrypted)):
        plaintext += arr[i % columns][count:count+1]
        if (i % columns == columns - 1):
            count += 1
    return plaintext