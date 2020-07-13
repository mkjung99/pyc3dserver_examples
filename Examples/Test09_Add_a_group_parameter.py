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

c3d.add_param(itf, 'MANUFACTURER', 'EDITED', 'PyC3Dserver', log=True)
c3d.add_param(itf, 'MANUFACTURER', 'YEAR', 2020, log=True)

ret = c3d.save_c3d(itf, tgt_c3d_path, compress_param_blocks=True, log=True)
ret = c3d.close_c3d(itf, log=True)
