import json
from pathlib import Path
from datetime import datetime


class ModificationJsonFile:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def __str__(self):
        return f'User data: {self.kwargs}'

    @staticmethod
    def load_file(file_path):
        """Method loads the file and check if file is not empty and contains valid information

        Args:
            file_path (Path): File pat

        Raises:
            FileNotFoundError: Rasie if file not found
            ValueError: Raise if file extention is not valid
            ValueError: Raise if file is empty

        Returns:
            dict: Loaded JSON file
        """
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"File path {file_path} not found.")
            if len(file_path) == 0:
                raise ValueError("File is empty")
            with path.open('r', encoding='utf-8') as file:
                if not path.suffix == '.json':
                    raise ValueError("Invalid file format. Expected JSON file")
                return json.load(file)
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except json.JSONDecodeError as e:
            print(f"Unexprcted error occured: {e}")
        except ValueError as e:
            print(f"Error: {e}")

    @staticmethod
    def write_file(file_name, data):
        """Write data to file

        Args:
            file_name (str): The name or path of the file to write the data to. 
                         The file will be created if it doesn't exist, 
                         and overwritten if it does
            data (dict or list): The data to be written to the file.
        """
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def from_json_file(cls, file_path):
        """Load data from a JSON file and convert it into a list of class instances

        Args:
            file_path (str): Path to the JSON file containing the data

        Returns:
            list: List of instances of the class, where each instance is initialized with the data 
              from JSON file
        """
        data = cls.load_file(file_path)
        return [cls(**item) for item in data]

    @classmethod
    def remove_id(cls, file_path, output_file_path):
        """Remove id from the file and rewrite to new file

        Args:
            file_path (str): Path to the JSON file from which the data will be read
            output_file_path (str): Path to the output file where the modified data without 'id' fields will be saved
        """
        # type as object of existing class
        data = cls.from_json_file(file_path)

        for value in data:
            if 'id' in value.kwargs:
                del value.kwargs['id']

        modified_data = [item.kwargs for item in data]
        cls.write_file(output_file_path, modified_data)

    @classmethod
    def replace_birth_date(cls, file_path, output_file_path):
        """Change birth_date field to new format and rewrite to new file

        Args:
            file_path (str): Path to the JSON file from which the data will be read
            output_file_path (str): Path to the output file where the modified data without 'id' fields will be saved
        """

        # type as object of existing class
        data = cls.from_json_file(file_path)

        for value in data:
            if 'birth_date' in value.kwargs:
                value.kwargs['birth_date'] = datetime.strptime(
                    value.kwargs['birth_date'], "%m/%d/%Y").strftime("%Y-%m-%d")

        modified_data = [item.kwargs for item in data]
        cls.write_file(output_file_path, modified_data)


file_path = 'templates/test.json'

json_file_data = ModificationJsonFile.from_json_file(file_path)
# Unexprcted error occured: Expecting ',' delimiter: line 11 column 5 (char 218)
json_file_data = ModificationJsonFile.load_file(
    'templates/not_valid_json.json')
# Error: Invalid file format. Expected JSON file
json_file_data = ModificationJsonFile.load_file('templates/empty.txt')
# Unexprcted error occured: Expecting value: line 1 column 1 (char 0)
json_file_data = ModificationJsonFile.load_file('templates/empty.json')


ModificationJsonFile.remove_id(file_path, 'templates/write_without_id.json')
ModificationJsonFile.replace_birth_date(
    file_path, 'templates/write_new_date_format.json')
