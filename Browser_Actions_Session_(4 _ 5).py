"""
Session 4 - Xpath (Basics)
    * Syntax                                        ----example---> 
    * Absolute and Relative                         ----example---> 
    * Attributes(id, name, value, text, class,...)  ----example---> //* [@id = 'fname' )] |-------| //* [text () = ' Option 1']
    * or                                            ----example---> //* [@name='moption' or @value='Option 1']
    * and                                           ----example---> //* [@id='moption' and @name='option1']
    * and/or                                        ----example---> //* [(@name='option1' or @value='Option 1') and @type ='checkbox']
    * Parent                                        ----example---> 
    * Child                                         ----example---> 
    * Parent & Child                                ----example--->
    * Index                                         ----example---> //*[@id='moption'][3] |-------| (//*[text()='Option 1'])[2]
    * Element as attribute                          ----example---> //tr [ // td [ text() = 'Actor']] |--------| //tr [ // td [ text() = 'Actor']][2]
                                                                    //tbody//tr[3]
Session 5
Web sites for training web automation

Xpath (Functions) :         
    * contains()             ----example---> //*[ contains( @id, 'lna' )]
    * text()                 ----example---> //*[ contains( text(), 'layout two' )]
    * starts-with()          ----example---> //*[ starts-with(@id, 'lna') ] |-------| //*[ starts-with(@class, 'fak') ]
    * position()             ----example---> //tbody//tr[ position()=2]
    * last()                 ----example---> //tbody//tr[ last()] |-------| //tbody//tr[ last()]/td[1] |-------| //tbody//tr[ last() - 1]
    * count()                ----example---> //tbody [count( .//tr) = 7] |-------| 
    * normalize-space()      ----example---> //*[normalize-space (text()) ='Option 1']
    * translate()            ----example---> //* [translate (@value, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz") = 'option 1']
    * normalize-space() & translate()       ----example---> //* [normalize-space (translate (@value, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")) = 'option 1']
    * string-length()        ----example---> //*[string-length ( @id ) = 4]
    * round()                ----example---> //*[round (text()) = '27']
    * floor()                ----example---> //*[floor (text()) = '28']
    * not()                  ----example---> //*[@type ='radio' and not (@id ='male')]
    * substring-before()     ----example---> //*[substring-before (text(), ':') = 'Username']
    * substring-after()      ----example---> //*[substring-after ( text(), ':' ) = 'test ' ]

https://trytestingthis.netlify.app/

"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://trytestingthis.netlify.app/')
sleep(2)
driver.find_element('xpath', "//* [@name='moption' or @value='Option 1']").click()
sleep(20)


driver.quit()