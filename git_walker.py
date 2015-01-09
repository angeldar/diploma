__author__ = 'Vasiliy Zemlyanov'

import subprocess
import re
import os

GIT_PATH = "C:/Users/NoNeed/AppData/Local/GitHub/PortableGit_ed44d00daa128db527396557813e7b68709ed0e2/bin/git.exe"

class git_walker():

    def __init__(self, repo_directory):
        self.repo_directory = repo_directory

    def status(self):
        '''Get status of repository'''
        p = subprocess.Popen([GIT_PATH,  'status'], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE, cwd = self.repo_directory)
        (res, err) = p.communicate()
        if not err:
            return res
        else:
            print("Errors: ", err)
            return -1

    def next(self):
        assert "Not implemented"
        p = subprocess.Popen(['git', 'rev-list --children --all'], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE, cwd = self.repo_directory)
        rev_list, err = p.communicate()

        # refs = rev_list.scan
        # pass

    def prev(self):
        assert "Not implemented"
        p = subprocess.Popen(['git', 'checkout HEAD^'], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE, cwd = self.repo_directory)
        res, err = p.communicate()
        pass

    def firs(self):
        assert "Not implemented"
        pass

    def last(self):
        assert "Not implemented"
        pass

    def number_of_commits(self):
        '''Get number of commits in git repository'''
        p = subprocess.Popen([GIT_PATH, 'rev-list', 'HEAD', '--count'], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE, shell=False, cwd = self.repo_directory)
        (res, err) = p.communicate()
        if not err:
            return int(res)
        else:
            print("Errors: ", err)
            return -1

    def get_commits_hashes(self):
        '''Get hashes of the commits in the git repository in reverse order.
        (From first one to the last one)'''
        p = subprocess.Popen([GIT_PATH, 'log', '--reverse'], stdout = subprocess.PIPE,
            stderr = subprocess.PIPE, shell=False, cwd = self.repo_directory)
        (res, err) = p.communicate()
        if not err:
            res = res.decode('utf-8')
            regex = re.compile("commit ([a-f0-9]{40})")
            hashes = regex.findall(res)
            return hashes
        else:
            print('err ',err)

    def get_commit_date(self, commit_hash):
        '''Get the date of the commit by the hash of this commit'''
        p = subprocess.Popen([GIT_PATH, 'show', '-s', '--format=%ci', commit_hash], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE, shell = False, cwd = self.repo_directory)
        (res, err) = p.communicate()
        if err:
            print("Error: ", err)
        date = res.decode('utf-8').split()[0]
        return date

    def create_path(self, number_of_steps):
        '''Create path through branch history with the number of steps'''
        number_of_commits = self.number_of_commits()
        if number_of_steps > number_of_commits:
            assert "Error: Number of steps can't be larger then number of commits"
        step = int(number_of_commits / number_of_steps)
        path = []
        hashes = self.get_commits_hashes()
        print(hashes)
        for i in range(0, number_of_steps):
            path.append(hashes[i * step])
        return path

    def reset_to_commit(self, commit_hash):
        '''reset the current state to the commit by its hash'''
        p = subprocess.Popen([GIT_PATH, 'reset', '--hard', commit_hash], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE, shell=False, cwd = self.repo_directory)
        (res, err) = p.communicate()
        DEBUG = False
        if err and DEBUG:
            print("Error: ", err)
        print(res)

    def pull(self):
        p = subprocess.Popen([GIT_PATH, 'pull'], stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE, shell=False, cwd = self.repo_directory)
        (res, err) = p.communicate()
        if err:
            print("Git Error: ", err)
        print(res)

def test_git_walker(repo_path = 'G:/dev/django'):
    gw = git_walker(repo_path)
    print (gw.status())
    # print("Number of commits: ", gw.number_of_commits())
    # commits = gw.get_commits_hashes()
    # print("Hashes of the commits: ", commits)

if __name__ == '__main__':
    test_git_walker()