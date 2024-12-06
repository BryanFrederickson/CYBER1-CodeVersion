## A collection of project files and documentation regarding the CYBER1-CodeVersion CPTS 421 group capstone project. ## 

# CYBER1-CodeVersion

Developers: Bryan Frederickson, Samantha Brewer (KleinMandolin)

## Project summary

### One-sentence description of the project

Develop a tool to generate unique permutations of a given C/C++ or Python source code file, where the outputs function the same as the original.

### Additional information about the project

This project is meant to help signature-based intrusion detection by being able to generate semantic copies of known code, to better identify malicious software that has been changed to avoid detection.

Rough prototypes can be found in the `python_notebook_tests` branch, which has been kept separate to ensure that main contains only accessible, functional code.

## CSTRenamer
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

## License

[License](./LICENSE)
