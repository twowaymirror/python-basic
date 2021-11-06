

class Test():
    def __init__(self):
        """Test of init when creating object"""
        print("In init")

    def test_print(self):
        print("Kenneth")

    @property
    def value(self):
        return "1234"

def test_class():
    Test().test_print()

if __name__ == "__main__":
    print(Test().value)
