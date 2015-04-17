#!/bin/bash

if [ "$#" -ne 1 ]; then
echo "Usage - ./arping.sh [interface]"
echo "Example - ./arping.sh eth0"
echo "Example will perform an ARP scan of the local subnet to which eth0 is assigned"
exit
fi

interface=$1
prefix=$(ifconfig $interface | grep 'inet addr' | cut -d ':' -f 2 | cut -d ' ' -f 1 | cut -d '.' -f 1-2)
echo $interface
echo $prefix
for addr in $(seq 112 119); do
for moo in $(seq 1 254); do

echo $prefix.$addr.$moo
arping -c 1 $prefix.$addr.$moo | grep "Unicast reply" >> fish
done
done
#sed 's/Unicast reply from //g' fish > foo
#sed 's/[ //g' fish > foo | sed 's/] //g' fish > foo
