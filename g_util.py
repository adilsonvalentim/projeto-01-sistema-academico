def code_existance_verifier(user_code, codes_list):
    for dictionary in codes_list:
        if user_code in dictionary.values():
            return True, dictionary['Nome']
    return False, None