from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.trex-game.skipser.com/')
browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)

#infinite loop, the bot will play forever
while(1):
	#we can return any variable that we can access the scope of
	#If you press F12, and pause the app, you can see all the variables
	#The obstacles that can kill your dinosaur are stored in an obstacles array
	#The basic idea: wait until the obstacles get within 100 feet, then jump
    closestObstacle = browser.execute_script("return Runner.instance_.horizon.obstacles[0]")
    

    if closestObstacle != None:
		#closestObstacle has an "xPos" and a "yPos", these variables determine how close it is to you (height and width)
        closestX = closestObstacle.get("xPos")
        closestY = closestObstacle.get("yPos")
 
		#this is the current speed of the game (it slowly speeds up, you must jump sooner then)
        speed = browser.execute_script("return Runner.instance_.currentSpeed")

        if speed != None:
        
            if speed <= 7.5:
               if closestX <= 100:
                    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
                    
            elif speed > 7.5:

                if closestX <= 110 and closestY > 50:
                    browser.find_element_by_tag_name('body').send_keys(Keys.SPACE)
                    
                if closestX <= 110 and closestY <= 50:
                    browser.find_element_by_tag_name('body').send_keys(Keys.DOWN)
