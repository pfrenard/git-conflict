import random

def feature_a():
    """
    feature A

    """
    return [x for x in range(0,random.randint(0,10000)) ]

def feature_b():
    """
    feature B
    """
    print("J\'adore les fleurs")

print("Ma liste", feature_a() )

