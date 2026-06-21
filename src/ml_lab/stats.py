def mean(values):
    return sum(values) / len(values)

def variance(values):
    """Population variance of a non empty list of numbers."""
    m = mean(values)
    return sum((x-m)**2 for x in values)/len(values)
