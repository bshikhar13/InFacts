<?php

$text = $_POST['comment'];
$text = filter_var($text, FILTER_SANITIZE_STRING);

echo $text;
$tmp =  exec("python processinpython.py $text",$output);
echo "<pre>";
print_r($output);
echo "</pre>";
?>