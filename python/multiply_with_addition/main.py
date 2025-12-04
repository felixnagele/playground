def multiply_with_addition(a, b):
    """Multiply two numbers using repeated addition."""
    result = 0
    sign = 1
    if b < 0:
        sign = -1
        b = -b
    for _ in range(b):
        result += a
    return result * sign

def main():
    a = 3
    b = -4
    product = multiply_with_addition(a, b)
    print(f"{a} * {b} = {product}")


if __name__ == "__main__":
    main()
