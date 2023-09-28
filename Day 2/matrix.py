import random

def check_rows_cols_diags(matrix):
    row_results = {"1r": 0, "0r": 0}
    col_results = {"1c": 0, "0c": 0}
    left_diag_results = {"1l": 0, "0l": 0}
    right_diag_results = {"1ri": 0, "0ri": 0}

    for i in range(n):
        row = matrix[i]
        col = [matrix[j][i] for j in range(n)]

        if all(row):
            row_results["1r"] += 1
        elif not any(row):
            row_results["0r"] += 1

        if all(col):
            col_results["1c"] += 1
        elif not any(col):
            col_results["0c"] += 1

        if i == n - 1:
            left_diag = [matrix[j][j] for j in range(n)]
            right_diag = [matrix[j][n - j - 1] for j in range(n)]

            if all(left_diag):
                left_diag_results["1l"] += 1
            elif not any(left_diag):
                left_diag_results["0l"] += 1

            if all(right_diag):
                right_diag_results["1ri"] += 1
            elif not any(right_diag):
                right_diag_results["0ri"] += 1

    return row_results, col_results, left_diag_results, right_diag_results




n = int(input())
matrix = [[random.choice([0, 1]) for _ in range(n)] for _ in range(n)]

row_results, col_results, left_diag_results, right_diag_results = check_rows_cols_diags(matrix)

for row in matrix:
    print(row)

for key, value in row_results.items():
    print(f"{key} {value}")

for key, value in col_results.items():
    print(f"{key} {value}")

for key, value in left_diag_results.items():
    print(f"{key} {value}")

for key, value in right_diag_results.items():
    print(f"{key} {value}")
