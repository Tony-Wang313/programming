#Question 1
def student_num(reading):
    compute = []
    for i in range(reading):
        value = input(f"Enter the value {i + 1}: ")
        compute.append(value)
    once=[]
    duplicates=[]
    for num in compute:
        if num in once:
            duplicates.append(num)
        else:
            once.append(num)
    return once

#Question 2
def sum_list(reading_2):
    sum_lst=[]
    total=0
    for i in range(reading_2):
        value = int(input(f"Enter the value {i + 1}: "))
        total += value
        sum_lst.append(total)
    return sum_lst

#Question 3
def step_list(reading_3, step_N):
    N_lst=[]
    for i in range(reading_3):
        value = int(input(f"Enter the value {i + 1}: "))
        if (i+1) % step_N == 0:
            N_lst.append(value)
    return N_lst

#Question 4
def product_list (reading_4):
    product_lst=[]
    first_lst=[]
    second_lst=[]
    for i in range(reading_4):
        value_1 = int(input(f"Enter the value {i + 1}: for the first list:"))
        first_lst.append(value_1)
    for i in range(reading_4):
        value_2 = int(input(f"Enter the value {i + 1}: for the second list:"))
        second_lst.append(value_2)
    product_lst=[a * b for a,b in zip(first_lst, second_lst)]
    return product_lst

#Question 5
def matrix_product(row, column):
    mat_1=[]
    mat_2=[]
    prod_mat=[]
    j=0
    while j < row:
        add_row=[]
        for i in range(column):
            val_1 = int(input(f"Enter the value {i + 1} for the line {j+1} in matrix 1:"))
            add_row.append(val_1)
        mat_1.append(add_row)
        j+=1
    a=0
    while a < row:
        new_row=[]
        for b in range(column):
            val_1 = int(input(f"Enter the value {b + 1} for the line {a+1} in matrix 2:"))
            new_row.append(val_1)
        mat_2.append(new_row)
        a+=1
    
    for i in range(row): 
        product_row = []
        for j in range(column):
            col = [row[j] for row in mat_2]  
            val = sum(a * b for a, b in zip(mat_1[i], col))
            product_row.append(val)
        prod_mat.append(product_row)
    return prod_mat


if __name__ == "__main__":
    reading=int(input("Enter the number of value:"))
    print(student_num(reading))
    reading_2=int(input("Enter the number of value:"))
    print(sum_list(reading_2))
    reading_3=int(input("Enter the number of value:"))
    step_N=int(input("Enter the nth step:"))
    print(step_list(reading_3, step_N))
    reading_4=int(input("Enter the number of value:"))
    print(product_list(reading_4))
    row=int(input("Enter the number of rows:"))
    column=int(input("Enter the number of columns:"))
    print(matrix_product(row, column))
