a_mrth=$1
a_brv=$2

b_mrth=$3
b_brv=$4

c_mrth=$5
c_brv=$6

d_mrth=$7
d_brv=$8

v_min=$9

curl -X POST -d "{\"port_name\": \"A-eth3\", \"type\": \"linux-htb\", \"max_rate\": \"104857600\", \"queues\": [{\"max_rate\": \"104857600\"}, {\"min_rate\": \"$a_brv\"}, {\"min_rate\": \"$b_brv\"}, {\"min_rate\": \"$c_brv\"}, {\"min_rate\": \"$v_min\"}]}" http://localhost:8080/qos/queue/0000000000000001

#sudo ovs-vsctl -- set Port A-eth3 qos=@newqos -- --id=@newqos create QoS type=linux-htb other-config:max-rate=104857600 queues=0=@q0,1=@q1 -- --id=@q0 create Queue other-config:max-rate=104857600 -- --id=@q1 create Queue other-config:min-rate=\"$a_brv\" -- --id=@q2 create Queue other-config:min-rate=\"$b_brv\" -- --id=@q3 create Queue other-config:min-rate=\"$c_brv\" -- --id=@q4 create Queue other-config:min-rate=\"$v_min\" && echo "a-min-rate=$a_brv, b-min-rate=$b_brv, c-min-rate=$c_brv, v-min-rate=$v_min"
