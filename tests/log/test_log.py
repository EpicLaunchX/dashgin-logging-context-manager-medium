import logging
from io import StringIO

from src.pytemplate.service.logs import log


def test_log_context_manager_for_info():
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logger = logging.getLogger()
    logger.addHandler(handler)

    original_level = logging.DEBUG
    logger.setLevel(original_level)

    with log(logging.INFO) as logger:
        assert logger.getEffectiveLevel() == logging.INFO
        logger.info("This is an info message")

    # Ensure the logging level is restored after context manager exits
    assert logger.getEffectiveLevel() == original_level

    # Check that the info message was logged
    log_contents = log_stream.getvalue()
    assert "This is an info message" in log_contents

    log_stream.close()


def test_log_context_manager_for_warning():
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logger = logging.getLogger()
    logger.addHandler(handler)

    original_level = logging.DEBUG
    logger.setLevel(original_level)

    with log(logging.WARNING) as logger:
        assert logger.getEffectiveLevel() == logging.WARNING
        logger.warning("This is a warning message")

    # Ensure the logging level is restored after context manager exits
    assert logger.getEffectiveLevel() == original_level

    # Check that the warning message was logged
    log_contents = log_stream.getvalue()
    assert "This is a warning message" in log_contents

    log_stream.close()


def test_log_context_manager_for_error():
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logger = logging.getLogger()
    logger.addHandler(handler)

    original_level = logging.DEBUG
    logger.setLevel(original_level)

    with log(logging.ERROR) as logger:
        assert logger.getEffectiveLevel() == logging.ERROR
        logger.error("This is an error message")

    # Ensure the logging level is restored after context manager exits
    assert logger.getEffectiveLevel() == original_level

    # Check that the error message was logged
    log_contents = log_stream.getvalue()
    assert "This is an error message" in log_contents

    log_stream.close()
