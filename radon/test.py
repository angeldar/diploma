from radon.cli_init import cc, raw, mi, log
from radon.metrics import  h_visit

from radon.tools import _open, iter_filenames, merge_files, convert_old_version_file

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
def halstead_test(path):
    print("Halstead metrics")
    res = []
    with _open(path) as fobj:
        halstead = h_visit(fobj.read())
        res.append(halstead)
    return res

def test_merge_files(folders = ['G:\\dev\\django']):
    # VERY IMPORTANT - iter_filenames folders must be an ARRAY of string, not single string
    filenames = []
    for filename in iter_filenames(folders,[],[]):
        filenames.append(filename)
    return merge_files(filenames)

def get_cc_from_repo():
    REPO_PATH = 'G:/dev/django'
    res_file_name='G:/django_p2.txt'
    gw = git_walker(REPO_PATH)
    path = gw.create_path(20)
    open(res_file_name,'w+').close()
    for hash in reversed(path):
        date = gw.get_commit_date(hash)
        gw.reset_to_commit(hash)
        print(date)
        ranks = get_ciclomatic_for_folder([REPO_PATH])

        res = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(
            ranks['A'], ranks['B'], ranks['C'], ranks['D'], ranks['E'], ranks['F'])

        print(res)

        with open(res_file_name, 'a+') as f:
            f.write(date + '\t' + res)

def halstead_from_repo():
    REPO_PATH = 'G:/dev/django'
    RES_FILE_NAME = 'G:/django_holster.txt'
    gw = git_walker(REPO_PATH)
    path = gw.create_path(20)
    open(RES_FILE_NAME, 'w+').close()
    for hash in reversed(path):
        date = gw.get_commit_date(hash)
        print(date)
        gw.reset_to_commit(hash)
        (file_dir, file_name) = test_merge_files(folders = ['G:\\dev\\django'])
        holst = halstead_test(file_dir + '\\' + file_name)
        print(date, holst)

def halstead_for_file_from_repo(filenames):
    REPO_PATH = 'G:/dev/django'
    RES_FILE_NAME = 'G:/django_holster.txt'
    gw = git_walker(REPO_PATH)
    path = gw.create_path(20)
    open(RES_FILE_NAME, 'w+').close()
    for hash in reversed(path):
        date = gw.get_commit_date(hash)
        print(date)
        gw.reset_to_commit(hash)
        for file in filenames:
            try:
                convert_old_version_file(file)
                holst = halstead_test(file)
                print(file, holst)
            except:
                print("Holstead error")

print('Start')

filedir = 'G:\\TEMP'
filename = 'TEMP.py'

# regexp except\W[_a-zA-Z0-9\.]+, [a-zA-Z]+:
# replace except FuckingError as FuckOldPythonVersion:

# filedir, filename = test_merge_files(folders = ['G:\\dev\\django'])

# ciclomatic_test([filedir], [filedir + '\\' + filename])
# raw_test([filedir])
# mi_test([filedir])
# print(halstead_test(filedir + '\\' + filename))

# halstead_for_file_from_repo(['G:/dev/django/django/http/multipartparser.py'])

# get_cc_from_repo()
halstead_from_repo()


print('End')