

# In[149]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


# In[150]:





# In[157]:


from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://sse.umkc.edu/about-us/computer-science-and-information-technologydirectory.html#'
driver.get(url)
while True:
    soup_obj = BeautifulSoup(driver.page_source, 'html5lib')
    driver.quit()
    break
  


# In[158]:


lst = soup_obj.find_all('a', class_="sd-nav-text-umkc-blue ng-binding") #collect indiviudal links of each faculty

#print(lst)

file_path_faculty_links='C:/Users/HP/Downloads/bio_links.txt'
hlink = []

for tag in lst:
    hlink.append(tag.get('href').replace('..','https://sse.umkc.edu/'))
    #file.write(tag.text + '\n')


print(hlink[1])
for i in range(len(hlink)):
    print(hlink[i])


# In[159]:f


names = []
titles = []
depts = []
abouts = []
interests = []

print (hlink[1])
for link in hlink:
    page = requests.get(link)
    soupobj1 = BeautifulSoup(page.text, 'html.parser')
    name = soupobj1.find('h2', class_="text-white text-umkc-40px bg-umkc-dark-blue p-3" ).text.strip().replace('\n',' ')
    title = soupobj1.find('div', class_="h3 text-umkc-24px text-umkc-dark-gray mt-3" ).text.strip().replace('\n',' ')
    dept = soupobj1.find('div', class_="h3 text-umkc-16px" ).text.strip().replace('\n',' ')
    about = soupobj1.find('h3', class_="text-umkc-dark-blue").text.strip().replace('\n',' ')
    names.append(name)
    titles.append(title)
    depts.append(dept)
    abouts.append(about)
    intrst =soupobj1.find("span", class_="small" )
    if intrst:
        intrst = intrst.text.strip().replace('\n',' ')
    else:
        intrst = soupobj1.find("div", class_="sptp-content" )
        if intrst:
            intrst = intrst.text.strip().replace('\n',' ')
        else:
            intrst ='Not available'
    interests.append(intrst)
    
print(names)
print("hello")


# In[160]:


dataframe = pd.DataFrame({'Names':names, 'Titles': titles, 'Department': depts, 'Bio': hlink, 'Courses': interests})


# In[161]:


print(dataframe)
