# MENDY Serge Wilson --- Master 2 - Data Science
import os
import nbformat
import git

folders = {
    "data":{"cleaned":{},"processed":{}, "raw":{} },
    "docs":{"README.md":None},
    "LICENSE":None,
    "Makefile":None,
    "models":{"README.md":None},
    "notebooks": {
        "main.ipynb":"from math import sqrt\n\nprint(sqrt(25))"
        },
    "README.md":None,
    "reports":{"README.md":None},
    "requirements.txt":None,
    "src": {
        "utils.py":None,
        "process.py":None,
        "train.py":None
        }
}

def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    print(f"Folder '{folder_name}' created successfully!!!!")


def create_file(filename, content):
    path = filename
    if not os.path.exists(path):
        extension = filename.split(".")[-1]
        if extension == "ipynb":
            nb = nbformat.v4.new_notebook()
            nb["cells"] = [nbformat.v4.new_code_cell(content)]
            nbformat.write(nb, path)
            print(f"Notebook '{filename}' created successfully!!!!")
        else:
            
            with open(path,"w") as file:
                if content:
                    file.write(content)
                print(f"File '{filename}' created successfully!!!!")
        

def create_directories_and_files():
    cwd = os.getcwd()
    repo = git.Repo(cwd)

    for f in folders.keys():
        is_folder = isinstance(folders.get(f), dict)
        if is_folder:
            create_folder(f)
            subs = folders.get(f)
            for sub in subs:
                path_sub = os.path.join(f, sub)
                if isinstance(subs.get(sub), dict):
                    create_folder(path_sub)
                else:
                    content = subs.get(sub)
                    create_file(path_sub, content)
        else:
            content=folders.get(f)
            create_file(f, content)


if __name__=="__main__":
    create_directories_and_files()