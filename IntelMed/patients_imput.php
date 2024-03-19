<?php
require_once "/group_projectDBWS/connector.php";

// check if the form data is posted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // error flag
    $error_flag = false;
    // collect and sanitize input data for patient table
    $health_insurance = $conn->real_escape_string($_POST['health_insurance_number']);
    $area = $conn->real_escape_string($_POST['area']);
    $address = $conn->real_escape_string($_POST['address']);

    // now the same will be done to user table
    $first_name = $conn->real_escape_string($_POST["firstname"]);
    $last_name = $conn->real_escape_string($_POST["lastname"]);
    $sex = $conn->real_escape_string($_POST["sex"]);
    $phone_number = $conn->real_escape_string($_POST["phonenumber"]);
    $email = $conn->real_escape_string($_POST["email"]);
    $password = $conn->real_escape_string($_POST["password"]);

    // Insert into user table
    $sqlUser = "INSERT INTO user (name, surname, sex, email, phone_number, password) VALUES (?, ?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($sqlUser);
    $stmt->bind_param("ssssss", $first_name, $last_name, $sex, $email, $phone_number, $password);
    if(!$stmt->execute()){
        $error_flag = true;
    }
    $stmt->close();

    if(!$error_flag) {
        $userId = $conn->insert_id;
        $stmt = $conn->prepare("INSERT INTO patient (health_insurance, user_id, area, address) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("siss", $health_insurance, $userId, $area, $address);
        if (!$stmt->execute()) {
            $error_flag = true;
        }
        $stmt->close();
    }
    // Close the connection
    $conn->close();

    if($error_flag) {
        header("Location: /group_projectDBWS/feedback_error.html");
        exit;
    }
    else{
        header("Location: /group_projectDBWS/feedback_success.html");
        exit;
    }
}
?>