
def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('io', parent_package, top_path)
    config.add_subpackage('BaseDataProtocol')     # io first to detect if RSL is missing.

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
