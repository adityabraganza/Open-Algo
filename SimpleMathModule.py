from math import sqrt

def Power(num: int or float, powerof: int or float) -> float or int:
    """
    Gives the value of a given number to the power of another number

    Args:
        num (int or float): given number
        powerof (int or float): number to the power of

    Returns:
    float or int: 'num^powerof'
    """
    __val__ = 1

    if num == 0:
        return 0
    elif powerof == 0:
        return 1
    else:
        while powerof > 0:
            __val__ = __val__*num
            powerof -= 1

        if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

        return __val__

def StandardDeviation(list: list) -> float or int:
    """
    Gives the standard deviation of a given list

    Args:
        list (list): list of only numbers of the sample/population

    Returns:
        float or int: Standard deviation of list
    """
    __TopOfFraction__ = 0
    __len__ = len(list)
    __mean__ = sum(list) / __len__

    for num in list:
        __TopOfFraction__ += Power((num - __mean__), 2)

    __val__ = sqrt(__TopOfFraction__/__len__)

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return(__val__)

def LinearEquationY(m: int or float, x: int or float, c: int or float) -> int or float:
    """
    Find the value of 'y' in 'y = mx + c' if 'm', 'x' and 'c' is given

    Args:
        m (int or float): Slope of the equation
        x (int or float): X value
        c (int or float): Constant

    Returns:
        int or float: Value of y in 'y = mx + c'
    """
    __val__ = (m * x) + c

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def LinearEquationX(y: int or float, m: int or float, c: int or float) -> int or float:
    """
    Finds the value of 'x' in 'y = mx + c' if 'y', 'm', and 'c' are given

    Args:
        y (int or float): Y value
        m (int or float): Slope of the equation
        c (int or float): Constant

    Returns:
        int or float: Value of x in 'y = mx + c'
    """
    __val__ = (y - c) / m

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def LinearEquationM(y: int or float, x: int or float, c: int or float) -> int or float:
    """
    Finds the value of 'm' in 'y = mx + c' if 'y', 'x', and 'c' are given

    Args:
        y (int or float): Y value
        x (int or float): X value
        c (int or float): Constant

    Returns:
        int or float: Value of m in 'y = mx + c'
    """
    __val__ = (y - c) / x

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def LinearEquationC(y: int or float, m: int or float, x: int or float):
    """
    Finds the value of 'm' in 'y = mx + c' if 'y', 'x', and 'c' are given

    Args:
        y (int or float): Y value
        m (int or float): Slope of the equation
        x (int or float): X value

    Returns:
        int or float: Value of c in 'y = mx + c'
    """
    __val__ = (m * x) - y

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def QuadraticEquation(a: int or float, b: int or float, c: int or float) -> int or float or list or bool:
    """
    Finds the roots of a quadratic equation given the variables a, b, and c in the form 'ax^2 + bx + c = 0'

    Args:
        a (int or float): Value of a
        b (int or float): Value of b
        c (int or float): Value of c

    Returns:
        int or float or list or bool: If there are no roots it returns the boolean value False. If there is one root it gives the value as an integer or float. If there are two values it gives the values as a list
    """
    __discriminant__ = Power(b, 2) - (4*a*c)
    if __discriminant__ > 0:
        __val__ = [
            ((b*(-1))+(sqrt((b*b)-(4*a*c))))/(2*a),
            ((b*(-1))-(sqrt((b*b)-(4*a*c))))/(2*a)
        ]
    if __discriminant__ == 0:
        __val__ = (-b) * 2 * a

    if __discriminant__ < 0:
        __val__ = False

    if type(__val__) == float:
            if __val__.is_integer():
                __val__ = int(__val__)

    return __val__

def Sum(list: list) -> int or float:
    """
    Adds every number in a list

    Args:
        list (list): List of integers or floats

    Returns:
        int or float: Sum of the numbers
    """
    __total__ = 0

    for val in list:
        __total__ += val

    if type(__total__) == float:
        if __total__.is_integer():
            __total__ = int(__total__)

    return __total__