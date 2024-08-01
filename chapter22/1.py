import logging
from fastapi import FastAPI

# 로거 설정: 기본 로거를 구성하여 디버그 레벨 이상의 모든 메시지를 콘솔에 출력합니다.
logging.basicConfig(level = logging.DEBUG)

# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


# 다양한 로깅 레벨의 메시지를 생성합니다.
logging.debug("디버그 메시지: 가장 자세한 정보를 포함.")
logging.info("정보 메시지: 일반적인 운영에 대한 정보.")
logging.warning("경고 메시지: 예상치 못한 일이 발생했거나 발생할 수 있는 문제.")
logging.error("오류 메시지: 심각한 문제로 인해 프로그램의 일부 기능이 실패함.")
logging.critical("크리티컬 메시지: 매우 심각한 문제로, 프로그램의 주요 기능에 영향을 미침.")

# 이 예제를 실행하면 설정된 로그 레벨에 따라 콘솔에 로그가 출력됩니다.


# Logger 생성
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)


# Console handler 생성 및 추가
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# File handler 생성 및 추가
file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.ERROR)

# Formatter 생성 및 핸들러에 설정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
# Handlers를 Logger에 추가
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Filter 정의 및 추가
class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

error_filter = ErrorFilter()
file_handler.addFilter(error_filter)

# 로그 기록
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')