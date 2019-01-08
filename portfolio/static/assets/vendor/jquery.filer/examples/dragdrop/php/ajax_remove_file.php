<?php
if(isset($_POST['file'])){
    $file = 'static/assets/../uploads/' . $_POST['file'];
    if(file_exists($file)){
        unlink($file);
    }
}
?>
