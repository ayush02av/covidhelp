# covidhelp
[Link to the Project website](https://covidhelp.pythonanywhere.com "CovidHelp")

E-Yantra hackathon submission
# Discription
COVID-19 pandemic has brought upon us unforeseeable challenges and one of them being  scarcity of resources. The main objective behind developing this website was to provide a one stop destination for COVID related information and sources. Our website has 3 main features like as blog, vaccination, resource lead. 

We identified that a lot of people are facing issues in finding legitimate verified leads for medicines, hospital beds, oxygen etc which is required for treatment. Our website has an exhaustive database of leads which are personally verified by our team, it also enables the users to submit leads which will be verified before being added to our database. 

We also understand that currently there is a difference in the demand and supply of vaccination in our country due to which it is difficult to easily find the nearest vaccination centre and book slot. In order to tackle this issue we have developed a feature which will allow the user to find their nearest available vaccination centre by simply entering their area pin code. The website will redirect the user to COWIN website to book the slot for vaccination. 

This is an unprecedented crisis and their is a need for authentic information regarding COVID and its treatment, in order to bridge this gap and provide the users with authentic information regarding COVID we regularly update and post blogs relating to the treatment, tips and guidance for COVID. 

# Software Used

1. Frontend
- HTML (layout)
- CSS (design)
- JS DOM (element manipulation and data insertion)
- Jquery (API call)

2. Backend
- Django, Python (For managing url management, template and css rendering, database connectivity)
- SQLITE3 (Database used)

# Process Flow
Our database (sqlite3) mainly consists of 4 tables, and they're as following:
1. Blog articles
2. Cases
3. Non verified Leads
4. Verified Leads

- Cases
One Case record consists of 
1. total number of COVID positive patients in the nation that have been reported
2. total active cases of COVID in the nation
3. total number of deaths reported due to COVID
4. total number of patients that recovered from COVID
till date.

The cases are updated on daily basis, and the difference of cases to analyse the situation is counted by directly finding the difference in the respective fields.
We chose this approach instead of making new fields for difference in cases, to save storage, without compromising memory at run-time much.

- Verified Leads

One Verified Lead consists of personally verified resource (oxygen cylinders, ambulance services, plasma donors/arrangers etc) that are dispayed directly in the homepage table.

- Non-Verified Leads

This contains all the leads that are posted by the viewers who have sources of those who can help in providing resources for the cause.
We aim to verify each lead personally, before converting it into a verified lead, so that those who need it, get legit leads only.

- Blog Articles

These are the articles that we share on our blog, to help people get information about how to prevent covid, and tips for vaccination etc.

- Vaccination Slots

Although not a table in our database, but it is a vital part of the website.
Viewers can check available vaccine slots by filling up their pincode and date, and using cowin api, the available respective vaccine slots are displayed in the vaccine table
