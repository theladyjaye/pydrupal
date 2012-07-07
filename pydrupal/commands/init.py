from cliff.command import Command

class Init(Command):

    def take_action(self, parsed_args):
        self.app.stdout.write('BAM!\n')
        print(parsed_args)