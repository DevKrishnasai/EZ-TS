# def fibonacci(n):
#     fib_sequence = [0, 1]

#     while len(fib_sequence) < n:
#         next_num = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_num)

#     return fib_sequence


# n = 10
# result = fibonacci(n)
# print(result)


# def fibonacci_recursive(n):
#     print(n)
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:

#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# n = 3
# result = fibonacci_recursive(n)
# print(result)


def custom_fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return custom_fibonacci_recursive(n - 1) + custom_fibonacci_recursive(n - 2)

n = 40
sequence = [custom_fibonacci_recursive(i) for i in range(n)]
print(sequence)
