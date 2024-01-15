#!/usr/bin/python3
"""Base class for all models, managing object IDs"""
import json
import csv


class Base:
    """Base class for all models in project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base object with optional id.

        Args:
        id (int): id of object. Defaults to None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file."""
        filename = "{}.csv".format(cls.__name__)
        csv_list = []
        if list_objs is not None:
            csv_list = [obj.to_csv() for obj in list_objs]

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(csv_list)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from a CSV file."""
        filename = "{}.csv".format(cls.__name__)

        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                csv_data = list(reader)
                if csv_data:
                    instances = [cls.create(*map(int, data)) for data in csv_data]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []
