#!/usr/bin/env python3
"""
Simple runner for Termux
IMMU-WEB YouTube Automation
"""

import os
import sys

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import main

if __name__ == "__main__":
    main()
