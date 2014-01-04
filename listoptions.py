#!/usr/bin/env python

import os
import time
import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds
from pprint import pprint

creds = get_nova_creds()
nova = nvclient.Client(**creds)

image = nova.images.list()
flavor = nova.flavors.list()
network = nova.networks.list()

print "\n\nList all options"
print "---------------------------------------"
pprint(image)
print "---------------------------------------"
pprint(flavor)
print "---------------------------------------"
pprint(network)
print "---------------------------------------\n\n"

