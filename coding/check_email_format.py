import re
import pytest

def check_email_format(email):
    """
    Check that the provided email format is valid.
    """
    if not re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        raise Exception('Invalid email format')
    else:
        return 'Email format is valid'


def test_email_exception():
    """
    Test that exception is raised for invalid emails.
    """
    with pytest.raises(Exception) as e:
        assert check_email_format('bademail.com')
    assert str(e.value) == 'Invalid email format'


def test_simple_email():
    """
    Test a simple email address.
    """
    email = 'nobody@email.com'
    expected = 'Email format is valid'
    result = check_email_format(email)
    assert result == expected
