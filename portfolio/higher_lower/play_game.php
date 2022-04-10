<?php
    $login_required = True;
    include("includes/session_config.php");

    function gameError($error_message){
        $_SESSION['error_message'] = $error_message;
        header("Location: play_game.php");
    }
?>
<!DOCTYPE html>
<html>
    <?php include("includes/head.php"); ?>
    <body>
        <?php include("includes/nav.php"); ?>
        
        <div class="card col-md-8 mx-auto mt-3 p-3">
            <h1 class="card-title mx-auto my-3">Higher/Lower</h1>
            <?php
                // initialize new game if not currently running
                if(!isset($_SESSION['number'])) {
                    $_SESSION['number'] = random_int(1, 100);
                    $_SESSION['guess_count'] = 0;
                }

                // check guess if one has been made
                if(isset($_POST['guess'])) {
                    $guess = $_POST['guess'];
                    
                    // check if guess is valid
                    if($guess < 1 || $guess > 100) {
                        gameError("Invalid guess. Please enter number between 1 and 100.");
                    }

                    // if valid, increment count
                    $_SESSION['guess_count'] += 1;

                    // if guess is correct, add username and score to highscores, clear current number, and redirect to highscores page
                    if($guess == $_SESSION['number']) {
                        $query = "INSERT INTO HighScore (username, score) VALUES('" . $_SESSION['username'] . "', " . $_SESSION['guess_count'] . ");";
                        mysqli_query($db, $query);
                        $_SESSION['score_id'] = mysqli_insert_id($db);
                        unset($_SESSION['number']);
                        header("Location: high_scores.php");
                        
                    // if incorrect, tell whether the number is higher or lower
                    } else {
                        if ($guess < $_SESSION['number']) {
                            echo '<h2 class="card-heading mx-auto mb-3">The number is higher than ' . $guess . ". Guess again.</h2>";
                        } else {
                            echo '<h2 class="card-heading mx-auto mb-3">The number is lower than ' . $guess . ". Guess again.</h2>";
                        }
                    }
                        
                // if new game, print instructions
                } else {
                    echo '<h2 class="card-heading mx-auto mb-3">Guess the number between 1 and 100</h2>';
                }

                // guessing form
                echo '<form action="play_game.php" method="POST"><label class="form-label mb-3" for="guess">Guess:</label><input class="form-control mb-3" autofocus="autofocus" type="text" name="guess"/><input class="btn btn-primary" type="submit" name="submit_guess"/></form>';
            ?>
        </div>
    </body>
</html>
