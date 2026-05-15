from conan import ConanFile

class DependenciesRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "PkgConfigDeps"

    def requirements(self):
        self.requires("libiconv/1.17")
        self.requires("zlib/1.3.1")
        if self.settings.os == "Windows":
            self.requires("gettext/1.0")
            self.requires("libgettext/0.26")
            self.tool_requires("winflexbison/2.5.25")
            self.requires("zstd/1.5.5")
            self.requires("bzip2/1.0.8")
            self.requires("xz_utils/5.8.3")
            self.requires("libxslt/1.1.45")

    def configure(self):
        self.options["libiconv"].shared = False
        self.options["gettext"].shared = False
        self.options["zlib"].shared = False
        self.options["libgettext"].shared = False
        self.options["zstd"].shared = False
        self.options["bzip2"].shared = False
        self.options["xz_utils"].shared = False
        self.options["libxslt"].shared = False

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "lib", "lib")
