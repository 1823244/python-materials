import glob, os

path = 'c:/PROJECTS/012_AccountingCorpIFRS_7_acc_chart_stor/files/Circular_200_2014_TT-BTC_ENG/doxygen/code/'
os.chdir(path)
for file in glob.glob("*.java"):

	if file.find('_Account_')>-1:
		#print(file)
		code = file[file.index("_Account_")+len("_Account_"):file.index(".java")]
		#print(code)
		os.rename(path+file, path+'acc_'+code+'.java')
