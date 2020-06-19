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
def logger_init(name=None, logger_lvl='WARNING', c_hdlr_lvl='DEBUG', f_hdlr_lvl='ERROR', f_hdlr_f_path=None):
    if name is None:
        name = __file__
    logger = logging.getLogger(name)
    logger.setLevel(logger_lvl)
    while logger.hasHandlers():
        logger.removeHandler(logger.handlers[0])    
    if not logger.handlers:
        c_hdlr = logging.StreamHandler()
        c_hdlr.setLevel(c_hdlr_lvl)
        c_fmt = logging.Formatter('%(name)s[%(levelname)s] - %(message)s')
        c_hdlr.setFormatter(c_fmt)
        logger.addHandler(c_hdlr)
        if f_hdlr_f_path is not None:
            f_hdlr = logging.FileHandler(f_hdlr_f_path, mode='w')
            f_hdlr.setLevel(f_hdlr_lvl)
            f_fmt = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')
            f_hdlr.setFormatter(f_fmt)
            logger.addHandler(f_hdlr)  
    return logger
#%%
c3d_sample_dir_path = os.path.join(os.getcwd(), r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')
# tgt_c3d_path = os.path.splitext(src_c3d_path)[0]+'_modified.c3d'

logger = logger_init(name='C3D', logger_lvl='DEBUG', c_hdlr_lvl='INFO', f_hdlr_lvl='INFO', f_hdlr_f_path=None)

itf = c3d.c3dserver()
ret = c3d.open_c3d(itf, src_c3d_path, 'C3D')
dict_header = c3d.get_dict_header(itf)
dict_groups = c3d.get_dict_groups(itf)
dict_mkr = c3d.get_dict_markers(itf, blocked_nan=True, residual=True, mask=False)
dict_forces = c3d.get_dict_forces(itf)

val0 = c3d.get_analog_data_scaled(itf, 'Force.Fx1')
val1 = c3d.get_analog_data_scaled2(itf, 'Force.Fx1')
# ret = c3d.save_c3d(itf, tgt_c3d_path)
ret = c3d.close_c3d(itf)

# logging.shutdown()