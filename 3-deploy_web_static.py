#!/usr/bin/python3
"""
Fabric script to automate creation and distribution of web_static archive.
"""
import os
from fabric.api import env, local, run, put
from datetime import datetime


env.hosts = ['52.91.124.142', '52.91.118.158']


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
        print('New version deployed!')
        return True

    except Exception as e:
        return False


def deploy():
    """
    Deploy web_static archive to web servers.
    Call the do_pack() function and store the path of the created archive
    Call the do_deploy(archive_path) function,using the new path of new archive

    Returns:
        True if deployment succeeded, otherwise False.
    """
    new_archive_path = do_pack()
    if exists(new_archive_path) is False:
        return False
    return do_deploy(new_archive_path)
