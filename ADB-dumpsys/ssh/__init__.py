__author__ = 'barin.huseyin'
import pxssh


def main():

    s = pxssh.pxssh()
    if not s.login ('localhost', 'myusername', 'mypassword'):
        print "SSH session failed on login."
        print str(s)
    else:
        print "SSH session login successful"
        s.sendline ('ls -l')
        s.prompt()         # match the prompt
        print s.before     # print everything before the prompt.
        s.logout()


if __name__=="__main__":main()