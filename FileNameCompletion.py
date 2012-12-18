import sublime_plugin
from glob import iglob
import os
import re

class FileNameCompletion(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if len(prefix) == 0:
            return []

        words = []
        for folder in sublime.active_window().folders():
            for filepath in iglob(folder + "**/%s*" % prefix):
                words.append(os.path.basename(filepath))
        return [(w,) * 2 for w in words]
