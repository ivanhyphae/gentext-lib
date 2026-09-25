---
asset_id: ebd-approaches-deck
source_system: gdrive
source_id: 1-QSkLPP2qUm4-P_tz9NLTMBK5S4gq3M8GVhKl5KyJIk
source_title: "Evidence-based design approaches: Modeling, measurement, and design at Hyphae Design Lab"
acquired: 2026-09-25
via: connector-text
tool: google-drive read_file_content (includeComments=true)
truncated: unknown
---

# Evidence-based design approachesModeling, measurement, and design at Hyphae Design Lab# AgendaIntroductions (5-10 min)
hyphae’s framework: Adapt-OS
Groundwork USA’s goals in this space
Samples of hyphae’s work
Opportunities for collaborationhyphae staff contributing to this workResearch lead, sensor network engineerDaniel FleischerIvan HeitmannJuan Penaloza Gutierrez, PhDModeling and design contributorCFD specialist
Brent BucknumFounder and strategistADAPT FRAMEWORKRemote sensing data of existing conditionsintervention design iterationsEBD rubrics based on simulation results.Digital twin of urban regionSensors monitoring dataMonitoring validates simulationThermal stress simulation Air pollution simulation Wind  simulationTraffic dataMeteorological datahyphae’s network of evidence-based design products supporting our EJ mission: MeasureEg., High resolution satellite imaging and ground-based sensors for ongoing monitoring and analysis. Also essential for validation.ModifyWe optimize design scenarios to maximize health benefits through iterative modeling process.  ModelWe model indicators like mean radiant temperature and leverage real time data to create environmental simulations that will be used to predict design outcomes.<comment_start id="AAABn2DK4n0">[Image]<comment_end id="AAABn2DK4n0">We use a combination of microclimate measurement & modelling to first predict & optimize changes to the environment, then measure them# The old wayInterventionUnintended
ImpactsIdeologyModify
(Design & Intervention)Model
(Predict and compare)Measure
(Before & after)Validation# Evidence-based designAnalyze DataModel ScenariosDesign OptionsBuild InterventionsMonitor Results# The Adapt FrameworkOur Approach to urban ecosystem intervention# Simulation platforms we utilize:Partially validated
Holistic, incl. veg
Blocky, lower accuracy
Accessible for designersRigorous / validated
Flexible & modular
Detail where needed
Models vehicle- induced-turbulence (VIT)GIS based
Rapid at coarser scale
Uses our derivatives of public LiDAR & others…AspectENVI-metOpenFOAMUMEPNumerical AccuracyModerate. Simple upwind schemesHigh. Access to simple and advanced schemesLow-moderate. Simplified physics (empirical and balanced flow); no CFD numerical solver; lacks turbulence modelingMesh / GeometrySimplified block-based geometry and mesh; flat surfaces; limited terrain fidelitySupports complex 3D geometries (buildings, terrain) with structured/unstructured meshesRaster-based inputs; geometry simplified into stacked blocks; no mesh generationSimulation SpeedOptimized for moderate scenarios; typically fastDepends on model complexity; can require HPCVery fast (single CPU); no solvers or meshing involvedValidationValidated for urban microclimate and thermal comfort; less frequently used in peer-reviewed pollutant dispersion validationExtensive. Widely validated in academic literature (wind tunnel, field, and regulatory modeling); often used in regulatory, academic, and peer-reviewed studiesValidated as a screening tool; not used for high-accuracy flow modeling; Validated against wind tunnel and QUIC-URB for various building/tree layoutsStrengthsQuick setup, urban design tools, vegetation & thermal comfort analysisHigh-fidelity physics, custom solvers, scalable to complex domainsLightweight, rapid results, supports large-area screening; GIS integrationLimitationsNot ideal for high-wind conditions, large domains, or complex terrainRequires CFD expertise; time-consuming setupNo CFD capabilities, no turbulence modeling, simplified physics; limited accuracy, flat terrain only, single-core onlyLicensing and AccessProprietary software (limited transparency, support dependency)Open-source (full code access; large user community; free for academic and commercial use)Open-source; runs in QGISVisualizationBuilt-in visualization; good GUIRequires ParaView or custom scripting for post-processingGIS-native output (QGIS maps)Learning CurveLow (intuitive GUI, pre-packaged workflows)High (requires understanding of CFD and OpenFOAM architecture)Low (easy to learn for urban planners and GIS users)# ENVI-met vs OpenFOAM vs UMEP# Measure, Model, Modify
Case Study
Southwestern Medical District Dallas, TX
Collaboration with SWMD and TTF and Field OperationsCurrent Day: Aerial of Dallas+ LOVE FIELD AIRPORTSouthwestern Medical District
# Imagine a Green, Inclusive, Safe, Accessible, and Healthy DistrictTexas Trees FoundationHarry Hines Blvd Today2017 Dallas’ Urban Heat IslandTree Canopy CoveragePaving Surface CoverageAverage Daily High TemperatureSWMDSWMDSWMDMedical District DriveThe Green Heart
10 AcresThe Green Spine
1.75 MilesButler StreetInwood RoadTreadway StreetParkland HospitalChildren’s HospitalUTSW South CampusUTSW West CampusUTSW North CampusUTSW ClementsNew 
Children’s 
HospitalSouthwestern Medical District
4,000 New TreesPROPOSED TREESEXISTING TREESNEW PEDIACTRIC CAMPUSUTSW 
BEHAVIORAL HEALTH HOSPITALSouthwestern Medical District# MeasureMonitoringSensor SetupSolar panel, battery and LoRaWAN radioWind speed and direction sensorBlack globe temp sensor for calculating mean radiant temperatureAir temperature and humidity probeLight sensorTo measure inputs to UTCI equation, we need air temp, radiant temp, humidity, and wind speed. To ground-truth simulation, we need those plus wind direction and light.One radio hub was installed on the highest roof of Parkland Hospital, and gets coverage of the whole corridorAs of May 1st 2023 
27 sensors were placed along Harry Hines from Butler to Medical District DriveSensor Network Sensor Network: CoverageHub location driven by lines of sight. LoRaWAN can reach >10km with line of sight.3ft antenna9”x9” boxMonitoring database: sensor readings sent every 10-20 minutes since May 2023. Stored in both influxdb and timescale postgres databasesIn bus shelters4 top level conditions for temperature measurements:Monitoring for cross sectional analysis of landscape featuresWe also use the sensor data to ground-truth simulations Real-time insights, 12:47pm June 7th 2023Under trees, GT is ~33CWithin a few feet, but in the sun, GT is ~46In summer afternoons, mean globe temperature is 7.8 degrees C higher in the sun than under a large tree, while the mean temperature under a small tree is 4.3 degrees lower than in the sun.Monitoring for cross sectional analysis of landscape featuresIn summer afternoons, mean air temperature is 3.4 degrees C higher in the sun than under a large tree, while the mean temperature under a small tree is 1.4 degrees lower than in the sun.  Bus shelter sensors were 6.9 degrees hotter than sensors under big trees.Monitoring for cross sectional analysis of landscape features# Benefits of monitoring in our frameworkMonitoring enables before and after comparisons of the interventions

