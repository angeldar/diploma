from radon.cli_init import cc, raw, mi, log
from radon.metrics import  h_visit

from radon.tools import _open, iter_filenames, merge_files

PATH = ['./tests']

# Ciclomatic Complexity
def ciclomatic_test(path, filename):
    print("Ciclomatic")
    harvester = cc(path)
    harvester.run()
    with open('G:/test.txt','w+') as f:
        f.write(harvester.as_json())
    # for func in harvester._to_dicts()[filename]:
    #     print("{0} : {1}".format((func['classname'] + "." if 'classname' in func else "" ) + func['name'], func['complexity']))

# Raw Metrics
def raw_test(path):
    print("Raw metrics")
    raw_harvester = raw(path)
    raw_harvester.run()
    print(raw_harvester.as_json())

# Mi Metrics
def mi_test(path):
    print("Mi metrics")
    mi_harvester = mi(path)
    mi_harvester.run()
    print(mi_harvester.as_json())

# Holstead metrics
def holstead_test(path):
    print("Holstead metrics")
    with _open('tests/TEMP.py') as fobj:
        holstead = h_visit(fobj.read())
        print(holstead)

def test_merge_files(folders):
    # VERY IMPORTANT - iter_filenames folders должен принимать МАССИВ строк, а не строку
    filenames = []
    for filename in iter_filenames(folders,[],[]):
        filenames.append(filename)
    return merge_files(filenames)

print('Start')

filedir, filename = test_merge_files(folders = ['G:\\dev\\django'])

ciclomatic_test([filedir], [filedir + '/' + filename])
raw_test([filedir])
mi_test([filedir])
holstead_test([filedir])


print('End')