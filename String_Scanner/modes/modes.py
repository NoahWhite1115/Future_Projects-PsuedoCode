import re
from datetime import datetime
from sysadmin.sysadmin import SystemAdmin
import pandas as pd

class DefaultRegex():
    def __init__(self,custom_regex: str, multiple : bool):
        print('\n\n Initing Default')
        self.custom_regex = custom_regex
        self.multiple = multiple

    def findMatches(self, search_str:str, keywords: list = []) -> list:
        """
        Return list of all matches. Each match should be isolated string and not contain groups.
        Returned list will be evaluated for length in next step.
        """
        if self.multiple == False:
            for kw in keywords:
                comb_regex = self.buildRegex(keyword = kw, custom_regex = self.custom_regex) 
                matches = re.findall(pattern = comb_regex,string = search_str) #returns list with inner tuples for found_groupings
                #... Logic to parse through match results
                if len(matches) == 1:
                    return [self.isolateMatch(matches)]
                elif len(matches) > 1:
                    return self.checkDuplicates(matches = self.isolateMatches(matches))
            #Implied no matches here
            return []
        else:
            match_list = []
            for kw in keywords:
                comb_regex = self.buildRegex(keyword = kw, custom_regex = self.custom_regex) 
                matches = re.findall(pattern = comb_regex,string = search_str) #returns list with inner tuples for found_groupings
                #... Logic to parse through match results
                if len(matches) == 1:
                    match_list.append(self.isolateMatch(matches))
                elif len(matches) > 1:
                    match_list.extend(self.checkDuplicates(matches = self.isolateMatches(matches))) #TODO check duplicates too
            #Implied no matches here
            return match_list

    def trimDelims(self,delims:list):
        pass

    def checkDuplicates(self, matches: list) -> list:
        uniques = {matches[0]:True}
        for match in matches:
            if match not in uniques:
                uniques[match]=True
        return uniques.keys()
            
    def isolateMatch(self,match: any) -> str:
        if isinstance(match,tuple) or isinstance(match,list):
            match = match[0] #first index of tuple is the whole match
        elif isinstance(match,str):
            pass
        return match

    def evaluateReplace(self,match:str,search_str:str):
        return search_str

    def isolateMatches(self,matches:list = []) -> list:
        """
        Args:
            matches variable will be list with either strings or tuple
        """
        new_matches = []
        for match in matches:
            if isinstance(match,tuple):
                new_matches.append(match[0]) #first index of tuple is the whole match
            elif isinstance(match,str):
                new_matches.append(match)
        return new_matches

    def buildRegex(self,keyword:str,custom_regex: str) -> str:
        # logic to allow custom regex patterns per particular case i.e. if scanning pdf documents for different financial documents, each vendor has different format hence -> custom regex patterns
        return f"({keyword}{custom_regex})"
        

class Scan(DefaultRegex, SystemAdmin): #has Category properties Category.__dict__
    def __init__(self,categ_attribs:dict, multiple: bool, replace_all: bool):
        print('\n\n Init Scan')
        self.categ_attribs = categ_attribs # to store for debugging
        self.keywords = categ_attribs['keywords']
        self.custom_regex = categ_attribs['custom_regex']
        #self.replace_all = replace_all #NOTE Never used for this class
        DefaultRegex.__init__(self,custom_regex = categ_attribs['custom_regex'],  multiple = multiple)
        SystemAdmin.__init__(self)
        

class Replace(DefaultRegex, SystemAdmin):
    do_multiple = False
    def __init__(self,categ_attribs:dict, multiple: bool, replace_all: bool):
        print('\n\n Init Replace')
        self.categ_attribs = categ_attribs # to store for debugging
        self.keywords = categ_attribs['keywords']
        self.custom_regex = categ_attribs['custom_regex']
        self.replace_all = replace_all
        DefaultRegex.__init__(self,custom_regex = categ_attribs['custom_regex'], multiple = multiple)
        SystemAdmin.__init__(self)


    def evaluateReplace(self,match:list,search_str:str):
        replace_count = 1
        if self.replace_all == True:
            replace_count = -1
        for i in match:
            search_str = search_str.replace(i,'',replace_count)
        return search_str
        


