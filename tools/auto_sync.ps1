$ErrorActionPreference = "Stop"

$repo = Split-Path -Parent $PSScriptRoot
$lockFile = Join-Path $env:TEMP "github-profile-auto-sync.lock"

if (Test-Path $lockFile) {
    exit 0
}

New-Item -ItemType File -Path $lockFile -Force | Out-Null

try {
    git -C $repo add -A

    git -C $repo diff --cached --quiet
    if ($LASTEXITCODE -eq 0) {
        exit 0
    }

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git -C $repo commit -m "chore: auto-sync $timestamp"
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }

    git -C $repo push origin HEAD
    exit $LASTEXITCODE
}
finally {
    Remove-Item -Path $lockFile -Force -ErrorAction SilentlyContinue
}
