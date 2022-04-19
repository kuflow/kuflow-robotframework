*** Settings ***
Library    KuFlow


*** Variables ***
${TASK_ID}=    458fd52a-2b61-33f0-a2fc-1e164df210c1

*** Tasks ***
KuFlow One Robot Test

    Set Client Authentication    %{KUFLOW_API_ENDPOINT}    %{KUFLOW_APPLICATION_IDENTIFIER}    %{KUFLOW_APPLICATION_TOKEN}

    Append Log Message    ${TASK_ID}    I'm a message form KuFlow RobotFramework Library  level=WARN 

    Save Element Document    ${TASK_ID}    DOC_MULTIPLE    /home/zeben/dummy/coyote.jpg

    Save Element    ${TASK_ID}    FIELD    My field value

    Save Element    ${TASK_ID}    FIELD    My field value    valid=${False}

    &{element_one} =    Create Dictionary    value=My Example Value One    valid=${False}
    &{element_two} =    Create Dictionary    value=My Example Value Two
    ${elements} =    Create List    ${element_one}    ${element_two}
    Save Elements    ${TASK_ID}    FIELD_MULTIPLE    ${elements}
