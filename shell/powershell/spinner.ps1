Clear-Host
$spin = @("|","/","-","\")
while ($true) {
  foreach ($c in $spin) {
    Write-Host -NoNewline "`r$c" -ForegroundColor DarkBlue
    Start-Sleep -Milliseconds 100
  }
}
