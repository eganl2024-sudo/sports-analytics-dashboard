import os
import json
import re

notebook_dir = "notebooks"
notebooks = [f for f in os.listdir(notebook_dir) if f.endswith(".ipynb")]

def capitalize_text(text):
    # Split text by inline code or block code
    parts = re.split(r'(```.*?```|`.*?`)', text, flags=re.DOTALL)
    
    for i in range(0, len(parts), 2):
        part = parts[i]
        
        # Split part by newlines to preserve them exactly
        lines = part.split('\n')
        for j, line in enumerate(lines):
            # Find the first letter to capitalize (ignoring leading '#' or '-', etc)
            # A simple regex to find the first letter of a sentence/line
            
            # Capitalize first [a-z] letter in the line if it is preceded by non-letters or nothing
            lines[j] = re.sub(r'(^|^\s*#+\s*|^\s*-\s*|^\s*\*\s*|^\s*\d+\.\s*)([a-z])', 
                              lambda m: m.group(1) + m.group(2).upper(), lines[j])
            
            # Capitalize after period, question, exclamation and space
            lines[j] = re.sub(r'([.!?]\s+)([a-z])', 
                              lambda m: m.group(1) + m.group(2).upper(), lines[j])
        
        parts[i] = '\n'.join(lines)
        
    return "".join(parts)

for nb_file in notebooks:
    path = os.path.join(notebook_dir, nb_file)
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    modified = False
    for cell in nb.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = cell.get('source', [])
            if isinstance(source, list):
                new_source = []
                for line in source:
                    new_line = capitalize_text(line)
                    if new_line != line:
                        modified = True
                    new_source.append(new_line)
                cell['source'] = new_source
            elif isinstance(source, str):
                new_text = capitalize_text(source)
                if source != new_text:
                    cell['source'] = new_text
                    modified = True
                    
    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"Updated {nb_file}")

print("Done")
