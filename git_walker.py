__author__ = 'Vasiliy Zemlyanov'

#!/usr/bin/env ruby
# Walks up and down revisions in a git repo.
# Usage:
#   git walk next
#   git walk prev
# case ARGV[0]
# when "next"
#   rev_list = `git rev-list --children --all`
#   refs = rev_list.scan(/[a-z0-9]{40}(?= )/)
#   refs.unshift(rev_list[/[a-z0-9]{40}/])
#   refs.reverse!
#
#   head = `git rev-parse HEAD`.chomp
#   ref_for_next_commit = refs[refs.index(head) + 1]
#
#   if ref_for_next_commit
#     puts `git checkout #{ref_for_next_commit}`
#   else
#     puts "You're already on the latest commit."
#   end
# when "prev"
#   puts `git checkout HEAD^`
# else
#   puts "Usage: git-walk next|prev"
# end

import os
import subprocess
import re

# Number of commits
# git rev-list HEAD --count

GIT_PATH = "C:/Users/NoNeed/AppData/Local/GitHub/PortableGit_ed44d00daa128db527396557813e7b68709ed0e2/bin/git.exe"

class GitWalker():

    def __init__(self, repo_directory):
        self.repo_directory = repo_directory
        os.chdir(repo_directory)

    def next(self):
        assert "Not implemented"
        p = subprocess.Popen(['git', 'rev-list --children --all'], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)
        rev_list, err = p.communicate()

        # refs = rev_list.scan
        # pass

    def prev(self):
        assert "Not implemented"
        p = subprocess.Popen(['git', 'checkout HEAD^'], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)
        res, err = p.communicate()
        pass

    def firs(self):
        assert "Not implemented"
        pass

    def last(self):
        assert "Not implemented"
        pass

    def number_of_commits(self):
        '''
        Get number of commits in git repository
        '''
        p = subprocess.Popen([GIT_PATH, 'rev-list', 'HEAD', '--count'], stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE, shell=False)
        (res, err) = p.communicate()
        if not err:
            return int(res)
        else:
            print("Errors: ", err)
            return -1

    def log_reverse_commits_hashes(self):
        '''
        Get hashes of the commits in the git repository in reverse order.
        (From first one to the last one)
        '''
        p = subprocess.Popen([GIT_PATH, 'log', '--reverse'], stdout = subprocess.PIPE,
            stderr = subprocess.PIPE, shell=False)
        (res, err) = p.communicate()
        if not err:
            res = res.decode('utf-8')
            regex = re.compile("commit ([a-f0-9]{40})")
            hashes = regex.findall(res)
            return hashes
        else:
            print('err ',err)

def test_git_walker():
    gw = GitWalker('G:\\dev\\diploma')
    print("Number of commits: ", gw.number_of_commits())
    print("Hashes of the commitsL ", gw.log_reverse_commits_hashes())

test_git_walker()