Monitoring enables ground truthing of simulations that are used for iterative design

Monitoring enables cross sectional analysis of landscape features# Model# Digital twinArea of InterestPublic GISUSGS ElevationOpenStreetMap / MicrosoftMerging numerous data sources City GISModel the Built EnvironmentModel the tree canopy 3D LAD voxels from LIDAR can now be turned directly into ENVI-met tree objects

ENVI-met uses specimen level 3d models, which are placed in the CFD domain with a point set indicating location. 

Thus to account for existing trees without radial symmetry, our pipeline generates specimen level 3D models from LIDAR, and then applies an appropriate rotation within the grid to fit the CFD domain.LIDAR -> LAI -> ENVI-met trees# Thermal comfortBröde, Peter & Krüger, Eduardo & Rossi, Francine. (2011). ASSESSMENT OF URBAN OUTDOOR THERMAL COMFORT BY THE UNIVERSAL THERMAL CLIMATE INDEX UTCI. Universal Thermal Climate IndexUTCI provides a ‘feels like’ number equivalent temperature and guidelines on corresponding thermal stresses for people.Digital twin allows simulation of MRT for observed meteorology

Simulation ground truth with sensors: https://widgets.hyphae.net/harry_hines_umep_sensors/r2 = 0.82 maybe off due to geopositioning and old lidar data (2018)r2 = 0.91 pretty closer2 = 0.45 maybe off due to geopositioning and old lidar datar2 = 0.54 old lidar data: this small tree didn’t exist in the simulationOn left is the simulation domain given the prevailing wind, with tree canopy denoted by white squiggly shapes, and wind vectors shown as colored arrows. This shows the wind speed reducing effects of the vegetation and the ability of certain building geometries to increase wind velocity. On the right is the UTCI computed from the air & surface temperature, sky exposure, relative humidity and wind velocity, showing that the shading effect of trees is still improving thermal comfort in spite of the wind velocity reduction of the trees, but that beneficial cooling can also be had by increasing wind velocity, even without shade. This helps prioritize tree planting areas, as higher wind-velocity areas may have a lower benefit per cost from tree planting than areas with already lower wind velocity. 
Areas where adding new shade trees might not helpWhere new shade trees would help a lotWhere structures increase wind-speedWhere trees reduce wind-speedFebruaryMayAugustCold and warm season comfort dynamics are inverted, so sunny and slow-wind areas are most comfortable in the winter, while shady, fast-wind areas are most comfortable in the spring and summer. Built-environment planners can leverage this for seasonal programming. 70 C42 CExisting Conditions: Average MRT = 64.7 CMaximal Canopy: Average MRT = 55.6 C9.1 degrees C lower MRT!Benchmarking: Existing Conditions vs “Maximal Canopy”
Summer Afternoon Mean Radiant TemperatureProject boundary (white polygon)Year 0Year 5Year 10Year 20Year 50Canopy Height model of planting plan in years 0, 5, 10 , 20 and 50 0m30mCanopy Growth BenchmarkingYear 0Year 10Year 20Year 50Canopy Growth Model of FO-30% design0m30m77 C43 CExisting Conditions: Average MRT = 66.76 CFO 30% design Year 0: average MRT = 62.8 C (4C cooling over existing conditions)
Existing Conditions vs FO 30% Summer Afternoon Mean Radiant Temperature, years 0 and 50FO 30% design Year 50: average MRT = 52.38 C (14C cooling over existing conditions)
# Modeling Radiant Temperature @ Microclimate Scale# OpenFOAM based wind and pollution simulationFocus on West OaklandAspectENVI-metOpenFOAMUMEPNumerical AccuracyModerate. Simple upwind schemesHigh. Access to simple and advanced schemesLow-moderate. Simplified physics (empirical and balanced flow); no CFD numerical solver; lacks turbulence modelingMesh / GeometrySimplified block-based geometry and mesh; flat surfaces; limited terrain fidelitySupports complex 3D geometries (buildings, terrain) with structured/unstructured meshesRaster-based inputs; geometry simplified into stacked blocks; no mesh generationSimulation SpeedOptimized for moderate scenarios; typically fastDepends on model complexity; can require HPCVery fast (single CPU); no solvers or meshing involvedValidationValidated for urban microclimate and thermal comfort; less frequently used in peer-reviewed pollutant dispersion validationExtensive. Widely validated in academic literature (wind tunnel, field, and regulatory modeling); often used in regulatory, academic, and peer-reviewed studiesValidated as a screening tool; not used for high-accuracy flow modeling; Validated against wind tunnel and QUIC-URB for various building/tree layoutsStrengthsQuick setup, urban design tools, vegetation & thermal comfort analysisHigh-fidelity physics, custom solvers, scalable to complex domainsLightweight, rapid results, supports large-area screening; GIS integrationLimitationsNot ideal for high-wind conditions, large domains, or complex terrainRequires CFD expertise; time-consuming setupNo CFD capabilities, no turbulence modeling, simplified physics; limited accuracy, flat terrain only, single-core onlyLicensing and AccessProprietary software (limited transparency, support dependency)Open-source (full code access; large user community; free for academic and commercial use)Open-source; runs in QGISVisualizationBuilt-in visualization; good GUIRequires ParaView or custom scripting for post-processingGIS-native output (QGIS maps)Learning CurveLow (intuitive GUI, pre-packaged workflows)High (requires understanding of CFD and OpenFOAM architecture)Low (easy to learn for urban planners and GIS users)# ENVI-met vs OpenFOAM vs UMEPPrescott Impact ZoneCaltrans PlantingFrontage Road DietImmediately Plantable7th StreetEDF/Aclima Black Carbon Measurements

