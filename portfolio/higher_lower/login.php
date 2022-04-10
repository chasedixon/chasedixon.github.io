<?php include('includes/session_config.php') ?>
<!DOCTYPE html>
<html>
    <?php include("includes/head.php"); ?>
    <body>
        <?php include("includes/alert.php") ?>
        <div class="card col-md-8 mx-auto mt-3 p-3">
            <h1 class="card-title mx-auto my-3 p-3">Login</h1>
            <form action="authenticate.php" method="POST">
                <label class="form-label mb-3" for="username">Username</label>
                <input class="form-control mb-3" autofocus="autofocus" type="textfield" name="username"/>
                <label class="form-label mb-3" for="password">Password</label>
                <input class="form-control mb-3" type="password" name="password"/>

                <input class="btn btn-success mb-3" type="submit" name="login"/>
            </form>
            <p>Don't have an account? <a href="register.php">Register</a> here.</p>
        </div>
    </body>
</html>
    