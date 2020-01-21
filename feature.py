import random

def feature_a():
    """
    feature A

    """
    return [x for x in range(0,random.randint(10000)) ]

def feature_b():
    """
    feature B
    """
    pass

print(feature_a())
