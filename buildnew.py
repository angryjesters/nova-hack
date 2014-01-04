#!/usr/bin/env python
# author: rhughes
#
# :set ts=4
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

parser = argparse.ArgumentParser(description='basic OpenStack nova boot script')
parser.add_argument('-s', '--server', help='Server Name', required=True)
parser.add_argument('-f', '--flavor', help='Flavor', required=True)
parser.add_argument('-i', '--image', help='Input file name', required=True)
parser.add_argument('-n', '--net', help='Input file name', required=True)
parser.add_argument('-v', '--verbose', action='store_true', help='Enable debugging')

args = parser.parse_args()

if args.verbose:
	print ("Server name: %s" % args.server)
	print ("Flavor name: %s" % args.flavor)
	print ("Image name: %s" % args.image)
	print ("Network name: %s" % args.net)

creds = get_nova_creds()
nova = nvclient.Client(**creds)

if not nova.keypairs.findall(name="mykey"):
    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
        nova.keypairs.create(name="mykey", public_key=fpubkey.read())

image = nova.images.find(name=args.image)
flavor = nova.flavors.find(name=args.flavor)
network = nova.networks.find(label=args.net)

try:
	server = nova.servers.find(name=args.server)
	print "Instance with name %s already exists!\nExiting.." % args.server
	sys.exit(2)
except novaclient.exceptions.NotFound:
	if args.verbose:
		print "Instance %s not found. Continuing.." % args.server
	pass

if args.verbose:
	print "Network ID: %s" % str(network.id)

try: 
	instance = nova.servers.create(name=args.server, image=image.id, flavor=flavor.id, nics=[{'net-id':network.id}], key_name="macbook")
except exc.BadRequest:
	print "could not create new instance (%s)" % args.server
	sys.exit(2)

status = instance.status
print "Building instance \\",
syms = ['\\', '|', '/', '-']
bs = '\b'

while status == 'BUILD':
	#time.sleep(5)
	# Retrieve the instance again so the status field updates
	instance = nova.servers.get(instance.id)
	status = instance.status
	# print "status: %s" % status

	for sym in syms:
		sys.stdout.write("\b%s" % sym)
		sys.stdout.flush()
		time.sleep(.3)

print ("\nInstance %s is complete!\n" % args.server)
