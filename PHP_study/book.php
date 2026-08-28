<?php
    require 'book-con.php';
    if(isset($_POST['insert'])){
        $profile = htmlspecialchars($_POST['profile']);
        $title = htmlspecialchars($_POST['title']);
        $author = htmlspecialchars($_POST['author']);
        $rating = $_POST['rating'];

        $query = 'INSERT';
        $result = mysqli_query($conn, $query);
        $message = "Book data has been inputed";
        header("Location: book.php?msg=$message");    }
    if(isset($_POST['delete'])){
        $profile = htmlspecialchars($_POST['profile']);
        $title = htmlspecialchars($_POST['title']);
        $author = htmlspecialchars($_POST['author']);
        $rating = $_POST['rating'];

        $query = '';
        $result = mysqli_query($conn, $query);
        header("Location: book.php?msg=$message");
    }
$query = "SELECT";
$result = mysqli_query($conn, $query);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link style= "book.css">
    <title>Book Sorter</title>
</head>
<body>
    <div class="book-card">
        <div class="insert-boxes">

        </div>
    </div>
    <div class="inserted">
        <div class="book-profile">

        </div>
        <div class="book-author-title">
            <div class="book-title"></div>
            <div class="book-author"></div>
        </div>
        <div class="book-rating">

        </div>
        <Button name="Delete">Delete</Button>
        <button name="edit">Edit</button>
    </div>
</body>
</html>
