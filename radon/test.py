from radon.cli_init import cc, raw, mi, log
from radon.metrics import  h_visit

from radon.tools import _open

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
for func in harvester._to_dicts()['tests\\test_file.py']:
    print("{0} : {1}".format((func['classname'] + "." if 'classname' in func else "" ) + func['name'], func['complexity']))

print(raw_harvester.as_json())

print(mi_harvester.as_json())

# Holstead metrics
with _open('tests/test_file.py') as fobj:
    holstead = h_visit(fobj.read())
    print(holstead)

print('End')