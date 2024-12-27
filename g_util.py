
def code_existance_verifier(user_code, codes_list):
    exists = any(user_code == code.get('Código') for code in codes_list)
    if exists:
        return True
    else:
        return False