Set objShell = CreateObject("WScript.Shell")
objShell.Run "powershell -ExecutionPolicy Bypass -File ""D:\0 - Repositories\personal\juliana\GestaoApp\run_gestaoapp.ps1""", 0, True
Set objShell = Nothing
