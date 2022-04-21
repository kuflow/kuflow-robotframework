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


*** Variables ***
${TASK_ID}=    458fd52a-2b61-33f0-a2fc-1e164df210c1

*** Tasks ***
KuFlow One Fill Robot Test

    Set Client Authentication    %{KUFLOW_API_ENDPOINT}    %{KUFLOW_APPLICATION_IDENTIFIER}    %{KUFLOW_APPLICATION_TOKEN}

    Append Log Message    ${TASK_ID}    I'm a message form KuFlow RobotFramework Library  level=WARN 

    Save Element Document    ${TASK_ID}    DOC_MULTIPLE    /home/zeben/dummy/coyote.jpg

    Save Element    ${TASK_ID}    FIELD    My field value

    Save Element    ${TASK_ID}    FIELD    My field value    valid=${False}

    &{element_one} =    Create Dictionary    value=My Example Value One    valid=${False}
    &{element_two} =    Create Dictionary    value=My Example Value Two
    ${elements} =    Create List    ${element_one}    ${element_two}
    Save Elements    ${TASK_ID}    FIELD_MULTIPLE    ${elements}

KuFlow One Remove Robot Test

    Set Client Authentication    %{KUFLOW_API_ENDPOINT}    %{KUFLOW_APPLICATION_IDENTIFIER}    %{KUFLOW_APPLICATION_TOKEN}

    Delete Element Document    ${TASK_ID}    7dd16e94-2dac-4fca-931e-c2505baa695c
    
    Delete Element    ${TASK_ID}    DOC01
    