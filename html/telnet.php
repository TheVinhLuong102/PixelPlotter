<?php
$output = shell_exec('(sleep 5; echo root; sleep 3; echo "Just a bit off the block!"; sleep 3 ; echo "dropbear"; sleep 3; echo "quit") | telnet 192.168.8.200');
echo "<pre>$output</pre>";
?>
