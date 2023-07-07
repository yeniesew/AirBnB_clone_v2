#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

<<<<<<< HEAD
env.hosts = ["104.196.168.90", "35.196.46.172"]
=======
env.hosts = ["34.229.184.253", "54.157.187.58"]
>>>>>>> 58452de58208bd138722359b40ab3bf1ab2d4fe3


def do_clean(number=0):
    """Delete out-of-date archives.
<<<<<<< HEAD

    Args:
        number (int): The number of archives to keep.

=======
    Args:
        number (int): The number of archives to keep.
>>>>>>> 58452de58208bd138722359b40ab3bf1ab2d4fe3
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
