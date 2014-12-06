from radon.cli_init import cc, raw, mi, log
from radon.metrics import  h_visit

from radon.tools import _open, iter_filenames, merge_files

from git_walker import git_walker

PATH = ['./tests']

# Ciclomatic Complexity
def get_ciclomatic_for_folder(path):
    print("Ciclomatic")
    harvester = cc(path)
    harvester.run()
    data = harvester._to_dicts()
    ranks = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    for file in data:
        for func in data[file]:
            if 'name' in func:
                if 'rank' in func:
                    ranks[func['rank']] += 1
    return ranks

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

def get_cc_from_repo():
    REPO_PATH = 'G:/dev/django'
    res_file_name='G:/django.txt'
    gw = git_walker(REPO_PATH)
    path = gw.create_path(20)
    open(res_file_name,'w').close()
    for hash in reversed(path):
        date = gw.get_commit_date(hash)
        gw.reset_to_commit(hash)
        print(date)
        ranks = get_ciclomatic_for_folder([REPO_PATH])

        res = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(
            ranks['A'], ranks['B'], ranks['C'], ranks['D'], ranks['E'], ranks['F'])

        with open(res_file_name, 'a+') as f:
            f.write(date + '\t' + res)

print('Start')

filedir = 'G:\\TEMP'
filename = 'TEMP.py'

# filedir, filename = test_merge_files(folders = ['G:\\dev\\django'])

# ciclomatic_test([filedir], [filedir + '\\' + filename])
# raw_test([filedir])
# mi_test([filedir])
# holstead_test([filedir])

get_cc_from_repo()

print('End')