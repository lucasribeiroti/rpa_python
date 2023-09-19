$exclude = @("venv", "CustomerOnboarding.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "CustomerOnboarding.zip" -Force