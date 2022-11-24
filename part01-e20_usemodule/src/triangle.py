# Enter you module contents here
"""Properties of a triangle"""

def hypothenuse(l1, l2):
    """Return length of hypothenuse for right-angled triangle with side lengths l1 and l2"""
    return (l1**2 + l2**2)**0.5

def area(l1, l2):
    """returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters"""
    return (l1 * l2)/2

__version__ = "0.1"
__author__ = "M.M.T."
