#!/usr/bin/python3
"""
Fabric script to deploy and manage archives on web servers.
"""
import os
from fabric.api import env, local, run, lcd, cd


env.hosts = ['52.91.124.142', '52.91.118.158']


def do_clean(number=0):
    """
    Deletes out-of-date archives from local and remote servers.

    Args:
        number: Number of most recent archives to keep (including the latest).

    Returns:
        True if clean up is successful, otherwise False.
    """
    file_L = local('ls -t ~/AirBnB_Clone_V2/versions/').split()

    path = "/data/web_static/releases"
    with cd(path):
        file_R = sudo("ls -t .").split()

    number = int(number)
    if number == 0:
        num = 1
    else:
        num = number

    if len(file_R) > 0:
        if len(file_L) == number or len(file_L) == 0:
            pass
        else:
            count_local = file_L[num:]
            for i in range(len(count_local)):
                local("rm -f ~/AirBnB_Clone_V2/versions/{}".format(file_L[-1]))
        count_remote = file_R[num:]
        for j in range(len(count_remote)):
            sudo("rm -rf {}/{}".format(path, count_remote[-1].strip(".tgz")))
    else:
        pass
