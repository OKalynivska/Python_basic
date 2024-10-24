import json
from pathlib import Path
from datetime import datetime
from functools import wraps


class Person:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f"Person Info: {self.__dict__}"

    @classmethod
    def load_from_json_file_to_list(cls, file_name):
        try:
            if not file_name.exists():
                raise FileNotFoundError(f"File {file_name} not found.")
            with open(file_name, 'r') as file:
                if not file_name.suffix == '.json':
                    raise ValueError("Invalid file format. Expected JSON file")
                return [cls.to_object(data) for data in json.load(file)]
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except json.JSONDecodeError as e:
            print(f"Unexprcted error occured: {e}")
        except ValueError as e:
            print(f"Error: {e}")

    @classmethod
    def list_to_json_file(cls, objects, file_name):
        with open(file_name, 'w') as file:
            json.dump([cls.to_dict(ob) for ob in objects], file, indent=4)

    @classmethod
    def to_dict(cls, ob):
        dict_ob = {}
        for key, value in ob.__dict__.items():
            dict_ob[key] = value
        return dict_ob

    @classmethod
    def to_object(cls, data):
        return cls(**data)

    def write_to_file(func):
        @wraps(func)
        def wrapper(cls, *args, **kwargs):
            func(cls, *args, **kwargs)
            cls.list_to_json_file(*args, **kwargs)
        return wrapper

    @classmethod
    @write_to_file
    def remove_id(cls, objects, output_file_path):
        for ob in objects:
            # print(type(ob))  # <class '__main__.Person'>
            if 'id' in ob.__dict__:
                ob.__dict__.pop('id')
        return objects

    @classmethod
    @write_to_file
    def reformat_date(cls, objects, output_file_path):
        for ob in objects:
            if 'birth_date' in ob.__dict__:
                new_format = datetime.strptime(ob.__dict__.get(
                    'birth_date'), "%m/%d/%Y").strftime("%Y-%m-%d")
                ob.__dict__['birth_date'] = new_format
        return objects


file_path = Path('templates/valid_info.json')
invalid_data = Path('templates/invalid_data.json')
empty_data = Path('templates/empty.json')
another_format = Path('templates/file.txt')

# Person.load_from_json_file_to_list(invalid_data)
# Person.load_from_json_file_to_list(empty_data)
# Person.load_from_json_file_to_list(another_format)
valid_file = Person.load_from_json_file_to_list(file_path)
# print([str(f) for f in Person.load_from_json_file_to_list(file_path)])  # list type
Person.reformat_date(valid_file, 'templates/reformated_date.json')
Person.remove_id(valid_file, 'templates/without_id.json')
