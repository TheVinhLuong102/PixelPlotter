<?php
$upload_dir = "uploads/";
$img = $_POST['hidden_data'];
$img = str_replace('data:image/png;base64,', '', $img);
$img = str_replace('data:image/jpg;base64,', '', $img);
$img = str_replace(' ', '+', $img);
$data = base64_decode($img);
date_default_timezone_set("America/New_York");
$filen = $upload_dir . rtrim(shell_exec('date "+%H%M%S%d%m%Y"'),"\n") . "_" . $_GET['name']  . "_.png";
$filepts = explode('\n',$filen);
$file = $filepts[0] . $filepts[1];
echo $file;
echo $data;
echo $_POST['hidden_data'];
$success = file_put_contents($file, $data);
print $success ? $file : 'Unable to save the file.';
?>
