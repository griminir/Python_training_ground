from pathlib import Path
from zipfile import ZipFile

# with ZipFile('files.zip', 'w') as zip1:
#     for path in Path('module_learning/ecommerce').rglob('*.*'):
#         zip1.write(path)
#     zip1.close()

with ZipFile('files.zip') as zip1:
    print(zip1.namelist())
    info = zip1.getinfo('module_learning/ecommerce/__init__.py')
    print(info.file_size)
    print(info.compress_size)
    # zip1.extractall('extracted')