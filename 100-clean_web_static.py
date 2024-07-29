#!/usr/bin/python3
"""
Fabric script to deploy and manage archives on web servers.
"""
import os
from fabric.api import env, local, run, lcd, cd, sudo

env.hosts = ['52.91.124.142', '52.91.118.158']


def do_clean(number=0):
    """
    Deletes out-of-date archives from local and remote servers.

    Args:
        number: Number of most recent archives to keep (including the latest).

    Returns:
        True if clean up is successful, otherwise False.
    """
    number = int(number)
    if number == 0:
        number = 1

    # Clean local archives
    local_archives = local('ls -t ~/AirBnB_clone_v2/versions',
                           capture=True).split()
    if len(local_archives) > number:
        archives_to_delete = local_archives[number:]
        with lcd('~/AirBnB_clone_v2/versions'):
            for archive in archives_to_delete:
                local("rm -f ./{}".format(archive))

    # Clean remote archives
    with cd('/data/web_static/releases'):
        remote_archives = sudo('ls -t').split()
        if len(remote_archives) > number:
            archives_to_delete = remote_archives[number:]
            for archive in archives_to_delete:
                sudo('rm -rf ./{}'.format(archive))

    return True
