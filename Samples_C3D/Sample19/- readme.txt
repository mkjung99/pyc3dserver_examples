The C3D file contains 34672 frames of analog data (two channels) stored as a PC-Real formatted file.
Note that this file will not be read correctly by any application that reads the C3D header or the
parameters as 16-bit SIGNED values.  It should be read as an UNSIGNED value.

11/01/2005  02:15 PM         4,998,144 sample19.c3d

Note that the file has some incorrect FORCE_PLATFORM:ORIGIN information but since the file does not
contain any valid analog force data this is irrelevant.  The file is provided to allow applications
to be tested with large C3D files containing analog data.