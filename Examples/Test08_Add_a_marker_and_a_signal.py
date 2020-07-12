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
c3d_sample_dir_path = os.path.join(current_f_dir_path, r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')
tgt_c3d_path = os.path.splitext(__file__)[0]+'_result.c3d'
tgt_log_path = os.path.splitext(__file__)[0]+'_result.log'

itf = c3d.c3dserver()
c3d.init_logger(logger_lvl='DEBUG', c_hdlr_lvl='WARNING', f_hdlr_lvl='DEBUG', f_hdlr_f_path=tgt_log_path)

ret = c3d.open_c3d(itf, src_c3d_path, log=True)
# dict_header = c3d.get_dict_header(itf)
# dict_groups = c3d.get_dict_groups(itf, tgt_grp_names=('POINT', 'ANALOG', 'FORCE_PLATFORM'))
# dict_forces = c3d.get_dict_forces(itf, frame=True, time=True)
dict_markers = c3d.get_dict_markers(itf, blocked_nan=True, resid=True, mask=False, desc=False, frame=False, time=False)
dict_mkr_pos = dict_markers['DATA']['POS']

# Add a new marker 'Test1'
new_mkr_name = 'Test1'
new_mkr_pos = (dict_mkr_pos['RASI']+dict_mkr_pos['LASI'])*0.5
c3d.add_marker(itf, new_mkr_name, new_mkr_pos, mkr_resid=None, mkr_desc='Test1', log=True)

# Add a new analog channel 'Test2'
anl_fps = c3d.get_analog_fps(itf)
anl_time = c3d.get_analog_times(itf)
new_an_ch_name = 'Test2'
new_an_ch_val = 100.0*np.cos(anl_time*((2*np.pi)/(1.0)))
c3d.add_analog(itf, new_an_ch_name, new_an_ch_val, sig_unit='mV', sig_desc='Test2', log=True)

ret = c3d.save_c3d(itf, tgt_c3d_path, compress_param_blocks=True, log=True)
ret = c3d.close_c3d(itf, log=True)
