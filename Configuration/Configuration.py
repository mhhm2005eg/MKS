import os,  stat
import shlex, subprocess
import sys, getopt
import logging
import glob
from os.path import basename , dirname
#import CppHeaderParser
import shutil
import datetime
import configparser
import xml.etree.ElementTree as ET
import copy
DevPath="MFC4T0_B2_01.02"
ChangePackageList={"MFC400":"209686:2","SRLCam":"203064:1"}

CMPList = ["SAC_StereoAutoCalibration", "FSD_FreeSpaceDetection"]
#####################################################
ListOfProjects = ["MFC400", "SRLCam"]
PrjOfDevPath = {"MFC4T0_B1_01.01":"MFC400","MFC4T0_B2_01.02":"MFC400","SRLCam4T0_R2.0.0_INT1":"SRLCam","SRLCam4T0_2.1":"SRLCam","SRLCam4T0_2.2":"SRLCam",}
MainProjectName=PrjOfDevPath[DevPath]
ChangePackage=ChangePackageList[MainProjectName]

class SubProject:
	def __init__(self, ID):
		self.ID = ID
		self.path=""
		self.cmp=""
		self.label=""
		self.Cp=""
		self.Rev=""
		self.Typ=""
		
SubProjectList=[]

def dump(obj):
   for attr in dir(obj):
       if hasattr( obj, attr ):
           print( "obj.%s = %s" % (attr, getattr(obj, attr)))
		   
def ReadIni(IniFileName):
	returnValue = {}
	config = configparser.ConfigParser()
	config.read(IniFileName)
	SectionList = config.sections()	
	for section in SectionList:
		for x in config[section]:
			returnValue[x] = config[section][x]
	return (returnValue)
	
def ReadXml(XmlFileName, tag):
	returnValue = {}
	Paths = {}
	CurrentLabel = {}
	 
	SubPros = []
	tree = ET.parse(XmlFileName)
	root = tree.getroot()
	xx=0
	yy=0
	for Cfg in root.findall(tag):
		subPro = SubProject(xx)
		xx=xx+1
		CMPName = Cfg.get('CompName')
		Paths[CMPName] = Cfg.get('Path')
		CurrentLabel[CMPName] = Cfg.find('Label').get('Label')
		subPro.path=Cfg.get('Path')
		subPro.label = Cfg.find('Label').get('Label')
		subPro.Rev = Cfg.find('Revision').get('Revision')
		subPro.Typ = Cfg.find('Type').get('Type')
		subPro.cmp=CMPName
		#returnValue[Cfg.get('name')] = Cfg.text
		SubPros.append(copy.deepcopy(subPro))
		#dump(subPro)
		
	return SubPros

def GetRevisionForLabel(RootProject, SharedProject, Label):
		"""
		GetRevisionForLabel( SharedProject, Label)

		Description: Get the revision corresponding to a label

		Parameter: -SharedProject the path from where the shared project is shared
				   -Label serach the revision to this label

		return 0 if label could not be found in this shared project
		"""
		ret_value = "default"
		cmdline_info='si viewprojecthistory --batch  --fields=labels,revision --rfilter=labeled --project='+SharedProject
#		print SharedProject
		try:
			proc=subprocess.Popen(cmdline_info, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout_str, stderr_str = proc.communicate()
			stdout_str_lines = stdout_str.splitlines()
		except OSError,ValueError:
			print formatExceptionInfo()
#		print Label
		for line in stdout_str_lines:
			#print line
			if (len(line) > 1):
				argu = line.split()
				#print (argu)
				if (len(argu) > 2):
					argu[1] = argu[len(argu)-1]
					argu[0] = line.replace(argu[1],"")
					argu[0] = argu[0].rstrip()
					argu[0] = argu[0].replace("\n","")
	#					print argu[0]
					if (len(argu) > 1):
	#					print argu[0]
	#					print argu[1]

						# check if unicode
						try:
							argu[0].decode('ascii')
						except UnicodeDecodeError:
							Common.Tell("Decoding issue")
				else:
					# an ascii-encoded unicode string
					#print(argu[0],1)
					if (argu[0] == Label):
						ret_value = argu[1]
						#print(cmdline_info)
						break
#						print "Return value " + ret_value
		return ret_value
def ConfigCompList():
	for folder in BasicDestinationSubProjectList:
		for CMP in ExtendedCompanentNames	:
			#/nfs/projekte1/PROJECTS/MFC400/06_Algorithm/04_Engineering/05_Deliverables/lib/ti_c674x/algo/project.pj
			ProjectToBeConfigured="/nfs/projekte1/PROJECTS/"+PrjOfDevPath[DevPath]+"/06_Algorithm"+folder+CMP+"/project.pj"
			RootProjectToBeConfigured="/nfs/projekte1/PROJECTS/"+PrjOfDevPath[DevPath]+"/06_Algorithm"+folder+"project.pj"
			LabelList = ExtendedLabelsOfCMP[CMP]
			for Label in LabelList:
				CP = GetRevisionForLabel(RootProjectToBeConfigured, ProjectToBeConfigured, Label)
				if CP != "default":
					print()
					print(" ---- Start Config-----")
					print("Subproject: "+ProjectToBeConfigured)
					print("Label: "+Label)
					print("Checkpoint: "+CP)
					Command="si configuresubproject  --type=build --cpid="+ChangePackage+" --subprojectRevision="+CP+" --project="+RootProjectToBeConfigured +" --devpath="+DevPath +" "+ProjectToBeConfigured
					ret = subprocess.call(Command, shell=True)
					print(Command)
				#ret=1
				#if ret == 0:
					#Common.Tell(Command)

def FilterSubproject(Subs, COMPList):
	RetList = []
	for Sub in Subs:
		for CMP in COMPList:
			if Sub.cmp == CMP:
				RetList.append(Sub)
				
	return (RetList)

def printSubProj(Sub):
	att = Sub.__dict__
	for x in att:
		y = eval(x)
		print(y)
		
def ParsConfFiles()
def main():
	ret = ReadXml("D:\\Sandboxs\\SMFC4B0_07.00.00\\06_Algorithm\\post_config_shared_projects.xml", "SharedProjectConfig")
	#for x in ret:
		#dump(x)
	#printSubProj(ret)
	Filtered = FilterSubproject(ret, CMPList)
	for x in Filtered:
		dump(x)
	#print(Filtered)
	#ret = ReadIni("Conf.ini")
	#print(ret)
	
main()