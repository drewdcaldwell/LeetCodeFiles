#### FILL THIS IN BEFORE RUNNING PROGRAM EACH MONTH ####
# Month number
$month = 1
# Total Daysin the Month
$daysinMonth = 31
# Month Name
$month = "January"
# Year
$year = 2025
# Monthly Folder Name
$folder = $year.ToString() + "_" +$month.ToString() +"_" +$month



$day = 1
while($day -le $daysinMonth){
    Write-Host $i
    $NewFolderName = $month.ToString() +"_" +$day.ToString() +"_" +$year.ToString()
    New-Item -ItemType Directory -Path H:\VSCODE\LeetCode\$folder\$NewFolderName
    $day += 1
}