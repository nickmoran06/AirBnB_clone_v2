#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
"""
from fabric.api import *
from datetime import datetime
from os import path


def do_pack():
    """Function to geneate the .tgz file"""

    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        collected_f = "versions/web_static_" + date + ".tgz"

        if path.exists("versions") is False:
            local("mkdir versions")

        local("tar -zcvf {tar_file} web_static".format(tar_file=collected_f))

        return collected_f

    except Exception:
        return None
