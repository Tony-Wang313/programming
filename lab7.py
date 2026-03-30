#d1=5
#d2=6
#k=5
#shift=-1
#rows_keep=3

def student_num(total_num_ID):
    student_ID = []
    for i in range(total_num_ID):
        val = input(f"Enter the number: {i + 1}: ")
        student_ID.append(val)

    d1=student_ID[-1]
    d2 = student_ID[-2]
    return d1, d2

def mat(d1,d2):
    md1=int(d1)
    md2=int(d2)
    k = (md1 + md2) % 4 + 2
    shift = md1 - md2
    rows_keep = (md1 % 2) + 2

    matrix = [
        [5, 10, 15, 20, 25],
        [30, 35, 40, 45, 50]
    ]
    print("Table:")
    for row in matrix:
        print (row)
    print("Dimensions:")
    print("There are ",len(matrix), " row.")
    print("There are ", len(matrix[0])," columns.")
    last_column = [row[-1] for row in matrix]
    print("The last column: ", last_column)
    sub_ar=[row[:3] for row in matrix]
    print("The sub-array is ", sub_ar)
    #Component B
    a= md1 % (len(matrix))
    old_row=matrix[a]
    k_row=[num + k for num in matrix[a]]
    print("the old row is: ", old_row)
    print("The new row #", a, " increased by k is: ", k_row)
    b= md2 % 2
    sub_ar2=[row[b:] for row in matrix]
    print("The new column #", b, " is: ", sub_ar2)


if __name__ == "__main__":
    total = int(input("How many numbers do you want to enter? "))
    d1, d2 = student_num(total)
    mat(d1, d2)

#Explanation:
#d1=5, d1%2=1, the row to change is row 1 which is [30, 35, 40, 45, 50]
# k=5, so the new row have every value plus 5, which is [35, 40, 45, 50, 55]
#d2=6, d2%2=0, by printing every row from column 0, it print the same matrix