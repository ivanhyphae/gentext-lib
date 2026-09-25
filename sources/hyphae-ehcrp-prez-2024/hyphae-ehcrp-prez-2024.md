---
asset_id: hyphae-ehcrp-prez-2024
source_system: gdrive
source_id: 1AVtB2oOjZYFDN4xwMRHNtb958uNW87_Dw1yOlBJznp8
source_title: "Hyphae_EHCRP+prez"
acquired: 2026-09-25
via: connector-text
tool: google-drive read_file_content (includeComments=true)
truncated: unknown
---

Hyphae is a mission-driven organization. 
Our vision is to break down disciplinary silos and conventions to redefine the relationship between nature, humans and their built environment.
We understand that the only way to effectively improve overall ecosystem health and resilience is from a systems thinking approach that respects the interconnectedness of disciplines, nature and people.Monitor the results# Evidence Based DesignMicroclimate SensorsAverage Daily High TemperatureSWMDSWMDSWMDZone 2: 43.5 CZone 3b: 43.1 CZone 4: 44.3 CIn bus sheltersMicroclimate SensorsLoRaWAN radioSolar panel, batteryWind speed & direction Black Globe Temp Air temperature & humidity Light sensorMicroclimate Sensors & ModelMicroclimate Sensors# COMMON- SupplementYellow: Cities target
Red: Small <500 people 
Black Points: sensor locations
Blue Points Cooling Centers

CalAdapt data is high resolution temporarily, as in there is day to day data, but spatial it is only 3 mile grid, which means one value is provided for a large non-homogeneous area see example of Armona) not high enough to target vulnerable population and provide local solutions and respits. Local Climate Zones correlate with heat impactsLCZ significantly correlates with  temperature……thus we control for LCZ as a covariate when comparing DAC status with temperature. When we do this we see a significant 13.8 degree increase in temperature in DAC census tracts vs non-DACFarm crop data can also further explain with heat & land use (local climate zone data) at both local and broader resolutionEcoSTRESS data is far more helpful than county and lower resolution models, showing the fields to the north of kettleman city having a cooling effect, as compared to the hot unirrigated land below.But EcoSTRESS data is also too low resolution to identify the cooling effect of individual parks and individual features like trees. Whereas the shade under these large trees does provide heat stress relief, and could help more people if accurately measured and modelled.We’re building a technology platform to empower communities impacted by environmental justice and climate change to take control and determine their own future, a new approach to community-led, evidence-based urban revitalization. 

What previously required teams of engineers, epidemiologists, academics, government agencies and consultants can now be done by and for communities themselves, creating resilience, while re-localizing power, knowledge and capital in the communities.With funding from# SFOTWARE & HARDWARE
PROJECT EXAMPLE: DALLASSouthwestern Medical DistrictDigital twin areaDallasLiDAR processing for semantic segmentation and derivativesLiDAR is source information for tree canopy modelingMicroclimate Wind StudyRecent design draft from fieldoperations shared with publicExisting conditions# Visualizing radiant temp# Thermal comfort scenario comparisonBröde, Peter & Krüger, Eduardo & Rossi, Francine. (2011). ASSESSMENT OF URBAN OUTDOOR THERMAL COMFORT BY THE UNIVERSAL THERMAL CLIMATE INDEX UTCI. Universal Thermal Climate IndexUTCI provides a ‘feels like’ number equivalent temperature and guidelines on corresponding thermal stresses for people.70 C42 CExisting Conditions: Average MRT = 64.7 CMaximal Canopy: Average MRT = 55.6 C
Within project boundary (white polygon) the maximal scenario has on average 9.1 degrees C lower MRTBaseline and Benchmark: Existing Conditions vs “Maximal Canopy” Summer Afternoon Mean Radiant TemperatureParklandExisting conditions domainExisting conditions ‘EC’KHA 15% design ‘KH’Hedge and set-back larger canopy ‘H’Mature Grove on Grid ‘G’Hedge and set-back larger canopy ‘H’KHA 15% design ‘KH’Mature Grove on Grid ‘G’UTCI (℉) difference from ‘EC’-15+130Removing large, mature trees from the median reduces thermal comfort a lot, but mainly in the roadway. Adding small trees improves it slightly.
Achieving larger trees could produce 15 degree improvement in UTCI. Feasibility of acquisition should be studied.
The grid of the grove provides a 15 degree improvement for a large percentage of the path and surrounding areas.PARKLANDZALE LIPSHYSCENARIO ‘KH’
THERMAL COMFORTRemoving large, mature trees from the median reduces thermal comfort a lot, but mainly in the roadway. Adding small trees improves it slightly.  UTCI (℉) difference from ‘EC’-15+130It feels much hotter when the large trees are removedNew, smaller trees improve thermal comfort near the planting sites.SCENARIO ‘G’
THERMAL COMFORTUTCI (℉) difference from ‘EC’-15+130The grid of the grove provides a 15 degree improvement for a large percentage of the path and surrounding areas.

