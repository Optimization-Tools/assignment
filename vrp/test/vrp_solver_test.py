import sys, os, pytest

sys.path.append(os.getcwd())

from do_grader_lib import PartQuality
from vrp import solver

with open('vrp/data/vrp_5_4_1', 'r') as input_data_file:
    input_data = input_data_file.read()

def test_solver():
    result = solver.solve_it(input_data)
    assert(result == '94.79 0\n0 1 4 2 0\n0 3 0\n0  0\n0  0\n')
