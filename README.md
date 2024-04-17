1) Use any open-source API to access some data in Jason format and then parse the Jason data and
display it as some kind of dashboard (20 points).
a. When consuming APIs with Python, you may use python library: requests. With it, you
should be able to do most, if not all, of the actions required to consume any public API (for
example open weather API or Random User Generator API, or traffic API etc.) below are
some examples of the real-time APIs:
i. Amazon Price
ii. Fixer Currency
iii. TheRunDown
iv. OpenAPI 1.2
v. Zillow
vi. Sportspage Feeds
vii. Nexmo Number Insight
viii. Google Shopping
b. To display the data you may use python library Dash or some other library.



Data link for question 2: https://app.box.com/s/7qv44umhw0vnzgmoe9krfkfkv5kf2atv
2) The data file diabetes.csv contains data of 768 patients. In this data there are 8 attributes
(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, and Age)
and 1 response variable (Outcome). The response variable, Outcome, has binary value (1 indicating the
outcome is diabetes and 0 means no diabetes). For this assignment purposes we will consider this data
as a population. Use this data to perform the following:
a) set a seed (to ensure work reproducibility) and take a random sample of 25 observations and
find the mean Glucose and highest Glucose values of this sample and compare these statistics
with the population statistics of the same variable. You should use charts for this comparison.
(5 points)
b) Find the 98th percentile of BMI of your sample and the population and compare the results
using charts. (5 points)
c) Using bootstrap (replace= True), create 500 samples (of 150 observation each) from the
population and find the average mean, standard deviation and percentile for BloodPressure and
compare this with these statistics from the population for the same variable. Again, you should
create charts for this comparison. Report on your findings. (10 points)
