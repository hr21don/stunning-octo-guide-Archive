import os #manipulate file paths + search directories
from zipfile import ZipFile # build zip file

def zip_all(search_dir, extension_list, output_path):
      with ZipFile(output_path, 'w') as output_zip: #opening the output_zip file using a context manager
        for root, dirs, files in os.walk(search_dir):#Using os modules walk function to search the directory + subdirectories. (root - file path to the directory, dirs - a list of all the subdirectories within the root directory and files - all files in the root directory.)
            rel_path = os.path.relpath(root, search_dir)#using os.path.relpath function to conver the root into a relative path compared to the search directory
            for file in files: # iterate through all the files in each directory 
                name, ext = os.path.splitext(file)#using the os.path.splitext function to seperate the file name from its extension
                if ext.lower() in extension_list:#Comparison for extension matches in the extension_list
                    output_zip.write(os.path.join(root, file),#Using the join function on the root path and file name to rebuild the original file 
                                     arcname=os.path.join(rel_path, file)) #determines how the file will be named within the zip archive. 


