from email_validator import validate_email, EmailNotValidError

def validate_email_format(email):
    """Validate email format and normalize it"""
    try:
        validation = validate_email(email, check_deliverability=False)
        return validation.email
    except EmailNotValidError as e:
        raise ValueError(str(e))
