import os.path
import csv

class FlatFS:
    def __init__(self, name):
        self.file = name

    def save(self, write_object):
        if not os.path.isfile(self.file):
            with open(self.file, 'w') as file_obj:
                attr_line = [str(attr) for attr, value in write_object.__dict__.items()]
                file_obj.write('id,' + ','.join(attr_line) + '\n')

        with open(self.file, 'a') as file_obj:
            val_line = [str(value) for attr, value in write_object.__dict__.items()]
            val_line = map(lambda e : "''" if e == "" else e, val_line)
            file_obj.write(str(self.get_last_id() + 1) + "," + ','.join(val_line) + '\n')

    def get_all(self):
        objects = []
        with open(self.file, 'r') as file_obj:
            reader = csv.DictReader(file_obj)
            reader = sorted(reader, key=lambda k: k['id'])
            for row in reader:
                objects.append(row)
        return objects

    def get_last_id(self):
        with open(self.file, 'r') as file_obj:
            reader = csv.DictReader(file_obj)
            reader = sorted(reader, key=lambda k: k['id'], reverse=True)
            try:
                return int(reader[0]["id"])
            except IndexError:
                return 0
