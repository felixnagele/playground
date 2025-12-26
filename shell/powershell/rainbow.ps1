Clear-Host
while ($true) {
  0..15 | ForEach-Object {
    Write-Host ("Color $_") -ForegroundColor $_
    Start-Sleep -Milliseconds 100
  }
}
