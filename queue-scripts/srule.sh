#!/bin/bash

if [ $2 -eq 0 ]; then
#	curl -X POST --data "{\"match\": {\"nw_dst\": \"$1\", \"nw_proto\": \"UDP\"}, \"actions\":{\"queue\": \"$3\"}}" http://localhost:8080/qos/rules/0000000000000001
	sudo ovs-ofctl add-flow A "dl_type=0x0800,idle_timeout=1800,udp,priority=65535,nw_src=10.0.0.10,nw_dst=$1,in_port=1,actions=set_queue:$3,resubmit(,1)"
else
#	curl -X POST --data "{\"match\": {\"nw_dst\": \"$1\", \"nw_proto\": \"UDP\", \"tp_dst\": \"$2\"}, \"actions\":{\"queue\": \"$3\"}}" http://localhost:8080/qos/rules/0000000000000001
	sudo ovs-ofctl add-flow A "dl_type=0x0800,idle_timeout=1800,udp,priority=65535,nw_src=10.0.0.10,nw_dst=$1,udp_dst=$2,in_port=1,actions=set_queue:$3,resubmit(,1)"
fi
