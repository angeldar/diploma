from radon.cli_init import cc, raw, mi, log
from radon.metrics import  h_visit

from radon.tools import _open, iter_filenames, merge_files

PATH = ['./tests']

# Ciclomatic Complexity
harvester = cc(PATH)
harvester.run()

# Raw Metrics
raw_harvester = raw(PATH)
raw_harvester.run()

# Mi Metrics
mi_harvester = mi(PATH)
mi_harvester.run()

print('Start')
# FILE_PATHS = []
print("Ciclomatic")
for func in harvester._to_dicts()['tests\\TEMP.py']:#['tests\\test_file.py']:#
    print("{0} : {1}".format((func['classname'] + "." if 'classname' in func else "" ) + func['name'], func['complexity']))
#
print("Raw")
print(raw_harvester.as_json())
#
print("Mi")
print(mi_harvester.as_json())
#
# # Holstead metrics
print("Holstead")
with _open('tests/TEMP.py') as fobj:
    holstead = h_visit(fobj.read())
    print(holstead)

def test_merge_files():
    # VERY IMPORTANT - iter_filenames должен принимать МАССИВ строк, а не строку
    filenames = []
    for filename in iter_filenames(['G:\\django-master'],[],[]):
        print(filename)
        filenames.append(filename)
    merge_files(filenames)

print('End')