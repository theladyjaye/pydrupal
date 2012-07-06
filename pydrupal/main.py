import sys
import argparse
from pydrupal import actions
from pydrupal.utils import env
from pydrupal.utils import find_modules

def get_args():
    a_parser = argparse.ArgumentParser(description='PyDrupal Command Line Options')
    a_parser.add_argument('action', metavar='action', type=str,
                   help='Action to perform [create]')

    return a_parser.parse_args()

def main():
    env['module_path'] = find_modules()
    
    args = get_args()
    
    action = args.action.lower()
    worker = None

    if action == 'create':
        worker = actions.ModuleCreate()
    elif action == 'list':
        worker = actions.ModuleList()

    worker()


if __name__ == "__main__":
    sys.exit(main())