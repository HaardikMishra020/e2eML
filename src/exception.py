import sys
import logging
import logger

def error_msg_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_msg="Error aa gya bhai.Yeh [{0}] me hai aur yeh line no.[{1}] par mila mujhe. Bolta hai [{2}] toh maine socha bhai ko btadu".format (
        file_name,exc_tb.tb_lineno,str(error))
    return error_msg

class CustomException(Exception):
    def __str__(self):
        return self.error_msg

    def __init__(self, error_msg,error_details:sys) -> None:
        super().__init__(error_msg)
        self.error_msg=error_msg_details(error_msg,error_details=error_details)

# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Ab nawab ko zero se divide krna hai ?")
#         raise CustomException(e,sys)
    