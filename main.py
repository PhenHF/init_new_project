from path_creator.path_creator import InitProject
from path_creator.utils import EXCEPTED_ARGS_OBJECTS, read_json


def main():
    init_new_project = InitProject(EXCEPTED_ARGS_OBJECTS, read_json())
    init_new_project.init_project()


if __name__ == '__main__':
    main()
