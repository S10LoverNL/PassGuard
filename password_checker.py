import re
from utils import Colors
from breach_checker import check_password_breach
from zxcvbn import zxcvbn

def check_password_strength(password):
    """
    Checks the strength of a password using zxcvbn for advanced criteria.
    Returns a dictionary with score and feedback.
    """
    result = zxcvbn(password)
    score = result['score']  # 0-4
    feedback = []

    # Map zxcvbn score to strength
    if score == 4:
        strength = "Very Strong"
        color = Colors.GREEN
    elif score == 3:
        strength = "Strong"
        color = Colors.BLUE
    elif score == 2:
        strength = "Medium"
        color = Colors.YELLOW
    elif score == 1:
        strength = "Weak"
        color = Colors.MAGENTA
    else:
        strength = "Very Weak"
        color = Colors.RED

    # Add zxcvbn feedback
    if result['feedback']['warning']:
        feedback.append(result['feedback']['warning'])
    if result['feedback']['suggestions']:
        feedback.extend(result['feedback']['suggestions'])

    # Check for breaches
    breach_count = check_password_breach(password)
    if breach_count > 0:
        feedback.append(f"This password has been found in {breach_count} known data breaches. Change it immediately!")
    elif breach_count == -1:
        feedback.append("Unable to check for data breaches (no internet or API error).")

    return {
        "score": score,
        "strength": strength,
        "color": color,
        "feedback": feedback,
        "breach_count": breach_count
    }