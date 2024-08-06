import subprocess as sp
import time, sys

while True:
    print()
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
    try:
        for line in iter(p.stdout.readline, ''):
            line = str(line)
            if 'Enrolling' in line:
                print('Tap finger on reader')
            if 'retry' in line:
                print('Failed! Try again... (Press Ctrl+C to reset)')
            if 'passed' in line:
                print('Passed!')
                break
    except KeyboardInterrupt:
        p.kill()
        continue
    p.kill()
    sys.stdout.flush()
    input('Unplug fingerprint reader and press Enter.')