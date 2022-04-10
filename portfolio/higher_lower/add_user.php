<?php
    include('includes/session_config.php');

    function registrationFailed($error_message) {
        $_SESSION['error_message'] = $error_message;
        header("Location: register.php");
        exit;
    }

    // get username and password from regristration form
    $username = $_POST['username'];
    $password = $_POST['password'];

    // add salt and generate hash
    $salt = bin2hex(random_bytes(4));
    $password = $password . $salt;
    $password = hash('sha256', $password);

    // try to add user to database
    $query = "INSERT INTO User (username, password, salt) VALUES('" . $username . "', '" . $password . "', '" . $salt . "');";
    mysqli_query($db, $query) or registrationFailed("Username is not available.");

    // login user
    $_SESSION['username'] = $username;
    unset($_SESSION['error_message']);
    header("Location: home.php");
?>
