from utilities.mixins import ValidatorMixin


class CommandLineInterface(ValidatorMixin):

    def __init__(self, arguments):
        super().__init__()
        self.action_type = None
        self.part_of_speech = None
        self.target_type = None
        self.directories = []

        action_type = self.validate_cli(arguments)
        self.set_action_type(action_type)

    def validate_cli(self, arguments):
        if len(arguments) != 2:
            raise AttributeError(self.error_message)
        _, action_type = arguments
        self.validate_action_type(action_type)
        return action_type

    def set_action_type(self, action_type):
        self.action_type = action_type

    def get_action_type(self):
        return self.action_type

    def set_part_of_speech(self, part_of_speech):
        self.validate_part_of_speech(part_of_speech)
        self.part_of_speech = part_of_speech

    def get_part_of_speech(self):
        while not self.part_of_speech:
            inp = input("Enter part of speech: verb or noun: ").lower()
            self.set_part_of_speech(inp)
        return self.part_of_speech

    def set_target_type(self, target_type):
        self.validate_target_type(target_type)
        self.target_type = target_type

    def get_target_type(self):
        while not self.target_type:
            inp = input("Enter target type: func or var: ").lower()
            self.set_target_type(inp)
        return self.target_type

    def add_directory(self, directory):
        self.validate_directory(directory)
        self.directories.append(directory)

    def set_directories(self, directories):
        for directory in directories:
            self.validate_directory(directory)
        self.directories = directories

    def get_directories(self):
        while True:
            inp = input("""Enter a folder path to be parsed (once finished type 'done'): """).lower()
            if inp == 'done':
                break
            self.add_directory(inp)
        return self.directories



