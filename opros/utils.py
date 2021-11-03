
def create_choice(*args):
    choice = []
    for arg in args:
        if arg:
            choice.append([arg, arg])
    return choice