This includes planting Parkland property and may not be a feasible design scenario but provides a benchmark for what is possible.# Towards defining paths of analysis:Designs can be optimized towards improving specific areas and routes, 
we need to agree/determine what those should be for future analysisRoutes from 
Rose survey
Summer 2023Routes from 
PWP survey
2021?Routes from 
OSM & BB
Fall 2023Existing conditions ‘EC’KHA 15% design ‘KH’Hedge and set-back larger canopy ‘H’Mature Grove on Grid ‘G’The next slide shows the results of the thermal comfort analysis walking paths through the scenarios shown here:Overall, the “KHA 15% Design” has the least thermally comfortable path.

“KHA 15% Design” is also the least thermally comfortable at all points along the route.

The “Mature Grove on Grid” Scenario is the most comfortable overall, and at almost all points along the route.

The “Hedge and set-back larger canopy” condition is slightly better than existing condition overall.4 SCENARIOS 
 PET COMPARISONThermal comfort along the walking path: comparison of 4 scenariosPET thermal comfort index (degrees C)Time walking along walking path in seconds (from west to east)NOTES: Above around 23C, the higher the PET, the worse the thermal comfort.           AUC is area under the curve, an aggregate metric of the time seriesHedge and set-back larger canopy# In situ monitoringSolar panel for anemometerRadiant temperature sensorAir temperature and humidity sensorAnemometerSensor Configuration “Anemometer, radiant/air temperature, humidity”, shown at left, the sites that have an anemometer will have the anemometer, the radiant and air temperature/humidity sensors. The anemometer is attached to the solar-panel, and the other sensors are attached to a single radio module, of the type  shown below.Sensor ID A2/TH34 is like this. A5/TH33 is similar, with the addition of a weather station illustrated on the next page.  Monitors measure:
 -globe temperature, 
 -air temperature, 
 -humidity, 
 -wind-speed and  
 -wind-direction. 

Sensor Network: Harry Hines Corridor - Butler to MDDAs of May 1st 2023 27 additional sensors were placed along Harry Hines from Butler to Medical Distric Drive
Sensor data being used to ground-truth UTCI simulations. Real-time insights, 12:47pm June 7th 2023:Under trees, GT is ~33CWithin a few feet, but in the sun, GT is ~46All Sensors Globe tempAll Sensors Humidity
All Sensors Wind 10s avgWe will perform time-series clustering to determine empirical categories, as well as compare a priori groupingsA priori groupings include but are not limited to: Shade status /tree size, wind cover, pavement qty/type, grass qty/type, Simulation UTCI score, We used mixed-effects linear regression models to separately analyze the globe temperature, air temperature and humidity data with respect to the sensor location category.
Location categories include under a big mature tree, under a small, recently planted tree, in a bus shelter, and out in the sun.
We initially focused only on sensor readings from summer afternoons (from June 1st to August 30th, and from 12pm to 5pm Central Time). 
 Within these time periods, the mean globe temperature is 7.8 degrees C higher in the sun than under a large tree, while the mean temperature under a small tree is 4.3 degrees higher. Monitoring Results AnalysisIn bus sheltersr2 = 0.82 maybe off due to geopositioning and old lidar data (2018)r2 = 0.91 pretty closer2 = 0.45 maybe off due to geopositioning and old lidar datar2 = 0.54 old lidar data: this small tree didn’t exist in the simulationCalAdapt data is at 3 mile gridWe’re building a technology platform to empower communities impacted by environmental justice and climate change to take control and determine their own future, a new approach to community-led, evidence-based urban revitalization. 

What previously required teams of engineers, epidemiologists, academics, government agencies and consultants can now be done by and for communities themselves, creating resilience, while re-localizing power, knowledge and capital in the communities.With funding fromHyphae’s street-view green viewindex analysis dashboardLeaf Area DensityTree shape and foliage density determine health benefits WEST OAKLAND – Our Home# Common chlorinated solvents include: tetrachloroethene (PCE) trichloroethene (TCE)