micrograms/m3Large differences in air quality from block to blockCaltrans PlantingFrontage Road DietImmediately Plantable7th StreetWest Oakland: Digital Twin OpenFOAM: Existing ConditionsENVI-met: Existing ConditionsOpenFOAM: Existing ConditionsENVI-met: Existing ConditionsOpenFOAM: Existing ConditionsENVI-met: Existing Conditions<comment_start id="AAABn2DK4nI">[Image]<comment_end id="AAABn2DK4nI">Terrain 
Buildings 
Vegetation
Traffic zones


700 mFigure. Digital twin: a three-dimensional model representing terrain, buildings, bridge, traffic zones and vegetation. (a) shows a close-up of the urban region (inner region). (b) shows the domain extents based on the tallest building height (H). (a)(b)Figure. Wind speed on a terrain-following surface 1.5 m above ground at the Harry Hines corridor. (a)-(b) Wind speed at pedestrian level for the selected wind directions. The color bar indicates the wind speed (m/s), and the yellow vectors indicate the direction of the wind. Note that the region shown extends 350 m from the center location.WINDWINDµg / m3µg / m3Figure. PM2.5 concentration on a terrain-following surface 1.5 m above ground at the Harry Hines corridor. (a)-(f) PM2.5 concentration at pedestrian level for the selected wind directions. Note that the region shown extends 350 m from the center location.WINDWINDµg / m3µg / m3WINDFigure. Wind speed on a terrain-following surface 1.5 m above ground at the Harry Hines corridor. Wind speed at pedestrian level (1.5 m above ground) for the selected wind directions. The color bar indicates the wind speed (m/s), and the yellow vectors indicate the direction of the wind flow. Note that the region shown extends 225 x 85 m.  # Planting concept performanceExisting vs. proposedexisting vegetationproposed vegetationexisting conditionsproposed planting4a7a10a1p4p6:30pUTCI difference on July 12th existing vs. proposedaverage wind directionCooling effect of trees extends beyond shaded areas, with places downwind of canopy receiving cooled air 4pUTCI difference on July 12th existing vs. proposed4a7a10a1p4p6:30p# ModifyImplement/Install the design# Evidence Based DesignPHYSICAL & DIGITAL MEASUREMENTValidate Modelling vs. MonitoringADAPT FRAMEWORK# hyphaePossible Collaboration Areas
Community-Based Air Quality Monitoring: Employ environmental simulation tools that model pollution dispersion patterns in redlined neighborhoods, aligning on our environmental justice missions using data-driven advocacy for cleaner air policies.
Urban Heat Island Mitigation Planning Collaborate on Climate Safe Neighborhoods initiative by assisting with thermal modeling capabilities to optimize tree canopy placement and cooling strategies in communities most vulnerable to extreme heat.
Health Impact Assessment Support community health programs by simulating air quality improvements and heat reduction benefits from proposed interventions, building evidence for funding and policy advocacy.
Youth Environmental Leadership Training Integrate modeling tools and outcomes into youth development programs, empowering next generation environmental leaders with new skills for climate resilience planning.
# Groundwork USA# ENDBrent’s comments:

