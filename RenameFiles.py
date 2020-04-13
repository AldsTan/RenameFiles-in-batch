import os, sys
from tkinter import (
	filedialog, Listbox, Button, Scrollbar,
	ttk, Tk, END,
	IntVar, StringVar
	)
# Function to rename multiple files 

def MainWindow():
	''' GUI of the program '''
	window = Tk()
	window.title('Batch rename files inside a folder')
	window.resizable(0, 0)

	# 1st row - files
	label_files = ttk.Label(window, text='Files: ')
	label_files.grid(row=0, column=0, sticky='w')

	text_files = Listbox(window, width=80)
	# @todo add x and y scrollbars
	text_files.grid(row=0, column=1, columnspan=10)

	btn_files = Button(window, text='Browse...', fg='black', command=lambda:text_files.insert(END, *getFilenames()))
	btn_files.grid(row=0, column=12)


	# 2nd row - index
	label_index = ttk.Label(window, text='Starting index: ')
	label_index.grid(row=1, column=0, sticky='w')
	i = IntVar()
	i.set(1)
	text_index = ttk.Entry(window, width=5, textvariable=i)
	text_index.bind('<Key>', lambda args: index_view.set(str(i.get()).zfill(f.get)))
	text_index.grid(row=1, column=1, sticky='w')

    # @todo fix skip indices
	# label_skip_indices = ttk.Label(window, text='Skip indices: ')
	# label_skip_indices.grid(row=1, column=2, sticky='e')
	skip = StringVar()
	# text_skip_indices = ttk.Entry(window, width=5, textvariable=skip)
	# text_skip_indices.grid(row=1, column=3, sticky='w')

	label_index_format = ttk.Label(window, text='Index width: ')
	label_index_format.grid(row=1, column=4, sticky='e')
	f = IntVar()
	f.set(2)
	text_index_format = ttk.Entry(window, width=5, textvariable=f)
	text_index_format.bind('<Key>', lambda args: index_view.set(str(i.get()).zfill(f.get)))
	text_index_format.grid(row=1, column=5, sticky='w')

	# @todo fix delay when editing index width and starting index
	index_view = StringVar()
	index_view.set(str(i.get()).zfill(f.get()))
	label_view = ttk.Label(window, textvariable=index_view)
	label_view.grid(row=1, column=6)

	# 3rd row - filename
	label_filename_template = ttk.Label(window, text='Filename template: ')
	label_filename_template.grid(row=2, column=0)
	filename_template = StringVar()
	filename_template.set('`i`')
	text_filename_template = ttk.Entry(window, width=80, textvariable=filename_template)
	text_filename_template.grid(row=2, column=1, columnspan=10)


	# 4th row - filename notes
	note_filename_template = ttk.Label(window, text='* Use " `i` " as placeholder for index.\n* Do not add name extensions')
	note_filename_template.grid(row=3, column=1, columnspan=10, sticky='w')

	# 5th row - buttons
	btn_rename = ttk.Button(window, text='Rename', command=lambda:rename(text_files.get(0, END), i.get(), list(skip.get()), f.get(), filename_template.get()))
	btn_rename.grid(row=4, column=5)
	# @todo 

	window.mainloop()

def rename(files_list, i, skip_list, z, filename_template):
    ''' Core rename function '''
    files_list = list(files_list)
    for filename in files_list:
    	orig_filename = filename.split('/')[-1]
    	ext = '.' + orig_filename.split('.')[-1] # to preserve filename extensions
    	directory = os.path.dirname(filename) + '/'
    	destn_filename = filename_template[:filename_template.find('`i`')] + str(i).zfill(z) + filename_template[filename_template.find('`i`') + 3:] + ext
    	try:
            #while str(i) in skip_list: i += 1
            os.rename(directory + orig_filename, directory + destn_filename)
            print(orig_filename + ' -> ' + destn_filename)
            i += 1
    	except Exception as error:
    		print(f'An error occurred: <{error}>')

def getFilenames():
	files = filedialog.askopenfilenames(title="Select all files to rename")
	return list(files)

if __name__ == '__main__': 
	MainWindow()
