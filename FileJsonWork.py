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
        path = Path(file_path)
        if path.exists():
            with path.open('r', encoding='utf-8') as file:
                return json.load(file)
        else:
            raise FileNotFoundError(f"File {file_path} not found.")

    @staticmethod
    def write_file(file_name, data):
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)

    @classmethod
    def from_json_file(cls, file_path):
        data = cls.load_file(file_path)
        return [cls(**item) for item in data]

    @classmethod
    def remove_id(cls, file_path, output_file_path):
        # type as object of existing class
        data = cls.from_json_file(file_path)

        for value in data:
            if 'id' in value.kwargs:
                del value.kwargs['id']

        modified_data = [item.kwargs for item in data]
        cls.write_file(output_file_path, modified_data)

    @classmethod
    def replace_birth_date(cls, file_path, output_file_path):

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


ModificationJsonFile.remove_id(file_path, 'templates/write_without_id.json')
ModificationJsonFile.replace_birth_date(
    file_path, 'templates/write_new_date_format.json')
