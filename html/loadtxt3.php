    <?php
        $file = "log3.txt";
        $f = fopen($file, "r");
        while ( $line = fgets($f, 1000) ) {
            print $line;
        }
    ?>
