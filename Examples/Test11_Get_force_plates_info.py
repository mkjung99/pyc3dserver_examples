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
cwd = os.path.dirname(__file__)

# Type 2 example
c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')

# Type 2 example
# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample01')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'Eb015pr.c3d')

# Type 2 example
# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample05')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'vicon512.c3d')

# Type 3 example
# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample00\Codamotion')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'codamotion_gaitwands_19970212.c3d')

# Type 3 example
# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample26')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'Capture0002.c3d')

# Type 3 example
# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample27')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'kyowadengyo.c3d')

# Type 4 example
# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample10')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'TYPE-4a.c3d')

# Type 1 example
# c3d_sample_dir_path = os.path.join(cwd, r'..\Samples_C3D\Sample28')
# src_c3d_path = os.path.join(c3d_sample_dir_path, 'type1.c3d')

itf = c3d.c3dserver()
c3d.init_logger(logger_lvl='DEBUG', c_hdlr_lvl='DEBUG', f_hdlr_lvl='DEBUG', f_hdlr_f_path=None)
ret = c3d.open_c3d(itf, src_c3d_path)

fp_output = c3d.get_fp_output(itf, 5.0, log=True)

# ground reaction force from a force plate to a subject, expressed in the force plate's local coordinate system, at its top surface center
f_surf_local = fp_output[0]['F_SURF_LOCAL']

# ground reaction moment from a force plate to a subject, expressed in the force plate's local coordinate system, at its top surface center
m_surf_local = fp_output[0]['M_SURF_LOCAL']

# ground reaction force from a force plate to a subject, expressed in the force plate's global coordinate system, at its top surface center
f_surf_global = fp_output[0]['F_SURF_GLOBAL']

# ground reaction moment from a force plate to a subject, expressed in the force plate's global coordinate system, at its top surface center
m_surf_global = fp_output[0]['M_SURF_GLOBAL']

# ground reaction force from a force plate to a subject, expressed in the lab's global coordinate system, at the center of pressure (COP)
f_cop_lab = fp_output[0]['F_COP_LAB']

# ground reaction moment from a force plate to a subject, expressed in the lab's global coordinate system, at the center of pressure (COP)
m_cop_lab = fp_output[0]['M_COP_LAB']

# trajectory of COP, expressed in the lab's global coordinate system
cop_lab = fp_output[0]['COP_LAB']

ret = c3d.close_c3d(itf)
