# Refactor code
# -------------
# Not timed (good to get it back within 24 hours)
#
# An intern has provided the code below to update the version number
# within two different files.
# The intern has left and you need to review and improve the code before
# submitting to source control.
#
# Please do not be constrained by the existing code (i.e. you don't have
# to keep the same function names, structure)
# Aim for production quality 'best-practice/clean' code
#
# Original Requirements
# ---------------------
# A script in a build process needs to update the build version number in 2
# locations.
# - The version number will be in an environment variable "BuildNum"
# - The files to be modified will be under "$SourcePath/develop/global/src"
# directory
# - The "SConstruct" file has a line "point=123," (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)
# - The "VERSION"file has a line "ADLMSDK_VERSION_POINT= 123" (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)

import os
import re
# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)

def replace_line(file_path, new_line, old_line):
   with open(file_path, 'r+') as f:
      contents = f.read()
      contents = re.sub(old_line, new_line, contents)
      f.seek(0)
      f.truncate()
      f.write(contents)

def updateSconstruct():
    # "Update the build number in the SConstruct file"

    file_path = os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct")
    os.chmod(file_path, 0o755) # owner can read, write and search
    old_line = "point\=[\d]+"
    new_line = "point="+os.environ["BuildNum"]
    replace_line(file_path, new_line, old_line)

# VERSION file interesting line
# ADLMSDK_VERSION_POINT=6
def updateVersion():
    # "Update the build number in the VERSION file"

    file_path = os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION")
    os.chmod(file_path, 0o755)
    old_line = "ADLMSDK_VERSION_POINT=[\d]+"
    new_line = "ADLMSDK_VERSION_POINT="+os.environ["BuildNum"]
    replace_line(file_path, new_line, old_line)

def main():
    updateSconstruct()
    updateVersion()

main()