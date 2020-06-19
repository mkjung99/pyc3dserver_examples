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
c3d_sample_dir_path = os.path.join(os.getcwd(), r'..\Samples_C3D\Sample05')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'vicon512.c3d')
tgt_c3d_path = os.path.splitext(src_c3d_path)[0]+'_modified.c3d'

itf = c3d.c3dserver()
ret = c3d.open_c3d(itf, src_c3d_path)
# c3d_f_type = c3d.get_file_type(itf)
frs = c3d.get_video_frames(itf)
# mkr_names = c3d.get_marker_names(itf)
# mkr_unit = c3d.get_marker_unit(itf)
# mkr_scale = c3d.get_marker_scale(itf)
# anal_names = c3d.get_analog_names(itf)
# anal_format = c3d.get_analog_format(itf)
# anal_fps = c3d.get_analog_fps(itf)
# anal_frs = c3d.get_analog_frames(itf)
# anal_t_arr = c3d.get_analog_times(itf)
# dict_header = c3d.get_dict_header(itf)
# dict_groups = c3d.get_dict_groups(itf)
dict_markers = c3d.get_dict_markers(itf, blocked_nan=True, residual=True, mask=False, time=True)
# dict_forces = c3d.get_dict_forces(itf, time=True)
# F1X1_scaled = c3d.get_analog_data_scaled2(itf, 'F1X1')
# F1X3_scaled = c3d.get_analog_data_scaled2(itf, 'F1X3')
# F1Y1_scaled = c3d.get_analog_data_scaled2(itf, 'F1Y1')
# F1Y2_scaled = c3d.get_analog_data_scaled2(itf, 'F1Y2')
# F1Z1_scaled = c3d.get_analog_data_scaled2(itf, 'F1Z1')
# F1Z2_scaled = c3d.get_analog_data_scaled2(itf, 'F1Z2')
# F1Z3_scaled = c3d.get_analog_data_scaled2(itf, 'F1Z3')
# F1Z4_scaled = c3d.get_analog_data_scaled2(itf, 'F1Z4')
# Lgm_unscaled = c3d.get_analog_data_unscaled(itf, 'Lgm')
# Lgm_scaled = c3d.get_analog_data_scaled(itf, 'Lgm')
# Lgm_scaled2 = c3d.get_analog_data_scaled2(itf, 'Lgm')
# Rgm_unscaled = c3d.get_analog_data_unscaled(itf, 'Rgm')
# Rgm_scaled = c3d.get_analog_data_scaled(itf, 'Rgm')
# Rgm_scaled2 = c3d.get_analog_data_scaled2(itf, 'Rgm')
# new_anal_ch_val = np.cos(anal_t_arr*(anal_fps/(100*np.pi)))
# c3d.add_analog(itf, 'test', 'mV', new_anal_ch_val, sig_gain=1)

# mkr_data0 = c3d.get_marker_coords(itf, 'RFT1', scaled=False, blocked_nan=False, msg=True)
# mkr_data1 = c3d.get_marker_coords2(itf, 'RFT1', scaled=False, blocked_nan=False, msg=True)
# mkr_resid = c3d.get_marker_residual(itf, 'RFT1')

# mkr_data_before = c3d.get_marker_coords(itf, 'R_SHANK_3')
# c3d.recover_marker_relative(itf, 'R_SHANK_3', ['R_SHANK_1', 'R_SHANK_2', 'R_SHANK_4'], msg=True)
# mkr_data_after = c3d.get_marker_coords(itf, 'R_SHANK_3')

# ret = c3d.save_c3d(itf, tgt_c3d_path)
ret = c3d.close_c3d(itf)
