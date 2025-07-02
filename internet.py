import subprocess

def check_internet() :
    try:
        subprocess.check_call(['ping','-c','1','8.8.8.8'])
        return 'internet is working'
    except subprocess.CalledProcessError:
        return 'no internet connection'
        

