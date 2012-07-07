from console.console import Console
from pydrupal.models import Module
from pydrupal.services import ModuleService


class ModuleCreate(object):
    
    def __init__(self):
        pass

    def __call__(self):
        c = Console('')
        service = ModuleService()
        module = Module()
        module.name = c.console(intro="PyDrupal -- Create a new module",
                                prompt="Module Name: ")

        module.description    = c.console(prompt="Module Description: ")
        module.package        = c.console(default=None, prompt="Module Package [None]: ")
        module.version        = c.console(default='VERSION', prompt="Module Version [VERSION]: ")
        module.drupal_version = c.console(default='7.x', prompt="Supported Drupal Version [7.x]: ")

        if service.exists(module.name):
            overwrite = c.console(default='n', prompt="WARNING: This module already exists, overwrite? [y/N]: ")            
            overwrite = overwrite.lower()
            overwrite = True if overwrite == 'y' else False
            
            if overwrite:
                service.save(module)
            else:
                print("Aye Aye Cap'n, sending this process to walk the plank")
            
            return
        
        service.save(module)


class ModuleInfo(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        service = ModuleService()
        service.load(self.name)


class ModuleList(object):

    def __init__(self):
        pass

    def __call__(self):
        print("PyDrupal -- Listing all modules")
        service = ModuleService()
        modules = service.load()
        for  module in modules:
            print("{} : {}".format(module.name, module.description))