Chlorinated solvents are industrial chemicals used widely for metal cleaning and in production of thermoplastics, lacquers, perfumes and polyvinylchloride (PVC) products.+=West Oakland Environmental Indicators Projecthyphae design lab# Prescott Greening Project
This preliminary result shows 7th St. acting as a channel holding particulates.BASELINE MODELExisting treelineINTERVENTIONDIFFERENCEz = 5m (~16ft)Model PollutionModel SolutionsDesignBuild InterventionsPrescott Greening: Adapt CycleMonitor ResultsWith funding fromWith funding from# Community-led Heat AdaptationCoalition Building
Neighborhood(s) Selection:
Community & Data DrivenCitizen Science:
Mapping & Sensor TrainingGreening ProjectsSensor Deployment & ManagementImmediate Use of Data# Community-led Adaptation# Year 1# Year 2# Year 2-Ongoing# Year 2# Year 1Evaluation & Reporting# Year 3Dissemination & Early warning systemsLMR, CCEJN, HDL, NASA, UCMERCED
Community, Feedback on tools, design
Fixed and farmworkers
With funding fromCoalition Building
Neighborhood(s) Selection:
Community & Data DrivenCitizen Science:
Mapping & Sensor TrainingGreening ProjectsSensor Deployment & ManagementImmediate Use of Data# Community-led Adaptation# Year 1# Year 2# Year 2-Ongoing# Year 2# Year 1Evaluation & Reporting# Year 3Dissemination & Early warning systemsHDL,NASA,UCMERCED
Community, Feedback on tools, design
LAD = 3LAD = 1For roadside vegetated air-barriers, the leaf area density is a key parameter that determines their effectiveness for air pollution mitigation. 

The images at the right show the results of fluid dynamics and particle transport simulations on roadside vegetated air barriers with leaf area density (LAD) of 3 (top) and 10 (bottom). 

In each simulation, roadway traffic pollution (PM0.1) was produced with the wind blowing it towards the vegetation.

The higher LAD clearly increases the mitigation of the air pollution dowind of the air-barrier. This is due to increased deposition (capture) of particles on leaf surfaces, and to greater dispersion of the particles up, leading to mixing and dilution.

These insights can drive evidence-based design decisions.  LAD = 10Workflows: Evidence-based Design Question Development # Workflows: Decision-makingeffective bufferopen sightlinesvegetation at human heightvisual barrier btw traffic and pedsnot bufferedcount on reductions to traffic sourcevegetation overheadextra effort for security?political resistanceslower windmore roughness featuresopen understorybetter dissipation?transparent barriersreduced radiant heatmaintenance costplanting configurationhigher pollutionaesthetic / design opportunitylower pollutionlower pollutionmore simulation neededhigher pollutionBoyle Heights 
Industrial Green ZoneINDUSTRIAL ZONES FROM COMMUNITY PLANPROJECT FOCUS AREA# Higher Resolution Shade mapping
# Community-Led Neighborhood Assessment Mapping & Design# Community Observing Local Temperature Extremes# Particulate matter dispersion# Simulations suggest lots of high canopy in the street canyon impedes dispersion of particulate matter: i.e. more trees can be bad (?!)Numerical experiments involving street canyons of varying aspect ratio with traffic-induced pollutants (PM2.5) and implanted trees of varying aspect ratio, leaf area index, leaf area density distribution, trunk height, tree-covered area, and tree planting pattern under different wind conditions were conducted using a computational fluid dynamics (CFD) model, ENVI-met. Various aspects of dispersion and deposition were investigated, which include the influence of various tree configurations and wind condition on dispersion within the street canyon, pollutant mass at the free stream layer and street canyon, and comparison between mass removal by surface (leaf) deposition and mass enhancement due to the presence of trees. Results revealed that concentration level was enhanced especially within pedestrian level in street canyons with trees relative to their tree-free counterparts. Additionally, we found a dependence of the magnitude of concentration increase (within pedestrian level) and decrease (above pedestrian level) due to tree configuration and wind condition. Furthermore, we realized that only ∼0.1–3 % of PM2.5 was dispersed to the free stream layer while a larger percentage (∼97 %) remained in the canyon, regardless of its aspect ratio, prevailing wind condition, and either tree-free or with tree (of various configuration). Lastly, results indicate that pollutant removal due to deposition on leaf surfaces is potentially sufficient to counterbalance the enhancement of PM2.5 by such trees under some tree planting scenarios and wind conditions

