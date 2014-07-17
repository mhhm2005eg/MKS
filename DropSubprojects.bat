@echo off

set ProjectName=SRLCam
set DevPathName=SRLCam4T0_2.0
set SubProjectName=06_Algorithm/04_Engineering/05_Deliverables/include/algo/sib

rem si dropproject --hostname=mks-psad --port=7001 /nfs/projekte1/PROJECTS/PROJECTS.pj#%ProjectName%#d=%DevPathName%#%SubProjectName% 
si drop sib --devpath=%DevPathName%  --project=/nfs/projekte1/PROJECTS/SRLCam/06_Algorithm/04_Engineering/05_Deliverables/include/algo/project.pj rem --hostname=mks-psad --port=7001 

pause


rem /nfs/projekte1/PROJECTS/<corect pathe>/06_Algorithm/04_Engineering/05_Deliverables/include/algo/sib/project.pj