from globals.globals_config import CATEG_MAP, MODE_MAP, CLI_ORDER, RE_ORDER
from util.util import kwargsReturnValues, splitStringbyDelim
import click, traceback
from sysadmin.sysadmin import SystemAdmin as SA

sys_admin = SA()

"""
Author: Hung Tran

Summary:
    Goal of this utility is to find text matches from any giving string or extracted text of files within a directory.
    Matches are found using combined regex formats, dynamically adjusted per the keywords sent in and custom category classes with their own unique formats.
    There are primarily two different modes or actions to take with the results of the match using: Scan or Replace
    Scan will only give us the results of the match. Replace will give us the results of the match while replacing the match with empty for now. #TODO replace with format/word of our choosing.
    Other optional arguments will change functionality of operation. Detais listed below in CLI Args.

CLI Args:
    Keywords: List, List of target words to search in text. First argument for building regex with customized formats
    Location: String, text string, filepath, or directory. All text based on extension argument will be extracted for text
    Debug: Bool, debug mode will disable/enable loggers placed inside main.py
    Mode: String, Choose different modes - Scan, Replace, etc.
    Category: String, Choose one of pre-made categories for searching, i.e. Balance, SSN, Date, etc.
    Custom_Regex: Raw String, Use your own regex to overwrite category or General Regex in Universal category class (when no category is specified)
    File_Type: String, Extension type used to find files within location
    Cases: String, Very optional. In the event clients want to build their own custom classes #TODO not implemented yet
    Multiple: Bool, True or False to set return values for scan/replace to all matches or single match

Return: None
"""

@click.command()
@click.option("--keywords", multiple = True, default = []) #target for text or prepended phrases for finding type of data
@click.option("--location",type = str,required = True) #directory/filepath
@click.option("--debug",type=bool,default = True) #additional special cases #TODO for how to use
@click.option("--mode",type=str,default = "Scan") #to scan or replace match found inside str
@click.option("--category",type=str,default = "Universal") #to scan or replace match found inside str
@click.option("--custom_regex",type=str, default = "") #custom regex option to overwrite regexBuilder
@click.option("--file_type",type=str,default = '') #are we passing in a str or a file path
@click.option("--cases",type=str,default = '') #additional special cases #TODO for how to use
@click.option("--multiple",type=bool,default = False) #additional special cases #TODO for how to use
@click.option("--replace_all",type=bool,default = False) #additional special cases #TODO for how to use
@click.option("--repl_vals", multiple = True,default=[])  #target for text or prepended phrases for finding type of data
@click.option("--open_file", type = bool, default = False) #Set mode to open file and extract text. If false and looking at a file, only scan through filename
@click.option("--choose_group",type = str, default = '')  #Choose group in regex match results to get exact match
def main(keywords:list,location:str,**kwargs:dict) -> None:
    try:
            #print(kwargs)
        original_location = str(location)
        var_names = splitStringbyDelim(CLI_ORDER,[','],[' '])
        debug, category, mode, custom_regex, file_type, cases, multiple, replace_all, repl_vals, open_file, choose_group= \
            kwargsReturnValues(kwargs = kwargs, var_names = var_names)
        debug_dict = kwargs
        debug_dict['original_src'], debug_dict['location']=\
            original_location, location
        categ_obj = CATEG_MAP[category]()
        if len(keywords) != 0:
            categ_obj.keywords = keywords
            debug_dict['keywords'] = keywords
        if custom_regex != "":
            categ_obj.custom_regex = custom_regex
            debug_dict['custom_regex'] = custom_regex
        if len(repl_vals) != 0:
            categ_obj.repl_vals = repl_vals
            debug_dict['repl_vals'] = repl_vals
        mode_obj = MODE_MAP[mode](categ_attribs = categ_obj.__dict__, multiple = multiple, replace_all = replace_all, repl_vals = repl_vals, open_file = open_file)
        debug_dict['keywords'] = mode_obj.keywords
        #print(kwargs)
        #mode_obj.logger(debug = debug,vars = debug_dict)

        files = []
        files = mode_obj.findFilesbyExt(location = location, file_type = file_type)
        debug_dict['files'] = files
        if len(files) == 0:
            debug_dict['custom_regex']=mode_obj.buildRegex(keyword = f"############{str(mode_obj.keywords)}############", custom_regex = mode_obj.custom_regex)
            match = mode_obj.evaluateMultiple(search_str= location, keywords = mode_obj.keywords)
            location = mode_obj.evaluateReplace(matches = match, search_str = location)   
            debug_dict['location'], debug_dict['match']=  location , match
            #mode_obj.logger(debug = True,vars = debug_dict, isolate = ['location'])
        else:
            for file in files:
                extracted_text = mode_obj.extractText(file = file)
                debug_dict['custom_regex']=mode_obj.buildRegex(keyword = f"############{str(mode_obj.keywords)}############", custom_regex = mode_obj.custom_regex)
                match = mode_obj.evaluateMultiple(search_str= extracted_text, keywords = mode_obj.keywords)
                location = mode_obj.evaluateReplace(search_str = extracted_text, matches = match)   
                debug_dict['location'], debug_dict['match']=  location , match
                mode_obj.logger(debug = debug,vars = debug_dict, isolate = ['keywords','repl_vals','location','custom_regex','match'])

    except BaseException:
        error_log = traceback.format_exc().split('File')
        sys_admin.traceRelevantErrors(error_log = error_log, script_loc =  __file__, latest = True)
        

    # logic here to place in custom_Regex and use categories.py classes for building specific regex strings using REGEX globals and hard-coded logic
if __name__ == '__main__':
    T= True
    if T:
        main(\
            [
                "--debug", True,
                #"--keywords", r'NEW BALANCE ',
                #"--keywords", r'def',
                #"--keywords", r'logger',
                #"--keywords",r"datetime",
                "--location", r"c:\Users\hduon\Documents\Future_Projects-PsuedoCode\test files",#__file__,
                "--mode", 'Replace',
                "--category", "Balance",
                #"--custom_regex",r"",
                "--file_type", '.txt',
                #"--cases","Capital One",
                "--multiple", True,
                "--replace_all", True,
                "--repl_vals","############Replaced############",
                #"--repl_vals","test2",
                #"--repl_vals","test3",
                #"--repl_vals","test4",
                "--open_file", True,
                #"--choose_group", 2
            ])
    else:
        main()
    # python main.py --keywords import --keywords def --location 'C:\Users\hduon\Documents\Future_Projects-PsuedoCode\test files' --file_type '.py' --mode Replace --replace_all True --multiple True