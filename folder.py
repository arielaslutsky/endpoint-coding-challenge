class Folder:
    def __init__(self, name):
        self.name = name
        self.sub_folders = {}
        self.files = []

    def create_sub_folder(self, name):
        self.sub_folders[name] = Folder(name)

    def __str__(self):
        # Custom string representation
        return f"Folder(name: {self.name}, sub folders: {', '.join(self.sub_folders.keys())})"

