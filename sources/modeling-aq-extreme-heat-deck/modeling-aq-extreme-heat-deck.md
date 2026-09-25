---
asset_id: modeling-aq-extreme-heat-deck
source_system: gdrive
source_id: 1fcFcxMSzMIZFH3RwQceSEV_mC2hZNJ5qYS9rgamzvs4
source_title: "Modeling for AQ and Extreme Heat"
acquired: 2026-09-25
via: connector-text
tool: google-drive read_file_content (includeComments=true)
truncated: unknown
---

We’re building a technology platform to empower communities impacted by environmental injustice and climate change to take control and determine their own future, a new approach to community-led, evidence-based urban revitalization. What previously required teams of engineers, epidemiologists, academics, government agencies and consultants can now be done by and for communities, themselves, creating resilience, while re-localizing power, knowledge and capital in the communities.ADAPT FRAMEWORKModel PollutionModel SolutionsDesignBuild InterventionsPrescott Greening: Adapt CycleMonitor ResultsWest Oakland - Prescott Neighborhood# digital twin: south prescottThis model is used to create a baseline for air quality at the 7th St. underpass7th St.7th St.FrontageBART880We model the existing environment to allow for optimizing solutions before spending on infrastructureThis preliminary result shows 7th St. acting as a channel holding particulates.BASELINE MODELExisting treelineINTERVENTIONDIFFERENCEz = 5m (~16ft)Leaf Area DensityTree shape and foliage density determine health benefits The 3 dimensions of foliage distribution can have an impact on environmental benefits of tree plantings. In the diagram above on the left we see the air pollution benefits of a high leaf area density conical tree that reaches ground level, but has a lower canopy area and NDVI per square foot than the lollipop tree on the right, which actually makes air pollution worse! Leaf area density (LAD) is the leaf surface are per unit of volume. It provides a more 3-dimensional metric of plant surface area than LAI, which relates to air pollution mitigating capacity of the trees.Height
At least 4 meters of height will prevent downwind spreadPorosity
High porosity leads to pollution stagnation,
low porosity is similar to a wallThickness
5-10 meters recommended, but effectiveness impacted by porosity of barrierBarrier Length
Extend at least 50 meters past area of concern to limit downwind concentrationsCoverage 
No gaps between or below trees is ideal. Bushes can be used to block low gapsAccording to Rich Baldauf, these are the important factors to roadside vegetation design:
Source: Roadside Vegetation Design to Improve Local, Near-Road Air Quality. Transp Res D Transp Environ. 2017 May 4; 52(11): 354–361.
doi: 10.1016/j.trd.2017.03.013
Effective Barrier Ineffective Barrier SUPERSTRUCTUREMODULARLIGHTPREFABVIEWSSCREENSFLEXIBLEHyphae uses Google streetview images and computer visions algorithms, enabling discrimination of diverse environmental classifications, including between trees, grass, shrubs, roads, cars, and various other aspects of the built environment. This provides quantification of the built environment as a view-index, which relates to the human experience of the environment more than satellite or aerial analyses. These view-indices have been associated with human health outcomes and can also provide insights into the distribution of infrastructure and, over time, change detection. # Streetview AnalysisTop row is Google Street-View photograph, middle row is semantic segmentation, and bottom row is our deep learning prediction of LAD. Left column is dense, purpose built vegetated air barrier at Saint Margaret Mary School in Lousiville. Middle row shows a gradient in tree health from left to right, with the leftmost tree being healthy and dense, and the rightmost tree almost dead. Right column shows an increasing gradient of low density foliage from left to right.
Using deep-learning algorithms trained on mobile LIDAR data, we can further characterize Street-View images by vegetation leaf area density, porosity and quality.Above: mobile lidar data used to generate leaf area density estimates for training street-view analysis algorithmsVegetated air barriers optimized for mitigating air pollution must be planted close together without any gaps, otherwise the pollution can squeeze through! # Measure, Model, Modify

