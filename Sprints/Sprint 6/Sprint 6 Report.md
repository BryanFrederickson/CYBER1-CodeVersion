# Sprint 6 Report (3/18/2025 - 4/10/2025)

[Sprint 6 Video](https://www.youtube.com/watch?v=Jm5sc__DUwI)

## What's New (User Facing)
* The [Python Obfuscator](https://github.com/BryanFrederickson/CYBER1-CodeVersion?tab=readme-ov-file#python-obfuscator) is finished, with all of the major issues fixed. There are still edgecases that aren't properly covered such as specific implementations of variables, but would require extensive work to cover reliably.
  

## Work Summary (Developer Facing)
The Python Obfuscator is now in a finished state. Clone Log output was fully finished, foreign alphabet translation was fixed, and other small issues were addressed (see Completed Issues below).

Halfway through the sprint, our client requested we work on an external paper regarding our research to be published in Military Cyber Affairs. As such, once the Python Obfuscator was declared finished, we moved to working on it instead, which involved testing the Obfuscator with various complex inputs. Due to the priority of the research paper, issues encountered during testing, such as the ones mentioned in the previous section, were not able to be properly addressed.

## Unfinished Work
As this is our last sprint on this project, we won't be able to address any remaining issues or unfinished work. There are still issues with the Obfuscator, such as specific uses for variables (nested subscripting for example), but they only result in the output being nonfunctional, rather than fully crashing the program. Due to the nature of this project and the way we parse the code using a CST, there will always be more polish and edgecases we could cover that go beyond the scope of the Capstone.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * #25  - [Fix Foreign Alphabet Translation](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/25)
   - Made sure input and output code was parsed using UTF-8 to address encoding issues. If a translated object name is not suitable, the code will then attempt to transliterate it, before finally using unique placeholder names.
 * #26  - [Add more Output Var/Func Name Convention Styles](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/26)
   - All of the naming conventions already supported for input now can be used for translated variables and functions. A random naming convention is chosen for Variables and for Functions per clone.
 * #27  - [Optimize Translation](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/27)
   - Translation model is now created on per-clone rather than per-call basis. May be reopened if changes with large amounts of time save are identified.
 * #28  - [Implement External Log Output to Obfuscator](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/28)
   - Logs include timestamps for every change and lists the parameters for that clone's generation.
 * #30  - [Logic Obfuscation Logs](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/30)
   - See Issue #28 above.
 * #32  - [Cover Subscripted Variables in Renaming](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/32)
   - Subscripted variables e.g. `var="hello", print(var[0])` are now renamed as normal.
 
 ## Incomplete Issues/User Stories
 Here are links to issues we worked on but did not complete in this sprint:
TODO
 * #29 - [Logic Branches](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/29)
   - Due to the research paper being highest priority in the latter half of this sprint (see Developer Facing Work Summary above), we were unable to expand the Logic Obfuscation to have more options per individual compenent to change. Logic changes will remain the same for every clone (e.g. a given For loop will always become the same While loop).
 * #31 - [Implement try/except](https://github.com/BryanFrederickson/CYBER1-CodeVersion/issues/31)
   - Try-Except blocks were implemented for code, but due to limited development time and the research paper, they are not very robust. Currently, any exception will just cause the component to be unchanged. Given more development time, this could have been improved to better compensate for the variety of possible errors encountered.


## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality (for more info on file functionality, see the [Main Branch READEME](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/d441899c093c13e51d996bdf9c3109f6f130bf16/README.md)):
### Python Obfuscator
 * [Python_Obfuscator.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Python_Obfuscator/Python_Obfuscator.py)
 * [Python_Obfuscator_support.py](https://github.com/BryanFrederickson/CYBER1-CodeVersion/blob/main/Python_Obfuscator/Python_Obfuscator_support.py)


## Retrospective Summary
Here's what went well:
  * Communication and teamwork, where we would change our current work based on what the other teammate was doing/struggling with.
 
Here's what we'd like to improve:
  * Clearly lay out the various use cases for variables/functions/component to change, instead of adding edge cases as we encounter them
  * More robust testing, where we use random Python code rather than specifically crafted test cases

  
Note: There is no listing for changes to implement next sprint, as this was the final sprint for the project.
