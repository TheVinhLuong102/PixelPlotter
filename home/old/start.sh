#!/bin/ash
cd /mnt/mmcblk0/www
php-cli -S 192.168.8.1:8000 &
cd /mnt/mmcblk0/home
sleep 2
(sleep 5; echo root; sleep 3; echo "Just a bit off the block!"; sleep 3 ; echo "dropbear"; sleep 3; echo "quit") | telnet 192.168.8.200
cd /mnt/mmcblk0/home
python printer3.py&
python sendcolorp2.py &
sleep 1
python sendp2.py &

