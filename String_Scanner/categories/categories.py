from globals.globals_regex import *
class Balance:
    def __init__(self):
        self.keywords=\
            [
                'NEW BALANCE '
            ]
        self.custom_regex = f"(\$?{ANY_FLOAT}{ANY_PHRASE}?{NL})"
        self.repl_vals = []
        self.choose_group = '2'
#((([\d]{3}\,)+[\d]{3})|[\d]+)(\.[\d]+)
class Name:
    def __init__(self):
        self.keywords=\
            [
                'Name'
            ]
        self.custom_regex = 'Default'
        self.repl_vals = []
        self.choose_group = '2'

class Date:
    def __init__(self):
        self.keywords=\
            [
                'Date'
            ]
        self.custom_regex = 'Default'
        self.repl_vals = []
        self.choose_group = '2'

class SSN:
    def __init__(self):
        self.keywords=\
            [
                'SSN'
            ]
        self.custom_regex = 'Default'
        self.repl_vals = []
        self.choose_group = '2'

class Address:
    def __init__(self):
        self.keywords=\
            [
                'Address'
            ]
        self.custom_regex = 'Default'
        self.repl_vals = []

class CreditCards:
    def __init__(self):
        self.keywords=\
            [
                'CreditCards'
            ]
        self.custom_regex = 'Default'
        self.repl_vals = []
        self.choose_group = '2'

class Property_IDs:
    def __init__(self):
        self.keywords=\
            [
                'Property_IDs'
            ]
        self.custom_regex = 'Default'
        self.repl_vals = []

class File_Numbers:
    def __init__(self):
        self.keywords=\
            [
                'File_Numbers'
            ]
        self.custom_regex = 'Default'
        self.repl_vals = []
        self.choose_group = '2'

class Universal:
    def __init__(self):
        self.keywords=\
            [
                ''
            ]
        self.custom_regex = ''
        self.repl_vals = []
        self.choose_group = ''