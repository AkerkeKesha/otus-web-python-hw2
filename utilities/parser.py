import os
import collections

from utilities.mixins import ValidatorMixin, PyScriptParserMixin


class Parser(ValidatorMixin, PyScriptParserMixin):
    def __init__(self):
        self.script_files = []
        self.part_of_speech = None
        self.target_type = None
        self.directories = []
        self.most_common_words = collections.Counter()

    def set_part_of_speech(self, part_of_speech):
        self.part_of_speech = part_of_speech

    def set_target_type(self, target_type):
        self.target_type = target_type

    def set_directories(self, directories):
        self.directories = directories

    def parse_most_common_words(self, part_of_speech, target_type, directories):
        self.set_part_of_speech(part_of_speech)
        self.set_target_type(target_type)
        self.set_directories(directories)

        paths = self.get_paths_to_scripts_file()
        words = self.get_words(paths)
        counted_words = collections.Counter(words)
        self.set_most_common_words(counted_words.most_common())

    def get_paths_to_scripts_file(self, extension = '.py'):
        paths = []
        for directory in self.directories:
            for dirname, _, filenames in os.walk(directory, topdown=True):
                paths.extend([os.path.join(dirname, filename)
                              for filename in filenames if filename.endswith(extension)])
        return paths

    def get_words(self, paths):
        return
        # content_holding_tree = self.get_trees(paths)
        # func_names = []
        # for tree in content_holding_tree:
        #     func_names.extend(self.parse_functions(tree))
        # return self.parse_words_of_given_pos(func_names)


    def set_most_common_words(self, counter):
        self.most_common_words = counter


    def save_results(self):
        pass