I think getting to software comparison on page 70 is burying the lead a bit~
I think we also need to have a comparison chart thats simplified.
I also think you have the slides, but we really want to hyper focus early on our unique modeling/measuring philosophy/approach/ technology/capabilities.
I think some of juans flow diagrams made for prescott on the open foam process would also be enlightening. I think those presentations build up the process logically

I think some side by side slides of envimet outputs vas openfoam outputs form dallas or prescott would be interesting.

I think some of the high level values and inherent systemic benefits of openfoam over envimet that you all have communicated are maybe in the large comparison table, but could be made more clear on seperate slide or table.
like abilty to do Vehichle induced turbulence, more complex forms, etc..

you should introduce early, then again at the end how you may want to or be able to collaborate with them.
also could be helpful to structure the agenda to understand their needs/interests early. they for example were already iterated in envimet.

maybe do intros, then a quick 5 or 10 minute overview of the adapt, modelling monitoring tools/approach quickly. then have them talk about their projects for 5-10. then go back in more detail to dallas, prescott etc, with some understanding of whats most relevant to their project network
# More sample analysesSimulation tools in practice# Comparing 4 planting scenarios during early design explorationEvaluation of configurations for their impact on thermal comfort and air quality.ParklandExisting conditions domainExisting conditions ‘EC’KHA 15% design ‘KH’Hedge and set-back larger canopy ‘H’Mature Grove on Grid ‘G’Hedge and set-back larger canopy ‘H’KHA 15% design ‘KH’Mature Grove on Grid ‘G’UTCI (℉) difference from ‘EC’-15+130Removing large, mature trees from the median reduces thermal comfort a lot, but mainly in the roadway. Adding small trees improves it slightly.
Achieving larger trees could produce 15 degree improvement in UTCI. Feasibility of acquisition should be studied.
The grid of the grove provides a 15 degree improvement for a large percentage of the path and surrounding areas.PARKLANDZALE LIPSHYSCENARIO ‘EC’
THERMAL COMFORTTree size is absolutely crucial to thermal benefitsSidewalk elms provide little thermal benefit when so smallsmall trees only provide improvement over a very small areaLarge, mature trees provide thermal improvements widely PARKLANDZALE LIPSHYSCENARIO ‘KH’
THERMAL COMFORTRemoving large, mature trees from the median reduces thermal comfort a lot, but mainly in the roadway. Adding small trees improves it slightly.  UTCI (℉) difference from ‘EC’-15+130It feels much hotter when the large trees are removedNew, smaller trees improve thermal comfort near the planting sites.SCENARIO ‘H’
THERMAL COMFORTUTCI (℉) difference from ‘EC’-15+130Achieving larger trees could produce 15 degree improvement in UTCI. Feasibility of acquisition should be studied.

