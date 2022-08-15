# Shell, basics

## Description
* File `0-current_working_directory` prints the absolute path name of the current working directory.
* File `1-listit` displays the contents list of your current directory.
* File `2-bring_me_home` changes the working directory to the user’s home directory.
* File `3-listfiles` displays the contents of the current directory in a long format.
* File `4-listmorefiles` displays the current directory contents, including hidden files in the long format.
* File `5-listfilesdigitonly' displays the current directory contents in long format, with user and group IDs displayed numerically, and hidden files.
* File `6-firstdirectory` creates a directory named `my_first_directory` in the `/tmp/` directory.
* File `7-movethatfile` moves the file `betty` from `/tmp/` to `/tmp/my_first_directory.`
* File `8-firstdelete` deletes the file `betty`.
* File `9-firstdirdeletion` deletes the directory `my_first_directory` that is in the `/tmp` directory.
* File `10-back` changes the working directory to the previous one.
* File `11-lists` lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
* File `12-file_type` prints the type of the file named `iamafile.` The file `iamafile` will be in the `/tmp` directory.
* File `13-symbolic_link` creates a symbolic link to `/bin/ls`, named `__ls__.` The symbolic link will be created in the current working directory.
* File `14-copy_html` copies all the HTML files from the current working directory to the parent of the working directory, but only copies files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
* File `100-lets_move` moves all files beginning with an uppercase letter to the directory `/tmp/u.`
* File `101-clean_emacs` deletes all files in the current working directory that end with the character `~.`
* File `102-tree` creates the directories `welcome/`, `welcome/to/` and `welcome/to/school` in the current directory.
* File `103-commas` lists all the files and directories of the current directory, separated by commas (,).

  * Directory names should end with a slash (/)
  * Files and directories starting with a dot (.) should be listed
  * The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
  * Only digits and letters are used to sort; Digits should come first
  * The listing should ends with a new line.

* File `school.mgc` is a magic file that can be used with the command `file` to detect `School` data files. `School` data files always contain the string `SCHOOL` at offset 0.
