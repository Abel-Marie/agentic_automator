import re

def extract_code_block(text: str) -> str:
    """
    Extracts the content of a python code block from a markdown string.
    """
    pattern = r"```python\n(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Fallback: try to find just ``` if python is missing
    pattern_generic = r"```\n(.*?)```"
    match_generic = re.search(pattern_generic, text, re.DOTALL)
    if match_generic:
        return match_generic.group(1).strip()
        
    return text.strip() 
