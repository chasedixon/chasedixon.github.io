<?php
    if(isset($_SESSION['error_message'])) {
        echo '<div class="alert alert-primary" role="alert">' . $_SESSION['error_message'] . '</div>';
        unset($_SESSION['error_message']);
    }
?>