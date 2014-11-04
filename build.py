print "Building..."

from fabric.api import env
from fabric.operations import run, put, sudo
from fabric.tasks import execute


env.hosts = ['mbjerkness@bjerkness.net']
env.key_filename = "id_rsa"

def copy():
    # make sure the directory is there!
    sudo('mkdir -p /opt/local/codeflow')
    sudo('chown mbjerkness /opt/local/codeflow')
    # our local 'testdirectory' - it may contain files or subdirectories ...
    put('index.html', '/opt/local/codeflow/')
    put('media', '/opt/local/codeflow/')
    #put('images', '/opt/local/codeflow/')

results = execute(copy)
