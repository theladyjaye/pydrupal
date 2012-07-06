import os
from pydrupal.utils import env
from pydrupal.utils import ModuleInfoParser
from pydrupal.models import Module

class ModuleFilesystem(object):
    
    def save(self, module):

        if self._can_load_module(module.name):
            self._write(module)
            return

        self._create_module_directory(module.name)
        self._write(module)


    def exists(self, module_name):
        return self._can_load_module(module_name)
    

    def load_one(self, module):
        if self._can_load_module(module):
            return [self._load_info(module)]


    def load_all(self):
        collection = []
        
        for current in os.listdir(env['module_path']):
            if self._can_load_module(current):
                collection.append(self._load_info(current))

        return collection
        

    def _create_module_directory(self, module_name):
        module_name = module_name.lower()
        path = "{}/{}".format(env['module_path'], module_name)
        os.mkdir(path)

    def _write(self, module):
        module_name = module.name.lower()
        path = "{}/{}/{}.info".format(env['module_path'], 
                                      module_name, 
                                      module_name)
        with open(path, 'w') as f:
            f.write("name = {}\n".format(module.name))
            f.write("description = {}\n".format(module.description))
            
            if module.package:
                f.write("package = {}\n".format(module.package))

            f.write("version = {}\n".format(module.version))
            f.write("core = {}\n".format(module.drupal_version))

    def _can_load_module(self, module_name):
        module_name = module_name.lower()
        module_path = env['module_path']
        path = "{}/{}".format(module_path, module_name)
        if os.path.isdir(path):
            if os.path.isfile("{}/{}.info".format(path, module_name)):
                return True

        return False
        
    def _load_info(self, module_name):
        module_name = module_name.lower()
        path = "{}/{}/{}.info".format(env['module_path'], 
                                      module_name, 
                                      module_name)
        config = ModuleInfoParser()
        config.read(path)

        obj = Module()
        obj.name           = config['name']
        obj.description    = config['description']
        obj.package        = config['package']
        obj.drupal_version = config['core']
        obj.version        = config['version']

        return obj