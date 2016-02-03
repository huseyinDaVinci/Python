__author__ = 'barin.huseyin'

import sys
from os import listdir, getcwd
from os.path import join
from subprocess import call, check_output, CalledProcessError


def push_to_device(device_type, folder_name):
    mp3_files = []
    for mFile in listdir(getcwd()):
        if ".mp3" in mFile:
            mp3_files.append(mFile)
    try:
        dest_path = "/sdcard/" + folder_name + "/"

        for mp3 in mp3_files:
            call(["adb", device_type, "push", join(getcwd(), mp3), dest_path + mp3])
            print "{} mp3 is transferred ...".format(mp3)
        raw_input("Enter anything to exit:")
    except CalledProcessError as e:
        print "CalledProcessError: {}".format(e.message)


def copyToDevice():
    lines = [f for f in check_output(["adb", "devices"]).split("\r") if f != '\n']
    args_length = len(lines)

    if args_length > 2:
        if len(sys.argv) == 1:
            print "more than one device please specify the device type as arg= {} or {}".format("-d", "-e")
        else:
            args = list(sys.argv)
            device_type = args[1]
            print "device type: {}".format(device_type)
            if device_type == "-d" or device_type == "-e":
                folder_name = args[2]
                push_to_device(device_type, folder_name)
            else:
                print "enter arguments like a man !! "

    else:
        if ":555" in str(lines):
            push_to_device("-e", "Music")


def main():
    copyToDevice()


if __name__ == "__main__":
    main()
