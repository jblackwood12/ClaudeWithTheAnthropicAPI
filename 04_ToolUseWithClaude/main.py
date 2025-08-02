def greeting():
    test_val = 123
    return "This is all the function does"

def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal places using the Nilakantha series.
    
    Args:
        digits: Number of decimal digits of precision (default is 5)
        
    Returns:
        A float value representing pi to the specified precision
    """
    # We need more iterations to ensure 5 digits of precision
    # Using Nilakantha series: π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - ...
    
    # Start with the first term
    pi = 3.0
    
    # Number of iterations to ensure 5 decimal places of precision
    # This is an empirical value - more iterations give more precision
    iterations = 1000
    
    sign = 1
    for i in range(2, iterations * 2, 2):
        # Calculate the denominator for this term
        denominator = i * (i + 1) * (i + 2)
        # Add or subtract the next term based on the sign
        pi += sign * (4.0 / denominator)
        # Flip the sign for the next iteration
        sign *= -1
    
    # Round to the specified number of digits
    return round(pi, digits)