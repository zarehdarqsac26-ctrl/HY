[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,yt-dlp,charset-normalizer==2.1.1
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
