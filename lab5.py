class File:
    """
    Represents a file with its name, extension, and size.
    """
    def __init__(self, name, extension, size):
        """
        Initializes a File object.

        Args:
        - name (str): The name of the file.
        - extension (str): The extension of the file.
        - size (int): The size of the file in bytes.
        """
        self.name = name
        self.extension = extension
        self.size = size

    def __str__(self):
        """
        Returns a string representation of the File object.
        """
        return f"{self.name}.{self.extension} ({self.size} bytes)"


class Folder:
    """
    Represents a folder containing files and subfolders.
    """
    def __init__(self, name):
        """
        Initializes a Folder object.

        Args:
        - name (str): The name of the folder.
        """
        self.name = name
        self.files = []
        self.folders = []

    def add_file(self, file):
        """Adds a File object to the current folder."""
        self.files.append(file)

    def add_folder(self, folder):
        """Adds a subfolder (Folder object) to the current folder."""
        self.folders.append(folder)

    def display_folder_tree(self, prefix=""):
        """
        Displays the folder structure.

        Args:
        - prefix (str): Indentation in the folder tree.
        """
        print(prefix + self.name + "/")
        for file in self.files:
            print(prefix + str(file))
        for folder in self.folders:
            folder.display_folder_tree(prefix + "  ")

    def get_longest_path(self, path=""):
        """
        Retrieves the longest path of files within the folder structure.

        Args:
        - path (str): The current path while going through
         the folder structure.

        Returns:
        - str: The longest path in the folder structure +
        the longest named file in this path.
        """
        current_path = path + self.name + "/"
        longest_path = current_path

        for file in self.files:
            file_path = current_path + file.name
            if len(file_path) > len(longest_path):
                longest_path = file_path + "." + file.extension
                # file view representation (example: file1.mp3)

        for folder in self.folders:
            folder_path = folder.get_longest_path(current_path)
            if len(folder_path) > len(longest_path):
                longest_path = folder_path

        return longest_path


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

    folder1.display_folder_tree()

    print(f"Longest path: {folder1.get_longest_path()}")


if __name__ == "__main__":
    main()
