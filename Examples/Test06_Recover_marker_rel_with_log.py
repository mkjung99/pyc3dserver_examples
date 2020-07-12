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
import logging
#%%
current_f_dir_path = os.path.dirname(__file__)
c3d_sample_dir_path = os.path.join(current_f_dir_path, r'..\Samples_C3D\Sample26')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'Walking_Hybrid_1_1.c3d')
tgt_c3d_path = os.path.splitext(__file__)[0]+'_result.c3d'

itf = c3d.c3dserver()
c3d.init_logger(logger_lvl='INFO', c_hdlr_lvl='DEBUG', f_hdlr_lvl='DEBUG', f_hdlr_f_path=None)

ret = c3d.open_c3d(itf, src_c3d_path, log=True)
# c3d_f_type = c3d.get_file_type(itf)
# dict_header = c3d.get_dict_header(itf)
# dict_groups = c3d.get_dict_groups(itf)
# dict_markers = c3d.get_dict_markers(itf, blocked_nan=True, resid=True, mask=False, time=True)

c3d.recover_marker_rel(itf, 'L_SHANK_2', ['L_SHANK_1', 'L_SHANK_3', 'L_SHANK_4'], log=True)
# c3d.fill_marker_gap_pattern(itf, tgt_mkr_name='L_SHANK_2', dnr_mkr_name='L_SHANK_1', log=True)
# ret = c3d.fill_marker_gap_interp(itf, 'L_SHANK_2', log=True)

ret = c3d.save_c3d(itf, tgt_c3d_path, log=True)
ret = c3d.close_c3d(itf, log=True)
