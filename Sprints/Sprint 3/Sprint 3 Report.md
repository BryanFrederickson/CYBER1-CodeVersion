# Sprint 3 Report (Dates from Sprint 2 to Sprint 3)

[Sprint 3 Demo Video](https://www.youtube.com/watch?v=GbDYehnC3po)

## What's New (User Facing)
* Command Prompt (Windows) Terminal Implementation of CST Renamer (in `main` branch)
* Google Colab Notebook Implementation of CST Renamer (in `python-notebook-tests` branch)

## Work Summary (Developer Facing)
Finished full CST renamer, with both a Command Prompt and Google Colab Notebook implementation (with the main difference being the way files are saved). N-parameter and multiple unique outputs are supported, with nondeterministic generation by specifying the probabilities a variabel or function is renamed for that specific run. In the Command Prompt, an input file path and output file path can be parsed and accessed.

## Unfinished Work
Stretch goals such as more complex CST manipulations (e.g. converting `for` loops to `while` loops and vice versa) were not reached. A more involved GUI was deemed unecesseary compared to making sure the CST Renamer fully functioned and covered as many edge cases as possible.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * #1  - [Unique N Permutations](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/1)
 * #17 - [Auto Rename Variables](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/17)
 * #18 - [Google Gemini Synonym Generation (Variables)](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/18)
 * #19 - [Google Gemini Synonym Generation (Functions)](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/19)
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:

 * #3  - [Create a UI for Python file parameter input](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/3)
   - Left as simple text imput for Command Prompt and as built-in file upload for Google Colab.
 * #14 - [Create a base GUI window](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/14)
   - A detailed GUI was deemed a stretch goal as we prioritized covering edge cases in the CST Renamer itself. The GUI is limited to typing parameters into the terminal for both implementations.


## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality (found in python-notebook-tests branch):
 * [CS421_Project_CYBER1_CodeVersion.ipynb](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/python-notebook-tests/CS421_Project_CYBER1_CodeVersion.ipynb)
 * [CSTRename.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/CSTRenamer/CSTRename.py)
 
## Retrospective Summary
Here's what went well:
  * Communication was great between the team. Comments surrounding code snippets helped team understand the functionality and implementations of solutions so we could test functional components in conjunction with each other.
  * Google Colab was very organized and well documented to show a step by step iteration of how the Cyber1 - CodeVersion performs in a linear step fashion.
 
Here's what we'd like to improve:
   * While we do have a great method for backup synonym renaming using lists of animals and colors, the team will explore better methods than the Gemini API which gets exausted relatively quickly.
   * The team plans to improve understanding and allocate more time to research newly focused topics that was introduced by our client.
  
Here are changes we plan to implement in the next sprint:
   * Instead of utilizing AST and CST structures, the team plans to explore Property Graphs as well as genetic algorithms to help develop semantic clones.
   * More focus will be allocated for the UI design to allow the Cybersecurity professioanl to efficiently interact with the tool.
