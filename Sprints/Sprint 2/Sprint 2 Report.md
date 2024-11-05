# Sprint x Report (Dates from Sprint 1 to Sprint 2)

## YouTube link of Sprint 2 Video (Make this video unlisted)

## What's New (User Facing)
Nothing new has been developed specifically for end-users, however the python-notebook-tests branch contains files for viewers who want to test the Python notebook.

## Work Summary (Developer Facing)
Most of the development was done on the CST-based semantic clone generation, with the developers familiarizing themselves with LibCST nodes and beginning to automate renaming of functions and variables. The developers have also looked into LLM-based generation of synonyms for a given function or variable name, so that the clones generated appear manually written (e.g. the function make_nodes becoming create_nodes rather than some filler word). For function renaming, edge-cases such as functions being redefined or 'imported as' had to be covered, while also making sure predefined functions like print() are not edited.

## Unfinished Work
Due to the complexity of the algorithm implementation, development on any user-facing elements such as a GUI have been left for Sprint 3. This also ensures that the algorithm is fully tested and functional before time is spent on the less necessary visual elements. This is the reason for any GUI-related issues remaining open. Other functional-based issues, such as ChatGPT synonym generation, are being left open due to it being too complex to finish in this sprint or because the resources needed were found to be out of scope (e.g. ChatGPT's limited free API calls).

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * #2  - [Implement Abstract Syntax Trees](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/2)
 * #4  - [Implement Program String Generator](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/4) (This function only necessary for program AST analysis.)
 * #15 - [Proto File Input to LibCST Conversion](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/15)
 * #16 - [Auto Rename Functions](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/16)
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:

 * #1 - [Unique N Permutations](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/1)
   - Due to the complexity of the program, we were only able to generate one given clone for an input Python file. Sprint 3 will focus on implementing probabilities to changing parts of the code (e.g. 20% chance to rename this function) and thus allowing for multiple concurrent clones to be generated.
 * #3 - [Create a UI for Python file parameter input](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/3)
   - User-facing visual elements will be left for Sprint 3 so that we could prioritize a functional algorithm.
 * #14 - [Create a base GUI window](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/14)
   - User-facing visual elements will be left for Sprint 3 so that we could prioritize a functional algorithm.
 * #17 - [Auto Rename Variables](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/17)
   - LibCST nodes are not well documented, finishing the Function renamer was prioritized. Base functionality works for low level complex code.
 * #18 - [Google Gemini Synonym Generation (Variables)](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/18)
   - Gemini has more restrictions on certain phrases such as 'hash' or 'password' that results sensitive content. Some logic clashes when it comes to local variables versus libraries imported as objects. ( Ex: x. versus libsct.func() where x is a varname and libsct is an imported library)
 * #19 - [Google Gemini Synonym Generation (Functions)](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/19)
   - Since the function renamer was our main priority for this sprint, the team decided to focus on getting a simple function name change. If the logic is implemented right, the Gemini API will be very simple to use instead of pre-existing names to swap with.


## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality (found in python-notebook-tests branch):
 * [CS421_Project_CYBER1_CodeVersion.ipynb](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/python-notebook-tests/CS421_Project_CYBER1_CodeVersion.ipynb)
 * [func-names-complex.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/python-notebook-tests/test%20files/func-names-complex.py)
 
## Retrospective Summary
Here's what went well:
  * The function renamer has been fully written and, due to the nature of LibCST nodes, for other implementations like variable renaming, the attributes and parameters just need to be renamed.
  * The team began to clearly lay out responsibilities in a collaborative environment, compared to the more isolated research of Sprint 1.
 
Here's what we'd like to improve:
   * More productivity on developing the algorithm. However, now that the function renamer has been implemented, other renamers or node manipulators should be easy to code.
   * More test cases for the algorithm, since the function renamer only had the one engineered edge case file (func-names-complex.py).
  
Here are changes we plan to implement in the next sprint:
   * Begin working with tkinter as well as on the algorithm, so that a GUI can be implemented by the end of the semester.
   * More complex renaming logic in the algorithm, using synonym generation and probabilities.
