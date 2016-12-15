#!/usr/bin/env python3
"""Configuration reader module. Very short & simple"""
import yaml


CONFIG_NAME = 'config.yaml'
"""Name of the config file"""


def getConfig():
    """Read config and return it.

    Returns:
        dict: The config dict or an empty dict if there are any errors.
    """
    try:
        with open('config.yaml') as config_file:
            return yaml.load(config_file)
    except:
        return {}
