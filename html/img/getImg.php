<?php
/*
 *  Author: Harter·Liang
 *  Function: Getting the second of the time when the file created
 *  Date: 2021/01/20
 *  Version: 1.0
 *  Created by PHPStorm
 */
    function getTimeDiff($fileName){

        $createdTime = filemtime($fileName);
        //Getting the unix second timestamp of time the file created

        $timeArr = getdate($createdTime);
        //Getting the array format of the real-type date instead of the unix timestamp of the time the file created

        $sec = $timeArr["seconds"];
        //Getting the seconds of the array of date

        $currTime = getdate(time());
        //Getting the current time with unix timestamp version

        $currSec = $currTime["seconds"];
        //Getting the second value of date version

        $secDiff = abs($currSec-$sec);
        //Calculate the difference of the second values

        return $secDiff;
    }

    function getNewestFile($fileName1, $fileName2, $fileName3){

        $timeDiff1 = getTimeDiff($fileName1);
        $timeDiff2 = getTimeDiff($fileName2);
        $timeDiff3 = getTimeDiff($fileName3);

        $diffArr = array($timeDiff1 => $fileName1, $timeDiff2 => $fileName2, $timeDiff3 => $fileName3);

        $minDiff = min($timeDiff1, $timeDiff2, $timeDiff3);

        return $diffArr[$minDiff];
    }

    $aimFile = getNewestFile("TestFig0.png", "TestFig17.png", "TestFig34.png");

    echo "<img src=\"img/" . $aimFile . "?t=" . Date("Y-m-d-H-i-s") . "\">";
