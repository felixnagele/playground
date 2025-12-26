Clear-Host
while ($true) {
  Write-Host (Get-Random) -ForegroundColor Green -NoNewline
  Start-Sleep -Milliseconds 5
}
