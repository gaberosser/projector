__author__ = 'gabriel'
import settings
import os
import sys
import subprocess
import models
import cv2
import cv
import json

movie_extensions = [
    'avi',
    'mp4',
    'divx',
    'mkv'
]


def count_frames(infile):
    vc = cv2.VideoCapture(infile)
    if vc.isOpened():
        count = -1
        rval = True
        while rval:
            rval, frame = vc.read()
            count += 1
            if frame is None:
                break
        return count
    else:
        return 0


def retrieve_thumbnail(video):
    pass


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

            # try to generate thumbnail
            thumbnail = None
            try:
                # vs = cv2.VideoCapture(f)
                # if vs.isOpened():
                #     rval, frame = vs.open()
                vs = cv.CaptureFromFile(f)
                num_frames = cv.GetCaptureProperty(vs, cv.CV_CAP_PROP_FRAME_COUNT)
                if num_frames == 0:
                    print "No frames detected: %s" % f
                    break

            except Exception as exc:
                print repr(exc)

            # create entry
            try:
                dr = models.Videos(path=f, name=f)
                dr.save()
                movie_files.append(dr)
                print dr
            except Exception as exc:
                print repr(exc)
                pass

    return movie_files

