import importlib
import os

# Для удобства, также можно сделать функцию для импорта всех модулей пакета
def import_all_modules():
  modules = {}
  folder_path = os.path.dirname(os.path.abspath(__file__)) # текущая папка
  for filename in os.listdir(folder_path):
    if filename.endswith(".py") and filename != "__init__.py":
      module_name = filename[:-3] #убрать .py
      try:
           module = importlib.import_module(f".{module_name}", __name__)
           modules[module_name] = module
           print(f"Модуль '{module_name}' успешно импортирован.")
      except ImportError as e:
           print(f"Ошибка импорта модуля '{module_name}': {e}")
  return modules
