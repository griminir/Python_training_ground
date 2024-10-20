from pathlib import Path

path = Path('module_learning/ecommerce')
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename('timmy')

paths = [p for p in path.iterdir() if p.is_dir()]
py_files = [p for p in path.rglob('*.py')]
print(py_files)
