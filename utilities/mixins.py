import ast
from nltk import pos_tag

from utilities.logger import Logger


class ValidatorMixin:

    def __init__(self):
        self.error_message = "error in input parameters for this program"
        self.action_types = ['parse', 'clone']
        self.parts_of_speech = ['verb', 'noun']
        self.target_types = ['func', 'var']

    def validate_action_type(self, action_type):
        if action_type not in self.action_types:
            Logger().error("Wrong action type.\n")
            raise AttributeError(self.error_message)

    def validate_part_of_speech(self, part_of_speech):
        if part_of_speech not in self.parts_of_speech:
            Logger().error("Not supported part of speech.\n")
            raise AttributeError(self.error_message)

    def validate_target_type(self, target_type):
        if target_type not in self.target_types:
            Logger().error("Not supported target type.\n")
            raise AttributeError(self.error_message)

    def validate_directory(selfs, directory):
        pass


class PyScriptParserMixin:

    def get_trees(self, paths):
        trees = []
        for path in paths:
            content = self.get_content(path)
            tree = ast.parse(content)
            trees.append(tree)
        return trees

    def parse_functions(self, tree):
        if self.get_target_type() == 'func':
            return [node.name.lower()
                    for node in ast.walk(tree)
                        if isinstance(node, ast.FunctionDef)]
        elif self.get_target_type() == 'var':
            return [node.targets[0].id.lower()
                    for node in ast.walk(tree)
                        if isinstance(node, ast.Assign)]

    def parse_words_of_given_pos(self, func_names):
        pos = self.get_part_of_speech()
        look_up_tag = self.get_look_up_tag(pos)
        words = []
        for func_name in func_names:
            if self.is_special_function(func_name):
                continue
            words.extend([word for word in func_name.split('_') if word])
        return [word for word, tag in pos_tag(words) if look_up_tag in tag]

    def get_look_up_tag(self, pos):
        look_up_tags = {'verb': 'VB', 'noun': 'NN'}
        return look_up_tags[pos]

    def is_special_function(self, f):
        return f.startswith('__') and f.endswith('__')