The thermal improvements of the hedge are limited to the area immediately adjacent.Area shaded by larger trees is 15 degrees coolerThermal benefits of hedge are limited to areas immediately northSCENARIO ‘G’
THERMAL COMFORTUTCI (℉) difference from ‘EC’-15+130The grid of the grove provides a 15 degree improvement for a large percentage of the path and surrounding areas.

This includes planting Parkland property and may not be a feasible design scenario but provides a benchmark for what is possible.SCENARIO ‘EC’
TRAFFIC SOURCE PARTICULATESDuring typical Southerly wind conditions particulates drift Northward over sidewalksSCENARIO ‘KH’
TRAFFIC SOURCE PARTICULATESParticulate concentration at the sidewalk is increased. Further study is needed to explain.SCENARIO ‘KH’
WIND SPEEDLower canopy means reducing wind speed at human height, which reduces dissipation of PM.SCENARIO ‘H’
TRAFFIC SOURCE PARTICULATESThese images show the difference between the ‘H’ scenario and the ‘EC’ scenario. 

The combination of a hedge and set-back canopy tree results in noticeable downwind improvement in particulate pollution. This is at the expense of higher pollution concentrations on the roadway side of the hedge. Hedge creates high pressure zone……which reduces particulates downwindWind direction —>Wind direction —>Where buffer ends, pollution can increase, so longer is betterSCENARIO ‘G’
WIND SPEEDThese images show the difference between the ‘G’ scenario and the ‘EC’ scenario. 

With steady southerly wind the the dense overhead canopy increases wind speed at human height and improves dissipation. Study in calm conditions is needed. SCENARIO ‘G’
TRAFFIC SOURCE PARTICULATESThese images show the difference between the ‘G’ scenario and the ‘EC’ scenario. 

With steady southerly wind the the dense overhead canopy increases wind speed at human height and improves dissipation. Study in calm conditions is needed. # Agent based dynamic heat exposure modeling As a method for quantifying key stressors across designs we can calculate the total exposure over specified routes to provide existing benchmarks against proposed. This allows us to compare before and after conditions in a similar way even if they are physically different and  is in alignment with JCFO’s “Loop” concepts.Quantifying thermal comfort and particulate exposure across routes # Agent based paths of analysis:Designs can be optimized towards improving specific areas and routes, 
we need to agree/determine what those should be for future analysisRoutes from 
Rose survey
Summer 2023Routes from 
PWP survey
2021?Routes from 
OSM & BB
Fall 2023Image from: Kántor, N., Kovács, A. & Takács, Á. (2016). Small-scale human-biometeorological impacts of shading by a large tree. Open Geosciences, 8(1), 231-245. https://doi.org/10.1515/geo-2016-0021Physiological Equivalent TemperaturePET provides an equivalency with and indoor reference environment

PET is costly to calculate, so we do not use it for mapping a large area, but instead for mapping a route taken by a hypothetical agent.# dPET graph - existing conditions# dPET graph - proposed planting# comparison of schemes: walking profilesexisting conditionsproposed planting
city standardproposed planting10a1p4pUTCI difference on July 12th existing vs. city standard# dPET graph - city standard configurationOverall, the “KHA 15% Design” has the least thermally comfortable path.

