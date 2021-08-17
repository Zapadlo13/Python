import os


def create_dir(dirs):
    for dir in dirs:
        if not os.path.exists(dir):
            os.makedirs(dir)


my_project = 'my_project'

dirs = [os.path.join(my_project, ),
        os.path.join(my_project, 'settings'),
        os.path.join(my_project, 'mainapp'),
        os.path.join(my_project, 'adminapp'),
        os.path.join(my_project, 'authapp')]

create_dir(dirs)