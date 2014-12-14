import sublime, sublime_plugin
import platform
from os import environ

# this script relies on the ld_lib_path_original and ld_lib_path_settings globals defined below

def is_mac():
  # not very found of this one, but, whatever
  if platform.system() == "Darwin":
    return True
  else:
    return False

def ld_path_env_name():
  # on OS X, the linker searches for DYLD_LIBRARY_PATH
  return ("DY" if is_mac() else "") + "LD_LIBRARY_PATH"

def ld_lib_path():
  global ld_lib_path_original
  global ld_lib_path_settings

  # concatenations with ':' (colon) join, just like the PATH environment variable
  environ[ld_path_env_name()] = ':'.join(ld_lib_path_settings.get("ld_library_path_items", []))

def plugin_loaded():
  global ld_lib_path_original
  global ld_lib_path_settings

  ld_lib_path_original = None
  ld_lib_path_settings = None

  ld_lib_path_settings = sublime.load_settings("Preferences.sublime-settings")
  ld_lib_path_settings.clear_on_change('ldlibpath-reload')
  ld_lib_path_settings.add_on_change('ldlibpath-reload', ld_lib_path)
  
  if ld_path_env_name() in environ:
    ld_lib_path_original = environ[ld_path_env_name()]

  ld_lib_path()

def plugin_unloaded():
  global ld_lib_path_original
  global ld_lib_path_settings

  environ[ld_path_env_name()] = ld_lib_path_original
  ld_lib_path_settings.clear_on_change('ldlibpath-reload')

  
plugin_loaded()