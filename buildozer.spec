[app]

title = Jester King GM Simulator
package.name = jkgmsim
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
p4a.ndk_api = 24
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

android.debug_artifact = apk
android.release_artifact = aab

android.release_keystore = ./release.keystore
android.release_keyalias = jkgmsim
android.release_storepass =
android.release_keypass =

[buildozer]

log_level = 2
warn_on_root = 1
