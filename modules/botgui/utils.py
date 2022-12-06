import math

def divide_by_rows(count: int, items: list):
    rows = []
    for i in range(math.ceil(len(items)/count)):
        rows.append([])

    for i in range(len(items)):
        item = items[i]
        row = math.floor(i/count)
        rows[row].append(item)
    return rows