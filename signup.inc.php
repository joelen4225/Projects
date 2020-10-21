<?php

if (isset($_POST["submit"]))
{
    $name = $_POST["name"];
    $email = $_POST["email"];
    $user = $_POST["user"];
    $pass = $_POST["pass"];
    $pass2 = $_POST["pass2"];
    
    require_once 'dbh.inc.php';
    require_once 'functions.inc.php';
    
    if (emptyInputSignup($name, $email, $user, $pass, $pass2) !== false)
    {
        header("location: signup.php?error=emptyinput");
        exit();
    }
    if (invalidUid($user) !== false)
    {
        header("location: signup.php?error=invalidusername");
        exit();
    }
    if (invalidEmail($email) !== false)
    {
        header("location: signup.php?error=invalidemail");
        exit();
    }
    if (passwordMatch($pass, $pass2) !== false)
    {
        header("location: signup.php?error=passwordsdontmatch");
        exit();
    }
    if (userExists($conn, $user, $email) !== false)
    {
        header("location: signup.php?error=usernameoremailtaken");
        exit();
    }
    createUser($conn, $name, $email, $user, $pass);
}
else
{
    header("location: signup.php");
    exit();
}