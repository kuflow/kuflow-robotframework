*** Settings ***
Library    KuFlow


*** Variables ***
${TASK_ID}=    458fd52a-2b61-33f0-a2fc-1e164df210c1
# &{ELEMENT_SAMPLE}    value=Example Value

*** Tasks ***
KuFlow One Robot Test
    Append Log Message    ${TASK_ID}    I'm a message form KuFlow RobotFramework Library  level=WARN 

    Save Element Document    ${TASK_ID}    DOC_MULTIPLE    /home/zeben/dummy/Demonio_de_tazmania.jpg

    Save Element    ${TASK_ID}    FIELD    My field value

    Save Element    ${TASK_ID}    FIELD    My field value    valid=${False}

    &{element_one} =    Create Dictionary    value=My Example Value One    valid=${False}
    &{element_two} =    Create Dictionary    value=My Example Value Two
    ${elements} =    Create List    ${element_one}    ${element_two}
    Save Elements    ${TASK_ID}    FIELD_MULTIPLE    ${elements}
    # Log To Console            =======: ${campo}

    # ${campo} =    Say Hello
    # Log To Console            Hello Robot: ${campo}