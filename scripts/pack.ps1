# Wrapper: Compress-Archive writes backslash entry names, which the Anthropic uploader rejects.
# Packaging is done by scripts/pack.py (forward-slash entries, manifest at zip root).
$ErrorActionPreference = "Stop"
python (Join-Path $PSScriptRoot "pack.py")
exit $LASTEXITCODE
