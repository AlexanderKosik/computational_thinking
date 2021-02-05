
num_comp = 0
def fib(number):
    global num_comp
    num_comp += 1
    if number == 0 or number == 1:
        return 1
    else:
        result = fib(number - 1 ) + fib(number - 2)
        return result

# for i in range(100):
#     num_comp = 0
#     print(f"Fib({i}) = {fib(i)} ({num_comp} computations)")


def fast_fib(number, memo={}):
    if number == 0 or number == 1:
        return 1
    else:
        try:
            result = memo[number]
            return result
        except KeyError:
            result = fast_fib(number - 1, memo) + fast_fib(number - 2, memo)
            memo[number] = result
            return result


for i in range(100):
    lookup = {}
    print(f"Fib({i}) = {fast_fib(i, lookup)}, {len(lookup)}")
