<html>
    <body>
        <?php
            date_default_timezone_set('MST');
            $fw   = fopen("flag_submit.log", 'a') or die("Unable to open flag_submit.log for writing");
            $ans  = "SazpOC8Ykl3a2";
            $salt = "SuperBallerKickAssSaltValue";
            $flag = crypt($_POST["flag"].$_POST["user"].$_POST["pass"], $salt);
            if($flag == $ans)
            {
                # Write out info to file
                fwrite($fw, date("Y-m-d H:i:s")." - Correct submission from ".$_SERVER['REMOTE_ADDR']);
                fwrite($fw, ", Content - ".$flag."\n");
                # Display a success message.
                # Print out that the flag has been found.
                print("Success!  You have captured the flag!\n");
            }
            else
            {
                fwrite($fw, date("Y-m-d H:i:s")." - Incorrect submission from ".$_SERVER['REMOTE_ADDR']);
                fwrite($fw, ", Content - ".$flag."\n");
                print("Incorrect flag attempt.  This submission has been logged.\n");
                # Display a failure message.
            }
            fclose($fw)
        ?>
    </body>
</html
