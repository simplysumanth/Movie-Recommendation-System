# Movie Recommendation System

## &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/simplysumanth/apple_leaf_disease_classifier/main/app.py) 
Dataset: <a href = "https://www.kaggle.com/c/plant-pathology-2020-fgvc7/data"> Plant Pathology dataset </a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Built using : &nbsp; ![image](https://user-images.githubusercontent.com/26655188/143618035-3efecc7a-92e5-4548-a566-94de785454c3.png) &nbsp; &nbsp; ![image](https://user-images.githubusercontent.com/26655188/143617981-be944849-80e3-4440-93c7-1df0e5dc2cae.png)

## Demo:
![image](https://user-images.githubusercontent.com/26655188/155879073-b07d89a4-fcd5-4503-a3dc-ea67064f66a2.png)


## Project Aim:
Given a photo of an apple leaf, accurately assess its health. The aim is to distinguish between leaves which are healthy, those which are infected with apple rust, those that have apple scab, and those with more than one disease(combinations).

## Data Description
* train.csv
  * image_id: The image path/Name
  * combinations: one of the target labels
  * healthy: one of the target labels
  * rust: one of the target labels
  * scab: one of the target labels
* Images : A folder containing the train and test images, in jpg format.

## Motivation
Misdiagnosis of the many diseases impacting agricultural crops can lead to misuse of chemicals leading to the emergence of resistant pathogen strains, increased input costs, and more outbreaks with significant economic loss and environmental impacts. Current disease diagnosis based on human scouting is time-consuming and expensive, and although computer-vision based models have the promise to increase efficiency, the great variance in symptoms due to age of infected tissues, genetic variations, and light conditions within trees decreases the accuracy of detection.

## Project Structure
<table border="0">
 <tr>
    <th scope="col">
      <img src = "https://user-images.githubusercontent.com/26655188/143619050-5c0ba744-1bb5-4623-b9df-6fb28dc1942e.png"/>
    </th>
    <td>
      <ul>
        <li>Images : Has sample leaf images (the ones which are not used for training)</li>
        <li>Model :Has the xresnet50 model pickle file trained on images. </li>
        <li>Notebook : Has model_training and inference notebook </li>
      <li>app.py : it is the streamlit app </li>
        <li>requirements.txt : has the necessary packages needed to reproduce the app.</li>
      </ul>
   </td>
  </tr>
</table>

## Model Performance
**Core Architecture :** Resnet50\
**Metric :** Average of the individual ROC_AUC Score of each predicted column.\

### Learning Rate Finder:
<img src = 'https://www.kaggleusercontent.com/kf/80082306/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..LyMZvL_fOX54b6Ywn7LKIQ.7JW37mD7ICssXzu9kSATmnnH6UHUpohfUYfDL2jb-UtuT2hONotW9Nz9eHc_Bg45PRC9Mgdga7UiYZRt6lNQKfhakhElXuSaSR3gFojFrFqBOHBj7Mnu0wa2G2LMEQ1vEYTPWdif3XXxcW6TGu5ANYbT9i3wEMQ8c35qkZpLv_LNvWBzfNhemXS7jwogrVxcAu_wS0SwYbjombffnwktYz9UdiCw7ODTdr75VD36Qsj0j1GMB_RdhBuFfjqDVXZfQkSW00mbPlw7JkMTyAbcWgg8b1rRCVgAABMi_VgqtAXtQ2rhTn9KJGJDJcATlue0U046qqK-3Wzfl4JAfXzeqqAm9U0zuBsnjX76pCiYR8rDg_QEXZAtSVkzbq-802YIRVyJX5kr9AcmC_X8rUnbttOXwSsB_SRg4Q4PQEa7GEzVGkXmxUBhYJ4Zi0pIsT9WTlNGw2sZ0xTmqhawdOtic6BBu8z_9lsyK9_Xyx8V1GsaGz6e8_6q8OV27mRn6CPcjYjygUv6I2kwdPGyITAdWq4qqcGGoSmNvEHkvF-dtmpRruPFyOrcvc-sNWNWX-gdhABGNG4omwT5eIroPg_JRlGs4vWInz5rAwFDqmXn9RbcTIhRxSJR67ZZxD8Mw6pu5JYsCW5p4lR-HYF1rFgp0RCxEQA3zeb1lwXrbBYZ_gE.6lAs4-_BfhAgrlYbd52Ltw/__results___files/__results___24_2.png'>

### Training:
![image](https://user-images.githubusercontent.com/26655188/143623846-48a4c55f-abe3-4fbf-9fc8-7f811554bbdf.png)

### Outcome:
The model has average ROC_AUC Score of ~ 0.94



