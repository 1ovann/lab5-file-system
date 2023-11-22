class File:
    # pylint: disable=R0903
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size

    def __str__(self):
        return f"{self.name}.{self.extension} ({self.size} bytes)"


class Folder:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.folders = []

    def add_file(self, file):
        self.files.append(file)

    def add_folder(self, folder):
        self.folders.append(folder)

    def print_contents(self, indent=0):
        print("  " * indent + self.name + "/")
        for file in self.files:
            print("  " * (indent + 1) + str(file))
        for folder in self.folders:
            folder.print_contents(indent + 1)

    def get_longest_path(self):
        if not self.folders:
            return [self.name]

        longest_path = max(folder.get_longest_path() for folder in self.folders)
        return [self.name] + longest_path


def main():
    file1 = File("file1", "txt", 1024)
    file2 = File("file2", "doc", 2048)
    file3 = File("file3", "jpg", 3072)

    folder1 = Folder("folder1")
    folder2 = Folder("folder2")
    folder3 = Folder("folder3")

    folder1.add_file(file1)
    folder2.add_file(file2)
    folder3.add_file(file3)

    folder1.add_folder(folder2)
    folder2.add_folder(folder3)

    folder1.print_contents()

    print("Найдовший шлях: ", "/".join(folder1.get_longest_path()))


if __name__ == "__main__":
    main()
