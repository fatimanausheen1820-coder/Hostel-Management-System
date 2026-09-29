def validate_student_id(student_id):
    if not student_id.strip():
        return False
    return True
    
def validate_age(age):
    try:
        age = int(age)
        return 16 <= age <= 100
    except ValueError:
        return False

def validate_amount(amount):
    try:
        amount = float(amount)
        return amount >= 0
    except ValueError:
        return False

def validate_room_number(room_no):
    if not room_no.strip():
        return False
    return True