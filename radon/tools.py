'''This module contains various utility functions used in the CLI interface.'''

import os
import re
import sys
import fnmatch
import xml.etree.cElementTree as et
from contextlib import contextmanager
from radon.visitors import Function
from radon.complexity import cc_rank
import ast

@contextmanager
def _open(path):
    '''Mock of the built-in `open()` function. If `path` is `-` then
    `sys.stdin` is returned.
    '''
    if path == '-':
        yield sys.stdin
    else:
        with open(path) as f:
            yield f


def iter_filenames(paths, exclude=None, ignore=None):
    '''A generator that yields all sub-paths of the ones specified in
    `paths`. Optional `exclude` filters can be passed as a comma-separated
    string of regexes, while `ignore` filters are a comma-separated list of
    directory names to ignore. Ignore patterns are can be plain names or glob
    patterns. If paths contains only a single hyphen, stdin is implied,
    returned as is.
    '''
    if set(paths) == set(('-',)):
        yield '-'
        return
    for path in paths:
        if os.path.isfile(path):
            yield path
            continue
        for filename in explore_directories(path, exclude, ignore):
            yield filename


def explore_directories(start, exclude, ignore):
    '''Explore files and directories under `start`. `explore` and `ignore`
    arguments are the same as in :func:`iter_filenames`.
    '''
    e = '*[!p][!y]'
    exclude = '{0},{1}'.format(e, exclude).split(',') if exclude else [e]
    ignore = '.*,{0}'.format(ignore).split(',') if ignore else ['.*']
    for root, dirs, files in os.walk(start):
        dirs[:] = list(filter_out(dirs, ignore))
        fullpaths = (os.path.normpath(os.path.join(root, p)) for p in files)
        for filename in filter_out(fullpaths, exclude):
            if (not os.path.basename(filename).startswith('.') and
                    filename.endswith('.py')):
                yield filename


def filter_out(strings, patterns):
    '''Filter out any string that matches any of the specified patterns.'''
    for s in strings:
        if all(not fnmatch.fnmatch(s, p) for p in patterns):
            yield s


def cc_to_dict(obj):
    '''Convert an object holding CC results into a dictionary. This is meant
    for JSON dumping.'''
    def get_type(obj):
        '''The object can be of type *method*, *function* or *class*.'''
        if isinstance(obj, Function):
            return 'method' if obj.is_method else 'function'
        return 'class'

    result = {
        'type': get_type(obj),
        'rank': cc_rank(obj.complexity),
    }
    attrs = set(Function._fields) - set(('is_method', 'clojures'))
    for a in attrs:
        v = getattr(obj, a, None)
        if v is not None:
            result[a] = v
    for key in ('methods', 'clojures'):
        if hasattr(obj, key):
            result[key] = list(map(cc_to_dict, getattr(obj, key)))
    return result


def raw_to_dict(obj):
    '''Convert an object holding raw analysis results into a dictionary. This
    is meant for JSON dumping.'''
    result = {}
    for a in obj._fields:
        v = getattr(obj, a, None)
        if v is not None:
            result[a] = v
    return result


def dict_to_xml(results):
    '''Convert a dictionary holding CC analysis result into a string containing
    xml.'''
    ccm = et.Element('ccm')
    for filename, blocks in results.items():
        for block in blocks:
            metric = et.SubElement(ccm, 'metric')
            complexity = et.SubElement(metric, 'complexity')
            complexity.text = str(block['complexity'])
            unit = et.SubElement(metric, 'unit')
            name = block['name']
            if 'classname' in block:
                name = '{0}.{1}'.format(block['classname'], block['name'])
            unit.text = name
            classification = et.SubElement(metric, 'classification')
            classification.text = block['rank']
            file = et.SubElement(metric, 'file')
            file.text = filename
    return et.tostring(ccm).decode('utf-8')

def merge_files(files, only_norm_files = True):
    '''Merge :files: into one .py file for future analise of hole project.
    '''
    FILE_DIR = "G:\\TEMP"
    FILE_NAME = "TEMP.py"
    if not os.path.exists(FILE_DIR):
        os.makedirs(FILE_DIR)
    filename = FILE_DIR + "\\" + FILE_NAME
    with open(filename, 'w+') as result_file:
        for file in files:
            with open(file, 'r') as curr_file:
                addToRes = True
                try:
                    content = curr_file.read()
                    if only_norm_files:
                        try:
                            ast.parse(content)
                        except SyntaxError:
                            print("Error in parsing file: ", file)
                            addToRes = False
                    if not only_norm_files or (only_norm_files and  addToRes):
                        result_file.write("### " + file + "\n\r")
                        # content = re.sub('#.*\-\*\-.+\-\*-', "\n", content)
                        result_file.write(content + "\n\r")
                except:
                    print("Error in file: " + file)
    return (FILE_DIR, FILE_NAME)