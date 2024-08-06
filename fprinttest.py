import subprocess as sp
import time

while True:
    input('Plug in new fingerprint reader and press Enter.')
    print()
    print('Waiting for biometric service to reset...')
    # Stop fprint daemon
    while True:
        process = sp.run(['systemctl', 'kill', 'fprintd'], stderr=sp.DEVNULL)
        if process.returncode == 1: # process is already killed
            break
        time.sleep(1)
    print('Done!')
    p = sp.Popen('fprintd-enroll', stdout=sp.PIPE)
    for line in iter(p.stdout.readline, ''):
        line = str(line)
        if 'Enrolling' in line:
            print('Tap finger on reader')
        if 'retry' in line:
            print('Failed! Try again...')
        if 'passed' in line:
            print('Passed!')
            break
    p.kill()
    sys.stdout.flush()
    time.sleep(1)
    input('Unplug fingerprint reader and press Enter.')