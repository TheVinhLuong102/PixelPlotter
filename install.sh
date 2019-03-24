#!/bin/bash
sudo cp -rv html/* /var/www/html/
cp -rv home/* ~/
sudo chown www-data:www-data /var/www/html/uploads
sudo chmod 755 /var/www/html/uploads
sudo touch /var/www/html/log.txt
sudo chmod 777 /var/www/html/log.txt
