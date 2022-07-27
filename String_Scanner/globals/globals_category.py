from ast import Add
from sre_parse import CATEGORIES
from categories.categories import *

CATEG_MAP = \
{
    'Balance':Balance,
    'Name':Name,
    'Date':Date,
    'SSN':SSN,
    'Address':Address,
    'CreditCards':CreditCards,
    'Property_IDs':Property_IDs,
    'File_Numbers':File_Numbers
}
