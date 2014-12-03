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

class GitWalker():

    def __init__(self):
        pass

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