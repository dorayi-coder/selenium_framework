import configparser
import os


class ReadConfig:
    _config = None

    @staticmethod
    def _load_config():
        if ReadConfig._config is None:
            config_path = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "Configurations", "config.ini"
            )
            ReadConfig._config = configparser.ConfigParser()
            ReadConfig._config.read(config_path)
        return ReadConfig._config

    @staticmethod
    def get(section, key):
        config = ReadConfig._load_config()
        try:
            return config.get(section, key)
        except configparser.NoSectionError:
            raise ValueError(f"Section '{section}' not found in config.ini")
        except configparser.NoOptionError:
            raise ValueError(f"Key '{key}' not found in section '{section}' of config.ini")
