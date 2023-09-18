$exclude = @("venv", "MyCRM.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "MyCRM.zip" -Force