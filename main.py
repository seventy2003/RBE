# -*- coding: utf-8 -*-

"""
FILE : main 

DESCRIPTION:   
                                                                                       
FUNCTION LIST:  
  1. main

REVISION:  

  
Ver  | yyyymmdd | Who    | Description of changes
1.00 | 20181105 | wxhao  | Create.

"""

from view import *
from docx import Document
from sqlalchemy import *

if __name__ == "__main__":

    # command line view
    v = CmdView()
    v.run()



