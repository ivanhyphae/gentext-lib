---
asset_id: greenheart-report-2022
source_system: gdrive
source_id: 1p-Y-A7gC7LP0UvKMsUYpaf2Ia19-e4mI
source_title: "Greenheart_Report_20220328_final.pdf"
acquired: 2026-09-25
via: connector-text
tool: google-drive read_file_content (includeComments=false)
truncated: unknown
---

Microsoft Word - Greenheart\_Report\_20220328\_final 

DRG GREENHEART URBAN FORESTRY ANALYTICS March 28, 2022

Prepared For:

Davey Resource Group, Inc. Josh Behounek, Urban Forestry Market Manager 203 W. Plane St. Bethel, OH 45106

1100 NE Circle Blvd Suite 126 Corvallis, OR 97330

DRG GREENHEART URBAN FORESTRY ANALYTICS

TABLE OF CONTENTS

1.0 Introduction.............................................................................................................................. 1 2.0 Source Data ............................................................................................................................. 1 3.0 Methods .................................................................................................................................... 2 3.1 Tree Segmentation ........................................................................................................................... 3 3.2 Species Classification and Tree Biometrics ................................................................................. 3 4.0 Results ...................................................................................................................................... 5 4.1 Validation ........................................................................................................................................... 6

LIST OF TABLES

Table 1: Deliverable product projection information. ................................................................... 1 Table 2: Products delivered to DRG for the Greenheart site. ...................................................... 1 Table 3: Field data composition. ...................................................................................................... 2 Table 4: Formulas for vegetation indices used in the species and tree biometric models. ... 4 Table 5: Descriptive statistics for each tree biometric attribute in the Greenheart delivery. 5 Table 6: Data dictionary for the Greenheart tree polygon deliverables. .................................... 6 Table 7: Data dictionary for the Greenheart validation point deliverables ............................... 6 Table 8: Confusion matrix of species group classification comparing the predicted class to the reference (actual) class for tree polygons. Values represent percentages of the total number of reference polygons. ........................................................................................................ 7 Table 9: Accuracy statistics by species group. .............................................................................. 7 Table 10: Model evaluation results for the tree biometric models. ........................................... 7

LIST OF FIGURES

Figure 1: Distribution of field plots collected for the Greenheart area of interest. .................. 2 Figure 2: Tree mapping process overview. ..................................................................................... 3 Figure 3: Examples of a paired prediction and label image used to train the species group classifier. .............................................................................................................................................. 4 Figure 4: Map showing where reference canopies were interpolated to create complete coverage of the model training tiles. .............................................................................................. 4

DRG GREENHEART URBAN FORESTRY ANALYTICS NV5.COM/GEOSPATIAL | i

Figure 5: Map depicting the leaf area density predictions for a subset of the area of interest. ................................................................................................................................................ 5 Figure 6: Plot showing predicted vs. actual leaf biomass. .......................................................... 8 Figure 7: Plot showing predicted vs. actual leaf area density. .................................................... 8 Figure 8: Plot showing predicted vs. actual leaf area index. ....................................................... 9

DRG GREENHEART URBAN FORESTRY ANALYTICS NV5.COM/GEOSPATIAL | ii

1.0 INTRODUCTION

In 2019, NV5 Geospatial (previously Quantum Spatial, Inc.) was contracted by Davey Resource Group, Inc. (DRG) to collect Light Detection and Ranging (lidar) and digital imagery for an area of interest (AOI) in Louisville, Kentucky to facilitate an urban forest inventory and tree health assessment. This report represents the methods and results of individual tree delineation and tree biometric attribution. The goal of this analysis was to identify and attribute individual trees with species group classifications and tree biometrics such as biomass, leaf area density (LAD), and leaf area index (LAI) using lidar, imagery, and field data provided by DRG.

This report accompanies the delivered urban forest mapping products and documents contract specifications, processing methods, and analysis of the final dataset. Projection information for the Greenheart AOI is shown in Table 1 and a complete list of analytic deliverables provided to DRG is shown in Table 2.

Table 1: Deliverable product projection information.

Projections EPSG Horizontal Datum Units Kentucky North (ft US) 2246 NAD83 US Survey Feet

Table 2: Products delivered to DRG for the Greenheart site.

Product Type File Type Product Details

Vectors ESRI File Geodatabase (\*.gdb)

Individual tree polygons attributed with:

• Species Group

• Biomass

• Leaf Area Density

• Leaf Area Index Validation points

• Reference data points attributed with predicted and field measured data, used for result validation.

2.0 SOURCE DATA

The source data used in the forest mapping analysis for the Greenheart AOI includes ray traced digital 4 band imagery (red, green, blue, and near infrared) at a 12-inch resolution, lidar, and field data collected by DRG. The Greenheart field data contained geolocated tree stem locations and tree measurements detailing species, diameter at breast height, total height, canopy cover, tree condition, leaf area, leaf biomass, leaf area index, and basal area. The reference data composition is outlined in Table 3 and the spatial distribution of the Greenheart field data is shown in Figure 1.

