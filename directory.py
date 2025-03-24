import sys
from folder import Folder

class Directory:
    def __init__(self, name="Home"):
        self.name = name
        self.sub_folders = {}

    def create(self, path):
        folder_names = path.split("/")
        i = 1
        if folder_names[0] in self.sub_folders:
            parent = self.sub_folders[folder_names[0]]
        else:
            parent = Folder(folder_names[0])
            self.sub_folders[folder_names[0]] = parent
        while i < len(folder_names):
            if folder_names[i] not in parent.sub_folders:
                parent.create_sub_folder(folder_names[i])
            folder = parent.sub_folders[folder_names[i]]
            parent = folder
            i+=1

    def list_folders(self, parent, distance_from_root, output_lines):
        if not parent.sub_folders:
            return
        for name in sorted(list(parent.sub_folders.keys())):
            output_lines.append("  " * distance_from_root + name)
            self.list_folders(parent.sub_folders[name], distance_from_root + 1, output_lines)

    def move(self, source, target):
        path = source.split("/")
        folder = self.sub_folders[path[0]]
        if len(path) == 1:
            del self.sub_folders[path[0]]
        i = 1
        while i < len(path):
            curr = folder.sub_folders[path[i]]
            if curr.name == path[-1]:
                del folder.sub_folders[path[i]]
            folder = curr
            i+=1
        target_path = target.split("/")
        i = 0
        curr = self.sub_folders[target_path[0]]
        while i < len(target_path):
            if curr.name == target_path[-1]:
                curr.sub_folders[folder.name] = folder
                break
            curr = curr.sub_folders[target_path[i]]
            i+=1

    def delete(self, source, output_lines):
        path = source.split("/")
        if path[0] not in self.sub_folders:
            output_lines.append(f"Cannot delete {source} - {path[0]} does not exist")
            return
        if len(path) == 1:
            del self.sub_folders[path[0]]
        i = 1
        folder = self.sub_folders[path[0]]
        while i < len(path):
            if path[i] not in folder.sub_folders:
                output_lines.append(f"Cannot delete {source} - {folder[i]} does not exist")
            curr = folder.sub_folders[path[i]]
            if curr.name == path[-1]:
                del folder.sub_folders[path[i]]
            folder = curr
            i+=1

    def main(self):
        if len(sys.argv) <= 1:
            print("No input file provided.")
            return
        input_file = sys.argv[1]
        with open(input_file, "r") as input:
            lines = input.readlines()
 
        output_lines = []
        for l in lines:
            line_list = l.strip().split(" ")
            command = line_list[0]
            output_lines.append(l.strip())
            if command == "CREATE":
                if len(line_list) > 1:
                    path = line_list[1]
                    self.create(path)
            if command == "LIST":
                self.list_folders(self, 0, output_lines)
            if command == "MOVE":
                if len(line_list) > 2:
                    self.move(line_list[1], line_list[2])
            if command == "DELETE":
                if len(line_list) > 1:
                    self.delete(line_list[1], output_lines)
        output_file = "output.txt"
        if len(sys.argv) > 2:
            output_file = sys.argv[2]
        with open(output_file, "w") as output:
            i = 0
            while i < len(output_lines) - 1:
                output.write(output_lines[i] + "\n")
                i+=1
            output.write(output_lines[i])

if __name__ == "__main__":
    directory = Directory()
    directory.main()

