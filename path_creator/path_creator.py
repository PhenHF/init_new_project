from argparse import Namespace
from dataclasses import dataclass
from pathlib import Path
import sys

from .sys_arg_parser import SysArgsParserBuilder, ExceptedSysArg


@dataclass(frozen=True)
class PathCreator:
    @staticmethod
    def create_dir(path_to: str, dir_name: str, force_create: bool):
        try:
            p = Path(path_to) / Path(dir_name)
            p.mkdir(
                exist_ok=True,
                parents=force_create
            )

            return p
        except FileNotFoundError:
            return False

    @staticmethod
    def create_file(path_to, file_name):
        p = Path(path_to) / file_name
        p.touch()


class InitProject(SysArgsParserBuilder):
    def __init__(self, excepted_args_objects: list[ExceptedSysArg], paths_json: dict) -> None:
        super().__init__(excepted_args_objects)
        self.paths_json = paths_json

    def __get_sys_args(self) -> Namespace:
        return self._build_parser().parse_args(sys.argv[1:])

    def __prepare_for_init_project(self):
        sys_args = self.__get_sys_args()
        return PathCreator.create_dir(
            path_to=sys_args.path, dir_name=sys_args.name, force_create=sys_args.fcreate
        )

    def init_project(self):
        path_to_project = self.__prepare_for_init_project()
        if path_to_project:
            for package, files in self.paths_json['packages'].items():
                package_path = PathCreator.create_dir(
                    path_to=path_to_project, dir_name=package, force_create=False
                )
                for file in files:
                    PathCreator.create_file(
                        path_to=package_path, file_name=file+'.py'
                    )
        else:
            raise FileNotFoundError(
                'Check the path is correct or specify a flag - -fcreate or -fc for forced creation'
            )
