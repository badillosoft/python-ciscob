import re

# Return the text with regex pattern masked
def mask(text):
    pattern = "(\d{4}[\-\s]?){4}"
    new_text = re.sub(pattern, "XXXX-XXXX-XXXX-XXXX", text)
    return new_text

def mask3(text):
    pattern = "(\d{4}[\-\s]?){3}"
    new_text = re.sub(pattern, "XXXX-XXXX-XXXX-", text)
    return new_text

def mask2(text):
    pattern = "((\d{4}[\-\s]?){3})(\d{4})"
    new_text = list(text)
    for m in re.finditer(pattern, text):
        # Group 1: XXXX-XXXX-XXXX
        i, j = m.span(1) # i - start index for group 1. j - end index for group 1
        new_text[i:j] = "XXXX-XXXX-XXXX-"
    return "".join(new_text)