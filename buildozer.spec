[app]
title = AAN
package.name = YT.prt
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,yt-dlp
orientation = portrait

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
