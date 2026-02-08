import pytest
from app import add,subtract,multiply,divide

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    print("Add test Passed")

def test_subtract():
    assert subtract(5,2)=3
    assert subtract(10,10)==0
    print("Sub test Passed")

def test_multiply():
    assert multiply(3,4)==12
    assert multiply(0,5)==0
    print("Multiply test Passed")

def test_divide():
    assert divide(10,2)==5
    assert divide(0,5)==0
    assert divide(5,0)=="Cant divide by zero"
    print("divide test Passed")

if __name__ = "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
print("\n All Tests Passed")
