import logging
from io import StringIO

from src.pytemplate.service.logs import log


def test_log_context_manager():
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logger = logging.getLogger()
    logger.addHandler(handler)

    original_level = logging.DEBUG
    logger.setLevel(original_level)

    with log(logging.INFO) as logger:
        assert logger.getEffectiveLevel() == logging.INFO
        logger.info("This is an info message")
    log_contents = log_stream.getvalue()
    assert "This is an info message" in log_contents
    # clear the log stream
    log_stream.truncate(0)

    with log(logging.DEBUG) as logger:
        assert logger.getEffectiveLevel() == logging.DEBUG
        logger.debug("This is a debug message")

    log_contents = log_stream.getvalue()
    assert "This is a debug message" in log_contents

    with log(logging.ERROR) as logger:
        assert logger.getEffectiveLevel() == logging.ERROR
        logger.error("This is an error message")

    log_contents = log_stream.getvalue()
    assert "This is an error message" in log_contents

    with log(logging.CRITICAL) as logger:
        assert logger.getEffectiveLevel() == logging.CRITICAL
        logger.critical("This is a critical message")

    log_contents = log_stream.getvalue()
    assert "This is a critical message" in log_contents

    with log(logging.WARNING) as logger:
        assert logger.getEffectiveLevel() == logging.WARNING
        logger.warning("This is a warning message")

    # Ensure the logging level is restored after context manager exits
    assert logger.getEffectiveLevel() == original_level
    log_contents = log_stream.getvalue()

    assert "This is a warning message" in log_contents

    log_stream.close()
