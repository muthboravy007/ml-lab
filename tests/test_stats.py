from ml_lab.stats import mean 
from ml_lab.stats import variance

def test_mean_basic():
    assert mean([1,2,3]) == 2.0

def test_mean_single():
    assert mean([42]) == 42.0

def test_variance_basic():
    assert variance([1,2,3,4,5]) == 2.0
