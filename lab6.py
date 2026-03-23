def student_num(total_num_ID):
    student_ID = []
    for i in range(total_num_ID):
        val = input(f"Enter the number: {i + 1}: ")
        student_ID.append(val)

    d1=student_ID[-1]
    d2 = student_ID[-2]
    return d1, d2

def matrix_rec(d1,d2):
    md1=int(d1)
    md2=int(d2)
    k = (md1 + md2) % 4 + 2
    shift = md1 - md2
    rows_keep = (md1 % 2) + 2

    matrix = [
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]
    ]
    print("The temperature table is:")
    for row in matrix:
        print(row)
    print()

    print("Specific element matrix[1][2]:", matrix[1][2])
    print("The first two rows:", matrix[:2])

    first_column = [row[0] for row in matrix]
    print("First column:", first_column)

    upper_left_2x2 = [row[:2] for row in matrix[:2]]
    print("Upper-left 2x2 sub-array:", upper_left_2x2)
    
    row_index =md1 % 3
    matrix_second=[num + shift for num in matrix[row_index]]
    print("The shift row is:",matrix_second)

    col_index = md2 % 4
    matrix_third=[k * row[col_index] for row in matrix]
    print("The k column is:",matrix_third)

    second_sub=[row[:rows_keep] for row in matrix [:k]]
    print("The second sub array is:", second_sub)


if __name__ == "__main__":
    total = int(input("How many numbers do you want to enter? "))
    d1, d2 = student_num(total)
    matrix_rec(d1, d2)
