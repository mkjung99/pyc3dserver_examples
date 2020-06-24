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
c3d_sample_dir_path = os.path.join(os.getcwd(), r'..\Samples_C3D\Sample08')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'EB015PI.c3d')
tgt_c3d_path = os.path.splitext(__file__)[0]+'_result.c3d'
tgt_log_path = os.path.splitext(__file__)[0]+'_result.log'

itf = c3d.c3dserver()
c3d.init_logger(logger_lvl='DEBUG', c_hdlr_lvl='WARNING', f_hdlr_lvl='DEBUG', f_hdlr_f_path=tgt_log_path)

ret = c3d.open_c3d(itf, src_c3d_path, log=True)
c3d_f_type = c3d.get_file_type(itf)
c3d_data_type = c3d.get_data_type(itf)

# Change a marker's name from 'pv4' to 'PV4'
ret = c3d.change_marker_name(itf, 'pv4', 'PV4', log=True)

# dict_header = c3d.get_dict_header(itf)
# dict_groups = c3d.get_dict_groups(itf)
# dict_markers = c3d.get_dict_markers(itf, blocked_nan=True, resid=True, mask=False, time=True)
# dict_mkr_pos = dict_markers['DATA']['POS']

# Try to test different gap filling functions
c3d.fill_marker_gap_rbt(itf, 'PV2', ['PV1', 'PV3', 'PV4'], log=True)
# c3d.fill_marker_gap_pattern(itf, tgt_mkr_name='PV2', dnr_mkr_name='PV3', log=True)
# c3d.fill_marker_gap_interp(itf, 'PV2', log=True)

ret = c3d.save_c3d(itf, tgt_c3d_path, log=True)
ret = c3d.close_c3d(itf, log=True)
