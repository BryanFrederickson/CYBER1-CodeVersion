# Sprint 5 Report (2/11/25 - 3/17/2025)

Sprint 5 Demo Video WIP

## What's New (User Facing)
* [Argos Translate Language Installer](https://github.com/BryanFrederickson/CYBER1-CodeVersion?tab=readme-ov-file#argos-translate-language-installer) - to automate installation of specific languages in Argos Translate
* [Python Obfuscator](https://github.com/BryanFrederickson/CYBER1-CodeVersion?tab=readme-ov-file#python-obfuscator) - to automate clone generation
  

## Work Summary (Developer Facing)
Created two separate GUI-based python programs: the [Argos Translate Language Installer](https://github.com/BryanFrederickson/CYBER1-CodeVersion?tab=readme-ov-file#argos-translate-language-installer) and the [Python Obfuscator](https://github.com/BryanFrederickson/CYBER1-CodeVersion?tab=readme-ov-file#python-obfuscator).

The Argos Translate Language Installer is used to install language packages for translation in the obfuscator. If none are installed, translation is disabled in the Python Obfuscator. Included in the folder [Langs_Installer](https://github.com/BryanFrederickson/CYBER1-CodeVersion/tree/ec1200c8e0fd2cca01e124562dd132b97c388d13/Langs_Installer) is a test file that prints installed language packages and can also uninstall all installed packages.

The Python Obfuscator allows the user to select clone generation parameters and begin automatic generation. There is robust parameter handling, so that invalid parameters or data cannot be used. If the user changes a parameter, the generation button is disabled if previous parameters were valid and tested, and input data is stored on input select so that it cannot be edited after validation but before generation. Once the user selects their parameters, they can begin generation and watch the output while clones are generated.

## Unfinished Work
WIP


## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * #3  - [Create a UI for Python file parameter input](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/3)
   - Completed as part of larger completed Python Obfuscator GUI (see below). Implemented by selecting an 'Open' button that opens the OS's filesystem navigator for the user to select and input file, with robust error handling.
 * #14 - [Create a base GUI window](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/14)
   - Completed as part of larger Python Obfuscator GUI (see issue closed comment). Allows the user to select generation parameters (input file, output locations, clone count, language input and outputs, and probabilities).
 * #23 - [Translate Variable/Function Names](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/23)
   - Translation works as expected and outputs normally with minimal wait between translation queries (although it has not been tested with larger files). Certain features are functional but limited, with their continued development relegated to new issues (see below).
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:

 * #24  - [Logic Obfuscation](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/24)
   - WIP
 * #25 - [Fix Foreign Alphabet Translation](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/25)
   - A new issue created after finishing the Python Obfuscator to address limitations in the current translation algorithm. Currently, translation replaces non-Latin characters with random Latin letters to solve issues regarding unsupported UTF-8 characters. Work will be done to better parse characters so that translation is accurate but functionality is preserved.
 * #26 - [Add more Output Var/Func Name Convention Styles](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/26)
   - A new issue created after finishing the Python Obfuscator to address limitations in the current translation algorithm. Currently, translated variables and functions follow the snake case (underscores) naming convention. Work will be done to add more possible naming conventions.
 * #27 - [Optimize Translation](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/27)
   - A new issue created after finishing the Python Obfuscator to address limitations in the current translation algorithm. Currently, the translation module (specific to a given input and output language) is regenerated with each call to translate a given name. Since the output language is selected per clone, the translation module can be generated once per clone generation instead of per name. Work will be done to implement this and other optimizations.
* #28 - [Implement External Log Output to Obfuscator](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/28)
   - A new issue created following Client request for more generation data being made accessible to the user. Includes both more updates (e.g. each variable being renamed and what it was renamed to) as well as external log files. These saved log files can be used to address crashes/unexpected behaviour as well as allow the user to see generation data without needing to keep the program open.


## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality (for more info on file functionality, see the [Main Branch READEME](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/d441899c093c13e51d996bdf9c3109f6f130bf16/README.md)):
### Argos Translate Language Installer
 * [ArgosTranslate_Installed_Langs.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Langs_Installer/ArgosTranslate_Installed_Langs.py)
 * [ArgosTranslate_PreReqs_Installer.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Langs_Installer/ArgosTranslate_PreReqs_Installer.py)
 * [ArgosTranslate_PreReqs_Installer_support.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Langs_Installer/ArgosTranslate_PreReqs_Installer_support.py)
 * [ScrolledCheckedListBox.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Langs_Installer/ScrolledCheckedListBox.py)
### Python Obfuscator
 * [Python_Obfuscator.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Python_Obfuscator/Python_Obfuscator.py)
 * [Python_Obfuscator_support.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Python_Obfuscator/Python_Obfuscator_support.py)
 * [ScrolledCheckedListBox.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Python_Obfuscator/ScrolledCheckedListBox.py)
 * [coding_abbreviations.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Python_Obfuscator/coding_abbreviations.py)


## Retrospective Summary
Here's what went well:
  * WIP
 
Here's what we'd like to improve:
   * WIP
  
Here are changes we plan to implement in the next sprint:
   * WIP
