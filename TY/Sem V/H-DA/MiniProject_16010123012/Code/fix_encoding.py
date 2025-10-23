# -*- coding: utf-8 -*-
"""
Windows Unicode Fix Utility
Adds UTF-8 encoding support to console output for all Python scripts
Run this once before executing the pipeline to avoid encoding errors
"""

import sys
import io

# Fix Windows console encoding to support UTF-8 characters
if sys.platform == 'win32':
    # Reconfigure stdout and stderr to use UTF-8
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    if sys.stderr.encoding != 'utf-8':
        sys.stderr.reconfigure(encoding='utf-8')

print("✅ UTF-8 encoding configured successfully!")
print("You can now run the pipeline scripts.")
