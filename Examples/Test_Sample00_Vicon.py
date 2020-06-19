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
c3d_sample_dir_path = os.path.join(os.getcwd(), r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')
# tgt_c3d_path = os.path.splitext(src_c3d_path)[0]+'_modified.c3d'

itf = c3d.c3dserver()
ret = c3d.open_c3d(itf, src_c3d_path)
dict_header = c3d.get_dict_header(itf)
dict_groups = c3d.get_dict_groups(itf)
dict_mkr = c3d.get_dict_markers(itf, blocked_nan=True, residual=True, mask=False)
dict_forces = c3d.get_dict_forces(itf)

# ret = c3d.save_c3d(itf, tgt_c3d_path)
ret = c3d.close_c3d(itf)