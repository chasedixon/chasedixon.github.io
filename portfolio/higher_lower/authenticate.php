<?php
    include('includes/session_config.php');

    function loginFailed($error_message) {
        $_SESSION['login_failed'] = True;
        $_SESSION['error_message'] = $error_message;
        header("Location: login.php");
        exit;
    }

    // get username and password from login form
    $username = $_POST['username'];
    $password = $_POST['password'];

    // get user info from the database for given username
    $query = "SELECT * FROM User WHERE username = '" . $username . "';";
    $result = mysqli_query($db, $query) or loginFailed("Could not find username.");
    $row = mysqli_fetch_assoc($result);
    
    // verify entered password
    $password = $password . $row['salt'];
    $password = hash('sha256', $password);

    // if password was correct, login user, otherwise redirect to login
    if($password == $row['password']) {
        $_SESSION['username'] = $username;
        unset($_SESSION['error_message']);
        header("Location: home.php");
    } else {
        loginFailed("Incorrect username or password.");
    }
?>
