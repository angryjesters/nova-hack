#!/usr/bin/python
#
# simple build script for OpenStack Nova boot that relies more on human readable 
# than uuid entries

import argparse
import os
import sys
import time
import novaclient.v1_1.client as nvclient
import novaclient.exceptions
from credentials import get_nova_creds

parser = argparse.ArgumentParser(description='this is a test')
parser.add_argument('-s', '--server', help='Server Name', required=True)
parser.add_argument('-v', '--verbose', action='store_true', help='Enable debugging')

args = parser.parse_args()

if args.verbose:
    print ("Server name: %s" % args.server)

creds = get_nova_creds()
nova = nvclient.Client(**creds)

try:
	server = nova.servers.find(name=args.server)
	print "instance with name %s already exists!\nExiting.." % args.server
	sys.exit(2)
except novaclient.exceptions.NotFound:
	print "not found!"
	pass


