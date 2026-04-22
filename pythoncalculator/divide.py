import typing

T = typing.TypeVar("T")

def divide(x: T, y: T) -> T:
    """
    Performs a division of two values.

    Parameters
    ----------
    x : T
        The first division operand, to be divided
    y : T
        The second division operand, to divide by

    Returns
    -------
    T
        The result of the division
    """

    return x / y

