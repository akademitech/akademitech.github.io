with open('generate_tutorials.py', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('    {\n        "filename": "project-web.html"')
end_idx = content.find('    {\n        "filename": "pengenalan-css.html"', start_idx)

if start_idx != -1 and end_idx != -1:
    block = content[start_idx:end_idx]
    content = content[:start_idx] + content[end_idx:]
    
    insert_pos = content.find(']\n\n# Generate Next')
    if insert_pos != -1:
        content = content[:insert_pos] + block + content[insert_pos:]
        with open('generate_tutorials.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
    else:
        print("No insert pos")
else:
    print("No indices")
