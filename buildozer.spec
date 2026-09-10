[app]

# (str) Title of your application
title = تطبيق مؤسسة الباقيات الصالحات

# (str) Package name
package.name = baqiyat_salihat

# (str) Package domain (needed for android/ios packaging)
package.domain = org.baqiyat

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,db,h,cpp,txt,cmake

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy,flet
requirements = python3,flet,sqlite3

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE, VIBRATE, ACCESS_FINE_LOCATION

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version
android.ndk = 25.2.9519653

# (bool) Use --private data directory (True) or --dir public storage (False)
android.private_storage = True

# (list) List of Java .jar files to add to the libs so that your application
android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project
#android.add_src =

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = disable, 1 = enable)
warn_on_root = 1
