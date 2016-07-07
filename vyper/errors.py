class UnsupportedConfigError(Exception):
    """Denotes encountering an unsupported configuration file type."""
    def __init__(self, message, *args):
        self.message = message
        super(UnsupportedConfigError, self).__init__(message, *args)

    def __str__(self):
        return 'Unsupported Config Type {}'.format(self.message)


class UnsupportedRemoteProviderError(Exception):
    """Denotes encountering an unsupported remote provider.
    Currently only etcd and Consul are supported.
    """
    def __init__(self, message, *args):
        self.message = message
        super(UnsupportedRemoteProviderError, self).__init__(message, *args)

    def __str__(self):
        return 'Unsupported Remote Provider Type {}'.format(self.message)


class RemoteConfigError(Exception):
    """Denotes encountering an error while trying to
    pull the configuration from the remote provider.
    """
    def __init__(self, message, *args):
        self.message = message
        super(RemoteConfigError, self).__init__(message, *args)

    def __str__(self):
        return 'Remote Configuration Error {}'.format(self.message)


class ConfigFileNotFoundError(Exception):
    """Denotes failing to find configuration file."""
    def __init__(self, message, locations, *args):
        self.message = message
        self.locations = locations
        super(ConfigFileNotFoundError, self).__init__(message, locations, *args)

    def __str__(self):
        return 'Config File {} Not Found in {}'.format(self.message,
                                                       self.locations)