Project/Report Number NV5.COM/GEOSPATIAL | 1

Table 3: Field data composition.

Species

Group Count Mean LAI SD LAI Mean

LAD SD LAD Mean

Biomass

SD Biomass Acer 81 4.35 1.45 5,088.80 3,662.02 65.18 46.37 Fraxinus 24 3.64 0.77 7,602.98 4,432.09 99.50 59.75 Other, Broadleaf 213 5.21 2.39 4,255.90 4,676.93 49.80 51.17 Other, Needleleaf 9 7.09 1.63 2,083.16 2,257.36 67.37 71.92 Picea 5 8.32 1.67 4,776.22 1,038.65 163.06 35.45 Quercus 162 3.47 1.25 3,853.63 4,527.17 70.50 83.86

Figure 1: Distribution of field plots collected for the Greenheart area of interest.

3.0 METHODS

The urban tree mapping products that make up the analytical component of this project were generated through five separate deep learning efforts: tree segmentation, species classification, leaf biomass, leaf area density (LAD), and leaf area index (LAI) prediction. Individual convolutional deep learning classifiers were trained to predict each tree attribute of interest in the analysis. To prepare the lidar and imagery for modeling, a suite of spectral and structural metrics were derived from both

Project/Report Number NV5.COM/GEOSPATIAL | 2

datasets to use as training inputs for the deep learning processes. An overview of the analytical process is shown in Figure 2.

Figure 2: Tree mapping process overview.

3.1 TREE SEGMENTATION

The first component of the tree mapping procedure is individual tree segmentation. In this process tree canopies are detected and delineated using a deep learning approach. The tree segmentation model is trained on spectral and structural information from imagery and lidar as well as manually digitized tree polygons created by trained photo interpreters. Once individual tree centers and canopy extents have been predicted, trees are iteratively ‘grown’ and allowed to spatially compete with each other using a cellular automata process. This gives them a natural look and complete spatial coverage of the tree canopied portions of the AOI. For dispersed trees, this corresponds to an individual tree crown, however within densely forested areas it will generally capture the dominant and co-dominant tree crowns with some segments representing multiple trees. Regions of dense canopy which were not well represented in the field data, were assigned a ‘1’ in the “MULTI” field of the deliverable geodatabase.

3.2 SPECIES CLASSIFICATION AND TREE BIOMETRICS

Deep learning classifiers are trained using raster datasets composed of prediction images and label images. Once tree segments were finalized, image-based training datasets were created to represent species group, biomass, LAD, and LAI attribution. Figure 3 shows an example of a prediction image and a label image used to train the species group classifier. Due to the spatial extent and pattern of the reference data collected in the field (shown in Figure 1), additional tree canopies were labeled using interpolation to complete 128 x 128 pixel training tiles. Figure 4 shows an example of how the reference data were augmented to provide complete data coverage. Four individual models were developed to predict a tree’s species group, biomass, LAD, and LAI using training datasets for each response variable. Vegetation indices such as normalized difference vegetation index (NDVI), absolute difference index (ZABUD), and imagery texture metrics from canny edge detection were used to train the species and biometric classifiers. Structural metrics derived from the lidar point cloud were also used to train each model. Equations for each spectral index can be found in Table 4.

Project/Report Number NV5.COM/GEOSPATIAL | 3

Figure 3: Examples of a paired prediction and label image used to train the species group classifier.

Figure 4: Map showing where reference canopies were interpolated to create complete coverage of the model training tiles.

Table 4: Formulas for vegetation indices used in the species and tree biometric models.

Index Acronym Formula Normalized difference vegetation index NDVI (NIR-R) / (NIR + R) Absolute difference index ZABUD (10 + (R–NIR)2 + (G–R)2 + (B–G)2 + (NIR –

(R+G+B)/3)2 )0.1

Project/Report Number NV5.COM/GEOSPATIAL | 4

Once model training was complete, the models were applied across the full area of interest. To attribute tree polygons with the predicted results, raster outputs were summarized to each tree polygon. Figure 5 shows an example of the results for leaf area density.

Figure 5: Map depicting the leaf area density predictions for a subset of the area of interest.

4.0 RESULTS

Canopied areas of the Greenheart AOI were delineated into over 100,000 individual tree polygons. Each tree polygon was attributed with its predicted species and tree biometrics. Table 5 contains a summary of the Greenheart tree biometric results. Table 6 and Table 7 contain data dictionaries for the delivered feature classes.

Table 5: Descriptive statistics for each tree biometric attribute in the Greenheart delivery.

Descriptive