Morakinyo, T.E., Lam, Y.F. Study of traffic-related pollutant removal from street canyon with trees: dispersion and deposition perspective. Environ Sci Pollut Res 23, 21652–21668 (2016). https://doi.org/10.1007/s11356-016-7322-9This is just one of a number of studies…This dense, conical conifer blocks pollution from reaching pedestrians, but provides little shade from noon-day sunThis canopy tree traps pollution at ground level, but provides good shade! Maybe it should be planted further from the road or be combined with understory shrubs!Heat benefits and pollution benefits can be at cross-purposes depending on the location and the tree species, thus carefully matching species / form with location is required to maximize benefits and prevent harm! Beyond Heat: Air pollution vs Heat benefitsARBY’SSALVATION ARMYSECTION i115TRAFFIC SOURCESBUILDINGNortherly wind pushes particulates up against the facade; trees reduce the spread of the plume.TRAFFIC SOURCESSoutherly wind pushed the plume northward but the trees reduce dissipationBUILDINGTRAFFIC SOURCESEven in calm conditions more numerous trees cause greater concentration of particulates.j=38i=25,26,27z=2mThe hedge scenario presents quantitatively the lowest concentration of pollutants at the sidewalk. The model suggests that high canopy trees in the median worsen the downwind condition - hypothesized to result from depressing air current and lessening upward dispersion.No treesExisting
(high canopy)3+3 road diet2+2 road dietLanes at NEHedge rowsPoint concentration comparison at human level from sidewalk# Studies in effective sidewalk buffering with smaller interventions# Roadside vegetation buffers 

Conventional wisdom for roadside vegetated air barriers is to make them as tall, wide, deep and thick as possible.

However, DOT regulations and other constraints often don’t allow roadside vegetation to be over a certain height to maintain sightlines.

Can we make an effective buffer system out of layered elements?

We have a few strategies that we are simulating:

Berms with grass and hedges on top
Combination of median trees to slow air and short buffers to push it generally upward.
Impermeable barriers (not vegetation)ParklandBaseline domainTraffic sourceTall grassBuffer treesExisting canopySidewalkMedianBermBare earthTraffic sourceBare earth1m grass1m grass + 1m bermBare earth1m grass1m grass + 1m bermXY cut plane at z=1.75 m height (5’9”)Comparison1m grass vs. Bare earth1m grass + 1m berm 
vs. Bare earthThe berm does have a substantial impact in this simulation by causing an upward movement of the air moving from the road.1m grass vs. Bare earth1m grass + 1m berm vs. Bare earthComparisonThe berm does have a substantial impact in this simulation by causing an upward movement of the air moving from the road. Median canopy + tall grass + downwind hedge vs. bare earthInsights: Trees in the median with a downwind hedge improve sidewalk air quality vs. a tree-less median with no downstream hedge. Tall grass in the median helps marginally.-Insights: Trees in the median while also having a berm and tall grass improve sidewalk air quality vs. a barren median with no berm or tall grass.-Tall grass under median canopy with downwind bermNOTE!Median hedge + 1m grass + 1m berm vs. Bare earthInsights: A large hedge in the median outperforms canopy in median. It also compounds the benefits of the berm dramatically. This design tends to concentrate pollution in the drive-aisles rather than allowing dispersal.-Addition of a glass wall aligned with 1m hedge-Insights: a 1.5m glass wall improves on the effect of a 1m hedge aloneWallCoalition Building
Neighborhood(s) SelectionCitizen Science:
Mapping & Sensor TrainingAdaptation PlanningSensor Deployment & ManagementImmediate Use of Data: Dissemination & Early warning systems# Community-led Adaptation# Year 1# Year 2-3# Year 2-3# Year 3# Year 1Thermal comfort
Very large trees are irreplaceable in mid-term timeframe with respect to cooling effects
Hardscape materials substantively impact thermal comfort
Seasonal options for pedestrians is a more practical strategy than trying to optimize for both summer and winter on every route / gathering space

Air Quality:
More near-road canopy increases concentration of traffic source particulates
Hence, canopy trees further away from road is better
Unbroken hedgerows improve downwind AQ conditions relative to canopy trees
When hedgerows are not possible, layered buffer designs may help
Slowing cars likely results in higher particulate concentrations and exposure
Hypotheses for immediate investigationThermal comfort
Very large trees are irreplaceable in mid-term timeframe with respect to cooling effects
Hardscape materials substantively impact thermal comfort
Seasonal options for pedestrians is a more practical strategy than trying to optimize for both summer and winter on every route / gathering space

Air Quality:
More near-road canopy increases concentration of traffic source particulates
Hence, canopy trees further away from road is better
Unbroken hedgerows improve downwind AQ conditions relative to canopy trees
When hedgerows are not possible, layered buffer designs may help
Slowing cars likely results in higher particulate concentrations and exposure
Hypotheses for immediate investigationDesignSimulationMonitoringValidation# Evidence-based designDesign teamModelingDesign ↔ modeling iterative process