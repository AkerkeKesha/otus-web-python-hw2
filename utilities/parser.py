import os
import collections

from utilities.mixins import ValidatorMixin, PyScriptParserMixin


class Parser(ValidatorMixin, PyScriptParserMixin):
    def __init__(self):
        self.script_files = []
        self.parts_of_speech = None
        self.words_count = None
        self.directories = []
        self.most_common_words = collections.Counter()

    def parse_most_common_words(self, part_of_speech, target_folder, directories):
        pass

    def save_results(self):
        pass




