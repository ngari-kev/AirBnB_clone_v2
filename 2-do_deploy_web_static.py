#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers using do_deploy function.
"""
import os
from fabric.api import env
from fabric.api import put
from fabric.api import run


env.hosts = ['52.91.124.142', '52.91.118.158']


def do_deploy(archive_path):
    """
    Distribute an archive to web servers.

    Args:
        archive_path: Path to the archive file to deploy.

    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file_name = archive_path.split("/")[-1]
    dir_ = '/data/web_static/releases/'
    dest_dir = dir_ + "{}".format(file_name.split('.')[0])
    tmp = "/tmp/" + file_name

    try:
        put(archive_path, "/tmp")

        run("mkdir -p {}/".format(dest_dir))

        run("tar -xzf {} -C {}".format(tmp, dest_dir))

        run("rm {}".format(tmp))

        run("mv {}/web_static/* {}/".format(dest_dir, dest_dir))
        run("rm -rf {}/web_static".format(dest_dir))

        run("rm -rf /data/web_static/current")

        run("ln -s {}/ /data/web_static/current".format(dest_dir))
        return True

    except:
        return False
