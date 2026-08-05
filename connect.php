<?php
    $host = "localhost";
    $user = "root";
    $password = "";
    $database = "sql-belajar";

    $connect = mysqli_connect($host, $user, $password, $database);
    
    if(!$connect){
        die("Koneksi gagal". mysqli_connect_error());
    }
?>