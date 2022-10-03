application_title= 'PE Assisstant'
main_python_file= 'main.py'
#icon_file = 
packs = []
mods = []
files_to_include = ['classJobForms.py',
                    'speed_torque.py',
                    'menu.py',
                    'job_dict.pickle',
                    'pg_1_templatev2.docx',
                    'st_word_temp.docx']
build_exe_options = {'includes': mods, 'packages': packs,
                     'include_files': files_to_include}
your_name= 'Matt Kenney'
program_description= '''

Easily perform PE tasks.

'''

#main
import sys

from cx_Freeze import setup, Executable

base=None
##if sys.platform=='win32':
##    base= 'Win32GUI'

setup(
    name= application_title,
    version= '1.0',
    description= program_description,
    author= your_name,
    options= {'build_exe': build_exe_options},
    executables= [Executable(main_python_file, base= base)])# icon= icon_file)])
