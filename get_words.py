import sys
import logging
from utilities.parser import Parser
from utilities.cli import CommandLineInterface


def clone(parser):
    url = input("Enter a github repo url: ").lower()
    target_folder = input("Enter a folder to clone git repo to: ").lower()
    parser.clone_repo(url, target_folder)


def parse(parser, cli):
    part_of_speech = cli.get_part_of_speech()
    target_type = cli.get_target_type()
    directories = cli.get_directories()

    parser.parse_most_common_words(part_of_speech, target_type, directories)
    return parser


def main():
    logging.basicConfig(filename='message.log', format='%(asctime)s - %(message)s', filemode='a')
    cli = CommandLineInterface(sys.argv)
    action_type = cli.get_action_type()

    parser = Parser()
    if action_type == 'parse':
        parse(parser, cli)
    elif action_type == 'clone':
        clone(parser)
    parser.save_results()


if __name__ == "__main__":
    main()