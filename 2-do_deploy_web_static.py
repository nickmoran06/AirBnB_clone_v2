#!/usr/bin/python3
"""
Module that store fabric functions
"""
from fabric.api import *
from datetime import datetime
from os import path

env.user = 'ubuntu'
env.hosts = ['35.231.153.28', '35.231.90.183']


def do_pack():
    """
    Function to geneate the .tgz file
    """

    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        collected_f = "versions/web_static_" + date + ".tgz"

        if path.exists("versions") is False:
            local("mkdir versions")

        local("tar -zcvf {tar_file} web_static".format(tar_file=collected_f))

        return collected_f

    except Exception:
        return None


def do_deploy(archive_path):
    """
    Function that distributes an archive to your web servers
    """

    try:
        file = archive_path.split(/)[-1]
        name_file = file.replace(".tgz", "")
        new_path = "/data/web_static/releases/" + name_file

        if path.exists(archive_path) is False:
            return False

        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(new_path))
        

        return True

    except Exception:
        return False
