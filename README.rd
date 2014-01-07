
Cheezy python script to supply more "human" readable parameters to make scripting easier.

[root@controller nova-hack]# ./buildnew.py -h
usage: buildnew.py [-h] -s SERVER -f FLAVOR -i IMAGE -n NET [-v]

basic OpenStack nova boot script

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        Server Name
  -f FLAVOR, --flavor FLAVOR
                        Flavor
  -i IMAGE, --image IMAGE
                        Input file name
  -n NET, --net NET     Input file name
  -v, --verbose         Enable debugging

[root@controller nova-hack(keystone_admin)]# ./buildnew.py -s pytest10 -i cirros -f m1.tiny -n qa_net
Building instance -
Instance pytest10 is complete!

[root@controller nova-hack(keystone_admin)]# ./buildnew.py -s pytest11 -i cirros -f m1.tiny -n qa_net -v
Server name: pytest11
Flavor name: m1.tiny
Image name: cirros
Network name: qa_net
Instance pytest11 not found. Continuing..
Network ID: 78ae5d87-306d-4c15-9024-f34d4843d04f
Building instance -
Instance pytest11 is complete!

[root@controller nova-hack(keystone_admin)]# nova list
+--------------------------------------+----------+--------+------------+-------------+-----------------------+
| ID                                   | Name     | Status | Task State | Power State | Networks              |
+--------------------------------------+----------+--------+------------+-------------+-----------------------+
| a9c4e082-9844-458f-b5fa-ff8c083f90a4 | pyTest1  | ACTIVE | None       | Running     | dev_net=10.0.0.11     |
| 93bc563c-45f4-401d-8e5b-6df969394368 | pyTest2  | ACTIVE | None       | Running     | qa_net=10.0.1.10      |
| c8556bfa-4f88-4c2d-8999-af451adfadce | pyTest3  | ACTIVE | None       | Running     | preprod_net=10.0.2.10 |
| 92e5bcfa-88f8-4c90-a774-857737c0a773 | pyTest4  | ACTIVE | None       | Running     | dev_net=10.0.0.12     |
| 568f51cd-9ec5-4930-99b5-1634c4c9c622 | pytest10 | ACTIVE | None       | Running     | qa_net=10.0.1.12      |
| 362f8430-ca10-424f-a8fc-d29d3f6a6e30 | pytest11 | ACTIVE | None       | Running     | qa_net=10.0.1.13      |
+--------------------------------------+----------+--------+------------+-------------+-----------------------+
