"""Package entrypoint."""
import sys

if __package__ is None:
    # direct call of __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import ddns

if __name__ == "__main__":
    ddns.main()