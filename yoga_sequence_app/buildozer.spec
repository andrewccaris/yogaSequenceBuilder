[app]

title = Asana Generator App
package.name = asanageneratorapp
package.domain = org.asanagenerator

source.dir = .
source.include_exts = py,png,kv,yml,atlas
source.include_patterns = assets/*,libs/*
source.exclude_exts = spec
source.exclude_dirs = build, dist

version = 0.1
requirements = python3,kivy,kivymd

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
