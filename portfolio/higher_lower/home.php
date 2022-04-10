<?php
    $login_required = True;
    include("includes/session_config.php");
?>
<!DOCTYPE html>
<html>
    <?php include("includes/head.php"); ?>
    <body>
        <?php include("includes/nav.php"); ?>
        <div class="card col-md-8 mx-auto mt-3 p-3">
            <h1 class="card-title mx-auto my-3">Welcome <?php echo $_SESSION['username'];?>!</h1>
            <?php
                if(isset($_SESSION['error_message'])) {
                    echo "<h2>" . $_SESSION['error_message'] . "</h2>";
                }
            ?>
            <div class="d-grid gap-2 d-md-block mx-auto">
                <a class="btn btn-success" href="play_game.php" role="button">Play Game</a>
                <a class="btn btn-primary" href="high_scores.php">High Scores</a>
            </div>
        </div>        
    </body>
</html>