#### FILL THIS IN BEFORE RUNNING PROGRAM EACH MONTH ####
# Month number
$monthNumber = 1
# Total Daysin the Month
$daysinMonth = 31
# Month Name
$month = "January"
# Year
$year = 2025
# Monthly Folder Name
$folder = $year.ToString() +"_" +$monthNumber.toString() + "_" +$month



$day = 1
while($day -le $daysinMonth){
    $NewFolderName = $monthNumber.ToString() +"_" +$day.ToString() +"_" +$year.ToString()
    $NewFileName = $monthNumber.ToString() +"_" +$day.ToString() +"_" +$year.ToString() +".py"
    New-Item H:\VSCODE\LeetCode\$folder\$NewFolderName\$NewFileName -type file
    #Write-Host $NewFolderName
    #Write-Host $NewFileName
    $day += 1
}
