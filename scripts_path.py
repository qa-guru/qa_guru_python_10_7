import os
import shutil

print(os.path.abspath(__file__))
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
print(PROJECT_ROOT_PATH)
print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp"))
# os.mkdir("")
# shutil.rmtree("tmp")  # rm -rf todo быть осторожными с этой командой

