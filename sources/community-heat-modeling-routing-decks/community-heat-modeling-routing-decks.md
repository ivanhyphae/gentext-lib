---
asset_id: community-heat-modeling-routing-decks
source_system: gdrive
source_id: 1-yJt72IY3BY4IjoSMU7o8raFfFL71hjewj3j36-TV7Y
source_title: "Community AQ & Heat Modeling, Monitoring and Routing"
acquired: 2026-09-25
via: connector-text
tool: google-drive read_file_content (includeComments=true)
truncated: unknown
---

Heat & Air Pollution Modeling, Monitoring, and RoutingEvidence-based adaptation frameworkModelling: Thermal ComfortFor comparison with sensors data see: https://widgets.hyphae.net/harry_hines_umep_sensors/

The R2 values ranged from 0.93 to -2.4 with RMSE ranging from 3.5 to 10.6# Modelling Radiant Temperature @ Microclimate ScaleCyan and blue vectors are higher velocity - wind flow is most pronounced around the edges of large buildings. To the right, air is compressed through building openings at Harry Hines, causing the velocity to increase.Modelling: WindOn left is the simulation domain given the prevailing wind, with tree canopy denoted by white squiggly shapes, and wind vectors shown as colored arrows. This shows the wind speed reducing effects of the vegetation and the ability of certain building geometries to increase wind velocity. On the right is the UTCI computed from the air & surface temperature, sky exposure, relative humidity and wind velocity, showing that the shading effect of trees is still improving thermal comfort in spite of the wind velocity reduction of the trees, but that beneficial cooling can also be had by increasing wind velocity, even without shade. This helps prioritize tree planting areas, as higher wind-velocity areas may have a lower benefit per cost from tree planting than areas with already lower wind velocity. 
Areas where adding new shade trees might not helpWhere new shade trees would help a lotWhere structures increase wind-speedWhere trees reduce wind-speedWind speed simulationUTCI simulationExisting conditions ‘EC’KHA 15% design ‘KH’Hedge and set-back larger canopy ‘H’Mature Grove on Grid ‘G’The next slide shows the results of the thermal comfort analysis walking paths through the scenarios shown here:Overall, the “KHA 15% Design” has the least thermally comfortable path.

“KHA 15% Design” is also the least thermally comfortable at all points along the route.

The “Mature Grove on Grid” Scenario is the most comfortable overall, and at almost all points along the route.

The “Hedge and set-back larger canopy” condition is slightly better than existing condition overall.4 SCENARIOS 
 PET COMPARISONThermal comfort along the walking path: comparison of 4 scenariosPET thermal comfort index (degrees C)Time walking along walking path in seconds (from west to east)NOTES: Above around 23C, the higher the PET, the worse the thermal comfort.           AUC is area under the curve, an aggregate metric of the time seriesHedge and set-back larger canopyMonitors measure:
 -globe temperature, 
 -air temperature, 
 -humidity, 
 -wind-speed and  
 -wind-direction.
- light level 

Sensor Network: Harry Hines Corridor - Butler to MDDAs of May 1st 2023 27 additional sensors were placed along Harry Hines from Butler to Medical Distric Drive
Globe temperature readings respond significantly to shade from both large and small trees, while air temperature only significantly differs for large trees.Globe temperature results:
 Within these time periods, the mean globe temperature is 7.8 degrees C higher in the sun than under a large tree, while the mean temperature under a small/medium tree is 4.3 degrees higher. r2 = 0.82 maybe off due to geopositioning and old lidar data (2018)r2 = 0.91 pretty closer2 = 0.45 maybe off due to geopositioning and old lidar datar2 = 0.54 old lidar data: this small tree didn’t exist in the simulationCar-mounted lidar misses backyards…      But gets detailed understory        Aerial lidar gets backyards…                      but misses understory!NSF is funding us to gather lidar data that can be used to develop modeling methods…So we want to strategically scan neighborhoods where interventions might be going in so we can later do pre-post studies…Why is a detailed understanding of roadside leaf area density (LAD) important for urban air pollution mitigation?LAI = leaf area m2 per m2 of Earth’s surfaceLAD = leaf area m2 per m3 of air volume# CFD modeling can add estimations of air improving efficacy for design iterations Prototype tree packing: AugustPrototype tree packing: AugustT-LIDAR point cloud of Saint Margaret Mary Buffer 2016Modelling: Air Pollution Interception by trees 10-40%
Monitoring Air Pollution Interception by trees 15-50%
Phase 1 + Phase 2 + Phase 3From Watterson Phase 3 Updates PresentationLZ-129LZ-130LZ-129LZ-130Engineered vegetated air barriers were planted along both side of a 2 mile stretch of I-264 freeway through Louisville, KY. in 2022

These are subject to ongoing UFP monitoring (before and after installation). 
SUPERSTRUCTUREMODULARLIGHTPREFABVIEWSSCREENSFLEXIBLEHyphae used streetview images and the Pyramid-Scene Parsing Network (PSPnet) algorithm. The algorithm performs open-vocabulary semantic segmentation taking global context into account, enabling discrimination of diverse classifications, including between trees, grass, shrubs, and various other aspects of the built environment:H. Zhao, J. Shi, X. Qi, X. Wang, and J. Jia. Pyramid scene parsing network.arXiv:1612.01105, 2016# Streetview AnalysisSky view indexsky view index is correlated with heat island effect and thermal comfort.Remote sensing data of existing conditionsintervention design iterationsEBD rubrics based on simulation results.Digital twin of neighborhoodSensors monitoring dataMonitoring validates simulationThermal stress simulation resultsAir pollution simulation resultsPhysics simulationTraffic modelhyphae design laboratory 2024