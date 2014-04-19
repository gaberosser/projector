__author__ = 'gabriel'
import settings
import os
import sys
import subprocess
import models
import re

movie_extensions = [
    'avi',
    'mp4',
    'divx',
    'mkv'
]


def populate_drive():

    file_list = []
    movie_files = []

    print "Generating file list..."
    for root, subFolders, files in os.walk(settings.ROOT_DIR):
        for file in files:
            file_list.append(os.path.join(root, file))
    print "Done"

    for f in file_list:
        fs = f.split('.')
        ext = fs[-1]
        if ext.lower() in movie_extensions:

            command = ["avconv", "-i", f, "-f", "ffmetadata", "-"]
            retval = subprocess.call(command)
            if retval != 0:
                print "Unable to read file: %s" % f
                continue
            # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # out, err = process.communicate()

            # create entry
            try:
                dr = models.Drive(path=f, name=f)
                dr.save()
                movie_files.append(dr)
                print dr
            except Exception as exc:
                print repr(exc)
                pass

    return movie_files