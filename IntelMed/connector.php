<?php

require_once "/group_projectDBWS/credentials.php";

// creating a connection

$conn = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

if ($conn->connect_error) {
    die("Connection failed: ". $conn->connect_error);
}
?>