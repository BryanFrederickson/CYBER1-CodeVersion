## A collection of project files and documentation regarding the CYBER1-CodeVersion CPTS 421 group capstone project. ## 

# CYBER1-CodeVersion

Developers: Bryan Frederickson, Samantha Brewer (KleinMandolin)

## Project summary

### One-sentence description of the project

Develop a tool to generate unique permutations of a given C/C++ or Python source code file, where the outputs function the same as the original.

### Additional information about the project

This project is meant to help signature-based intrusion detection by being able to generate semantic copies of known code, to better identify malicious software that has been changed to avoid detection.

Users will primarily interact with the Argos Translate Language Installer and Python Obfuscator.

## 1. Argos Translate Language Installer
This program is made to help install specific offline translation packages from Argos Translate for use in Variable and Function Obfuscation.

#### Prerequisites
These instructions are written primarily for modern Windows. For installing prerqs on Windows, run Command Prompt as administrator.
1. Python3 **[3.9 or earlier]** - Can be installed in multiple ways. The easiest way for Windows is via [installers](https://www.python.org/downloads/release/python-3913/). Check it's installed via `python --version` in terminal/command line and that the python installation was added to PATH environment variable.
2. tkinter - The Python library used to render a GUI for our programs. The library is usually included with Python installs, but you can check via `pip install tk` on Windows or `sudo apt-get install python3-tk` on Ubuntu.
3. [Argos Translate](https://github.com/argosopentech/argos-translate) - A library for offline language translation in Python. To install, simply run `pip install argostranslate` (more info in linked Repo).

#### Installation and General Use
Navigate to the [`Langs_Installer`](https://github.com/BryanFrederickson/CYBER1-CodeVersion/tree/76643a49d483dd935053f1e334928d436a46c7b2/Langs_Installer) folder on the Main Branch and download all of the files inside. Make sure when running any of the Python files that they are all in the same directory on your system.
- `ArgosTranslate_PreReqs_Installer.py`/`ArgosTranslate_PreReqs_Installer_support.py` - Due to the way the GUI's frontend (main file) and backend (`*_support.py`) work, you can run the program from either file. This program will let the user pick and choose from available language packages and automatically install them for the user.
- `ScrolledCheckedListBox_LangInstall.py` - This file is a dependency and does nothing on its own, serving as a custom tkinter widget for making a scrollable checklist.
- `ArgosTranslate_Installed_Langs.py` - This file does not contain a GUI and the code must be manually configured (commenting out options) to run as desired. The python script can be used to uninstall all installed Argos Translate language packages as well as simply print all packages currently installed.
- 
#### Known Problems
- Currently, there is an issue installing Argos Translate on Python 3.10 or later due to a deprecated dependency, so Python 3.9 - 3.5 is required. Documentation will be updated when issue is fixed.

## 2. Python Obfuscator
This program allows for automated generation of obfuscated semantic clones. A selected input Python source code file will be obfuscated, where variables/functions are translated to other languages and logic loops are changed, while still being functional.

#### Prerequisites
These instructions are written primarily for modern Windows. For installing prerqs on Windows, run Command Prompt as administrator.

The following prerequisites are the same as above for the Argos Translate Language Installer.
1. Python3 **[3.9 or earlier]** - Can be installed in multiple ways. The easiest way for Windows is via [installers](https://www.python.org/downloads/release/python-3913/). Check it's installed via `python --version` in terminal/command line and that the python installation was added to PATH environment variable.
2. tkinter - The Python library used to render a GUI for our programs. The library is usually included with Python installs, but you can check via `pip install tk` on Windows or `sudo apt-get install python3-tk` on Ubuntu.
3. [Argos Translate](https://github.com/argosopentech/argos-translate) - A library for offline language translation in Python. To install, simply run `pip install argostranslate` (more info in linked Repo).

Additionally required:

4. [LibCST](https://github.com/Instagram/LibCST) - A library for converting Python source code to and from Concrete Syntax Trees (CSTs). CSTs build on abstract syntax trees by preserving formatting and cosmetic parts of the code, allowing for changes to not disturb the overall program structure. Install via `pip install libcst`.

#### Installation and General Use
Navigate to the [Python_Obfuscator](https://github.com/BryanFrederickson/CYBER1-CodeVersion/tree/65599df46c11487d5cb75023a377683cd6733873/Python_Obfuscator) folder on the Main Branch and download all files inside. Make sure when running any of the Python files that they are all in the same directory on your system.
- `Python_Obfuscator.py`/`Python_Obfuscator_support.py` - Due to the way the GUI's frontend (main file) and backend (`*_support.py`) work, you can run the program from either file. This program will automate the process for generating obfuscated clones, while allowing the user to tweak generation parameters.
- `ScrolledCheckedListBox_PyObfsc.py` - This file is a dependency and does nothing on its own, serving as a custom tkinter widget for making a scrollable checklist.
- `coding_abbreviations.py` - This file contains common abbreviations in variable or function names e.g. mem -> memory. This dictionary is used to convert variable substring abbreviations to a corresponding full term for accurate language translation. Common abbreviations list from the [`Abbreviations in code`](https://github.com/abbrcode/abbreviations-in-code) repository.

#### Known Problems
- Currently, `Logic Obfuscation` is disabled as a parameter (set to 0% probability during generation) due to issues with edge cases. Will be enabled once logic obfuscation code has been made robust enough to no longer crash.
- Currently, there is an issue installing Argos Translate on Python 3.10 or later due to a deprecated dependency, so Python 3.9 - 3.5 is required. Documentation will be updated when issue is fixed.



## CSTRenamer
An old implementation of variable and function renaming in Python source code, working with Gemini for synonym translation and backup word banks (colors and animals). **Unsupported.**
#### Prerequisites
These instructions are written for modern Windows. For installing prerqs on Windows, run Command Prompt as administrator.
1. Python3 - Can be installed in multiple ways. The easiest way for Windows is via [installers](https://www.python.org/downloads/windows/). Check it's installed via `python --version` in powershell/command line and that the python installation was added to PATH environment variable.
2. LibCST - Installed in command line/powershell using `pip install libcst`
3. Gemini API - Installed via command line/powershell using `pip install -U google-generativeai`

#### Installation and General Use
1. Download the CSTRename.py file in the CSTRenamer folder on the main branch.
2. For modern Windows, run the Command Prompt with no administrator. This can be done in the folder with `CSTRename.py` so the command is simply `python CSTRename.py` or, if the Command Prompt is run from a different location, schift right click `CSTRename.py` and "copy as path", then paste into the Command Prompt via right click as `python path/to/file/CSTRename.py`.
3. Follow the in-terminal prompts to generate renamed code.

The user can specify the location of the input Python source file (only one is supported at a time), then the amount of unique clones to generate, the probabilities for variables or functions being renamed, and then the location to save the output files to. The output files have the naming scheme of `[original name]_RENAMED_[count].py`. For example, using the "func-names-complex.py" test file in the Python notebooks test branch, the second output would be `func-names-complex_RENAMED_1.py`.

#### Known Problems
- Due to the Gemini API key being linked to a free account, errors in requesting synonyms due to maxing out the API call limit print to the terminal (with additional warnings showing up in the Google Colab implementation). Since these errors are largely cosmetic (since an animal wordbank is used as a backup), they can be ignored.
- In the python Command Prompt implementation, there is an additional warning at the end of execution warning about error output being sent to STDERR instead. This is because of a dependency required for the Gemini API python library and is not fixed as of 11/30/2024, but does not seem to cause any actual running issues.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Additional Documentation

Sprint 1 Deliverables:
  * [Sprint 1 Report](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/a25a48244798548cd4a268eccc165d2b1de35dab/Sprints/Sprint%201/Sprint%201%20Report.md)
  * [Sprint 1 Video](https://youtu.be/1v400lVrzvU)

Sprint 2 Deliverables:
  * [Sprint 2 Report](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/6e0719cde0e0347c24d3416c51d3eb0ba2188fb2/Sprints/Sprint%202/Sprint%202%20Report.md)
  * [Sprint 2 Video](https://youtu.be/h4OGVBQQoWc)

Sprint 3 Deliverables:
  * [Sprint 3 Report](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Sprints/Sprint%203/Sprint%203%20Report.md)
  * [Sprint 3 Video](https://www.youtube.com/watch?v=I8yIiHRUb8E)

End of Semester 1 Documentation:
  * [In-Class Presentation Video](https://www.youtube.com/watch?v=1ktzkDxGp1U)
  * [CYBER1 Project Report](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Resources/CYBER1%20Project%20Report%20End%20of%20Semester%201.pdf)

Sprint 4 Deliverables:
* [Sprint 4 Report](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Sprints/Sprint%204/Sprint%204%20Report.md)
* [Sprint 4 Video](https://www.youtube.com/watch?v=KbjT55ulSEI)

Sprint 5 Deliverables:
* [Sprint 5 Report](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Sprints/Sprint%205/Sprint%205%20Report.md)
* [Sprint 5 Video](https://www.youtube.com/watch?v=H363BK4t65Y)

## License

[License](./LICENSE)
