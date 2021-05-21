import os
import os
def love():
    print("")
    print("")
    print("IF YOUR PHONE IS 64-BIT SELECT [1]")
    print("")
    print("IF YOUR PHONE IS 32-BIT SELECT [2]")
    print("")
    print("")
    select = raw_input('\x1b[1;33mChoose option: \x1b[0;97m')
    if select == '1':
        os.system ("python2 64bit.py")
    elif select == '2':
        os.system ("python2 32bit.py")
    elif select == '3':
        ex_id()
    elif select == '4':
        ex_post()
    else:
        print ('')
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ('')
love()
