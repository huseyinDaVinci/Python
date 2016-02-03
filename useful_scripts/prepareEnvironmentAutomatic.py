__author__ = 'barin.huseyin'
import sys
from subprocess import call, CalledProcessError, check_output
from os import listdir, getcwd
from os.path import join


def push_to_device(device_type):
    for mFile in listdir(getcwd()):
        if ".apk" in mFile:
            apk = mFile
        elif ".json" in mFile:
            config = mFile

    print "apk:{}   config:{}".format(apk, config)

    try:
        if len(apk) > 0:
            call(["adb", device_type, "push", join(getcwd(), apk), "/sdcard/APK/" + apk])
            print "{} is transferred to {}:".format(apk, "/sdcard/APK/" + apk)

        if len(config) > 0:
            call(["adb", device_type, "push", join(getcwd(), config),
                  "/sdcard/xfiles/" + config])

            print "{} is transferred to {}:".format(config, "/sdcard/xfiles/" + config)

        raw_input("Enter anything to exit:")
    except CalledProcessError as e:
        print "CalledProcessError: {}".format(e.message)


def push_necessary_files():
    lines = [f for f in check_output(["adb", "devices"]).split("\r") if f != '\n']
    args_length = len(lines)

    if args_length > 2:
        if len(sys.argv) == 1:
            print "more than one device please specify the device type as arg= {} or {}".format("-d", "-e")
        else:
            device_type = list(sys.argv)[1]
            print "device type: {}".format(device_type)
            if device_type == "-d" or device_type == "-e":
                push_to_device(device_type)
            else:
                print "enter arguments like a man !! "

    else:
        if ":555" in str(lines):
            push_to_device("-e")


def main():
    push_necessary_files()


if __name__ == "__main__":
    main()