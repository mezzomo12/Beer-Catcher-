# pip install cx_freeze
import cx_Freeze
executaveis = [ 
               cx_Freeze.Executable(script="main.py", icon="assets/gragas.ico") ]
cx_Freeze.setup(
    name = "Beer Catcher!",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables = executaveis
)

# python setup.py build
# python setup.py bdist_msi
