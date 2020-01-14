import ctypes
import subprocess


class VLang:
    def __init__(self, lib_path):
        """Create a library handler from a .so library file generated for v"""
        self.lib = ctypes.CDLL(lib_path)

    def __getattr__(self, attr):
        """Transparently access library methods from this object"""
        function = getattr(self.lib, "main__{}".format(attr), None)

        def execute(*args):
            return function(*args)

        return execute

    @staticmethod
    def make_lib(source_file, target_path=None):
        """Generate a .so file from a v file that is usable with this handler"""
        target_path = target_path if target_path else source_file.replace(".v", ".so")
        result = subprocess.run(
            ["v", "-o", source_file.replace(".v", ".c"), source_file]
        )
        assert result.returncode == 0
        result = subprocess.run(
            [
                "gcc",
                "-shared",
                "-o",
                target_path,
                "-fPIC",
                source_file.replace(".v", ".c"),
            ]
        )
        assert result.returncode == 0

    @staticmethod
    def from_v(file_path):
        lib_path = file_path.replace('.v', '_vlib.so')
        VLang.make_lib(file_path, target_path=lib_path)
        return VLang(lib_path)
