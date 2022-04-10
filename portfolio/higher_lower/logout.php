<?php
    include('includes/session_config.php');
    if(isset($_SESSION['username'])) {
        unset($_SESSION['username']);
        $_SESSION["error_message"] = "Logged out successfully";
    }
    header("Location: login.php");
?>