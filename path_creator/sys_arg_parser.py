from argparse import ArgumentParser, Namespace
from dataclasses import dataclass, field
import sys


@dataclass(frozen=True)
class ExceptedSysArg:
    name_or_flag: str | tuple
    optional: field(default_factory=dict)  # type: ignore


class SysArgsParserBuilder:
    def __init__(self, excepted_args_objects: list[ExceptedSysArg]) -> None:
        self.excepted_args_objects = excepted_args_objects

    def _build_parser(self) -> ArgumentParser:
        sys_arg_parser = ArgumentParser()
        for args_object in self.excepted_args_objects:
            sys_arg_parser.add_argument(
                *args_object.name_or_flag, **args_object.optional
            )

        return sys_arg_parser
