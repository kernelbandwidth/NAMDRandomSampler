#!/usr/bin/env python

'''Simple script to randomly sample from dcd files.  Relys on VMD calls.'''

from random import randint
import subprocess
import sys

def write_vmd_script(dcdfilename, frame_number):
    pass

if __name__ == "__main__":
    local_directory = sys.argv[1]
    dcd_files = subprocess.check_output(["ls", local_directory + "/*.dcd"])
    for dcd_file in dcd_files:
        frame_number = randint(1000, 6000)
        write_vmd_script(dcd_file, frame_number)
        subprocess.call(["vmd"
                        ,"-dispdev"
                        ,"text"
                        ,"-eofexit"
                        
                        ,psf_file
                        ,dcd_file
                        ])
