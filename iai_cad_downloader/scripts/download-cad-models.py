#!/usr/bin/env python

import rospy
import os
import subprocess
from optparse import OptionParser

def checkout_svn_subdir(svn_address, subdir):
    svn_subdir_address = svn_address + "/" + subdir
    print "Checking out " + svn_subdir_address
    svn_command = "svn checkout " + svn_subdir_address
    subprocess.call(svn_command, shell=True)

def ensure_dir_exists(directory):
    if (not os.path.exists(directory)):
        rospy.loginfo("Creating directory: %s", directory)
        os.mkdir(directory)

def change_dir(directory):
    ensure_dir_exists(directory)
    print "Changing into directory " + directory
    os.chdir(directory)

def download_cad_models(source, dest, subdirs):
    change_dir(dest)

    for subdir in subdirs:
        checkout_svn_subdir(source, subdir)

if __name__ == '__main__':
    usage = "usage: %prog [options] [sub-dirs]"
    parser = OptionParser(usage)
    parser.add_option("-s", "--source", dest="source",
                      default="svn+ssh://svn@svn.ai.uni-bremen.de/cad_models",
                      help="svn server address to download from")
    parser.add_option("-d", "--dest", dest="destination",
                      default="./meshes",
                      help="destination directory for checkouts")

    (options, args) = parser.parse_args()

    if len(args) < 1:
        print "No subdirectories to checkout given. Stopping."
    else:
        download_cad_models(options.source, options.destination, args)
