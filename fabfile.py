from fabric.api import env
from fabric.api import run
from fabric.api import sudo
import utils

def slaves(label=None,names=None):
#    env.parallel = True
    env.warn = True
    env.skip_bad_hosts = True
    env.user = 'root'
    env.hosts = utils.list_nodes(label, names)

#
# fab slaves:smth,names="^srv" -- uname -a
#
