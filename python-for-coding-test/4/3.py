# 
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

move_types = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
#moved = (row, column)
result = 0

for move_type in move_types:
    next_row = row + move_type[0]
    next_column = column + move_type[1]

    if 1 <= next_row <=8 and 1 <= next_column <= 8:
        result += 1

print(result)
