<?php
    include "connect.php";
    if(isset($_POST['save'])){
        $nama = $_POST['nama'];
        $umur = $_POST['umur'];
        $deskripsi = $_POST['deskripsi'];

        $query = "INSERT INTO `biodata`(`Nama`, `Umur`, `Deskripsi`) VALUES ('$nama','$umur','$deskripsi')";
        mysqli_query($connect, $query);
    }
    if(isset($_GET['delete'])){
        $id = $_GET['delete'];
        $query = "DELETE FROM biodata WHERE Id = $id";
        mysqli_query($connect, $query);
        header("Location: database.php");
        exit();
    }
    if(isset($_POST['update'])){
        $namas = $_POST['nama2'];
        $umurs = $_POST['umur2'];
        $deskripsis = $_POST['deskripsi2'];
        $id = $_POST['id'];
        #$new_query = "INSERT INTO 'biodata'('Nama2', 'Umur2', 'Deskripsi2') VALUES ('$namas','$umurs','$deskripsis')";
        $query = "UPDATE biodata SET Nama = '$namas', Umur = '$umurs', Deskripsi = '$deskripsis' WHERE Id = $id";
        mysqli_query($connect, $query);
        header("Location: database.php");
        exit();
    }
    $editing = false;
    $edit_name = "";
    $edit_id = "";
    $edit_age = "";
    $edit_deskripsi = "";

    if(isset($_GET["edit"])){
        $editing = true;
        $id_edit = $_GET["edit"];
        $query_edit = "SELECT * FROM biodata WHERE Id = $id_edit";
        $result_edit = mysqli_query($connect, $query_edit);
        $row_edit = mysqli_fetch_assoc($result_edit);

        $edit_id = $row_edit['Id'];
        $edit_nama = $row_edit['Nama'];
        $edit_umur = $row_edit['Umur'];
        $edit_deskripsi = $row_edit['Deskripsi'];

    }
    $query = "SELECT * FROM biodata";
    $result = mysqli_query($connect, $query);
?>
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="database.css">
    <title>database</title>
</head>
<body>
<div class="body">
    <form method="POST" action="">
        <input type="text" name="nama" placeholder="Masukkan Nama" class="input" required><br>
        <input type="number" name="umur" placeholder="Masukkan Umur" class="input" required><br>
        <textarea type="text" name="deskripsi" placeholder="Masukkan Deskripsi" class="input" required></textarea><br>
        <div class="center">
            <button class="button" type="submit" name="save">Simpan Data</button>
        </div>
    </form>
</div>
<?php if($editing): ?>
<div class="body-2">
    <form method="POST" action="">
        <input type="text" name="nama2" placeholder="Masukkan Nama" class="input" value= "<?php echo $edit_nama; ?>" required><br>
        <input type="number" name="umur2" placeholder="Masukkan Umur" class="input" value= "<?php echo $edit_umur; ?>" required><br>
        <textarea type="text" name="deskripsi2" placeholder="Masukkan Deskripsi" class="input" value= "<?php echo $edit_deskripsi; ?>" required></textarea><br>
        <input type="hidden" name="id" value= "<?php echo $edit_id; ?>">
        <div class="center">
            <button class="update" type="submit" name="update">Update Data</button>
        </div>
</div>
<?php endif;?>
    <table>
        <tr>
            <th>ID</th>
            <th>NAMA</th>
            <th>UMUR</th>
            <th>DESKRIPSI</th>
        <tr>
        <tr>
            <?php
                while($row = mysqli_fetch_assoc($result)): ?>
                    <tr>
                        <td><?php echo $row['Id']?><br></td>
                        <td><?php echo $row['Nama']?><br></td>
                        <td><?php echo $row['Umur']?><br></td>
                        <td><?php echo $row['Deskripsi']?><br></td>
                        <td><a href="database.php?delete=<?php echo $row['Id'] ?>">Hapus</a><br></td>
                        <td><a href="database.php?edit=<?php echo $row['Id'] ?>">Edit</a></td>
                    </tr>
            <?php endwhile;?>
        </tr>
</body>
<script src="database.js"></script>
</html>
        