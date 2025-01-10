$months = @("January", "February", "March", 
"April", "May", "June", "July", "August", 
"September", "October", "November", "December")

$year = 2025
$count = 1


foreach ($m in $months){
    New-Item -ItemType Directory -Path H:\VSCODE\LeetCode\$year +"_" +$count +"_" +$m
    $count += 1
}
    

<#
####################################################################
#   Testing output of the iteration to make sure folders are named
#   correctly.
####################################################################
foreach($m in $months){
    $FolderName = $year.ToString() +"_" +$count.ToString() +"_" +$m
    $count += 1
    Write-Output $FolderName
}
#>