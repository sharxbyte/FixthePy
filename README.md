======================================
FixThePy - Python Code Correction Tool
======================================

FixThePy is a Python code correction tool that utilizes the OpenAI API to help you automatically correct errors in your Python scripts. This easy-to-use application provides a graphical user interface (GUI) to guide you through the process.

Usage
-----

1. Launch the FixThePy executable.

2. A splash screen will appear, followed by a window requesting your OpenAI API key. Enter your API key and click "OK". If you don't have an API key or don't want to use the tool, click "Cancel" to exit the application.

3. A file selection dialog will open, prompting you to choose the Python file you want to correct. Select the desired file and click "Open". If you decide not to correct any file, click "Cancel" to exit the application.

4. FixThePy will analyze your code and attempt to correct it using the OpenAI API. The corrected code will be saved in a new file in the same directory as the original file, with "_fixed" added to the end of the filename and a ".py" extension.

5. A message box will appear, informing you that the correction process is complete and displaying the name of the corrected file. Click "OK" to close the application.

Requirements
------------

- Windows, or a way to run windows EXE files on a different OS. (WINE, Parallels, etc.)
- OpenAI API key (obtained from the OpenAI website)

Notes
-----

- This application requires an active internet connection to communicate with the OpenAI API.
- Please ensure that your API key is valid and has the necessary permissions to access the OpenAI API.
- The correction process may take some time, depending on the size of the input file and the complexity of the code.
