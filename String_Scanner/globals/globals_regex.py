ANY_DELIM = "[ \-\.\_\/\,\;]"
ANY_CHAR = "[a-zA-Z]"
ANY_NUM = "[\d]"

ANY_FLOAT = "(((([\d]+\,?)+)|[\d]+)\.[\d]+)"
ANY_WORD_PHRASE = f"(({ANY_DELIM}+{ANY_CHAR}+)*{ANY_DELIM}*)"
ANY_PHRASE = f"(({ANY_DELIM}+({ANY_CHAR}+|{ANY_NUM}+))*{ANY_DELIM}*)"
NL = r"\n"
EVERYTHING = "[\s\S]*"

#(([ \-\.\_\/\,\;]+[a-zA-Z]+)*[ \-\.\_\/\,\;]+\\n)