"""
Jonathan Chen, Muhammad Akram
"""

import bulkPricing
import math

def test_happy_cases():  
    """
    This function tests some happy cases for the get_cost function
    """
    assert abs(bulkPricing.get_cost(25)-18.75)<=0.0000001
    assert abs(bulkPricing.get_cost(75)-54)<=0.0000001
    assert abs(bulkPricing.get_cost(150)-105)<=0.0000001
    assert abs(bulkPricing.get_cost(2000)-1340)<=0.0000001
    
def test_edge_cases():
    """
    This function tests some edge cases for the get_cost function
    """
    assert abs(bulkPricing.get_cost(49)-36.75)<=0.0000001
    assert abs(bulkPricing.get_cost(50)-36)<=0.0000001
    assert abs(bulkPricing.get_cost(99)-71.28)<=0.0000001
    assert abs(bulkPricing.get_cost(100)-70)<=0.0000001
    