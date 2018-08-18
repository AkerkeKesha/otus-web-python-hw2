import ast
from nltk import pos_tag

class ValidatorMixin:
    pass


class PyScriptParserMixin:

    def get_trees(self, paths):
        trees = []
        for path in paths:
            content = self.get_content(path)
            tree = ast.parse(content)
            trees.extend(tree)
        return trees

    def parse_functions(self, tree):
        print(self.get_target_type)
        if self.get_target_type() == 'func':
            return [node.name.lower()
                    for node in ast.walk(tree)
                        if isinstance(node, ast.FunctionDef)]
        #elif self.get_target_type() == 'var':

    def parse_words_of_given_pos(self, func_names):
        pos = self.get_part_of_speech()
        look_up_tag = self.get_look_up_tag(pos)
        words = []
        for func_name in func_names:
            if self.is_special_function(func_name):
                continue
            words.extend([word for word in func_name.split('_') if word])
        return [word for word, tag in pos_tag(words) if look_up_tag is tag]

    def get_look_up_tag(self, pos):
        look_up_tags = {'verb': 'VB', 'noun': 'NN'}
        return look_up_tags[pos]

    def is_special_function(self, f):
        return f.startswith('__') and f.endswith('__')

