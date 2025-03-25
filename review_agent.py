import re

def proofread(content):
    content = re.sub(r"\bteh\b", "the", content)  # Example typo correction
    return content

if _name_ == "_main_":
    content = "Teh HR industry is evolving."
    print(proofread(content))
