import platform
bit=platform.architecture()[0]
if bit =='64bit':

    from SUBHAN import main
    subhan1()
else:
    print('Sorry Your Device Not Support Mr.SUBHAN Tools')
    exit()
