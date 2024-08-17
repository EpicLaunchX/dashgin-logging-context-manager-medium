import logging
from io import StringIO

import pytest

from src.pytemplate.service.logs import log


def test_log_context_manager():
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logger = logging.getLogger()
    logger.addHandler(handler)

    original_level = logging.WARNING
    logger.setLevel(original_level)

    with log(logging.DEBUG) as logger:
        assert logger.getEffectiveLevel() == logging.DEBUG
        logger.debug("This is a debug message")

    # Ensure the logging level is restored after context manager exits
    assert logger.getEffectiveLevel() == original_level

    # Check that the debug message was logged
    log_contents = log_stream.getvalue()
    assert "This is a debug message" in log_contents

    log_stream.close()
