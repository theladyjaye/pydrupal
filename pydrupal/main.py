import sys
import argparse
from cliff.app import App
from cliff.commandmanager import CommandManager

from pydrupal import actions
from pydrupal.utils import env
from pydrupal.utils import find_modules


class PyDrupal(App):
    def __init__(self):
        super(PyDrupal, self).__init__(
            description='PyDrupal',
            version='0.1',
            command_manager=CommandManager('pydrupal.commands')
            )

# def get_args():
#     a_parser = argparse.ArgumentParser(description='PyDrupal Command Line Options')
#     a_parser.add_argument('action', metavar='action', type=str,
#                    help='Action to perform [create]')

#     return a_parser.parse_args()

def main(argv=sys.argv[1:]):
    env['module_path'] = find_modules()
    app = PyDrupal()
    return app.run(argv)    
    
    # args = get_args()
    
    # action = args.action.lower()
    # worker = None

    # if action == 'create':
    #     worker = actions.ModuleCreate()
    # elif action == 'list':
    #     worker = actions.ModuleList()

    # worker()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))