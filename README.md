# ECE0302Grader

Autograder for ECE0302 Data Structures and Algorithms

/sub directory should include zipped canvas submission for each student <br/>

/tests should contain CMakeLists.txt and .cpp test file. Make sure not to include any solution class files. <br/>

Before running, grader.py should be modified to include test file name.

Grader can be run using "python3 grader.py". This will generate an output.txt file to view results. If the output file does not contain the output for a student, it normally means they did not build using make submission or their code did not compile.
