#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the web_static folder
"""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        Path to the generated archive if successful, otherwise None.
    """
    local("sudo mkdir -p versions")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = "versions/web_static_{}.tgz".format(timestamp)
    result = local("sudo tar -cvzf {} web_static".format(file_name))
    if result.succeeded:
        return file_name
    else:
        return None
