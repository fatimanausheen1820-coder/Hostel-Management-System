from validation import (
    validate_student_id,
    validate_age,
    validate_amount,
    validate_room_number
)


def test_student_id():
    assert validate_student_id("S001") == True
    assert validate_student_id("") == False


def test_age():
    assert validate_age("20") == True
    assert validate_age("10") == False
    assert validate_age("abc") == False


def test_amount():
    assert validate_amount("5000") == True
    assert validate_amount("0") == False
    assert validate_amount("abc") == False


def test_room_number():
    assert validate_room_number("101") == True
    assert validate_room_number("") == False


print("All validation tests passed!")