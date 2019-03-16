<title>PIX3L PLOTT3R Web Control Panel</title>
<body>
<style>
input {
font-size: 20px;
}
</style>
<form action="iframe.php" target="my-iframe" method="post">
			
<!--  <label for="text">Command:</label>
  <input type="text" name="text" id="text">			
  <input type="submit" value="post" id="submit">-->
<script> 
dropbear = '(sleep 5; echo root; sleep 3; echo "Just a bit off the block!"; sleep 3 ; echo "dropbear"; sleep 3; echo "quit") | telnet 192.168.8.200'
ping = 'ping -w 1 192.168.8.200'
queue = './run.sh &> log.txt 2>&1 &'
activate = './act.sh &> log2.txt 2>&1 &'
inst = 'bash inst.sh >> log3.txt 2>&1 &'
kill = 'killall python ; echo done'
clearl = 'echo "" > log.txt; echo ""> log2.txt'
rmlock = 'rm -v /home/robot/lock*/lock*; echo done'
</script><!--<br><br>-->
<!--<input type="button" onclick="document.getElementById('text').value = queue ;document.getElementById('submit').click(); " value="run queuer"> 
<input type="button" onclick="document.getElementById('text').value = activate ;document.getElementById('submit').click(); " value="activate printer"> 
<input type="button" onclick="document.getElementById('text').value = kill ;document.getElementById('submit').click(); " value="killall python"> 
<input type="button" onclick="document.getElementById('text').value = rmlock ;document.getElementById('submit').click(); " value="remove lock"> 
<input type="button" onclick="location.href='/';" value="launch UI"> -->
</form>
<!--
		
<iframe width="40%" height="35%"  name="my-iframe" src="iframe.php"></iframe>
<iframe width="40%" height="35%"   src="frame3.html"></iframe>
-->
<iframe  style="display:none" width="90%" height="40%"  name="my-iframe2" src="iframe.php"></iframe>
<head>
    <meta charset="UTF-8">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"
            type="text/javascript">
    </script>
</head>
<iframe  width="100%" height="100%" src="frame.html"></iframe>
<!--<iframe  width="40%" height="40%" src="frame2.html"></iframe>




-->

<div style="display:none" id='containerDiv'></div>
<script>
function getLog() {
    $.ajax({
        url: 'log.txt',
        dataType: 'text',
        success: function(text) {
            $("#containerDiv").text(text);
//            setTimeout(getLog, 100); // refresh every 30 seconds
        }
    })
}

getLog();
</script>

<script type=text/javascript>
window.onload = function() {
    var frameRefreshInterval = setInterval(100, function() {
        document.getElementById("myframe").src = document.getElementById("myframe").src
    });
    // any other code
}
</script>
</body>
