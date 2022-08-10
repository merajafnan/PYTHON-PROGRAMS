#====================================================================================================================
# Copyright (c) 2019-2025 by cisco Systems, Inc.
# All rights reserved.
#====================================================================================================================
# Testcase: # Scale: OSPF Neighbor Scale #
#====================================================================================================================
# Modified by # merhassa #
#====================================================================================================================
# Testcase Description: # Branch - ISR1K/ISR4K/ASR1K 17.6.4 Certification #
#--------------------------------------------------------------------------------------------------------------------
#====================================================================================================================
# Modification History: <ver>   <user>   <date>:  <change>
#--------------------------------------------------------------------------------------------------------------------
#                        1.0   merhassa    10/08/2022:  Initial Creation
#                        2.0
#                        3.0
#====================================================================================================================

#SECTION ONE - PRE TEST : Save Runnig Config | CPU Util | CPU Process
#SECTION TWO - STEP 1 :
#SECTION TWO - STEP 2 :
#SECTION TWO - STEP 3 :
#SECTION TWO - STEP 4 :
#SECTION TWO - STEP 5 :
#FINAL SECTION - POST TEST

*** Settings ***
Library          CXTA
Library          String
Library          BuiltIn
Library          Dialogs
Library          DateTime
Library          Collections
Library          OperatingSystem
Library          Process
Library          CXTA
Resource         cxta.robot

Variables        /tmp/parameters.yaml
Resource         /tmp/attachments/MS_KeywordAIO.robot


Suite Setup      Run Keywords
...              load testbed
...              CONNECT TO CUSTOM DEVICES

Suite Teardown   Run Keywords
...              Disconnect From All Devices

*** Variables ***
# Template Variables


# Script Local Variables


*** Keywords ***
#All Keywords are in Keyword File MS_KeywordAIO.robot

*** Test Cases ***
# SECTION ONE - PRE TEST
#   [Documentation]  This step is to save Runnig Config, Check CPU Util, Check CPU Process
#     FOR    ${DUT}    IN     @{DUTS}
#       select device "${DUT}"
#       run "terminal length 0"
#       ${Clock}=    run "sh clock"
#       ${Time}=    Get Regexp Matches    ${Clock}    (\\d\\d:\\d\\d:\\d\\d)
#       ${Date}=    Get Regexp Matches    ${Clock}    (\\w\\w\\w|\\w\\w\\w\\w)\\s(\\d|\\d\\d)\\s\\d\\d\\d\\d
#       run "sh run" and save artifact as "${DUT}_Pre_TC_running_config_${Time[0]}-${Date[0]}.txt"
#       run "show version"
#     END

# SECTION TWO - STEP 1 : Basic Verification Commands
#     FOR    ${DUT}    IN     @{DUTS}
#       select device "${DUT}"
#         run "sh ip int br"
#         run "sh int des"
#         run "sh ip ro summ"
#         run "sh ip ro vrf DATA summ"
#         run "show ip ospf data"
#         run "show ip ospf neigh"
#         run "show ip ospf"
#         run "sh platform resource"
#     END

SECTION TWO - STEP 2 : Configure 500 sub-interfaces on DUT and peer
continue on failure enabled
select device "dc1_gw1"
${INT__}=    Set Variable    1
run "config t"
FOR    ${IP}    IN RANGE    1    255    4
IF    ${INT__} < 10
run "interface Gi1/1/1.${INT__}"
run "encapsulation dot1Q 100${INT__}"
run "ip add 60.1.1.${IP} 255.255.255.252"
run "shut"
run "no shut"
END
IF    ${INT__} >= 10 and ${INT__} < 100
run "interface Gi1/1/1.${INT__}"
run "encapsulation dot1Q 10${INT__}"
run "ip add 60.1.1.${IP} 255.255.255.252"
run "shut"
run "no shut"
END
IF    ${INT__} >= 100
run "interface Gi1/1/1.${INT__}"
run "encapsulation dot1Q 1${INT__}"
run "ip add 60.1.1.${IP} 255.255.255.252"
run "shut"
run "no shut"
END
${INT__}=    Evaluate    ${INT__} + 1
END
run "end"
#     # FOR    ${INT}    IN RANGE    256    260
#     #     run "interface Loopback66.${INT}"
#     #     ${INT__}=    Evaluate    ${INT} - 255
#     #     run "ip add 60.2.${INT__}.0 255.255.255.252"
#     #     run "shut"
#     #     run "no shut"
#     # END
#     run "end"
#     Sleep    5
#     run "sh ip int br"
select device "branch1_gw1"
${INT__}=    Set Variable    1
run "config t"
FOR    ${IP}    IN RANGE    1    255    4
IF    ${INT__} < 11
run "interface Gi0/0/2.${INT__}"
run "encapsulation dot1Q 100${INT__}"
run "ip add 70.1.1.${IP} 255.255.255.252"
run "shut"
run "no shut"
END
IF    ${INT__} >= 10 and ${INT__} < 100
run "interface Gi0/0/2.${INT__}"
run "encapsulation dot1Q 10${INT__}"
run "ip add 70.1.1.${IP} 255.255.255.252"
run "shut"
run "no shut"
END
IF    ${INT__} >= 100
run "interface Gi0/0/2.${INT__}"
run "encapsulation dot1Q 1${INT__}"
run "ip add 70.1.1.${IP} 255.255.255.252"
run "shut"
run "no shut"
END
${INT__}=    Evaluate    ${INT__} + 1
END
run "end"
#     # FOR    ${INT}    IN RANGE    256    260
#     #     run "interface Loopback76.${INT}"
#     #     ${INT__}=    Evaluate    ${INT} - 255
#     #     run "ip add 70.2.${INT__}.0 255.255.255.252"
#     #     run "shut"
#     #     run "no shut"
#     # END
#     run "end"
#     Sleep    5
#     run "sh ip int br"

SECTION TWO - STEP 3 : Remove 500 sub-interfaces on DUT and peer
continue on failure enabled
select device "dc1_gw1"
run "config t"
FOR    ${INT}    IN RANGE    1    64
run "no interface Gi1/1/1.${INT}"
END
run "end"
Sleep    5
run "sh int des | in Gi1/1/1."
select device "branch1_gw1"
run "config t"
FOR    ${INT}    IN RANGE    1    64
run "no interface Gi0/0/2.${INT}"
END
run "end"
Sleep    5
run "sh int des | in Gi0/0/2."

# SECTION TWO - STEP 4 :
# SECTION TWO - STEP 5 :

# FINAL SECTION - POST TEST
#   [Documentation]  This step is to Check CPU Util, Check CPU Process, Platform Resource
#     FOR    ${DUT}    IN     @{DUTS}
#       select device "${DUT}"
#       run "terminal length 0"
#       ${Clock}=    run "sh clock"
#       ${Time}=    Get Regexp Matches    ${Clock}    (\\d\\d:\\d\\d:\\d\\d)
#       ${Date}=    Get Regexp Matches    ${Clock}    (\\w\\w\\w|\\w\\w\\w\\w)\\s(\\d|\\d\\d)\\s\\d\\d\\d\\d
#       run "sh run" and save artifact as "${DUT}_Post_TC_running_config_${Time[0]}-${Date[0]}.txt"
#       Run Keyword And Ignore Error    run "show proc cpu sort"
#       Run Keyword And Ignore Error    run "show proc mem sort"
#       Run Keyword And Ignore Error    run "sh pl re"
#     END