---
marp: true
theme: default
paginate: true
---
# Windows - Path
- Query path: in command line type echo %path%
- Set path
  - 開啟設定 > 系統 > 關於 > 進階系統設定
  - Windows 預設應用程式位置: %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
  - 重開機生效新的path
---
# Windows - Uninstall Python
- Using the Control Panel
- Open “Control Panel” app
- Click “Programs” -> ”Programs and Features”
- Find Python
- Right click, then select uninstal
---
# Mac - Path
Open Terminal
- where python3
- which python3
- pwd
- echo $PATH
- echo $HOME
Modify path
- Open z-shell setting: open ~/.zshrc (open ~/.bash_profile)
- Add line: export PATH="/usr/local/example/bin:$PATH" 
- Save file
- Apply chanages: source ~/.zshrc

---
# Mac - 官方 Python 3.12
- code path: /Library/Frameworks/Python.framework/Versions/3.12/bin/Python3
- package path: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages
- Shell (RPEL: via terminal type python3)
- IDLE (default IDE)
- IPython是一種基於Python的互動式直譯器。相較於原生的Python Shell，IPython提供了更為強大的編輯和互動功能。基本上跟Jupyter綁一起

---
# Mac - Thonny 自帶 Python 3.10.11
- code path： /Users/jacky/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/bin/python3.10
- package path (使用者安裝):  /Users/Jacky/Library/Python/3.10/lib/python/site-packages
- package path (Thonny預裝): /Users/jacky/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages
---
# Mac - commands
- where python3
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3
/usr/local/bin/python3
/usr/bin/python3

- which python3
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

- python3 -m site : site-specific configuration hook
- import sys
  sys.executable
  sys.path
  sys.prefix

---
# Mac - Uninstall Python
- Navigate to /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
- Move it to trash
- Remove Python from PATH
- Open z-shell file to Remove any lines that add Python files and directories to the PATH variables

---
# Mac - Uninstall Anaconda
- conda install anaconda-clean
- anaconda-clean –yes
- rm -rf ~/anaconda3 or sudo rm -rf /anaconda3
- Manually delete ~/.anaconda_backup/<timestamp>
- In ~/.zshrc or ~/.bash_profile or .bashrc or .profile to remove conda related path setting, like
- Remove hidden files or directory i=under HOME, .condarc, .conda, .continuum
- Move Conda APP to trash 
---
# Windows - Uninstall Anaconda
- In the folder where you installed Anaconda (Example: C:\Users\username\Anaconda3) there should be an executable called Uninstall-Anaconda.exe. 
- Double click on this file to start uninstall Anaconda.



