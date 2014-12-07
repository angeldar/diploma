from radon.cli_init import cc
from radon.metrics import  h_visit

from radon.tools import _open, iter_filenames, merge_files

from git_walker import git_walker

def merge_files_in_folders(folders = ['G:\\dev\\django']):
    # VERY IMPORTANT - iter_filenames folders must be an ARRAY of string, not single string
    filenames = []
    for filename in iter_filenames(folders,[],[]):
        filenames.append(filename)
    return merge_files(filenames)

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

def get_cc_for_repo():
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

# Halstead metrics
def get_halstead_for_file(path):
    print("Halstead metric")
    res = []
    with _open(path) as fobj:
        halstead = h_visit(fobj.read())
        res.append(halstead)
    return res

def get_halstead_for_repo():
    REPO_PATH = 'G:/dev/django'
    RES_FILE_NAME = 'G:/django_holster.txt'
    gw = git_walker(REPO_PATH)
    path = gw.create_path(20)
    open(RES_FILE_NAME, 'w+').close()
    for hash in reversed(path):
        date = gw.get_commit_date(hash)
        print(date)
        gw.reset_to_commit(hash)
        (file_dir, file_name) = merge_files_in_folders(folders = ['G:\\dev\\django'])
        holst = get_halstead_for_file(file_dir + '\\' + file_name)
        print(date, holst)

if __name__ == '__main__':
    print('Start')

    # get_cc_from_repo()
    get_halstead_for_repo()

    print('End')