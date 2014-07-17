import os
#import SCons

#Env = Environment()

ProjectName="SMFC4B0"

OutFile="./Out\\"+ProjectName # name of the final executable.
LibFile="./Lib\\" # name of the final executable.
DllFile="./Dll\\" # name of the final executable.
ObjDir=str("./Obj/")          # Directory for the obj files.
IncDir=str("./Inc/")

RecursiveSourceFolders=[]#["./../../../../../04_Engineering/01_Source_Code"] #Folders which will be scanned recursivly for the extensions *.c
SourceFolders=[] #Folders which will be scanned for the extensions *.c
SourceFiles=[] #specific files to be built

RecursiveHeaderFolders=["./../../../../../04_Engineering/01_Source_Code/common"] #Folders which will be scanned recursivly for the extensions *.h
HeaderFolders=[] #Folders which will be scanned for the extensions *.h

RecursiveLibFolders=[] #Folders which will be scanned recursivly for the extensions *.lib
LibFolders=[] #Folders which will be scanned for the extensions *.lib
LibFiles=[] #specific files to be linked

ComponentsList = \
[ \
#"00_Custom",\
"cb",\
#"cct",\
#"cipp",\
"cml",\
"ecm",\
"em",\
"fct",\
"fex",\
"fsd",\
"ftrc",\
"gen",\
"hla",\
"ld",\
"memo",\
"ofc",\
"pc",\
"ped",\
"pv",\
"rtw",\
"sac",\
"semo",\
"sib",\
"sr",\
"tsa",\
"vcl",\
"vdy",\
"vodca"\
  ]
  
Targetdict = {\
#"00_Custom":"MCU",\
"cb":"VME_MONO",\
"cct":"VME_STEREO",\
"cipp":"MCU",\
"cml":"VME_STEREO",\
"ecm":"VME_STEREO",\
"em":"VME_STEREO",\
"fct":"VME_MONO",\
"fex":"VME_FPGA",\
"fsd":"VME_STEREO",\
"ftrc":"VME_STEREO",\
"gen":"VME_STEREO",\
"hla":"VME_MONO",\
"ld":"VME_MONO",\
"memo":"MCU",\
"ofc":"VME_STEREO",\
"pc":"VME_STEREO",\
"ped":"VME_STEREO",\
"pv":"VME_STEREO",\
"rtw":"VME_STEREO",\
"sac":"VME_STEREO",\
"semo":"VME_STEREO",\
"sib":"VME_STEREO",\
"sr":"VME_MONO",\
"tsa":"VME_STEREO",\
"vcl":"VME_STEREO",\
"vdy":"VME_MONO",\
"vodca":"VME_STEREO",\
}  

Includedict = {\
#"00_Custom":[],\
"cb":["D:/Sandboxs/Algorithm/CB_CameraBlockage/04_Engineering/02_Development_Tools/ti_tools"],\
"cct":[],\
"cipp":["D:/Sandboxs/Algorithm/CIPP_CommonImagePreProcessing/04_Engineering/02_Development_Tools/ti_tools"],\
"cml":[],\
"ecm":[],\
"em":[],\
"fct":[],\
"fex":[],\
"fsd":[],\
"ftrc":[],\
"gen":[],\
"hla":[],\
"ld":[],\
"memo":[],\
"ofc":[],\
"pc":[],\
"ped":[],\
"pv":[],\
"rtw":[],\
"sac":[],\
"semo":[],\
"sib":[],\
"sr":[],\
"tsa":[],\
"vcl":[],\
"vdy":[],\
"vodca":[],\
}  