import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Tunggu sebentar... Folder '+ directory +' sedang dibuat')
        os.makedirs(directory)

create_project_dir('goblinGrabber')