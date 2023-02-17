"""
Session 6 - Xpath(Axes)
* parent                ------> //*[@id='uname']/.. , //*[@id='uname']/parent::[@class='login form'] , //*[@id='uname']/parent::div , //*[@id='uname']/parent::* , 
* ancestor              ------> //td[text()='Singer']/ancestor::* , //td[text()='Singer']/ancestor::table , //td[text()='Singer']/ancestor::tr , //td[text()='Singer']/ancestor::table[@style='width:100%'] , //td[text()='Singer']/../..
* ancestor-or-self      ------> //*[@name='pwd']/ancestor-or-self::*[@id='pwd']
* child                 ------> //tbody/tr[3]/child::*[text()='Singer'] , //*/child::*[text()='Singer'] , //tbody/tr[3]/td[5]
* descendent            ------> //table/descendant::*[text()='Singer'] , //table//*[text()='Singer']
* descendent-or-self
* following             ------> //select[@id='option']/following::*[@value='option 1']
* following-sibling     ------> //*[@id='abcd123']/following-sibling::*[@value='option 2']
* preceding             ------> //select[@id='optonx']/preceding::*[@value='option 2']
* preceding-sibling     ------> //*[@id='abcd123']/preceding-sibling::*[@value='option 2']

https://trytestingthis.netlify.app/

"""