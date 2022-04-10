<?php
    session_start();

    // if page requires login, and user isn't logged in, redirect to login page
    if($login_required && !isset($_SESSION['username'])) {
        $_SESSION['error_message'] = "Please login to view page.";
        header("Location: login.php");
        exit;
    }

    // connect to database
    $db = mysqli_connect('sql204.byetcluster.com', 'epiz_30809344', 'zoGAlKXKVQeOF') or $_SESSION['error_message'] = "Failed to connect to database.";
    $selected = mysqli_select_db($db, 'epiz_30809344_NumberGuess') or $_SESSION['error_message'] = "Could not select database";

?>
