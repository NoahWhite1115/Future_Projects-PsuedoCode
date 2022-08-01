import os
from datetime import datetime
from util.util import *

class SystemAdmin():
    def __init__(self, open_file: bool = False):
        print('\n\n Init SystemAdmin')
        self.open_file = open_file

    def findFilesbyExt(self,file_type:str = '.txt', location: str = os.PathLike, dict_keys: bool = False) -> list:
        if file_type != None:
            if (not os.path.isdir(location)) and (not os.path.isfile(location)):
                return []
            file_list = []
            for file in os.scandir(location):
                f_path = file.path
                if os.path.isfile(f_path) and f_path.endswith(file_type):
                    file_list.append(f_path)
                elif os.path.isdir(f_path):
                    file_list.extend(self.findFilesbyExt(file_type = file_type, location = f_path))
            if dict_keys:
                dict_obj = {}
                for f in file_list:
                    dict_obj[f] = True
                file_list = dict_obj
            return file_list

    def extractText(self,file: os.PathLike) -> str:
        if self.open_file == True:
            with open(file = file, mode = 'r') as f:
                txt = ''.join(f.readlines())
                f.close()
                return txt
        else:
            return file

    def writeText(self,file: os.PathLike, text:str = '') -> str:
        lines = text.split("\\n', '")
        lines[0] = lines[0].replace("['",'')
        lines[len(lines)-1]= lines[len(lines)-1].replace("']",'')
        with open(file = file, mode = 'w') as f:
            f.writelines(text)
            f.close()
            return text

    def logger(self,debug:bool = True,vars:dict= {}, custom:str = '',isolate: list = []) -> None:
        if debug:
            var_log = []
            vars_length = len(vars)
            for index, var in enumerate(vars):
                if len(isolate) >=1 and not var in isolate:
                    continue
                if index == vars_length - 1:
                    var_log.append(f"\r{var} ------------- Type: {type(vars[var])} ---------------------- Value:----------------\n{vars[var]}")
                    break
                var_log.append(f"\r{var} ------------- Type: {type(vars[var])} ---------------------- Value:----------------\n{vars[var]}")
            var_log = '\n'.join(var_log)
            print(\
            f"""
            \r\n------------DEBUG LOGS-------------Time: {datetime.now()}\n
            {var_log}
            {custom}

            """)
    def traceRelevantErrors(self,error_log:list,script_loc:os.PathLike,latest = False):
        new_error_log = []
        proj_files_dict = self.findFilesbyExt(file_type = '.py',location = script_loc.replace('main.py',''), dict_keys=True)
        for error_file in error_log:
            file_name = os.path.join(error_file.split(", line")[0].replace(' ','').replace('"',''))
            #print(os.path.isfile(file_name), ' ',file_name)
            if file_name in proj_files_dict:
                new_error_log.append(error_file)
            #print(file_name)
        if latest:
            print('\nMy Error\n')
            print(new_error_log.pop())
        
        else:
            print('\nMy Error\n')
            print('\n'.join(new_error_log))
        #print('\n Original Below: \n')
        #print('\n'.join(error_log))
            

        pass

