#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


from fabric.decorators import runs_once


@runs_once
def do_pack():
    """ Write a script that generates archive the contents of web_static folder"""
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path
