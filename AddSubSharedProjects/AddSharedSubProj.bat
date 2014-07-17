@echo off
set DestenationProject=/nfs/projekte1/PROJECTS/MFC400/06_Algorithm/04_Engineering/03_Workspace/algo/project.pj --devpath MFC4T0
rem set DestenationProject=/nfs/projekte1/PROJECTS/PROJECTS.pj#MFC400#d=MFC4T0#06_Algorithm/04_Engineering/03_Workspace/algo

set ChangePackage=209686:2
set SourceProject=/nfs/projekte1/REPOSITORY/Base_Development/05_Algorithm/CCT_CommonCameraToolbox/04_Engineering/03_Workspace/algo/cct/project.pj --type=normal

set NewFolderPath=/nfs/projekte1/PROJECTS/MFC400/06_Algorithm/04_Engineering/03_Workspace/algo/cct/project.pj

rem --type=variant --variant=MFC4T0 --subprojectDevelopmentPath=MFC4T0
rem set DestenationProject=/nfs/projekte1/PROJECTS/MFC400/06_Algorithm/04_Engineering/03_Workspace/algo/project.pj#d=MFC4T0	
rem set test=-P "#/nfs/projekte1/PROJECTS/MFC400#d=MFC4T0#/06_Algorithm/04_Engineering/03_Workspace/algo"

si sharesubproject --cpid=%ChangePackage%   --project=%DestenationProject% --sharedProject=%SourceProject%  %NewFolderPath%

rem : correct
rem set test=-P "#p=/nfs/projekte1/PROJECTS/PROJECTS.pj#MFC400#d=MFC4T0#06_Algorithm/04_Engineering/03_Workspace/algo"
rem si sharesubproject --cpid=%ChangePackage%   %test% --sharedProject=%SourceProject% --type=normal %NewFolderPath%

rem : end correct 

