# Sprint 4 Report (1/10/25 - 2/10/25)

[Sprint 4 Demo Video](https://www.youtube.com/watch?v=KbjT55ulSEI)

## What's New (User Facing)
* Variable/Function token parsing to replace gemini API prompting approach
* Logic obfuscation techniques such as while loops to for loops
  

## Work Summary (Developer Facing)
Cases using the greater than and less than operator in while loops with the variable switching on LHS or RHS of expression is covered for logic obfuscation. Variable and function renamer offers tokenization to seperate words based on different types of coding syntax (camelCase, snake_case, etc.). 



## Unfinished Work
Logic obfuscation techniques require a number of specific edge cases. Implementation of vise versa needs to be covered as well as if statement obfuscation. Variable parser requires API tokens, runtime in Colab files requires a pretty hefty install. Work on making process simpler for those who want to utlize the software. GUI has been put on backburner, start working on integrating UI framework.


## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * #20  - [Understand Code Property Graph Significance](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/20)
   - Part of research into alternate methods of manipulating source code that did not pan out. Closed as Code Property Graphs are not manipulable and cannot be converted back into source code using existing software. Work will be done solely using Concrete Syntax Trees.
 * #21 - [Research Control Flow Graph](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/21)
   - See above. Control Flow Graphs do not present enough benefits over Concrete Syntax Trees to justify switching over or adding the new, unfamiliar data type. Work will be done solely using Concrete Syntax Trees.
 * #22 - [Python Library Exploration](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/22)
   - See both above issues, as they comprise the main goal of this issue.
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:

 * #3  - [Create a UI for Python file parameter input](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/3)
   - After basic terminal implementation was finished last sprint, more obfuscation techniques were prioritized over a new GUI implementation. After issues with Google Colab and translation library packages arose, it is now planned to begin developing a GUI with tkinter in the next sprint.
 * #14 - [Create a base GUI window](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/14)
   - See above.
 * #23 - [Translate Variable/Function Names](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/23)
   - A Variable/Funtion Name parser was developed, that can break the strings down into individual tokens based on common naming conventions (camelCase, snake_case, etc.) and also turn common abbreviations in coding into their full terms. However, translation ran into issues with limited API tokens and then lengthy installs for offline translation packages. The latter is the reason a GUI is now being prioritized, so that the installation can be done once rather than for each Colab runtime.
 * #24 = [Logic Obfuscation](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/24)
   - Developing a way to swap out loop types (for, while, etc.) has had several edge cases to account for that have impeded development time, so the feature was not fully completed this sprint.


## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality (found in python-notebook-tests branch):
 * [CS421_Project_CYBER1_CodeVersion.ipynb](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/python-notebook-tests/CS421_Project_CYBER1_CodeVersion.ipynb)
 
## Retrospective Summary
Here's what went well:
  * Team did a great job at distributing tasks for the current Sprint. Research on Control Flow Graphs and Property Graphs allowed team to understand the limits of future implementation and to focus on current CST methods.
 
Here's what we'd like to improve:
   * As the capstone requires a UI for users to interact with, more focus should be put on designing and interface that is convenient for others who want to utilize the tool.
  
Here are changes we plan to implement in the next sprint:
   * Next sprint, we plan to have a baseline or clear framework of how the user will interact with our system from a visual perspective. Function/Variable parsing will be more effecient, and more methods of logic obfuscation will be integrated.
