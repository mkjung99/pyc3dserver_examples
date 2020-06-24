This is a set of files that have been created to demonstrate that the C3D frame count can be stored
by writing the POINT:FRAMES parameter to the C3D file as a floating point value instead of the common
integer value or multiple parameter values.

There are two sets of three files, each file name documents the number of frames expected in the file.
The last letter in the file name indicates the POINT:FRAMES format as either integer (i) or floating 
point (f).  

Files written with POINT:FRAMES stored as an integer contain the traditional TRIAL and LONG_FRAMES
parameters.  Files written with POINT:FRAMES stored as a floating point number do not have either the
TRIAL or LONG_FRAMES parameters to ensure that when these files are read, the application is reading and
using only the POINT:FRAMES value.  

All applications that determine the parameter type before reading the parameter should have no problem
reading these files although applications that store the frame count internally as an integer may have
internal issues with the larger frame counts.

These files have been manually edited so there may be some minor internal parameter formatting issues.
Please let me know if you discover any errors.

