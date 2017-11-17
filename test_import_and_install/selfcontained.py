def install_and_import(package):
    import importlib
    import os, sys
    try:
        import package
    except ImportError:
        print(package + " not present. Installing " + package +" ...")
        os.system(sys.executable + " -m easy_install " +  package)
    finally:
        globals()[package] = importlib.import_module(package)
        import package

def install_and_import_2(package):
    import os, sys
    try:
        import package
    except ImportError:
        print(package + " not present. Installing " + package +" ...")
        os.system(sys.executable + " -m easy_install " + package)
        import package

def install_and_import_3(package):
    import os, sys
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        print(package + " not present. Installing " + package + " ...")
        import pip
        pip.main(['install', package])
        importlib.import_module(package)

def install_and_import_4(package):
    import os, sys
    import site
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        print(package + " not present. Installing " + package + " ...")
        os.system(sys.executable + " -m easy_install " + package)
        reload(site) # Most of the stuff is set up in Python's site.py which is automatically imported when starting the interpreter
        importlib.import_module(package)


def install_and_import_5(package):
    import os, sys
    import site
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        print(package + " not present. Installing " + package + " ...")
        import pip
        pip.main(['install', package])
        reload(site)
        import novaclient
        print novaclient.__version__

if __name__== '__main__':

    install_and_import_5('python-novaclient')  # this works

    #install_and_import_4('python-novaclient')# this fails

    #install_and_import('python-novaclient')# this fails

    #install_and_import_3('python-novaclient') # this fails

    #install_and_import_2('python-novaclient') # this fails