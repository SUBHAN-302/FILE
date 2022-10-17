import platform
bit=platform.architecture()[0]
if bit =='64bit':
    from FILE import main
    subhan()
else:
    print('Sorry Your Device Not Support Mr.SUBHAN Tools')
    exit()
