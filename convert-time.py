#!/usr/bin/env python3

import argparse

from dateutil import parser as datetime_parser


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('input')
arguments = argument_parser.parse_args()

datetime = datetime_parser.parse(arguments.input)
midnight = datetime.replace(hour=0, minute=0, second=0, microsecond=0)

print((datetime - midnight).total_seconds() / 86400)
