from conans import ConanFile, tools

import os


class MsgpackConan(ConanFile):
    name = "msgpack"
    version = "2.1.5"
    license = "https://raw.githubusercontent.com/msgpack/msgpack-c/master/COPYING"
    url = "https://github.com/ulricheck/conan-msgpack"
    description = "The official C++ library for MessagePack"
    
    def source(self):
        source_url = "https://github.com/msgpack/msgpack-c/releases/download"
        archive_name = self.name + "-" + self.version
        tools.get("{0}/cpp-{1}/{2}.tar.gz"
            .format(source_url,  self.version, archive_name))
            
        os.rename(archive_name, "sources")
        
    def build(self):
        pass # silence warning

    def package(self):
        include_dir = os.path.join("sources", "include")
        self.copy("*.h", dst="include", src=include_dir)
        self.copy("*.hpp", dst="include", src=include_dir)

    def package_info(self):
        self.cpp_info.includedirs.append(os.path.join(self.package_folder, "include"))

    def package_id(self):
        self.info.header_only()
