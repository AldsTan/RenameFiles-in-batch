# RenameFiles-in-Batch
This program is written in Python 3, it allows you to select multiple files, and rename those files to your desired filename template that has the "`i`" placeholder.

This program is designed to rename anime video files where the filename format is inconsistent. (ie. 11th episode of a series is Episode 11.mp4, and 12th episode is Episode 12.mp4, and the 111th is Episode 111.mp4. This causes problem in sorting on some operating systems where it will be shown in this order: Episode 11.mp4 -> Episode 111.mp4 -> Episode 12.mp4)

By using this program, you can easily resolve this problem by changing the filename to have uniform format. (ie. 11th episode will be renamed to Episode 011.mp4, 12th episode will be renamed to Episode 012.mp4, and so on.

## Usage
Requirements: 

> [Pyhon 3](https://www.python.org/downloads/)

The GUI is written in tkinter to minimize the use of big libraries.

### Future plans:
* Add skip indices
* Add scrollbars on listbox
* Fix the index format preview
