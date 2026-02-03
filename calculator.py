def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    """Multiply two numbers.""" 
    return a * b

def divide(a, b):
    """divide to numbers and return false on division by 0."""
    if b == 0:
        return False
    return a // b