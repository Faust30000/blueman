# coding=utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

from blueman.Sdp import uuid128_to_uuid16
from blueman.bluez.errors import BluezDBusException
import blueman.services
import inspect
import logging


def get_service(device, uuid):
    for name, cls in inspect.getmembers(blueman.services, inspect.isclass):
        if uuid128_to_uuid16(uuid) == cls.__svclass_id__:
            return cls(device, uuid)


def get_services(device):
    try:
        services = (get_service(device, uuid) for uuid in device['UUIDs'])
        return [service for service in services if service]
    except BluezDBusException as e:
        logging.exception(e)
        return []
