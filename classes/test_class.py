

class TestProperty():
    """ Testing the property functionality in Python,
        using getter and setter.
    """
    def __init__(self, value):
        """Test of init when creating object"""
        print("In init")
        self.value = value

    def test_print(self):
        print("Kenneth")

    @property
    def value(self):
        return "1234"
    
    @value.setter
    def value(self, new_value):
        self.value = new_value

def test_class():
    TestProperty().test_print()

if __name__ == "__main__":
    print(TestProperty().value)
