<?php
exec("~/sshpass -p 'Just a bit off the block!' ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 root@192.168.8.200 'echo 1 > ~/lms2012/prjs/plotter_ppwi/lock.rtf';echo done")
?>
