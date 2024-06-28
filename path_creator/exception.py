class DirNotFoundError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'DirNotFoundError {self.message}'
        else:
            return 'DirNotFoundError no such file or directory'
