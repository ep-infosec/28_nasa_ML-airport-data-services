__version__ = '1.0.1-dev97'

def get_major_version() -> str:
    return __version__.rpartition('.')[0]
