def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

def string_length(s):
    """
    Return the length of a string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The length of the string.
    """
    return len(s)

def update_dictionary(d, key, value):
    """
    Add a value to a key in a dictionary if it exists or set the value if it doesn't.

    Parameters:
    d (dict): The dictionary to update.
    key (str): The key to update.
    value (int or float): The value to add or set.

    Returns:
    dict: The updated dictionary.
    """
    if key in d:
        d[key] += value
    else:
        d[key] = value
    return d
