import re
from globals.globals_regex import *
class UTIL():
    def findMatch(self,keywords: list = [],search_str:str = ''):
        for kw in keywords:
            comb_regex = self.build_regex(kw) 
            match = re.findall(comb_regex,search_str) #returns list with inner tuples for found_groupings
            #... Logic to parse through match results
            if len(match) == 1:
                return match
    def removeGroupings(self,matches:list = []) -> list:
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
    def build_regex(self,keyword) -> str:
        # logic to allow custom regex patterns per particular case i.e. if scanning pdf documents for different financial documents, each vendor has different format hence -> custom regex patterns
        return f"{keyword}" #TODO: regex groupings from globals_regex.py containing fixed delimiters and other search parameters to be added to this variable


