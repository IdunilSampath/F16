import os
def love():
    print(" DEAR USERS NUMBER 2 32-BIT IS UPDATING PLEASE WAIT")
    print("")
    print("IF YOUR PHONE IS 64-BIT SELECT [1]")
    print("")
    print("IF YOUR PHONE IS 32-BIT SELECT [2]")
    print("")
    print("")
    select = raw_input('\x1b[1;33mChoose option: \x1b[0;97m')
    if select == '1':
        os.system("python2 64bit.py")
        love()
        if select == '2':
            os.system("python2 32bit.py")

            print ("")
love()
