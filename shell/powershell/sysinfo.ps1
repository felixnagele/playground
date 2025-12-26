Clear-Host
Write-Host "=== System Info ===" -ForegroundColor Cyan
Write-Host "Computer: $env:COMPUTERNAME" -ForegroundColor Green
Write-Host "User: $env:USERNAME" -ForegroundColor Magenta
Write-Host "Date: $(Get-Date)" -ForegroundColor Yellow
Write-Host "OS Version: $(Get-CimInstance Win32_OperatingSystem | Select-Object -ExpandProperty Version)" -ForegroundColor Blue
Write-Host "Uptime: $((Get-CimInstance Win32_OperatingSystem).LastBootUpTime | ForEach-Object { (Get-Date) - $_ } | Select-Object -ExpandProperty TotalHours) hours" -ForegroundColor Red
Write-Host "===================" -ForegroundColor Cyan
