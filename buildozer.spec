[app]

title = Jester King Market Lord
package.name = jkmarketlord
package.domain = org.jesterking

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 0.1

requirements = python3,kivy

orientation = landscape
fullscreen = 0

android.permissions =

android.api = 35
android.minapi = 24
android.ndk_api = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
