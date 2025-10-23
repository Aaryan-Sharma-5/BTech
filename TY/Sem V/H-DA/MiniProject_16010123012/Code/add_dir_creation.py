"""
Add directory creation to all scripts
"""

from pathlib import Path

scripts_to_update = [
    ('scripts/3)EDA.py', ['"outputs/visualizations"']),
    ('scripts/4)forecasting_with_arima.py', ['"outputs/visualizations"', '"outputs/metrics"']),
    ('scripts/5)model_evaluation.py', ['"outputs/visualizations"', '"outputs/metrics"']),
    ('scripts/6)forecasting_with_sarima.py', ['"outputs/visualizations"', '"outputs/metrics"']),
    ('scripts/7)model_evaluation_sarima.py', ['"outputs/visualizations"', '"outputs/metrics"']),
]

dir_creation_code = """from pathlib import Path

# Ensure required directories exist
Path('data').mkdir(parents=True, exist_ok=True)
Path('outputs/visualizations').mkdir(parents=True, exist_ok=True)
Path('outputs/metrics').mkdir(parents=True, exist_ok=True)
"""

for script_path, dirs_needed in scripts_to_update:
    print(f"\nProcessing: {script_path}")
    
    with open(script_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has Path import
    if 'from pathlib import Path' in content and "Path('outputs" in content:
        print(f"  ✓ Already has directory creation")
        continue
    
    # Find the imports section (after docstring, before first function/class)
    lines = content.split('\n')
    insert_position = 0
    in_docstring = False
    docstring_char = None
    
    for i, line in enumerate(lines):
        # Track docstrings
        if '"""' in line or "'''" in line:
            if not in_docstring:
                in_docstring = True
                docstring_char = '"""' if '"""' in line else "'''"
                # Check if docstring ends on same line
                if line.count(docstring_char) == 2:
                    in_docstring = False
            elif docstring_char in line:
                in_docstring = False
                continue
        
        # Skip if in docstring
        if in_docstring:
            continue
            
        # Find last import line
        if line.strip().startswith('import ') or line.strip().startswith('from '):
            insert_position = i + 1
    
    # Insert the directory creation code
    if insert_position > 0:
        # Add Path import if not present
        if 'from pathlib import Path' not in content:
            lines.insert(insert_position, 'from pathlib import Path')
            insert_position += 1
        
        # Add blank line and directory creation
        lines.insert(insert_position, '')
        insert_position += 1
        lines.insert(insert_position, "# Ensure required directories exist")
        insert_position += 1
        lines.insert(insert_position, "Path('data').mkdir(parents=True, exist_ok=True)")
        insert_position += 1
        lines.insert(insert_position, "Path('outputs/visualizations').mkdir(parents=True, exist_ok=True)")
        insert_position += 1
        lines.insert(insert_position, "Path('outputs/metrics').mkdir(parents=True, exist_ok=True)")
        
        # Write back
        with open(script_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"  ✅ Added directory creation code")
    else:
        print(f"  ❌ Could not find insertion point")

print("\n" + "="*70)
print("✅ Directory creation added to all scripts!")
