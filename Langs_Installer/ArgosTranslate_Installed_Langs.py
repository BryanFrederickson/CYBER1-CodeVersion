# Used to see Argos Translate Language Translation packages installed on system

import argostranslate.package

# uninstalls all language programs
'''
installed_packages=argostranslate.package.get_installed_packages()
for package in installed_packages:
    argostranslate.package.uninstall(package)
'''

# prints list of installed language programs
#'''
print(argostranslate.package.get_installed_packages())
#'''