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

c3d.init_logger(logger_lvl='DEBUG', c_hdlr_lvl='DEBUG', f_hdlr_lvl='DEBUG', f_hdlr_f_path=tgt_log_path)
itf = c3d.c3dserver(log=True)
ret_open = c3d.open_c3d(itf, src_c3d_path, log=True)
# ret_open = c3d.open_c3d(itf, '', log=True)
# sig_idx = c3d.get_analog_index(itf, 'Force.Fx1', log=True)
# mkr_idx = c3d.get_marker_index(itf, 'LASI', log=True)
# mkr_unit = c3d.get_marker_unit(itf, log=True)
# mkr_scale = c3d.get_marker_scale(itf, log=True)
# mkr_data = c3d.get_marker_data(itf, 'LASI', log=False)
# mkr_pos = c3d.get_marker_pos2(itf, 'LASI', log=False)
# mkr_resid = c3d.get_marker_resid(itf, 'LASI', log=False)
# f_type = c3d.get_file_type(itf, log=True)
# data_type = c3d.get_data_type(itf, log=True)
# first_fr = c3d.get_first_frame(itf, log=True)
# last_fr = c3d.get_last_frame(itf, log=True)

ret = c3d.delete_frames(itf, 1000, 200, log=True)
# n_frs = c3d.get_num_frames(itf, log=True)
# ret_check, fr_start, fr_end = c3d.check_frame_range_valid(itf, log=True)
# gen_scale = c3d.get_analog_gen_scale(itf, log=True)
# analog_fmt = c3d.get_analog_format(itf, log=True)
# unit = c3d.get_analog_unit(itf, 'Force.Fx1', log=True)
# dict_groups = c3d.get_dict_groups(itf)
# fp_params = c3d.get_fp_params(itf, log=True)
# test = c3d.get_group_params(itf, 'FORCE_PLATFORM', ['CORNERS'], log=True)
# anal_names = c3d.get_analog_names(itf, log=True)
# vid_fps = c3d.get_video_fps(itf, log=True)
# av_ratio = c3d.get_analog_video_ratio(itf, log=True)
# analog_fps = c3d.get_analog_fps(itf, log=True)
# mkr_frames = c3d.get_video_frames(itf, log=True)
# analog_frames = c3d.get_analog_frames(itf, log=True)
# vid_times = c3d.get_video_times(itf, log=True)
# analog_times = c3d.get_analog_times(itf, log=True)
# mkr_names = c3d.get_marker_names(itf, log=True)
# mkr_names = c3d.get_marker_names(itf, log=True)
# ret_save = c3d.save_c3d(itf, tgt_c3d_path, compress_param_blocks=True, log=True)

# ret_change_mkr = c3d.change_marker_name(itf, 'PELO1', 'PPPP', log=True)
# ret_change_sig = c3d.change_analog_name(itf, 'Force.Fx11', 'Force_Fx1', log=True)
# dict_header = c3d.get_dict_header(itf, log=True)
# dict_groups = c3d.get_dict_groups(itf, log=True)
# fp_corners = c3d.get_group_params(itf, 'FORCE_PLATFORM', ['CORNERS'], log=True)
# fp_params = c3d.get_fp_params(itf, log=True)
dict_mkrs = c3d.get_dict_markers(itf, blocked_nan=True, frame=True, log=True)
# dict_forces = c3d.get_dict_forces(itf, desc=True, frame=True, time=True, log=True)
# dict_analogs = c3d.get_dict_analogs(itf, excl_forces=False, log=True)

# ret_save = c3d.save_c3d(itf, tgt_c3d_path, compress_param_blocks=True, log=True)
ret_close = c3d.close_c3d(itf, log=True)
