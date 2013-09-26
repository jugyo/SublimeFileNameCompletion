import sublime, sublime_plugin
from glob import iglob
import os

class FileNameCompletion(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if len(prefix) == 0:
            return []

        words = set()
        for folder in sublime.active_window().folders():
            words.add(os.path.basename(folder))
            patterns = [
                "%s/%s*" % (folder, prefix),
                "%s/*/%s*" % (folder, prefix),
                "%s/*/*/%s*" % (folder, prefix),
                "%s/*/*/*/%s*" % (folder, prefix)
            ]
            for pattern in patterns:
                for filepath in iglob(pattern):
                    words.add(os.path.basename(filepath))

        words = list(words)
        words.sort()
        return [(w,) * 2 for w in words]
