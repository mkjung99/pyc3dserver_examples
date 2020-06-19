C3D files with TYPE-1 force plate data, one with missing parameter information.

11/13/2007  03:11 PM           170,688 dynamic.C3D
11/13/2007  03:11 PM           128,448 standing.C3D
03/23/2009  02:03 PM           143,360 type1.C3D

Two sample C3D files from a BTS system using their Biomech 2.5 software. These files are interesting
because they contain TYPE-1 force plate data but since the files are missing several important parameters
(e.g. POINT:RATE, POINT:DATA_START etc.) and contain duplicate POINT labels some applications may fail 
to read the data correctly.

A third C3D file (type1.c3d) has been created that corrects the BTS formatting errors to provide sample
TYPE-1 force plate data that should be readable by an C3D complient application.
