def ConfigList() :
	for FolderNameLoop in Subfolders:
		#print (FolderNameLoop)
		FolderName = os.path.basename(FolderNameLoop)
		#print(FolderName)
		for Component in ExecutiveComponentList:
			if FolderName == Component:
				Common.Tell ("------------------")
				Common.Tell ("Subproject Figured")
				Common.Tell ("------------------")
				Common.Tell (FolderNameLoop)
				ProjectName=FolderNameLoop+"/project.pj"
				Common.Tell (ProjectName)
				Command= RefCommand +"  "+ ProjectName
				subprocess.call(Command, shell=True)
				Common.Tell(Command)
				Common.Tell ("------------------")
			Common.Tell ("Subproject Removed")
			Common.Tell ("------------------")
import os
import Config
import Common
import shlex, subprocess
import sys, getopt
import logging

from os.path import basename
			
def ConfigAllSub() :
	for FolderNameLoop in Subfolders:
		#print (FolderNameLoop)
		FolderName = os.path.basename(FolderNameLoop)
		#print(FolderName)
		Common.Tell ("------------------")
		Common.Tell ("Subproject Figured")
		Common.Tell ("------------------")
		Common.Tell (FolderNameLoop)
		ProjectName=FolderNameLoop+"/project.pj"
		Common.Tell (ProjectName)
		Command= SharedFolderVariantCommand + +"  "+ ProjectName
		subprocess.call(Command, shell=True)
		Common.Tell(Command)
		Common.Tell ("------------------")
		Common.Tell ("Subproject OPerated")
		Common.Tell ("------------------")
			
			
def ConfigSharedListToVariant() :
	for FolderNameLoop in Subfolders:
		#print (FolderNameLoop)
		FolderName = os.path.basename(FolderNameLoop)
		#print(FolderName)
		for Component in ExecutiveComponentList:
			if FolderName == Component:
				Common.Tell ("------------------")
				Common.Tell ("Subproject Figured")
				Common.Tell ("------------------")
				Common.Tell (FolderNameLoop)
				ProjectName=FolderNameLoop+"/project.pj"
				Common.Tell (ProjectName)
				Command= SharedFolderVariantCommand + VariantConfigAll[Component]+"  "+ ProjectName
				subprocess.call(Command, shell=True)
				Common.Tell(Command)
				Common.Tell ("------------------")
				Common.Tell ("Subproject Configured")
				Common.Tell ("------------------")	