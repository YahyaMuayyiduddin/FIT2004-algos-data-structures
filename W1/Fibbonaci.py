def fib_recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):

    prev = 0
    acc = 1
    for i in range(n-1):
       temp = acc
       acc += prev
       prev = temp
    return acc


if __name__ == "__main__":
    # print(fib_recursive(4))
    for i in range(1, 10):
        assert fib_iterative(i) == fib_recursive(i)
