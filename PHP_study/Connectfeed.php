<?php
error_reporting(E_ALL);
ini_set('display_errors', '1');

$host = "localhost";
$user = "root";
$password = "";
$database = "feedback";

$connect = mysqli_connect($host, $user, $password, $database);
if (!$connect) {
    die("Database connection failed: " . mysqli_connect_error());
}
?>