cls
@echo
@ECHO OFF
DEL/F/Q "%USERPROFILE%\recent\*.lnk" 2>NUL
rd /s /q "%userprofile%\recent"
del %systemroot%\Prefetch\*.* /q /s
del %systemroot%\Temp\*.* /q /s
del %systemroot%\*.tmp /q /s
del %systemroot%\*.log /q /s
del “%userprofile%\CONFIG~1\TEMPOR~1\*.*” /s /q
del “%userprofile%\CONFIG~1\HISTRI~1\*.*” /s /q
del “%userprofile%\Cookies\*.*” /s /q /ah
del *.bak /s/q
@ECHO OFF
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 1
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 2
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 16
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 32
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 255
ECHO Done!
CLS