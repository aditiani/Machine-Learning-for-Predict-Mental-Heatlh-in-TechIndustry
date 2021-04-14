# Machine-Learning-for-Predict-Mental-Heatlh-in-Tech-Industry
Contains with Dashboard using Flask for Machine Learning Prediction

This is a final project to fulfill the final test in Purwadhika using data from Kaggle (https://www.kaggle.com/osmi/mental-health-in-tech-survey). 

**Open Sourcing Mental Illness is a non-profit, corporation dedicated to raising awareness, educating, and providing resources to support mental wellness in the tech and open source communities. OSMI began in 2013, with Ed Finkler speaking at tech conferences about his personal experiences as a web developer and open source advocate with a mental health disorder. The response was overwhelming, and thus OSMI was born.**
- Every year, OSMI came out with a new survey to see how employees want to get mental health treatment in tech companies around the world and I pick the survey from 2014.
- This survey is filled by respondents who suffer from mental health disorders (diagnose or un-diagnosed by medical, even it's just a feeling) in tech companies and see if any factors can affect the employee to get treatment or not.
- From this research, this machine learning can help HR to see what factors have the company needs to support so the employee wants to get mental health treatment.

###  Conclusion Based on EDA

Nearly 86% of employees report improved work performance and lower rates of absenteeism after receiving treatment for depression, according to an April 2018 article in the Journal of Occupational and Environmental Medicine. This means big gains in retention and productivity for employers. By providing employees access to mental health benefits, the company can begin to create a culture of understanding and compassion at the tech company. And having employees who feel cared for and happy isn’t just good, it’s good business.

#### Based on profiling the respondents
* Companies must know that gender and family history greatly influence the decision to get treatment for employees. So if the company wants to provide more support, the company must make an assessment of the employee's personality because different characters can determine different needs. Age can also be a trigger, considering that most of them are young so there is a high chance that they will be open-minded to get treatment.

#### Based on the work environment of respondents
* Work interference is the most influential of employees who want to get treatment. This means the company should consider providing facilities to anticipate job stress on employees. Some of the companies decide to make a private room or silent room in case employees suddenly feel stress and need a private moment to relieve.

#### Based on the mental health facilities of respondents
* The company needs to provide a good benefit for employees so they can maintain their mental health. If the company can don't have resources for it, there are so many third parties who can be hired to maintain a wellness program for the company. Building trust like keep private about whom employee that gets treatment also can also give a trigger for employee want to get treatment.


###  Modelling

*Define Target Data*

<img width="857" alt="Screen Shot 2021-04-13 at 13 46 34" src="https://user-images.githubusercontent.com/68433894/114510571-05eb4e80-9c61-11eb-8cc6-186d2ca6e6e8.png">
<img width="855" alt="Screen Shot 2021-04-13 at 13 46 55" src="https://user-images.githubusercontent.com/68433894/114510594-0a176c00-9c61-11eb-992b-8c8bf85f324b.png">

*Define Model*

<img width="855" alt="Screen Shot 2021-04-13 at 13 47 17" src="https://user-images.githubusercontent.com/68433894/114510642-1a2f4b80-9c61-11eb-92c7-a09a07fafbd6.png">

*Cross Validation Process & Model Evaluation*
<img width="855" alt="Screen Shot 2021-04-13 at 13 47 37" src="https://user-images.githubusercontent.com/68433894/114510700-2c10ee80-9c61-11eb-9bb4-03acd016754f.png">

*Hyperparameter Tuning Using Logistic Regression*
<img width="855" alt="Screen Shot 2021-04-13 at 13 47 51" src="https://user-images.githubusercontent.com/68433894/114510835-5367bb80-9c61-11eb-8193-1be6f5dbe878.png">

*Comparison Score Between Logistic Regression Before Tuning & After Tuning*
<img width="855" alt="Screen Shot 2021-04-13 at 13 48 06" src="https://user-images.githubusercontent.com/68433894/114510890-68dce580-9c61-11eb-91d2-6457dd2e436b.png">

*Feature Selection Using Cofficient Score*
<img width="855" alt="Screen Shot 2021-04-13 at 13 48 30" src="https://user-images.githubusercontent.com/68433894/114510934-772b0180-9c61-11eb-87f4-a3a312c258f4.png">

*Model Evaluation After Feature Selection*
<img width="855" alt="Screen Shot 2021-04-13 at 13 48 47" src="https://user-images.githubusercontent.com/68433894/114510980-87db7780-9c61-11eb-8daa-da0a2330342f.png">

###  DashBoard & Prediction

*Home Page*
<img width="1280" alt="Screen Shot 2021-04-13 at 14 09 10" src="https://user-images.githubusercontent.com/68433894/114511857-a5f5a780-9c62-11eb-86ac-8c1301a3d7b5.png">

*Profile Section*
<img width="1280" alt="Screen Shot 2021-04-13 at 14 09 16" src="https://user-images.githubusercontent.com/68433894/114511908-b443c380-9c62-11eb-966f-e0d8ef4c9835.png">

*About Section*
<img width="1280" alt="Screen Shot 2021-04-13 at 14 11 08" src="https://user-images.githubusercontent.com/68433894/114512298-2ae0c100-9c63-11eb-8f38-a3745e757e75.png">

*Visualization Section*
<img width="1280" alt="Screen Shot 2021-04-13 at 14 11 16" src="https://user-images.githubusercontent.com/68433894/114512347-36cc8300-9c63-11eb-8182-1bd169ce8efa.png">
<img width="1280" alt="Screen Shot 2021-04-13 at 14 11 24" src="https://user-images.githubusercontent.com/68433894/114512360-3af8a080-9c63-11eb-9b3d-dcbfe4fd08fd.png">
<img width="1280" alt="Screen Shot 2021-04-13 at 14 11 46" src="https://user-images.githubusercontent.com/68433894/114512364-3df39100-9c63-11eb-8da4-06cad32e0a5b.png">
<img width="1280" alt="Screen Shot 2021-04-13 at 14 11 53" src="https://user-images.githubusercontent.com/68433894/114512372-40ee8180-9c63-11eb-9455-90447ded7dda.png">
<img width="1280" alt="Screen Shot 2021-04-13 at 14 12 03" src="https://user-images.githubusercontent.com/68433894/114512387-451a9f00-9c63-11eb-8215-cd51323dbe23.png">
<img width="1280" alt="Screen Shot 2021-04-13 at 14 12 18" src="https://user-images.githubusercontent.com/68433894/114512399-48158f80-9c63-11eb-8d63-1c1c9703ee91.png">

*Conclusion Section*
<img width="1280" alt="Screen Shot 2021-04-13 at 14 12 34" src="https://user-images.githubusercontent.com/68433894/114512434-4fd53400-9c63-11eb-975e-2a3b27a7aba5.png">

*Dataset Section*
<img width="1280" alt="Screen Shot 2021-04-13 at 14 12 54" src="https://user-images.githubusercontent.com/68433894/114512476-58c60580-9c63-11eb-8a48-e571a22319a7.png">

*Prediction Section*
<img width="1280" alt="Screen Shot 2021-04-13 at 14 14 09" src="https://user-images.githubusercontent.com/68433894/114512505-624f6d80-9c63-11eb-9b6b-4f2a833ed653.png">

*Result Section*
<img width="1280" alt="Screen Shot 2021-04-13 at 14 14 31" src="https://user-images.githubusercontent.com/68433894/114512539-6c716c00-9c63-11eb-9d32-90af7a3e57ba.png">

Thank You!
