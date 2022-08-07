''' https://docs.python.org/3/library/os.path.html '''

from os import path

path_1 = 'Pandas_app/'
path_2 = 'Json_app'

print()

print('Real path: ', path.realpath(path_1))
print('If exists path: ', path.exists(path_1))

print()

print('Real path: ', path.realpath(path_2))
print('If exists path: ', path.exists(path_2))
