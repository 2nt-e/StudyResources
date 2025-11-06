Set WshShell = CreateObject("WScript.Shell")

' Start the HTTP server hidden
WshShell.Run "cmd /c python -m http.server 1929", 0, False
