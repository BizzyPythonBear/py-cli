from utils.error import error

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def check_str(s):
    if isinstance(s, str):
        return True
    return False

def cout(t: str) -> int:
    if check_int(t):
        error(t, 1, 'str')
        return 1
    else:
        print(t)
        return 0

def iout(t: str) -> int:
    if check_int(t):
        print(str(t))
        return 0
    else:
        error(str(t), 1, 'int')
        return 1