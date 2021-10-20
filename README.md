# stunning-octo-guide-Archive
Your goal for this challenge is to write a Python function to build a ZIP archive. 

## Input
 you want to include, a list of file extensions, and an output file path for the resulting archive.

## Output
The function should search the input directory and all of its subdirectories for files with the specified extension and then package them together into a ZIP file.

## Tips
Zip file should maintain folder structure relative to the top-level directory. 

## How to Run?  Remember these three parameters| search_dir |  extension_list |  output_path

for e.g. 

zip_all(r'.\\my_stuff', ['.png'], 'my_stuff.zip')
