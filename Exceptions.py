import sys
from typing import List


def error_detail_message_detail(error,error_detail:sys)->List[str]:
    
    _,_,exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in python script no [{2}] line no [{1}] error message [{}]'.format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_detail_message_detail(error=error_message,error_detail=error_detail)
        
    def __str__(self):
        
        return self.error_message