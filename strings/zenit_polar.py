

def replace_zenit_polar(text):
    replacements = [('Z','P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]

    for old, new in replacements:
        text = text.replace(old, new)

    return text
