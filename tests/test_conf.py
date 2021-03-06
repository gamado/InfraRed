import os

from tests.test_cwd import utils

our_cwd_setup = utils.our_cwd_setup


def test_get_config_dir(our_cwd_setup):
    from cli import conf
    conf_file = conf.load_config_file()
    assert os.path.abspath(
        conf_file.get("defaults", "settings")) == os.path.join(os.getcwd(),
                                                               "fake_settings")
