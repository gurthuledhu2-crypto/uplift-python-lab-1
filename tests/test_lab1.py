import solution

def test_double_five():
    # This checks if passing 5 to the student's code results in 10
    assert solution.double_number(5) == 10

def test_double_zero():
    assert solution.double_number(0) == 0
