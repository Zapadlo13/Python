import os

ROOT = os.path.dirname(__file__)  # папка, где находимся
project_path = os.path.join(ROOT, 'my_project')
templates_path = os.path.join(project_path, 'templates')
os.makedirs(templates_path, exist_ok=True)  # не выдавать ошибку, если папка уже существует
dir_paths = []
for root, dirs, files in os.walk(project_path):
    if 'templates' in dirs:
        dir_paths.append(root)
for dir_path in dir_paths:
    dir_name = os.path.basename(dir_path)
    old_templ_path = os.path.join(project_path, dir_name, 'templates', dir_name)
    new_templ_path = os.path.join(templates_path, dir_name)
    if os.path.exists(old_templ_path) and not os.path.exists(new_templ_path):
        os.rename(old_templ_path, new_templ_path)
        os.rmdir(os.path.join(project_path, dir_name, 'templates'))
