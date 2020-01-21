class AgeException(Exception):
    def __init__(self):
        super().__init__('Age isn\'t INT')