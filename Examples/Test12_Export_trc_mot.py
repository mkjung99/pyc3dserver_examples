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
from scipy.spatial.transform import Rotation as R
import logging
#%%
cwd = os.path.dirname(__file__)

# Type 2 example
c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')

trc_path = os.path.join(cwd, 'Test12_result.trc')
mot_path = os.path.join(cwd, 'Test12_result.mot')

itf = c3d.c3dserver()
c3d.init_logger(logger_lvl='DEBUG', c_hdlr_lvl='DEBUG', f_hdlr_lvl='DEBUG', f_hdlr_f_path=None)
ret = c3d.open_c3d(itf, src_c3d_path)

all_mkr_names = c3d.get_marker_names(itf)
tgt_mkr_names = [x for x in all_mkr_names if len(x)<=4]
axes_src = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
axes_tgt = [[0, -1, 0], [0, 0, 1], [-1, 0, 0]]
rot_ret = R.align_vectors(a=axes_src, b=axes_tgt)
rot_obj = rot_ret[0]
trf = rot_obj.as_matrix()

c3d.export_trc(itf, trc_path, rot_mat=trf, filt_fc=20.0, tgt_mkr_names=tgt_mkr_names)
c3d.export_mot(itf, mot_path, rot_mat=trf, filt_fc=20.0, threshold=15.0)

ret = c3d.close_c3d(itf)
