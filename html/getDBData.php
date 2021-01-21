<?php
/*
 *  Author: Harter·Liang
 *  Function: Getting the newest temperature data from the database and display it
 *  Date: 2021/01/19
 *  Version: 1.0
 *  Created by PHPStorm
 */
    $servername = "servername";
    $username = "username";
    $password = "password";
    $dbname = "dbname";
    $tempResult = 0;

    $conn = new mysqli($servername, $username, $password, $dbname);

    if($conn->connect_error){
        //When facing the error of connection
        die("Failed to connect: ".$conn->connect_error);
    }

    #echo "Connect successfully<br>";

    $sqlQuery = "SELECT 5sec_temp_value FROM TEMP_5SEC ORDER BY 5sec_record_id DESC LIMIT 0,1";
    //Select the newest temperature from the database

    $result = $conn->query($sqlQuery);

    if($result->num_rows>0){
        //Whether we get the data or not
        while($row = $result->fetch_assoc()){
            $tempResult = $row['5sec_temp_value'];
        }
    }
    else{
        echo "No any results!";
        $tempResult = 0;
    }

    echo $tempResult;
    //Show the temperature on the page
