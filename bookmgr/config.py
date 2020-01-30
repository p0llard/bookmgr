import os

import click

from yaml import load, dump, YAMLError

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def write_config(config, store):
    path = os.path.abspath(config)

    with open(path, "x") as f:
        conf = {"store": store}
        conf_yaml = dump(conf, Dumper=Dumper)
        f.write(conf_yaml)


def get_store(config):
    path = os.path.abspath(config)

    try:
        with open(path, "r") as f:
            conf = load(f, Loader=Loader)
            if conf:
                try:
                    return conf["store"]
                except KeyError:
                    return None
            else:
                return None

    except FileNotFoundError:
        return None

    except YAMLError:
        return None
