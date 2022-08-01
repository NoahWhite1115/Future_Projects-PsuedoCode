from categories.categories import *
from modes.modes import *

CATEG_MAP = \
{
    'Balance':Balance,
    'Name':Name,
    'Date':Date,
    'SSN':SSN,
    'Address':Address,
    'CreditCards':CreditCards,
    'Property_IDs':Property_IDs,
    'File_Numbers':File_Numbers,
    'Universal':Universal
}
MODE_MAP = \
{
    'Scan':Scan,
    'Replace':Replace
}

RE_ORDER = 'keywords, re_format'
CLI_ORDER = "debug, category, mode, custom_regex, file_type, cases, multiple, replace_all, repl_vals, open_file, choose_group"


