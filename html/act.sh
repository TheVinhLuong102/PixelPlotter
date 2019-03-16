cd /home/robot
rm lock/*
rm lockcolor2/*
#python /mnt/mmcblk0/home/printer3.py 
python sendcolor.py &
sleep 1
python send.py 
echo "" >> /var/www/html/log.txt
