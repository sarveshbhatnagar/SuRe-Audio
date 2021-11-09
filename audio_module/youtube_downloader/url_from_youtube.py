import glob
import os
def get_path(path=os.path.abspath("")):
    files=glob.glob(path+'/*.mp4', recursive=True)
    return files