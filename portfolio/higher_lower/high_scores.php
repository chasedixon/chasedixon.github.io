<?php
    $login_required = True;
    include("includes/session_config.php");

    // get high scores from database
    $query = "SELECT * FROM HighScore ORDER BY score ASC LIMIT 10;";
    $result = mysqli_query($db, $query) or die("Error getting high scores" . mysqli_error($db));

?>
<!DOCTYPE html>
<html>
    <?php include("includes/head.php"); ?>
    <body>
        <?php include("includes/nav.php"); ?>
        <div class="card col-md-8 mx-auto mt-3 p-3">
            <h1 class="card-title mx-auto my-3">High Scores</h1>
            <?php
                // if user just won game, get the win info from the database
                if(isset($_SESSION['score_id'])) {
                    $query = "SELECT * FROM HighScore WHERE high_score_id = " . $_SESSION['score_id'] . ";";
                    $my_result = mysqli_query($db, $query) or die("Error getting high score " . mysqli_error($db));
                    $my_score = mysqli_fetch_assoc($my_result);
                    echo '<h2 class="card-heading mx-auto mb-3">You won in ' . $my_score['score'] . " guesses!</h2>";
                }
            ?>
            <div class="col-md-9 mx-auto my-3">
                <table class="table">
                    <thead>
                        <tr>
                            <th scope="col" class='text-center'>#</th>
                            <th scope="col" class='text-center'>Username</th>
                            <th scope="col" class='text-center'>Score</th>
                            <th scope="col" class='text-center'>Date</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                            $rownum = 1;
                            // print all high scores, highlight row if user got a new high score
                            while($row = $result->fetch_assoc()) {

                                if(isset($_SESSION['score_id'])) {
                                    if($_SESSION['score_id'] == $row['high_score_id']) {
                                        $row_highlight = ' class="table-primary"';
                                    }
                                    else {
                                        $row_highlight = '';
                                    }
                                }
                                echo "<tr" . $row_highlight . '><th scope="row" class="text-center">' . $rownum . '</th><td class="text-center">' . $row['username'] . "</td><td class='text-center'>" . $row['score'] . "</td><td class='text-center'>" . $row['datetime'] . "</td></tr>";
                                $rownum += 1;
                            }

                            unset($_SESSION['score_id']);
                        ?>
                    </tbody>
                </table>
            </div>
            <div class="d-grid gap-2 d-md-block mx-auto">
                <a class="btn btn-primary" href="play_game.php">Play Again</a>
            </div>
        </div>
    </body>
</html>