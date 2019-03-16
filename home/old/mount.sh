cd /mnt/mmcblk0
opkg remove imagemagick --force-removal-of-dependent-packages
opkg -dest sdcard install *.ipk
opkg install python-imglib_1.1.7-1_ramips_24kec.ipk
pip install lock*.whl
cd home
python exec.py
python exec.py
python exec.py
python exec.py
python exec.py
python exec.py
 
