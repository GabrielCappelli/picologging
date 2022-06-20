import picologging
import logging
import io

def test_basic_handler():
    handler = picologging.Handler()
    record = picologging.LogRecord('test', logging.INFO, 'test', 1, 'test', (), None, None, None)
    handler.handle(record)

def test_stream_handler():
    stream = io.StringIO()
    handler = picologging.StreamHandler(stream)
    record = picologging.LogRecord('test', logging.INFO, __file__, 1, 'test', (), None, None, None)
    formatter = picologging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    handler.handle(record)
    assert stream.getvalue() == 'test\n'

def test_custom_handler():
    class CustomHandler(picologging.Handler):
        def __init__(self):
            super().__init__()
            self.records = []

        def emit(self, record):
            self.records.append(record)

    handler = CustomHandler()
    record = picologging.LogRecord('test', logging.INFO, __file__, 1, 'test', (), None, None, None)
    formatter = picologging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    handler.handle(record)
    assert len(handler.records) == 1
    assert handler.records[0] == record
