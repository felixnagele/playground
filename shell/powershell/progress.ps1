$barLength = 20
$charsFilled = "#"
$charsEmpty  = "-"

while ($true) {
  foreach ($p in 0..20) {   # 0..20 -> 0 to 100 in steps of 5
    $percent = $p * 5

    # Amount of filled characters
    $filled = [int]($percent * $barLength / 100)

    # Build progress bar
    $bar = ($charsFilled * $filled) + ($charsEmpty * ($barLength - $filled))

    Clear-Host
    Write-Host "Progress: [$bar] $percent%" -ForegroundColor Yellow

    Start-Sleep -Milliseconds 50
  }
}
