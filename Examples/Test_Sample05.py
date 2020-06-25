import os
import sys
if sys.path[0] != os.getcwd():
    sys.path.insert(0, os.getcwd())
lib_local_path = os.path.normpath(r'C:\WORKSPACE\DEV\pyc3dserver')
if os.path.exists(lib_local_path):
    if sys.path[1] != lib_local_path:
        sys.path.insert(1, lib_local_path)
import pyc3dserver as c3d
import numpy as np
#%%
current_f_dir_path = os.path.dirname(__file__)
c3d_sample_dir_path = os.path.join(current_f_dir_path, r'..\Samples_C3D\Sample05')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'vicon512.c3d')

itf = c3d.c3dserver()
ret = c3d.open_c3d(itf, src_c3d_path)
# dict_header = c3d.get_dict_header(itf)
# dict_groups = c3d.get_dict_groups(itf)
dict_markers = c3d.get_dict_markers(itf)
dict_forces = c3d.get_dict_forces(itf)
dict_analogs = c3d.get_dict_analogs(itf)
ret = c3d.close_c3d(itf)
