from conans import ConanFile, CMake, tools

import os


class MsgpackConan(ConanFile):
    name = "msgpack"
    version = "2.1.5"
    license = "https://raw.githubusercontent.com/msgpack/msgpack-c/master/COPYING"
    url = "https://github.com/ulricheck/conan-msgpack"
    description = "The official C++ library for MessagePack"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    
    def source(self):
        source_url = "https://github.com/msgpack/msgpack-c/releases/download"
        archive_name = self.name + "-" + self.version
        tools.get("{0}/cpp-{1}/{2}.tar.gz"
            .format(source_url,  self.version, archive_name))
            
        os.rename(archive_name, "source")
        
    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        #cmake.definitions["MSGPACK_CXX11"] = True
        if self.settings.arch == "x86":
            cmake.definitions["MSGPACK_32BIT"] = True
        cmake.configure(source_dir="source")
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.includedirs.append(os.path.join(self.package_folder, "include"))
        
        libs = tools.collect_libs(self)
        self.output.info("LIBS: %s" % ",".join(libs))
        if self.settings.os == "Linux":
            self.cpp_info.libs = [l for l in libs if l.endswith('.so')]
        else:
            self.cpp_info.libs = libs


