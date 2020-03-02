:: windows use \r\n for new line char while linux use \n  
:: when download sh file windows automatically convert \n -> \r\n 
:: To run scripts in linux environment, the must doing is convert all  \r\n -> n
:: first step download dos2unix
:: step 2 run: dir  /s /b *.sh
:: step 3 use note pad to add dos2unix to list directories