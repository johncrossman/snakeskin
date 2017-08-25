import importlib.util
import os


def load_configs(app):
    """
    On app creation, load and and override configs in the following order:
     - config/default.py
     - config/{SNAKESKIN_ENV}.py
     - {SNAKESKIN_LOCAL_CONFIGS}/{SNAKESKIN_ENV}-local.py (excluded from version control; sensitive values go here)
    """
    load_module_config(app, 'default')
    # SNAKESKIN_ENV defaults to 'development'.
    snakeskin_env = os.environ.get('SNAKESKIN_ENV', 'development')
    load_module_config(app, snakeskin_env)
    load_local_config(app, '{}-local.py'.format(snakeskin_env))


def load_module_config(app, config_name):
    """Load an individual module-hosted configuration file if it exists."""
    config_path = 'config.{}'.format(config_name)
    if importlib.util.find_spec(config_path) is not None:
        app.config.from_object(config_path)


def load_local_config(app, config_name):
    """Load the local configuration file (if any) from a location outside the package."""
    configs_location = os.environ.get('SNAKESKIN_LOCAL_CONFIGS') or '../config/'
    config_path = configs_location + config_name
    app.config.from_pyfile(config_path, silent=True)
