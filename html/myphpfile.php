<?php
$filename = '/mnt/mmcblk0/www/log.txt';  //about 500MB
$output = shell_exec('exec tail -n50 ' . $filename);  //only print last 50 lines
echo str_replace(PHP_EOL, '<br />', $output);         //add newlines
?>

