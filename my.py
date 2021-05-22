import platform

bit=platform.architecture()[0]

if bit=="64":
    import 64bit.py
    64bit.py.main()
elif bit=="32":
    import 32bit.py
    32bit.py.main()
