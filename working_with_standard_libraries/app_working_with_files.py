from pathlib import Path
from time import ctime
import shutil

path = Path("module_learning/ecommerce/__init__.py")

# path.exists()
# path.rename('init.txt')
# path.unlink()
# print(ctime(path.stat().st_ctime))

# print(path.read_text())
# path.write_text('timmy')
# path.write_bytes()


source = Path("module_learning/ecommerce/__init__.py")
target = Path() / '__init.py'

# long way of copying
# target.write_text(source.read_text())

#fast way using shutil
# shutil.copy(source, target)