#!/usr/bin/env python3
"""Entry point for the DSA learning agent. Run `python .github/agents/scripts/agent.py --help`."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dsa_agent.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