Statistic Leaf Area Density Leaf Biomass Leaf Area Index Minimum 131.4 2.64 1.70 1st Quartile 2,494.6 26.32 4.25 Median 3,329.8 46.54 4.74 Mean 4,379.9 60.00 4.86 3rd Quartile 5,183.6 78.30 5.39 Max 37,547.3 923.93 11.77

Project/Report Number NV5.COM/GEOSPATIAL | 5

Table 6: Data dictionary for the Greenheart tree polygon deliverables. Field Name Description Unit OBJECTID Shape identification, unique to each feature in dataset - LEAF\_BIOMASS Numerical value of Leaf Biomass US Pounds LEAF\_AREA Numerical value of leaf area US Feet

Squared LAI Numerical index value of leaf to ground area - GROUP\_ Simplified groupings of tree species into the following

categories -

MULTI

Denotes features that make up dense canopy cover where individual tree canopies are not distinguishable from the stand

\-

D0 Numerical value of tree species grouping - D1-10 Preserved diagnostic classification values - SHAPE\_Length Shape length of feature US Feet SHAPE\_Area Shape Area of feature US Feet

Squared

Table 7: Data dictionary for the Greenheart validation point deliverables Field Name Description Unit BIOMASS\_P Numerical value of Leaf Biomass US Pounds LEAF\_AR\_P Numerical value of leaf area US Feet

Squared LAI\_P Numerical index value of leaf to ground area - BIOMASS\_A Simplified groupings of tree species into the following

categories US Pounds

LEAF\_AR\_A

Denotes features that make up dense canopy cover where individual tree canopies are not distinguishable from the stand

US Feet Squared

LAI\_A Numerical value of tree species grouping -

4.1 VALIDATION

Species and tree biometric predictions were validated using a subset of reference data that were withheld from the model training exercise. Overall classification accuracy of the species model was 78.77% with a confidence interval of 71.24-85.09% and a kappa statistic of 0.6962. Classification accuracy was evaluated using a confusion matrix of predicted values compared to actual values. The confusion matrix for the species classification is shown in Table 8 and the accuracy statistics by class are shown in Table 9. The root mean square error (RMSE), mean absolute error (MAE), and R2 of tree biometric predictions are detailed in Table 10. Plots showing predicted vs. actual measurements for tree biometrics are shown in Figure 6, Figure 7, and Figure 8.

Project/Report Number NV5.COM/GEOSPATIAL | 6

Table 8: Confusion matrix of species group classification comparing the predicted class to the reference (actual) class for tree polygons. Values represent percentages of the total number of reference polygons.

Prediction Acer Fraxinus Broadleaf

Other,

Other, Needleleaf Picea Quercus

Acer 12.33 0 0.68 1.37 0 0.68

Fraxinus 0 3.42 0.68 0 0 0

Other, Broadleaf 0 0.68 40.41 2.05 0 0.68

Other, Needleleaf 0.68 0 0.68 2.05 0 0

Picea 0 0 0 1.37 0 0

Quercus 0 0.68 4.11 6.85 0 20.55

Table 9: Accuracy statistics by species group.

Species

Class Sensitivity Specificity

Positive Predictive Value

Negative Predictive Value

F1 Prevalence Detection

Rate

Balanced Accuracy

Acer 94.74 96.85 81.82 99.19 87.8 13.01 12.33 95.79

Fraxinus 71.43 99.28 83.33 98.57 76.92 4.79 3.42 85.35

Other, Broadleaf 86.76 93.59 92.19 89.02 89.39 46.58 40.41 90.18

Other, Needleleaf 15 98.41 60 87.94 24 13.7 2.05 56.71

Picea NA 98.63 NA NA NA 0 0 NA

Quercus 93.75 85.09 63.83 97.98 75.95 21.92 20.55 89.42

Table 10: Model evaluation results for the tree biometric models.

Evaluation

Metric Leaf Area Density Leaf Biomass Leaf Area Index RMSE 2,489.026 39.90419 1.811527 MAE 1,730.391 22.41506 1.323273 R2 0.6506318 0.5744764 0.2160403

Project/Report Number NV5.COM/GEOSPATIAL | 7

Figure 6: Plot showing predicted vs. actual leaf biomass.

Figure 7: Plot showing predicted vs. actual leaf area density.

Project/Report Number NV5.COM/GEOSPATIAL | 8

Figure 8: Plot showing predicted vs. actual leaf area index.

5.0 CONCLUSION

Models had varying performance with species, leaf area, and leaf biomass outperforming leaf area index. This is believed to be due to the complex 3-dimensional nature of leaf area index combined with limited field data from which to model the relationship. The combination of lidar based structure and coregistered 4-Band imagery yielded very good performance on the species classification comparable to results typically achieved with hyperspectral imagery. Through further efforts to refine these modeling approaches with additional field data we are optimistic that these technologies can be of great value to DRG’s urban forestry program. NV5G considers these results very promising and appreciates the opportunity to support DRG in this mapping effort.

Project/Report Number NV5.COM/GEOSPATIAL | 9