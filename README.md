## This repository holds a conan recipe for msgpack.

[Conan.io](https://conan.io) package for [the msgpack C++ library](https://github.com/msgpack/msgpack-c) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/tum-ubitrack/public-conan/msgpack%3Aulricheck).

## For Users: Use this package

### Basic setup

    $ conan install msgpack/2.1.5@ulricheck/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    msgpack/2.1.5@ulricheck/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..
	
Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they shoudl not be added to the root of the project, nor committed to git. 

## For Packagers: Publish this Package

The example below shows the commands used to publish to ulricheck conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly. 

## Build  

This is a header only library, so nothing needs to be built.

## Package 

    $ conan create ulricheck/testing
	
## Add Remote

	$ conan remote add tum-ubitrack "https://api.bintray.com/conan/tum-ubitrack/public-conan"

## Upload

    $ conan upload msgpack/2.1.5@ulricheck/stable -r tum-ubitrack

### License
[Boost](https://raw.githubusercontent.com/msgpack/msgpack-c/master/COPYING)
