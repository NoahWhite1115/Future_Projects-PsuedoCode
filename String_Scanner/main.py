from globals.globals_category import CATEG_MAP

def main(category: str = '',keywords:list = [],custom_regex:str = '') -> list:
    match_and_string = []
    if category == '':
        if len(keywords) == 0:
            setup = CATEG_MAP[category]()
        else:
            setup = CATEG_MAP[category](keywords)

    else:
        if len(keywords) == 0:
            setup = CATEG_MAP[category]()
        else:
            setup = CATEG_MAP[category](keywords)
    # logic here to place in custom_Regex and use categories.py classes for building specific regex strings using REGEX globals and hard-coded logic
    return match_and_string

if __name__ == '__main__':
    main()