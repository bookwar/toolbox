import requests
from pprint import pprint
from settings import JENKINS_URL
import re

def get_nodes_for_label(label):
    json_url = "/".join([JENKINS_URL.rstrip("/"), "label", label, "api", "json"])
    r = requests.get(json_url)
    nodes = [node['nodeName'] for node in r.json()['nodes']]
    return nodes

def get_nodes(online_only=True):
    json_url = "/".join([JENKINS_URL.rstrip("/"), "computer", "api", "json"])
    r = requests.get(json_url)
    nodes = [
        node['displayName'] for node in r.json()['computer'] if not
        (
            online_only and (node['offline'] or node['temporarilyOffline'])
        )
    ]
    return nodes

def list_nodes(label=None, names=None, online_only=True):

    nodes =  get_nodes(online_only=online_only)

    if label:
        all_labeled_nodes = get_nodes_for_label(label)
        nodes = [node for node in nodes if node in all_labeled_nodes]

    if names:
        nodes = [node for node in nodes if re.match(names, node)]

    return sorted(nodes)

