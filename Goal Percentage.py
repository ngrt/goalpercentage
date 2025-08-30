import os
import json

dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(dir, 'main.html')
json_path = os.path.join(dir, 'projects.json')

if os.path.exists(json_path):
    with open(json_path, 'r', encoding = 'utf-8') as f:
        projects = json.load(f)
else:
    projects = {}

lang = input('Choose language / Выберите язык\nru/en\n')
if lang == 'ru':
    print("Проекты:")
    for i, (project, progress) in enumerate(projects.items(), 1):
        print(f'{i}. {project} - {progress}%')

    choice = input('Выберите действие:\n1. Добавить проект\n2. Изменить прогресс\n')
    if choice == '1':
        project = input("Введите название проекта:\n")
        progress = int(input("Введите процент прогресса (0-100)\n"))
        if progress <= -1:
            progress = 0
        if progress >= 101:
            progress = 100
        projects[project] = progress
        
    elif choice == '2':
        project_name = input("Введите название проекта:\n")
        if project in projects:
            progress = int(input("Кол-во процентов (0-100): "))
            if progress <= -1:
                progress = 0
            if progress >= 101:
                progress = 100
            projects[project] = progress
        else:
            print('Проект не существует')

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(projects, f, ensure_ascii=False, indent=4)

project_html = ''
for project, progress in projects.items():
    project_html += f"""<div class='project'>
        <h2>{project}</h2>
        <p>Выполнено: {progress}%</p>
        <div class="progress-container">
            <div class="progress-bar" style='width: {progress}%;'>{progress}%</div>
        </div>
    </div>"""
    
html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Прогресс</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
        }}
        .progress-container {{
            width: 100%;
            background-color: #eee;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 5px;
        }}
        .progress-bar {{
            height: 30px;
            background-color: #4caf50;
            text-align: center;
            line-height: 30px;
            color: white;
            transition: width 0.5s;
        }}
        .project {{
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <h1>Прогресс проектов</h1>
    {project_html}
</body>
</html>
"""
with open(html_path, 'w', encoding="utf-8") as f:
        f.write(html_content)

if lang == 'en':
    print("Projects:")
    for i, (project, progress) in enumerate(projects.items(), 1):
        print(f'{i}. {project} - {progress}%')
    choice = input('Choose actions:\n1. New project\n2. Change progress\n')
    
    if choice == '1':
        project = input("Choose project name:\n")
        progress = int(input("Choose project progress (0-100)\n"))
        if progress <= -1:
            progress = 0
        if progress >= 101:
            progress = 100
        projects[project] = progress
        
    elif choice == '2':
        project_name = input("Choose project name:\n")
        if project in projects:
            progress = int(input("New progress (0-100): "))
            if progress <= -1:
                progress = 0
            if progress >= 101:
                progress = 100
            projects[project] = progress
        else:
            print("Project can't be found")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(projects, f, ensure_ascii=False, indent=4)

project_html = ''
for project, progress in projects.items():
    project_html += f"""<div class='project'>
        <h2>{project}</h2>
        <p>Completed: {progress}%</p>
        <div class="progress-container">
            <div class="progress-bar" style='width: {progress}%;'>{progress}%</div>
        </div>
    </div>"""
    
html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Progress</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
        }}
        .progress-container {{
            width: 100%;
            background-color: #eee;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 5px;
        }}
        .progress-bar {{
            height: 30px;
            background-color: #4caf50;
            text-align: center;
            line-height: 30px;
            color: white;
            transition: width 0.5s;
        }}
        .project {{
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <h1>Project progress</h1>
    {project_html}
</body>
</html>
"""

with open(html_path, 'w', encoding="utf-8") as f:
        f.write(html_content)

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(projects, f, ensure_ascii=False, indent=4)