from django.core.exceptions import ValidationError
import re

def validate_username_length(value):
    length= len(value)
    if length < 3 or length > 25:
        raise ValidationError("The length of the username must be between 3 and 25 characters")
    else:
        return value


def validate_username_alphadigits(value):
    validmatch= re.match('^[\w]+$', value)
    if not validmatch:
        raise ValidationError("The username can only contain alphabetical characters and numbers")
    else:
        return value

def validate_password_length(value):
    length= len(value)
    if length < 8 or length > 30:
        raise ValidationError("The password must be at least 8 characters in length and no greater than 30 characters")
    else:
        return value

def validate_password_digit(value):
    if not re.search(r"[\d]+", value):
        raise ValidationError("The password must contain at least one digit")
    else:
        return value

def validate_password_uppercase(value):
    if not re.search(r"[A-Z]+", value):
        raise ValidationError("The password must contain at least one uppercase character")
    else:
        return value

