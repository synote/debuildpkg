#build python package

```
tar -czvf ./debhello-1.1.tar.gz ./debhello-1.1/
cd debhello-1.1
debmake -b':py3'
```

Here, the -b':py3' option is used to specify the generated binary package 
contain Python3 script and module files.


The use of “--with python3” option invokes dh_python3 to calculate Python 
dependencies, adds maintainer scripts to byte compile files, etc. See 
dh_python3(1).


the debmake command sets “Architecture: all” and “Multi-Arch: foreign”


```
debuild
```

```
dpkg-buildpackage -rfakeroot -D -us -uc
```
