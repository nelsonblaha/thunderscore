import sublime, sublime_plugin  
  
# Extends TextCommand so that `() receives a View to modify.  
class ThunderscoreCommand(sublimeplugin.TextCommand):  
    def run(self, view, args):  
        