from typing import Dict, Any
from collections import OrderedDict


def add_suffix_to_dict_keys(dictionary: Dict[str, Any], suffix: str) -> Dict[str, Any]:
    return OrderedDict((key + suffix, dictionary[key]) for key in dictionary)


def add_prefix_to_dict_keys(dictionary: Dict[str, Any], prefix: str) -> Dict[str, Any]:
    return OrderedDict((prefix + key, dictionary[key]) for key in dictionary)
