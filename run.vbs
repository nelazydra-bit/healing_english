Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "powershell -Command ""$env:PYTHONUTF8='1'; python -m pygbag .""", 0, False