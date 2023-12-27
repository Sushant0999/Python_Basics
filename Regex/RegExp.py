import re


def check(email):
    email_pattern = r'\b[A-Za-z0-9._%+-]{4,}+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_pattern, email)
    if (matches != []):
        print("PASS")
    else:
        print("FAIL")
    print("Pattern Matches : ", matches)


check('sushant.raj@netsmartz.net')