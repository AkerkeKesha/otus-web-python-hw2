import ast
from nltk import pos_tag

class ValidatorMixin:
    pass


class PyScriptParserMixin:

    def get_trees(self, paths):
        return None

    def parse_functions(self, tree):
        pass

    def parse_words_of_given_pos(self, func_names):
        return None
