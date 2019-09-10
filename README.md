# group1_austin_animal_shelter
Austin Animal Center shelter intakes and outtakes

Analysis of  what type of breeds are coming into the shelter and how long do they stay. What breeds are getting adopted and where animals are found around the city of Austin. The data will be coming from a Kaggle dataset found here: 

https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes


# Austin Animal Center
Austin, Texas is the largest No Kill community in the nation, and home to the Austin Animal Center. We provide shelter to more than 16,000 animals each year and animal protection and pet resource services to all of Austin and Travis County.

The Austin Animal Center is an open-intake facility where lost and surrendered animals from all of Travis County in need of shelter are accepted regardless of age, health, species or breed. The goal of the Austin Animal Center is to place all adoptable animals in forever homes.




#Intakes 

Column Name	Description	Type

* Animal ID	 Plain	Text
* Name	Plain Text
* DateTime	Date & Time
* MonthYear	Date & Time
* Found Location	Plain Text
* Intake Type	Plain Text
* Intake Condition	Plain Text
* Animal Type	Plain Text
* Sex upon Intake	Plain Text
* Age upon Intake	Plain Text
* Breed	Plain Text
* Color	Plain Text


1. Total # of Intakes by Breed and Animal Type
2. Total # of Intakes by MonthYear
3. Total # of Intakes by Location (Zip?)
4. Total # of Intakes by Sex
5. Total # of Intakes by Age


# Outcomes
Column Name	Description	Type

* Animal ID	Plain Text
* Name		Plain Text
* DateTime	Date & Time
* MonthYear	Date & Time
* Date of Birth	Date & Time
* Outcome Type	Plain Text
* Outcome Subtype	Plain Text
* Animal Type		Plain Text
* Sex upon Outcome	Plain Text
* Age upon Outcome	Plain Text
* Breed	Plain Text
* Color	Plain Text

1. Total # of Outcomes by Breed and Animal Type
2. Total # of Outcomes by MonthYear
3. Total # of Outcomes by Location (Zip?)
4. Total # of Outcomes by Sex
5. Total # of Outcomes by Age



questions:
1. largest no kill community
2. accept animals regardless of age, health, species or breed. 
3. The goal of the Austin Animal Center is to place all adoptable animals in forever homes.


1. cleanup data
 * combine breed types into bigger categories
 * combine outcome type and group them
 * Animal age / breed into bins...

 2. Charts
 * bar charts breed group by intake and outcome
 * bar charts age group by intake and outcome
 * average length of stay by breed
 * average length of stay by age
 * outcome type by breed
 * outcome type by age
 * scatter plot of age vs length of stay
 * google map of intake location

