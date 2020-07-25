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
tgt_c3d_path = os.path.splitext(__file__)[0]+'_result.c3d'

itf = c3d.c3dserver()
ret = c3d.open_c3d(itf, src_c3d_path)
av_ratio = c3d.get_analog_video_ratio(itf)
first_fr = c3d.get_first_frame(itf)
last_fr = c3d.get_last_frame(itf)

new_val = np.array([100.0]*av_ratio*1000, dtype=np.float32)
ret = c3d.set_analog_data(itf, 'AUD1', new_val, start_frame=5000, end_frame=5999)
ret = c3d.set_analog_subframe_data(itf, 'AUD1', 200.0, start_frame=last_fr, sub_frame=9)
sig_data_unscaled = c3d.get_analog_data_unscaled(itf, 'AUD1')
sig_data_scaled = c3d.get_analog_data_scaled2(itf, 'AUD1')

ret = c3d.save_c3d(itf, tgt_c3d_path, compress_param_blocks=True)
ret = c3d.close_c3d(itf)
