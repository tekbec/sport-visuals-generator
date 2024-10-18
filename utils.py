import os

def init_tmp_dir() -> str:
    tmp_dir = os.path.abspath('tmp')
    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)
    return tmp_dir

def init_out_dir() -> str:
    tmp_dir = os.path.abspath('out')
    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)
    return tmp_dir