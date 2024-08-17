import logging
from io import StringIO

from src.pytemplate.service.logs import log


def test_log_context_manager():
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logger = logging.getLogger()
    logger.addHandler(handler)

    original_level = logging.INFO
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