“KHA 15% Design” is also the least thermally comfortable at all points along the route.

The “Mature Grove on Grid” Scenario is the most comfortable overall, and at almost all points along the route.

The “Hedge and set-back larger canopy” condition is slightly better than existing condition overall.4 SCENARIOS 
 PET COMPARISONThermal comfort along the walking path: comparison of 4 scenariosPET thermal comfort index (degrees C)Time walking along walking path in seconds (from west to east)NOTES: Above around 23C, the higher the PET, the worse the thermal comfort.           AUC is area under the curve, an aggregate metric of the time seriesHedge and set-back larger canopySUPERSTRUCTUREMODULARLIGHTPREFABVIEWSSCREENSFLEXIBLEHyphae uses Google streetview images and computer visions algorithms, enabling discrimination of diverse environmental classifications, including between trees, grass, shrubs, roads, cars, and various other aspects of the built environment. This provides quantification of the built environment as a view-index, which relates to the human experience of the environment more than satellite or aerial analyses. These view-indices have been associated with human health outcomes and can also provide insights into the distribution of infrastructure and, over time, change detection. # Streetview AnalysisTop row is Google Street-View photograph, middle row is semantic segmentation, and bottom row is our deep learning prediction of LAD. Left column is dense, purpose built vegetated air barrier at Saint Margaret Mary School in Lousiville. Middle row shows a gradient in tree health from left to right, with the leftmost tree being healthy and dense, and the rightmost tree almost dead. Right column shows an increasing gradient of low density foliage from left to right.
Using deep-learning algorithms trained on mobile LIDAR data, we can further characterize Street-View images by vegetation leaf area density, porosity and quality.Above: mobile lidar data used to generate leaf area density estimates for training street-view analysis algorithmsVegetated air barriers optimized for mitigating air pollution must be planted close together without any gaps, otherwise the pollution can squeeze through! Microclimate Wind StudyLarge masses of trees create a wind velocity momentum sink. Both images include the tree masses in the simulation, but the trees have been turned off in the second image to more clearly see the wind change. 
This reduction in velocity typically increases particulate deposition. Vegetation also influences microclimate through evapotranspiration which tends to locally reduce temperature. We have not modeled e-transp but may in a future round.Example of Tree influence at the bird sanctuarytrees hidden# Boulevard buffers for PMMore canopy consistently slows dispersion of traffic source particulates-~27% higher conc.More canopy consistently slows dispersion of traffic source particulates----Possible reasons for air quality decrease:
canopy traps air pollution at ground level
berm on downwind side of canopy can’t push pollution up above canopy
 advantages of median trees on berm performance not available when median trees are discontinuous.note left sim is crosswind only, while right sim is 24 hour full forcing with real wind data

<!-- connector commentThreads: verbatim JSON as returned by read_file_content -->
```json
[
  {
    "commentId": "AAABn2DK4n0",
    "headPost": {
      "authorName": "Ivan Heitmann",
      "content": "@fletch@hyphae.net what is this thingie?",
      "modifiedTime": "2025-08-08T00:39:29.293Z",
      "postId": "AAABn2DK4n0"
    },
    "replies": [
      {
        "authorName": "Daniel Fleischer",
        "content": "I don't know, never seen it before.. must the aeroqual sensor ttf installed before we started green spine?",
        "modifiedTime": "2025-08-08T00:34:01.575Z",
        "postId": "AAABn2DK4n4"
      },
      {
        "authorName": "Ivan Heitmann",
        "content": "maybe we should put our best foot forward and show something that we did",
        "modifiedTime": "2025-08-08T00:34:55.509Z",
        "postId": "AAABn2DK4n8"
      },
      {
        "authorName": "Daniel Fleischer",
        "content": "",
        "modifiedTime": "2025-08-08T00:39:29.293Z",
        "postId": "AAABn2DK4oA"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABn2DK4nI",
    "headPost": {
      "authorName": "Ivan Heitmann",
      "content": "is this the one you meant? @brent@hyphae.net",
      "modifiedTime": "2025-08-08T00:16:02.515Z",
      "postId": "AAABn2DK4nI"
    },
    "status": "OPEN"
  }
]
```
