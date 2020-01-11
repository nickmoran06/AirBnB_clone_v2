#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
import os

env.hosts = ['35.231.153.28', '35.231.90.183']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Function that distributes an archive to your web servers
    """
    if os.path.isfile(archive_path) is False:
        return False

    file_tgz = archive_path.split("/")[-1]
    name_file = file_tgz.replace(".tgz", "")
    path = "/data/web_static/releases/" + name_file

    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir {}/".format(path))
        run("sudo tar -xzf /tmp/{} -C {}/".format(file_tgz, path))
        run("sudo rm /tmp/{}".format(file_tgz))
        run("sudo mv {}/web_static/* {}/".format(path, path))
        run("sudo rm -rf {}/web_static".format(path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(path))
        print("New version deployed!")

        return True
    except:
        return False
