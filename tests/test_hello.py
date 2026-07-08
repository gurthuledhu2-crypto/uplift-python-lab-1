def test_hello_world():
    # This checks if 1 + 1 equals 2 (a basic sanity test)
    assert 1 + 1 == 2

def test_print_output(capsys):
    # This tests a real print statement
    print("hello world")
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello world"
