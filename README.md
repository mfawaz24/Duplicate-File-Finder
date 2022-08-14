# Duplicate-File-Finder
Simple Python script. Remove duplicate files in contents of a given file directory.

# Use and Features
Useful for large and messy backups and data storage. It can equally be used on your family photos storage.

The script is thorough and can handle the most messy assortments of subfolder nesting.

The duplicate files that are removed have their name and location printed out in the terminal as they are removed. When cleaning is complete, a full list of removed duplicates is shown in the terminal.

This script can very easily be rewritten to simply index the locations of various files.

# How to use
1. Navigate to script location in terminal
2. Set file directory:

     -Run file from terminal, with full file directory following file name

     `ex: python duplicate_finder.py C:\Users\myName\Desktop\dirtyDirectory`

     -Note: alternatively, directory can be set by editing the variable "loc" in the script and running without extra commandline arguments.

     -Note: in case of issues on Windows, set first backslash to double backslash, ie `C:\\...\...`
 
3. Enjoy
