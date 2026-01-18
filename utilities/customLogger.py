import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='./logs/test.log', level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


class LoggerFactory:
    _loggers = {}
    
    @staticmethod
    def get_logger(name):
        if name not in LoggerFactory._loggers:
            logger = logging.getLogger(name)
            if not logger.handlers:
                handler = logging.FileHandler('./logs/test.log')
                formatter = logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                )
                handler.setFormatter(formatter)
                logger.addHandler(handler)
                logger.setLevel(logging.INFO)
            LoggerFactory._loggers[name] = logger
        return LoggerFactory._loggers[name]
