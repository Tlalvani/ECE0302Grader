import os
import shutil

deleteDir = False

currDir = os.getcwd()

subDir = currDir+'/sub'
testSuite = currDir+'/tests'
testFileName = '/FindPalindrome_test.cpp' #.cpp test file. Example from project 2
testCmd = './FindPalindrome-tests' #command to run test


outputPath = currDir+'/output.txt'
output = open(outputPath,'w') #Overwrite output file
output.close()
    	
for filename in sorted(os.listdir(subDir)): #Loop through zipped submissions
	if filename == "README.md":
			continue
	f = os.path.join(subDir, filename)
    # checking if it is a file
	if os.path.isfile(f):
		name = f.replace(subDir, '')
		name = name[0:name.find('_')] #Student name
		print(name)
		tempDir = subDir + name
		testFile = tempDir+testFileName
    	

    	
		if os.path.exists(tempDir): #Delete directory if already exists
			shutil.rmtree(tempDir)
    		
		shutil.unpack_archive(f, tempDir) #Extract zip
    	
		if os.path.exists(testFile): #Remove student's test file
			os.remove(testFile);
		else: #Skip if not found, normally means student did not use make submission
			print("Skipped: ", name)
			continue
    	
    	
		files = os.listdir(tempDir)
    	
		shutil.copytree(testSuite, tempDir, dirs_exist_ok = True) #Copy test files into new directory

		output = open(outputPath,'a') #Append student name
		output.write('\n')
		output.write(name)
		output.close()
    	
    	
		cd = "cd {0}".format(tempDir)
		os.chdir(tempDir)
		os.system("make clean")
		os.system("cmake .")
		os.system("make")
		command = "./{0} >> {1}".format(testCmd, outputPath) #Append terminal output to output.txt
		os.system(command)
		if deleteDir:
			shutil.rmtree(tempDir)
