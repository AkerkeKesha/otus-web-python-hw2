import sys

from utilities.parser import Parser


def clone(parser):
    pass


def parse(parser):
    part_of_speech = 'verb'
    target_type = 'func'
    directories = 'target_folder'

    parser.parse_most_common_words(part_of_speech, target_type, directories)
    return parser


def main():
    _, action_type = sys.argv
    parser = Parser()
    if action_type == 'parse':
        parse(parser)
    elif action_type == 'clone':
        clone(parser)
    parser.save_results()


if __name__=="__main__":
    main()