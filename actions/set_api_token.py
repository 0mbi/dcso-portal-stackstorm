# Copyright (c) 2021, DCSO GmbH

import sys

from st2client.models import KeyValuePair
from st2common.runners.base_action import Action

from lib.helpers import get_key_client


class SetApiToken(Action):
    def run(self, value):
        try:
            key_client = get_key_client()
            key_client.keys.update(KeyValuePair(name='dcso.api_token', value=value, secret=True))
            print("Success", end="")
        except:
            print("Failure", end="")
            sys.exit(1)
