import os
import sys
# if sys.path[0] != os.getcwd():
#     sys.path.insert(0, os.getcwd())
# lib_local_path = os.path.normpath(r'C:\WORKSPACE\DEV\pyc3dserver')
# if os.path.exists(lib_local_path):
#     if sys.path[1] != lib_local_path:
#         sys.path.insert(1, lib_local_path)
import numpy as np
import pyvista as pv
import pyc3dserver as c3d
#%%
current_f_dir_path = os.path.dirname(__file__)
c3d_sample_dir_path = os.path.join(current_f_dir_path, r'..\Samples_C3D\Sample00\Vicon Motion Systems')
src_c3d_path = os.path.join(c3d_sample_dir_path, 'pyCGM2 lower limb CGM24 Walking01.c3d')

itf = c3d.c3dserver()
ret = c3d.open_c3d(itf, src_c3d_path)
dict_markers = c3d.get_dict_markers(itf, blocked_nan=True, resid=True, frame=True, time=True)
mkr_pos = dict_markers['DATA']['POS']
mkr_names = c3d.get_marker_names(itf)
frames = dict_markers['FRAME']-dict_markers['FRAME'][0]
plotter = pv.Plotter(line_smoothing=True, point_smoothing=True, window_size=[1280, 640])
plotter.set_background(color=[1, 1, 1])
plotter.enable_parallel_projection()
plotter.add_axes(color=[0, 0, 0])
# plotter.show_bounds(color=[0, 0, 0], location='outer', grid=False, ticks='inside', padding=0.5)

frames_new = np.arange(221-63, 334-63, 1)
cl_grps = [['RASI', 'RPSI', 'LPSI', 'LASI', 'RASI'],\
    ['RHJC_CGM_2.4', 'RKJC_CGM_2.4', 'RAJC_CGM_2.4', 'RFJC_CGM_2.4', 'RHEE', 'RAJC_CGM_2.4'],\
    ['LHJC_CGM_2.4', 'LKJC_CGM_2.4', 'LAJC_CGM_2.4', 'LFJC_CGM_2.4', 'LHEE', 'LAJC_CGM_2.4'],\
    ['RASI', 'RPSI', 'RHJC_CGM_2.4', 'RASI'], ['LASI', 'LPSI', 'LHJC_CGM_2.4', 'LASI']]
for cl in cl_grps:
    cl_mkr_names = cl
    cl_pts = np.zeros((frames_new.shape[0]*len(cl_mkr_names), 3), dtype=np.float)
    cl_lines = np.full((frames_new.shape[0], len(cl_mkr_names)+1), len(cl_mkr_names), dtype=np.int)
    for fr_idx, fr in enumerate(frames_new):
        for mkr_idx, mkr_name in enumerate(cl_mkr_names):
            cl_pts[fr_idx*len(cl_mkr_names)+mkr_idx,:] = mkr_pos[mkr_name][fr,:]
            cl_lines[fr_idx, mkr_idx+1] = fr_idx*len(cl_mkr_names)+mkr_idx
    poly = pv.PolyData()
    poly.points = cl_pts
    poly.lines = cl_lines
    poly['Cycle'] = (frames_new-frames_new[0])/(frames_new[-1]-frames_new[0])*100
    tube = poly.tube(radius=3)
    plotter.add_mesh(tube, smooth_shading=True, show_scalar_bar=False)
plotter.add_scalar_bar(title='Cycle(%)', color=[0, 0, 0], fmt='%.0f')
plotter.view_yz(negative=True)
# plotter.set_scale(xscale=1.5, yscale=1.5, zscale=1.5, reset_camera=False)
plotter.show(title='PyC3Dserver')
plotter.screenshot(filename='test.png', transparent_background=False)

ret = c3d.close_c3d(itf)
