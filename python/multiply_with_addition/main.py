def multiply_with_addition(a, b):
    """Multiply two numbers using repeated addition.
    
    Args:
        a: First number (can be int or float)
        b: Second number (must be int or convertible to int)
        
    Returns:
        The product of a and b
        
    Raises:
        TypeError: If b cannot be converted to an integer
    """
    # Validate that b can be used with range()
    if not isinstance(b, int):
        if isinstance(b, float):
            # Check for special float values
            if not b.is_integer():
                raise TypeError(f"Parameter 'b' must be an integer or a float representing an integer value, got {type(b).__name__}: {b}")
            try:
                b = int(b)
            except OverflowError as e:
                raise TypeError(f"Parameter 'b' cannot be converted to integer: {e}")
        else:
            raise TypeError(f"Parameter 'b' must be an integer or a float representing an integer value, got {type(b).__name__}: {b}")
    
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
