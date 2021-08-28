from cx_Freeze import *
includefiles=['icon.ico','background.jpg','password1.png','student.png','usericon.png']
excludes=[]
packages=[]
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "student",
     "TARGETDIR",
     "[TARGETDIR]\student.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Student Management System",
    author="faizan Khan",
    name="Student Management System",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="student.py",
            base=base,
            icon='icon.ico',
        )
    ]
)