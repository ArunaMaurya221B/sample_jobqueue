import os
import sys

from contextlib import contextmanger
from select import select
from logging import getLogger
from weakref import WeakValueDictionary

from json import dumps

from .utils import (
    Literal, prepared, transaction, convert_time_spec, utc_format
)

def create(self):
        queue = self['']

        with open(os.path.join(self.template_path, 'create.sql'), 'r') as f:
            sql = f.read()

        with queue._transaction() as cursor:
		cursor.execute(sql, {'name': Literal(queue.table)})
