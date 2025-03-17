---
marp: true
theme: default
class: invert
size: 16:9
paginate: true
footer: 國立陽明交通大學 電子與光子學士學位學程
headingDivider: 1
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
  
  .middle-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 75%;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid img {
    width: 100%;
  }
  .red-text {
    color: red;
  }
  
  .blue-text {
    color: blue;  
  }

  .small-text {
    font-size: 0.80rem;
  }
---
# Windows - Path
- Query path: in command line type echo %path%
- Set path
  - 開啟設定 > 系統 > 關於 > 進階系統設定
  - Windows 預設應用程式位置: %USERPROFILE%\AppData\Local\Microsoft\WindowsApps
  - 重開機生效新的path

# Windows - Uninstall Python
- Using the Control Panel
- Open “Control Panel” app
- Click “Programs” -> ”Programs and Features”
- Find Python
- Right click, then select uninstal

# Mac - Path
Open Terminal
- where python3; which python3
- pwd
- echo $PATH; echo $HOME

Modify path
- Open z-shell setting: open ~/.zshrc (open ~/.bash_profile)
- Add line: export PATH="/usr/local/example/bin:$PATH" 
- Save file
- Apply changes: source ~/.zshrc

# Mac - 官方 Python 3.12
- code path: /Library/Frameworks/Python.framework/Versions/3.12/bin/Python3
- package path: /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages
- Shell (RPEL: via terminal type python3)
- IDLE (default IDE)
- IPython是一種基於Python的互動式直譯器。相較於原生的Python Shell，IPython提供了更為強大的編輯和互動功能。基本上跟Jupyter綁一起

# Mac - Thonny 自帶 Python 3.10.11
- code path： /Users/jacky/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/bin/python3.10
- package path (使用者安裝):  /Users/Jacky/Library/Python/3.10/lib/python/site-packages
- package path (Thonny預裝): /Users/jacky/Applications/Thonny.app/Contents/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages

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

# Mac - Uninstall Python
- Navigate to /Library/Frameworks/Python.framework/Versions/3.13/bin/python3
- Move it to trash
- Remove Python from PATH
- Open z-shell file to Remove any lines that add Python files and directories to the PATH variables

# Mac - Uninstall Anaconda
- conda install anaconda-clean
- anaconda-clean –yes
- rm -rf ~/anaconda3 or sudo rm -rf /anaconda3
- Manually delete ~/.anaconda_backup/<timestamp>
- In ~/.zshrc or ~/.bash_profile or .bashrc or .profile to remove conda related path setting, like
- Remove hidden files or directory i=under HOME, .condarc, .conda, .continuum
- Move Conda APP to trash 

# Windows - Uninstall Anaconda
- In the folder where you installed Anaconda (Example: C:\Users\username\Anaconda3) there should be an executable called Uninstall-Anaconda.exe. 
- Double click on this file to start uninstall Anaconda.

# View ipynb File in Github Get "Unable to render code block"
<span class="small-text">
- Clear cache & cookies: outdated cache might sometimes cause rendering issues.<br>
- Browser extensions: browser extensions can occasionally interfere with content rendering. Disable extensions one by one to see if any extension cause the problem.<br>
<span class="red-text">"Dark Mode - Night Eye", "Youtube", "ContentShake AI Extension", "Ninja Cookie", "Awesome ScreenShot", "TopCashback", "Saladict", "Truffle", "Selectext: Copy Text from Videos", "SmoothScroll", "Tampermonkey", "word translation plugin", "ModHeader - Modify HTTP headers"</span><br>
- Update browser to latest version<br>
- Toggling hardware acceleration in Edge browser settings<br>
- Alternative approach: As an interim solution, you could consider using external platforms or tools like nbviewer to view your .ipynb files. Just paste the link to your GitHub .ipynb file there, and it should render appropriately.</span>
