# MIT License
#
# Copyright (c) 2022 KuFlow
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

*** Settings ***
Variables    devdata/env.py
Library    KuFlow

*** Tasks ***
KuFlow One Fill Robot Test

    Set Client Authentication    ${KUFLOW_API_ENDPOINT}    ${KUFLOW_APPLICATION_IDENTIFIER}    ${KUFLOW_APPLICATION_TOKEN}

    ## Add log message to the task
    # Append Log Message    ${KUFLOW_TASK_ID}    I'm a message form KuFlow RobotFramework Library  level=WARN 

    ## Upload a new file
    # Save Element Document    ${KUFLOW_TASK_ID}    DOC_MULTIPLE    /files/dummy/coyote.jpg

    # Replace a specific file in a multivalue element with new content
    # Save Element Document    ${KUFLOW_TASK_ID}    DOC_MULTIPLE    /files/dummy/marvin.jpg    8d59ccf6-251c-4f0d-856e-a3d516f40f65

    # Save a string element
    Save Element    ${KUFLOW_TASK_ID}    FIELD     Lorem ipsum

    # Save a multivalue string element with all elements with valid=True
    Save Element     one    two    three

    # Save a multivalue string element with all elements with valid=False
    Save Element     one    two    three    valid=False

    # Save a Number element (Integer)
    ${result} =    Convert To Integer    123
    Save Element    ${KUFLOW_TASK_ID}    FIELD    ${result}

    # Save a Number element (Integer)
    ${result} =    Convert To Integer    123
    Save Element    ${KUFLOW_TASK_ID}    FIELD    ${result}

    # Save a Number element (Float) with valid=True
    ${result} =    Convert To Number    123.123
    Save Element    ${KUFLOW_TASK_ID}    FIELD    ${result}    valid=${False}

    # Save a multivalue Number element
    ${result_one} =    Convert To Integer    123
    ${result_two} =    Convert To Number    123.123
    Save Element    ${KUFLOW_TASK_ID}    FIELD    ${result_one}    ${result_two}

    # Save a object element with valid=False
    &{result} =    Create Dictionary    one_key=My Example Value One    two_key=2    
    Save Element    ${KUFLOW_TASK_ID}    FIELD     ${result}    valid=${False}

    # Save a multivalue object element
    &{result_one} =    Create Dictionary    one_key=My Example Value One    two_key=2    
    &{result_two} =    Create Dictionary    a_key=My Example Value A    b_key=B    
    Save Element    ${KUFLOW_TASK_ID}    FIELD     ${result_one}    ${result_two}

    # Save a Principal element
    ${result} =    Convert To Element Value Principal Item    7dd16e94-2dac-4fca-931e-c2505baa695c
    Save Element    ${KUFLOW_TASK_ID}    FIELD    ${result}

    # Save a multiple Principal element with valid=False
    ${result_one} =    Convert To Element Value Principal Item    7dd16e94-2dac-4fca-931e-c2505baa695c
    ${result_two} =    Convert To Element Value Principal Item    7dd16e94-2dac-4fca-931e-c2505baa695c
    Save Element    ${KUFLOW_TASK_ID}    FIELD    ${result_one}    ${result_two}    valid=${False}

    # Save a Document element
    ${result} =    Convert To Element Value Document Item    7dd16e94-2dac-4fca-931e-c2505baa695c
    Save Element    ${KUFLOW_TASK_ID}    FIELD    ${result}

    # Save a multiple Document element with valid=False
    ${result_one} =    Convert To Element Value Document Item    7dd16e94-2dac-4fca-931e-c2505baa695c
    ${result_two} =    Convert To Element Value Document Item    7dd16e94-2dac-4fca-931e-c2505baa695c
    Save Element    ${KUFLOW_TASK_ID}    FIELD    ${result_one}    ${result_two}    valid=${False}

KuFlow One Remove Robot Test

    Set Client Authentication    ${KUFLOW_API_ENDPOINT}    ${KUFLOW_APPLICATION_IDENTIFIER}    ${KUFLOW_APPLICATION_TOKEN}

    # Delete Element Document    ${KUFLOW_API_ENDPOINT}    8d59ccf6-251c-4f0d-856e-a3d516f40f65
    
    # Delete Element    ${KUFLOW_API_ENDPOINT}    DOC01
    