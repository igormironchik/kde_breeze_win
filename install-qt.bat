echo "Installing aqt..."

pip install aqtinstall --upgrade

echo "Installing Qt..."

set /P qt_version=<%CD%\qt.version

set AQT_CONFIG=aqt.ini

aqt install-qt --outputdir ..\Qt windows desktop %qt_version% win64_msvc2022_64 -m qtimageformats qtshadertools

IF %ERRORLEVEL% NEQ 0 (
	exit /B %ERRORLEVEL%
)
