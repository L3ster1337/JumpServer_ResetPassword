# How to use it (for CVE-2024-4062, e.g)

Once you obtain a shell as root in Docker, go to the path below and create and place the passchanger.py file in it. This way, run it and change the administrator password, to try to escape docker or move laterally.<br>

```
/opt/jumpserver/apps/users/views/profile/passchanger.py
```
<br>

```
python3 passchanger.py
```
<br>
The user token will be generated and used to reset the password.


