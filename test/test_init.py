#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.join(os.path.abspath('..'),'code'))
from main import arith_sum

def test_arith_sum():
    assert arith_sum(2,3) == 5