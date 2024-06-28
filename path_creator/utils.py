import json
from .sys_arg_parser import ExceptedSysArg

EXCEPTED_ARGS_OBJECTS = [
    ExceptedSysArg(
        name_or_flag=('-name', '-n'), optional={
            'required': True
        }
    ),
    ExceptedSysArg(
        name_or_flag=('-path', '-p'), optional={
            'required': True
        }
    ),

    ExceptedSysArg(
        name_or_flag=('-fcreate', '-fc'), optional={
            'action': 'store_true',
            'default': False
        }
    )
]


def read_json(path_to_json: str = None):
    path_to_json = path_to_json if path_to_json else 'paths.json'

    with open(path_to_json, mode='r', encoding='UTF-8') as f:
        paths_json = json.load(f)
    return paths_json
