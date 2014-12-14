LD lib path
==============

Configure LD_LIBRARY_PATH (DYLD_LIBRARY_PATH on Mac OS X) environment variable to help library loader finding reloactable libs for your Sublime Text instance, especially to let build tools have custom install configurations.


Install
-------

LD Lib Path has been tested for Sublime Text 3 running on Mac OS X, but I have some confidence that it could work for other combinations like Linux or Sublime Text 2.

<i>submission to Package Control in the works</i>

To manually install LD Lib Path, run

    git clone https://github.com/int3h/SublimeLDLibPath.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/LDLibPath

for Sublime Text 2, or

    git clone https://github.com/int3h/SublimeLDLibPath.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/LDLibPath

for Sublime Text 3.


Options
-----------

You can optionally set the following option to your user preferences:

* `"ld_library_path_items": []`

  An array of strings of locations you wish to add to Sublime Text's library paths.

  For example, to add `/srv/lib` and `/opt/local/lib` to the library path in Sublime Text, you would use `"ld_library_path_items": ["/srv/lib", "/opt/local/lib"]`.


Credits
-----------

Thanks to [Matt Torok](https://github.com/int3h) for the code is largely inspired from [Fix Mac Path](https://github.com/int3h/SublimeFixMacPath)