Southwestern Medical District Dallas, TX
Collaboration with SWMD and TTF and Field OperationsTexas
Trees
FoundationHyphae
Design LabsField
OperationsMIGKimley-
HornTerrapin
Bright
GreenETM 
Assoc AuroraLUMJBCOperations and ManagementPublic Art
CurationLightingSoils &
IrrigationLandscape &
Urban DesignMEIARSMEP EngineeringSurveyEvidence-Based 
ProcessBiophilic Design ReviewCommunity
EngagementCivil, Traffic,​
and Structural ​
Engineering​Implementation TeamResearchAcademicsAgencyCurrent Day: Aerial of Dallas+ LOVE FIELD AIRPORT# Urban Heat Islands in DallasWarm season (May through September) average daily high temperature (°F)SWMDSatellite imagery can see trends over large areas and over timeZone 1: 44.6 CZone 2: 43.5 CZone 3: 43.3 CZone 3b: 43.1 CZone 4: 44.3 CZone 5: 45.5 CLandsat 8 Land Surface Temperature (LST) in C Variation between zones on July 17th 2020 around 11am
Newer satellites get to 50-100m resolution and pass every few days# Imagine a Green, Inclusive, Safe, Accessible, and Healthy DistrictTexas Trees FoundationHarry Hines Blvd TodayWhen your designing an intervention, work at that scale to measure change# MeasureHigh resolution satellite imaging and ground-based sensors for ongoing monitoring and analysis.
# Model# ModifyWe model the MRT and leverage real time data to create environmental simulations that will be used to predict design outcomes.  Optimize design scenarios to maximize health benefits through iterative modeling process.  # Measuring Thermal Comfort# Modeling Radiant Temperature @ Microclimate Scale Sensor SetupSolar panel, battery and LoRaWAN radioWind speed and direction sensorBlack globe temp sensor for calculating mean radiant temperatureAir temperature and humidity probeLight sensorTo measure inputs to UTCI equation, we need air temp, radiant temp, humidity, and wind speed. To ground-truth simulation, we need those plus wind direction and light.In bus sheltersAs of May 1st 2023 
27 sensors were placed along Harry Hines from Butler to Medical District DriveSensor Network 70 C42 CExisting Conditions: Average MRT = 64.7 CMaximal Canopy: Average MRT = 55.6 C9.1 degrees C lower MRT!Benchmarking: Existing Conditions vs “Maximal Canopy”
Summer Afternoon Mean Radiant TemperatureProject boundary (white polygon)Microclimate Wind StudyAreas where adding new shade trees might not helpWhere new shade trees would help a lotWhere structures increase wind-speedWhere trees reduce wind-speedFebruaryMayAugustCold and warm season comfort dynamics are inverted, so sunny and slow-wind areas are most comfortable in the winter, while shady, fast-wind areas are most comfortable in the spring and summer. Built-environment planners can leverage this for seasonal programming. # 3D MappingPublic GISUSGS ElevationOpenStreetMap / MicrosoftExisting data layersCity GISModel the Built EnvironmentModel the tree canopy 3D LAD voxels from LIDAR can now be turned directly into ENVI-met tree objects

ENVI-met uses specimen level 3d models, which are placed in the CFD domain with a point set indicating location. 

Thus to account for existing trees without radial symmetry, our pipeline generates specimen level 3D models from LIDAR, and then applies an appropriate rotation within the grid to fit the CFD domain.LIDAR -> LAI -> ENVI-met treesForeknowledge of species differences in average surface area can help guide planting decisions and also improve accuracy of convolutional neural networks for predicting surface area from photographs (if photographs are pre-segmented by tree species)Model Tree SpeciesLAD AnalysisModel Leaf Area Density - LADTop row is Google Street-View photograph, middle row is semantic segmentation, and bottom row is our deep learning prediction of LAD. Left column is dense, purpose built vegetated air barrier at Saint Margaret Mary School in Lousiville. Middle row shows a gradient in tree health from left to right, with the leftmost tree being healthy and dense, and the rightmost tree almost dead. Right column shows an increasing gradient of low density foliage from left to right.
Above: mobile lidar data used to generate leaf area density estimates for training street-view analysis algorithmsWe will also use the sensor data to ground-truth simulations Real-time insights, 12:47pm June 7th 2023Under trees, GT is ~33CWithin a few feet, but in the sun, GT is ~46r2 = 0.82 maybe off due to geopositioning and old lidar data (2018)r2 = 0.91 pretty closer2 = 0.45 maybe off due to geopositioning and old lidar datar2 = 0.54 old lidar data: this small tree didn’t exist in the simulation# Validating Simulations at the Microclimate ScaleDesign Process IntegrationExisting conditions ‘EC’Typical Streetscape ‘T’Hedge and set-back larger canopy ‘H’Mature Grove on Grid ‘G’PARKLANDZALE LIPSHYSCENARIO T
THERMAL COMFORTRemoving large, mature trees from the median reduces thermal comfort a lot, but mainly in the roadway. Adding small trees improves it slightly.  UTCI (℉) difference from ‘EC’-15+130It feels much hotter when the large trees are removedNew, smaller trees improve thermal comfort near the planting sites.SCENARIO ‘G’
THERMAL COMFORTUTCI (℉) difference from ‘EC’-15+130The grid of the grove provides a 15 degree improvement for a large percentage of the path and surrounding areas.Quantifying thermal comfort & particulate exposure across routes Human PerspectiveOverall, the “T 15% Design” has the least thermally comfortable path.

“T 15% Design” is also the least thermally comfortable at all points along the route.

The “Mature Grove on Grid” Scenario is the most comfortable overall, and at almost all points along the route.

The “Hedge and set-back larger canopy” condition is slightly better than existing condition overall.4 SCENARIOS 
 PET COMPARISONThermal comfort along the walking path: comparison of 4 scenariosPET thermal comfort index (degrees C)Time walking along walking path in seconds (from west to east)NOTES: Above around 23C, the higher the PET, the worse the thermal comfort.           AUC is area under the curve, an aggregate metric of the time series# Promotoras: Community-Led Design# Imagine a Green, Inclusive, Safe, Accessible, and Healthy DistrictTexas Trees FoundationHarry Hines Blvd TodayModifyTexas Trees FoundationVision -  a Connected, Inclusive, Safe, Healthy CampusTexas Trees FoundationHarry Hines BoulevardTree Groves for Maximum Shade and Cooling