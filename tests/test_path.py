import unittest

from carbonate.util import metric_to_fs, fs_to_metric


class PathTest(unittest.TestCase):
    def test_metric_to_fs_no_prepend(self):
        in_ = "servers.s0123.foo.bar"
        out = "servers/s0123/foo/bar.wsp"
        assert metric_to_fs(in_) == out

    def test_metric_to_fs_prepend(self):
        in_ = "servers.s0123.foo.bar"
        out = "/mnt/data/whisper/servers/s0123/foo/bar.wsp"
        assert metric_to_fs(in_, prepend='/mnt/data/whisper') == out

    def test_fs_to_metric(self):
        in_ = "servers/s0123/foo/bar.wsp"
        out = "servers.s0123.foo.bar"
        assert fs_to_metric(in_) == out
