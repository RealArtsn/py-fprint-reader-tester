# py-fprint-reader-tester
Python `fprint` wrapper to repeatedly test USB fingerprint readers. 

Kills any running systemd units for fprint and attempts to register fingerprint until a successful read is made. The user is then prompted to test another reader.

Tested for Arch Linux.