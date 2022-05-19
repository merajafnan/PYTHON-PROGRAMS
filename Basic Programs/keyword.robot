*** Keywords ***
CONNECT TO DEVICES
  [Documentation]  This keyword is to initilize the devices
  FOR    ${item}    IN    @{Dut}
        connect to device "${item}"
  END