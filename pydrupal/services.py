from pydrupal.repositories import ModuleFilesystem
class ModuleService(object):

    def __init__(self):
        self.dao = ModuleFilesystem()

    def save(self, module):
        self.dao.save(module)

    def exists(self, module_name):
        return self.dao.exists(module_name)

    def load(self, module=None):
        if module is None:
            return self.dao.load_all()

        return self.dao.load_one(module)
        