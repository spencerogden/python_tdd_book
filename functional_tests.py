from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. 
# Sho goes to check out its homepage
browser.get('http://localhost:8000')

#She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She types in "Buy peacock feathers" into the text box

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item on the list

# There is still a text box inviting her to add another item
# She enters "Use peacock feathers to make af l"

# The page updates again, and now shows both itmes

# Edith wonders whether the site will remmeber her list.
# Then she sees that the site has generated a unique URL for her
# there is some explanatory text to that effect

# She visists that URL - her list is still there

# She goes back to sleep

browser.quit()



