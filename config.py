#!/usr/bin/env python3
import yaml


CONFIG_NAME = 'config.yaml'


def getConfig():
    try:
        with open('config.yaml') as config_file:
            return yaml.load(config_file)
    except:
        return {}
