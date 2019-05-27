import logging
import sys


def init_logger_singleton(logger_name, log_level='DEBUG'):
    """
    Instantiate a custom logger object.

    Specify the name of the logger on instantiation, and optionally specify
    the logging level.

    This pattern for using the logging module is based on video by
    Sebastiaan Mathot "Application logging in Python | Python tricks"
    """

    # Make sure specified log_level is valid; default to logging.DEBUG
    if not logger_name: logger_name = 'root'
    if not log_level: log_level = 'debug'
    levels = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
        }
    log_level = levels.get(log_level.lower(), logging.DEBUG)

    ### Declaring `logger` as a global variable to make it available throughout
    global logger
    ### might be preferable to return an instance of the logging.getLogger class

    ### provide a logger name to distinguish it from the default `root`
    ### and activate it for all messages with at least the specified priority
    logger = logging.getLogger(name=logger_name)
    logger.setLevel(log_level)

    # The formatter will control how the log messages will be displayed
    ### note  we use square brackets and colons as delimiters in the output
    formatter = logging.Formatter(
        '[%(asctime)s:%(name)s:%(module)s:%(lineno)s:%(levelname)s] %(message)s'
        )
    #    '[%(name)s:%(filename)s:%(funcName)s:%(lineno)s:%(levelname)s] %(message)s'
    #      logger_name  module_file_name  function_name  line_no_with_module  logging_level_name  formatted_logging_message

    ### 1. create the handler to specify how/where messages will go
    ### 2. specify the priority level for the handler
    ### 3. specify formatting for the log message
    ### 4. add this handler to the logger object
    # Create a stream handler to output WARNING+ messages to stdout (or stderr ?)
    ### note that `streamhandler` is an arbitrary name
    streamhandler = logging.StreamHandler(sys.stdout)
    streamhandler.setLevel(logging.WARNING)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)

    # Create a file handler to output all messages (DEBUG+) to a file
    filehandler = logging.FileHandler(f'{logger_name}.log')
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)


def test_logger(logger_name, log_level=None):

    init_logger_singleton(logger_name, log_level)

    # just test all of the options...
    logger.debug('This is a DEBUG message.')
    logger.info('This is a INFO message.')
    logger.warning('This is a WARNING message.')
    logger.error('This is a ERROR message.')
    logger.critical('This is a CRITICAL message.')


if __name__ == '__main__':

    print('Test one, using default logging level')
    test_logger('MY_FIRST_LOGGER')

    print('Test two, using specified logging level = info')
    test_logger('ANOTHER_LOGGER', 'info')

