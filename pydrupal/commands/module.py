from cliff.command import Command

class Module(Command):

    def get_parser(self, prog_name):
        parser = super(Module, self).get_parser(prog_name)
        parser.add_argument('action', nargs='+')
        return parser

    def take_action(self, parsed_args):
        self.app.stdout.write('BAM!\n')
        print(parsed_args)