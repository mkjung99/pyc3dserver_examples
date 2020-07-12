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
c3d_sample_dir_path = os.path.join(current_f_dir_path, r'..\Samples_C3D\Sample01')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'Eb015pi.c3d')
tgt_c3d_path = os.path.splitext(__file__)[0]+'_result.c3d'

itf = c3d.c3dserver(False)
ret = c3d.open_c3d(itf, src_c3d_path)
# dict_header = c3d.get_dict_header(itf)
# dict_groups = c3d.get_dict_groups(itf)
# dict_markers = c3d.get_dict_markers(itf, blocked_nan=True, resid=True, mask=True, desc=True)
# dict_forces = c3d.get_dict_forces(itf, desc=True, frame=True, time=True)
# dict_analogs = c3d.get_dict_analogs(itf, desc=True, frame=True, excl_forces=True, time=True)
ret, n_frs_updated = c3d.recover_marker_rel(itf, 'LTH1', ['LTH2', 'LTH3', 'LTH4'])

ret = c3d.save_c3d(itf, tgt_c3d_path)
ret = c3d.close_c3d(itf)
