"""This package implements the tentaclio sharepoint client """
from tentaclio import *  # noqa

from .clients.sharepoint_client import ClientClassName


# Add DB registry
DB_REGISTRY.register("sharepoint", ClientClassName)  # type: ignore
