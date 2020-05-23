import argparse
import os
import tempfile
import json


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="takes key-word")
    parser.add_argument("--val", help="takes value for key-word")
    return parser.parse_args()


def fto_load(the_path):
    with open(the_path, 'r') as f:
        data = json.load(f)
    return data


def fto_dump(data, the_path):
    with open(the_path, 'w') as f:
        json.dump(data, f)


def main_p(key, value, the_path):
    if key and value:
        if os.path.exists(the_path):
            data = fto_load(the_path)
            if key in data:
                data[key].append(value)
                fto_dump(data, the_path)
            else:
                data[key] = [value]
                fto_dump(data, the_path)
        else:
            D = dict()  # use for store key-value => dump into temp storage.date
            D[key] = [value]
            fto_dump(D, the_path)
    elif key:
        if os.path.exists(the_path):
            data = fto_load()
            if key in data:
                print(', '.join(data[key]))
            else:
                print(None)
        else:
            print(None)


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data') 
    key = parse().key
    value = parse().val
    main_p(key, value, storage_path)
