import os
import copy
import csv
import stat
import sys
import subprocess
import time
import traceback
import xml.dom.minidom
import string
import shutil
import posixpath as posixpath  

cmdline_info='si viewprojecthistory --batch  --project=/nfs/projekte1/PROJECTS/MFC400/06_Algorithm/04_Engineering/05_Deliverables/lib/ti_c674x/algo/project.pj --fields=labels,revision --rfilter=labeled'

proc=subprocess.Popen(cmdline_info, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout_str, stderr_str = proc.communicate()
stdout_str_lines = stdout_str.splitlines()

print (stdout_str_lines)

