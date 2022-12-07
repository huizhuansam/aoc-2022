from collections import deque

import requests
from dotenv import dotenv_values

config = dotenv_values('.env')
r = requests.get('https://adventofcode.com/2022/day/7/input', cookies=config)

commands_outputs = [command.strip().split(b'\n') for command in r.content.strip().split(b'$ ') if command != b'']


# Part one
class Folder:
    def __init__(self):
        self.folders = {}
        self.files = {}
        self.total_size = 0
        pass

    def add_folder(self, folder):
        self.folders[folder] = Folder()
        pass

    def add_file(self, file, size):
        self.files[file] = File(size)
        pass

    def is_empty(self):
        return (len(self.files) + len(self.folders)) == 0

    def size(self):
        file_sizes = sum(file.size for file in self.files.values())
        folder_sizes = sum(folder.size() for folder in self.folders.values())
        self.total_size = file_sizes + folder_sizes
        return self.total_size


class File:
    def __init__(self, size):
        self.size = size
        pass


root = Folder()
nav_stack = []


def ls_handler(output):
    pwd = nav_stack[-1]
    if pwd.is_empty():
        for f in output:
            if f.startswith(b'dir'):
                d, n = f.split(b' ')
                pwd.add_folder(n)
                pass
            else:
                s, n = f.split(b' ')
                pwd.add_file(n, int(s))
                pass


def cd_handler(dst):
    if dst == b'/':
        nav_stack.clear()
        nav_stack.append(root)
    elif dst == b'..':
        nav_stack.pop()
    else:
        pwd = nav_stack[-1]
        nav_stack.append(pwd.folders[dst])


for command_output in commands_outputs:
    command = command_output[0]
    if command == b'ls':
        output = command_output[1:]
        ls_handler(output)
    else:
        dst = command.split(b' ')[1]
        cd_handler(dst)

root.size()

stk = [root]
res = 0

while stk:
    pwd = stk.pop()
    if pwd.total_size <= 100000:
        res += pwd.total_size
    for folder in pwd.folders.values():
        stk.append(folder)

print(res)

# Part two
total_space = 70000000
total_size = root.total_size
to_free_up = 30000000 - (total_space - total_size)

q = deque([root])
candidates = []

while q:
    pwd = q.popleft()
    size = pwd.total_size
    if size >= to_free_up:
        candidates.append(size)
    for folder in pwd.folders.values():
        q.append(folder)

print(min(candidates))
