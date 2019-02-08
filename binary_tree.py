def read_tree(matrix, father, index, n):
    for i in range(1, n+1):
        x = int(input("Enter %s child of %s or -1 if it has no children : " % (i, father)))
        if x != -1:
            matrix.append([x, index, -1, -1])
            read_tree(matrix, x, 3*index + i, n)
        else:
            for j in range(i, n+1):
                matrix.append([-1, index, -1, -1])
            break
    return matrix


def my_sort(matrix):
    a = []
    for x in matrix:
        a.append(x[1])
        for i in range(1, len(a)):
            key = a[i]
            ke = matrix[i]
            j = i - 1
            while j >= 0 and key < a[j]:
                a[j + 1] = a[j]
                matrix[j + 1] = matrix[j]
                j -= 1
            a[j + 1] = key
            matrix[j+1] = ke
    return matrix


def assign_childs(matrix, c):
    child = c + 1
    count = 0
    while count < 2:
        if child >= len(matrix):
            return
        if matrix[child][0] == -1:
            return
        matrix[child][1] = child - 1
        matrix[child - 1][3] = child
        count += 1
        child += 1
    return


def convert_to_binary_tree(matrix, n):
    for j in range(0, len(matrix) // n - 1):
        f = n * j + 1
        if f >= len(matrix):
            break
        if matrix[f][0] == -1:
            continue
        matrix[f][1] = j
        matrix[j][2] = f
        assign_childs(matrix, f)

    return matrix


matrix = []
n = int(input("Enter the biggest number of children of a node :"))
root = int(input("Enter root:"))
#              number, father, left-child, right-child, can-have-children-or-not
matrix.append([root, -1, -1, -1])
matrix = read_tree(matrix, root, 0, n)
matrix = my_sort(matrix)
for i in range(len(matrix)):
    print(i, "  ", matrix[i])
print()
print()
print()
print()
print()
matrix = convert_to_binary_tree(matrix, n)
for i in matrix:
    print(i)