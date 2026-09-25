---
asset_id: prescott-modeling-simulations-report
source_system: gdrive
source_id: 1XvEhLXAKChMuvwQv78xSJT-ZzeY54peya7z-DEM2qho
source_title: "Prescott Modeling and Simulations Report"
acquired: 2026-09-25
via: connector-text
tool: google-drive read_file_content (includeComments=true)
truncated: unknown
---

# Prescott Modeling and Simulations Report

# **Prescott**
## **Modeling & Simulations Report**
**Prepared by Hyphae Design Laboratory September, October 2024**
# Overview
The Port of Oakland is considering revision to freight truck traffic patterns. Hyphae is assisting in evaluation of this proposal using computational fluid dynamics simulation. Hyphae is studying several scenarios for future traffic patterns focused on an area around Frontage Rd in West Oakland.<comment_start id=kix.zi5zbo38ntlf> One focus for the 2024-Q4 efforts is on quantifying the impacts of different present and future traffic scenarios on the exposure levels for residents of West Oakland.<comment_end id=kix.zi5zbo38ntlf>
## Proposed Deadlines
|  |  |
| :- | :- |
| Domain hand-off | ~~September 13, 2024~~ |
| First wind solution | ~~September 27, 2024~~ |
| Preliminary review | ~~October 4, 2024~~ |
| Internal review | ~~October 11, 2024~~ |
| Presentation to partners | ~~October 18, 2024~~ December 5, 2024 |
| Presentation to community | ~~October 25, 2024~~ |

## Tasks
### Topics
Link to [Prescott Greening Board » Workstreams](https://miro.com/app/board/o9J_lvNfKVo=/?moveToWidget=3458764599194150937&cot=14)
# \[image\]\[image\]
### List of Tasks
[Truck Volume Comparison Simulations (ClickUp)](https://app.clickup.com/t/86b1q37qr)
# Simulation Methodology
## Precedents
### Links
#### **Slides**
[Prescott\_CFD](https://docs.google.com/presentation/d/12OoyJTFvM7mbBOOBTdUwPKPuZoIjrx_rSueq4FRrFIY/edit#slide=id.g312a2612207_0_0)
#### **Other reports**
[Particulate Modeling Methodology ](https://docs.google.com/document/d/1OyeAfZOvdCLvCuEkVcBBUT8O--mF9MtTjBfLKnT2DiI/edit#heading=h.mtix9t3ba8qx)
[CFD Methodology Report OF](https://docs.google.com/document/d/1MenT4KZGdos0voxW0rWzuv7vJIruDpT1Qit1GAy6KRg/edit)
[Report on Simulations](https://drive.google.com/file/d/1-QUYCov0VczzyprgVPouUGTowYq6c5D4/view?usp=drive_link) delivered with Invoice 3
[AQMD Draft](https://docs.google.com/document/d/16s2VXUswOjwzMrLMe4Y9Mm7p81hvTwsuqotOH8LUOMU/edit) includes preliminary WO simulation 
#### **Supporting tables**
[Prescott Inputs Tables](https://docs.google.com/spreadsheets/d/1HRJ3OfDqbIvCbc8rkVz665ALWSFXcazv1ypZwQke7rE/edit?gid=2104783519#gid=2104783519)
[Adaptation Conditions/Typologies](https://docs.google.com/spreadsheets/d/1OpcIdEDHS--9boeNG-Q1kHbVCSuhYhZnx--NF-nQ1LI/edit?gid=846722090#gid=846722090)
[Typologies matrix](https://docs.google.com/spreadsheets/d/1Odm8NKbuHZEdd-OZjUwrL5wbozXbwaM1h3YLBTN0LLM/edit?usp=drivesdk)
#### **Maps and diagrams**
Ivan’s diagram of [AERMOD emission rates](https://drive.google.com/file/d/1aO86cH-qYXg_XJ3NFJ8PvVG7wvuMyJJp/view?usp=drive_link)
Need to bring in more of the information from the [original Prescott Modeling Ongoing Report](https://app.clickup.com/1233555/v/dc/15mmk-5260/15mmk-5000)
[Aclima Data](https://drive.google.com/drive/folders/1DkpIn1Yz7PSqxHzLgCrhY3H0YNFSkOCB?usp=drive_link)
### Publications
EMFAC, CalEEMod
### Projects
Hyphae’s previous work in Oakland, Dallas, and elsewhere are helpful in defining our process.
## Subject
##### Essential subject matter
###### *Table of Simulations*
|  |  |  |  |  |  |
| :- | :- | :- | :- | :- | :- |
| Study | \# | Name | Caltrans | Plantable (frontage) | Road Diet\* (frontage) |
| 2024a | 1 | No Veg | \- | \- | \- |
| 2024a | 2 | Existing Vegetation | \- | \- | \- |
| 2024a | 3 | CalTrans + Plantable | x | x | \- |
| 2024a | 4 | CalTrans + Road Diet | x | \- | x |
| 2024a | 5 | Road Diet Only | \- | \- | x |
| 2024a | 6 | Soundwall Only | \- | x | \- |
| 2024a | 7 | Caltrans Only | x | \- | \- |
| 2024a | 8 | Caltrans + Soundwall + Wide edge in Frontage | x | x | x |
| 2024b | 1 | Existing, Frontage traffic | \- | \- | \- |
| 2024b | 2 | Existing, Freeway + Local traffic | \- | \- | \- |

In the first part of 2024 hyphae completed a study of the area around the 7th St underpass (2024a in the above table). <comment_start id=kix.ls9dl0jnfrjv>The primary line of inquiry was on different vegetation massing in possible plantable areas.<comment_end id=kix.ls9dl0jnfrjv>
Further refining emissions assumptions is deemed necessary because:
1.  BAAQMD has communicated in coordination discussions that their assumptions have changed substantially since their previous study in 2017 
2.  Predictions are uncertain how emissions will change over time. How important will truck emissions be when they are mostly electric by 2030? How will brake and tire wear impact health? Will these worsen since trucks will be heavier with batteries? 
How can we characterize changes to emissions over time? Predicting previous vs future scenarios of emissions, for example, fewer diesel vehicles is important for evaluating the potential impacts of vegetation in the future.
  - Can use EMFAC up to year 2050
  - Traffic counts are not available for the future from Streetlight
  - How did AQMD quantify the future (2017 to 2024)?
##### Additional subjects for consideration
Text
## Rationale
##### Core objectives
Text
##### Mitigating factors
Text
## Protocol
### Tools
OpenFoam, ENVI-met
#### **Limitations**
##### Steady-state simulation
No variability in conditions over time is resolved. If multiple states are of interest multiple simulations must be executed.
|  |
| :- |
| *Figure XX: Diagram of limitations* |
|  |

### Domain generation
#### **Building volumes**
OpenStreetMap building outlines are used for building masses. The outlines are used as clipping boundaries for LiDAR segmentation to isolate points for each building.
Gaps smaller than 3m between buildings are merged to prevent narrow regions of simulation mesh which are smaller than 6 cells wide (assuming 0.5 m cell size in the near-building refinement zone). The resulting building sets as single meshes are assigned a height averaging their members. Differentiation of the roof elevation is under consideration for algorithm development.
#### **Terrain**
Treating the USGS data product DEM as a point cloud allows decimation of points before triangulation. CloudCompare software provides matrix eigenvector based properties in the ‘compute geometric features’ tools. Using a 2m radius calculation, the ‘linearity’ property has good sensitivity to physical features that define edges. Subsampling with a variable spacing based on this property allows closer point density at edges and less density in less detailed DEM areas. Because the subsampling routine is a linear function with a maximum and minimum the result is better when first calculating the log of the linearity property. Because linearity is given between 0 and 1 the log will be negative and the distribution of values between -1 and -6 covers the useful geometric differentiation.
Because linearity is calculated at a 2m radius this method does not get at the structure of the terrain on a larger scale than 4m nor is it useful in decimating at greater distances than 4m, nor is it helpful in very flat areas larger than that size. An updated method might also integrate geometric attributes calculated over larger areas.
The existence of the underpass canyon is a significant challenge in automatically producing a workable simulation surface. We used a manually constructed polysurface and blended it into the larger terrain using a patch collar form that matched the edge of the canyon and the surface a few meters set back. This is somewhat laborious and not ideal for regular repetition.
#### **Vegetation and Canopy**
In the digital twin, trees are represented with different levels of detail based on available data. Using on-site tree surveys, trees may be placed according to specific point locations and incorporate spread and height where available. For a general representation, trees can be categorized into a limited set (3-5 types) of voxelized models stored in a matrix database. These models are then gridded into the simulation at runtime to capture vegetation structure efficiently. LiDAR point clouds are used to estimate leaf area density for a higher level of detail and accuracy, creating voxel grids for individual trees that better represent each specimen’s unique structure. Additionally,  meshing algorithms coalesce groups of tree canopy point cloud data into cohesive volumes. This multi-tiered approach allows flexibility, enabling us to adapt tree modeling to either a generalized or a highly detailed representation, depending on the requirements of the urban wind flow and pollutant dispersion analysis.
The Darcy and Forchheimer coefficients for each vegetation (3D representation) are required to set the momentum sink terms. Kastner and Dogan (2022)  digitized experimental data (Falkenstein-Smith et al., 2019) to calculate the densest and least dense vegetation coefficient for any given vegetation volume. Eddy3D, a toolkit for decoupled outdoor thermal comfort simulations in urban areas, is used to export the coefficients. 
Leaf area density is required to set the pollution deposition rate in the dispersion model. To reduce the computational cost, the vegetation volumes will be grouped based on Leaf Area Density (LAD). Instead of defining individual cell zones for each tree, which would require separate deposition rates for every unique vegetation entity, the volumes will be categorized into bins of 0.5 LAD intervals. For example, vegetation with LAD values from 0 to 0.5, 0.5 to 1, 1.0 to 1.5, and so on will be grouped. Each bin will represent a range of LAD values, allowing for the definition of a single deposition term for all vegetation within that bin. This approach minimizes the number of cell zones that must be explicitly defined in the pollution model, significantly reducing the computational overhead. The deposition rate for each bin may be derived from the max or median of the LAD bin range. Note that vegetation properties/coefficients (e.g., leaf area density) will not vary spatially in the 3D representations.
#### **Coordinate System**
Universal Transverse Mercator coordinates are used for the digital twin. Domains are offset and rotated to yield a smaller range of coordinate values appropriate for CFD. In this project the offset is 560,000m,4,184,000m and the rotation about that same point is -32° (counterclockwise). The underlying grid system is UTM 10N, EPSG:26910 and the datum is NAD83. Vertical coordinates are converted to meters using a multiplier of 0.3048 from NAVD88 values in ft.
### Methods for Calibrating Emission Rates & Vehicle-Induced Turbulence (VIT) 
#### **Introduction**
This section outlines the process for calibrating Vehicle-Induced Turbulence (VIT) and pollution emission rates using traffic data from StreetLight and emission factors from the EMissions FACtor Mode (EMFAC). 
StreetLight provides traffic data on predefined road segments from OpenStreetMap, including vehicle counts and moving speeds. Traffic counts are used to profile traffic quantities over time. The moving speed, size, and number of vehicles on a road segment influence VIT, as faster-moving or more vehicles create more turbulence, which enhances pollutant dispersion. Vehicles produce tailpipe emissions, brake and tire dust, and reintroduce road dust into the atmosphere both mechanically and by their wakes. Emissions factors evaluate the quantity of pollution generated per vehicle-travel distance. Factors for running exhausts, tire and brake wear are available in EMFAC. These factors are combined with the traffic counts to calculate pollution emission rates over road segments.  
#### **Comparison of familiar approaches**
|  |  |  |  |  |
| :- | :- | :- | :- | :- |
| **Parameter** | **AERMOD / BAAQMD** | **ENVI-met 2024** | **Latest Dallas OpenFOAM** | **Proposed Method** |
| Vehicle types | Exhaustive | Trucks only | Mixed (passenger, medium-duty, heavy-duty) | Trucks and passenger cars for VIT, trucks only for PM |
| Quantities | Post-sim multiplier | Relative, 3-4 classes | Unitized | Relative, by road segment |
| Quantity data source | Counts owned by Bentley, in-house analysis | Caltrans AADT, commissioned truck survey from 2018 (?) | Kimley-Horn mobility study | Streetlight quantities by segment and vehicle class |
| Diurnal profile | Counts owned by Bentley | Copying BAAQMD profiles | Average from traffic survey | Average from Streetlight data, hourly, or rush morning, noon, evening |
| Vehicle induced turbulence (VIT) | No | No | Turbulence injection scales with average vehicle count, speed, and size | Turbulence injection scales with average vehicle count, speed, and size |
| Pollutant types | PM2.5, diesel PM, TAC | PM0.015 (15nm) | PM2.5 | PM2.5 and/or others |
| Related models | EMFAC, CTAG (for regional inputs) |  |  | EMFAC, CalEEMod |
| Reference documents | [Final Plan Vol 2 100219 pdf.pdf](https://drive.google.com/open?id=106IFl4Bj2rhiF5903gsluKkiaR96ALwA) |  |  |  |

|  |
| :- |
| *<comment_start id=kix.fjfn2loeenar>Chart of histogram of traffic counts segmented by traffic type and road type (?)<comment_end id=kix.fjfn2loeenar>*    \- *compare AERMOD, ENVI-met, Streetlight, Caltrans AADT*    *\[image\]* |
| Figure XX: Normalized traffic counts. StreetLight data corresponds to passenger cars, medium-duty, and heavy-duty trucks on weekdays (Monday-Thursday) from 2022 on Nimitz Freeway.  |

Comparison of Streetlight values with BAAQMD AERMOD values from 2017
#### **Coordination with AQMD**
|  |  |
| :- | :- |
| **To** | [Stephen Reid](mailto:sreid@baaqmd.gov) [Song Bai](mailto:sbai@baaqmd.gov)  |
| **Cc** | [Daniel Fleischer](mailto:fletch@hyphae.net)[Mei Visco](mailto:mei@hyphae.net) [Brent Bucknum](mailto:brent@hyphae.net)  |
| **Bcc** |  |
| **Subject** | <comment_start id=kix.ytm1wc5z5tdn>west oakland emissions and simulation coordination<comment_end id=kix.ytm1wc5z5tdn> |
| Hello,    I hope you both are well.    We have been advancing the design and modeling of the Prescott Project and we would like to resume our discussion of our emissions studies in the Prescott neighborhood. We have a few questions for you:    \- <comment_start id=kix.uvfml6g9wo9g>Has your team concluded your revision of the emissions factors used in the Owning Our Air publication? If so, do you have documentation of the substance of the revisions and underlying assumptions?      - What are some of the significant changes coming from EMFAC?      - Are you predicting future projections from the present date and what assumptions are going into that?<comment_end id=kix.uvfml6g9wo9g>      - Do you have any data that you can share with us yet?    \- <comment_start id=kix.sjyx3kfl25wh>That publication mentioned that your method used data from StreetLight. We have acquired current streetlight data and want to share methodology details. We would like to discuss how to integrate it alongside AERMOD quantities and hope for any insight on integrating it in our CFD process.<comment_end id=kix.sjyx3kfl25wh>    \- We have been working on a condensed methodology document. We would like to get some direct feedback from some of you. Can we share it and ask for you to read through and comment?    Sincerely,    The hyphae team    **<comment_start id=kix.suop1l6ajj7j>Draft 2:<comment_end id=kix.suop1l6ajj7j>**    Hello,    I hope you both are well. We have been advancing the design and modeling of the Prescott Project, and we would like to resume our discussion of emissions studies in the Prescott neighborhood. We have a few questions for you.     The "Owning Our Air" report mentioned that your method utilized data from StreetLight. We have now acquired StreetLight data and would like to share details of our methodology. We have been working on a condensed<comment_start id=kix.ok2vkygj7mh5> methodology documen<comment_end id=kix.ok2vkygj7mh5>t and would appreciate your direct feedback. May we share it with you for review and comments?     We want to compare how your team integrated Streetlight data (traffic counts, moving speed) to determine the AERMOD emission quantities. We hope for insight on integrating it similarly in our CFD process.We are gathering StreetLight traffic data for light-duty (LD), medium-duty (MD), and heavy-duty (HD) vehicles. EMFAC vehicle categories are matched to StreetLight to obtain emission rates for LD, MD, and HD vehicles.      We noticed that your team has posted a revision of the emissions inventory for 2024. Our methodology considers local traffic emissions on highways and surface streets from operational emissions (running exhaust, brake wear, and tire wear). Can you share the emission rates (g/s) per road segment that your AERMOD model implemented? If possible, per operational emission. We want to compare with our emission rates.     Are you predicting future traffic projections with a growth factor based on EMFAC outputs of vehicle miles traveled (VMT) in Alameda County? If so, are you scaling StreetLight traffic data? We want to explore this.     Do you know of any additional shareable data that may help us develop further and align our methodology with yours?     Sincerely,    The hyphae team |  |

I belie they did update the models…ssed a meeting in avgust or september andthinkthey thsddy presented itnshould ask nicole for slides, I can also look back.
**Emission Inventory Updates (EMFAC)**
Here is the [link](https://www.baaqmd.gov/community-health/community-health-protection-program/west-oakland-community-action-plan) to the West Oakland Community Action Plan updates. The emissions inventory was updated for 2024. For example, since the WOCAP was adopted, CARB has released the EMFAC2021 mobile source model to replace the EMFAC2017 model used for WOCAP emissions estimation for on-road motor vehicles. PM2.5 emission rates for brake wear from light-duty vehicles are about 70% lower in EMFAC2021 than in EMFAC2017. Below are the key source updates. 
\[image\]
[Appendix 3 – Emissions Inventory Details](https://www.baaqmd.gov/~/media/files/ab617-community-health/west-oakland/fifth-year-report-files/appendix-3_woak_5yr_ei_appendix_20240821-pdf.pdf?rev=5c883429e6474f1391b5608d8b7eb114&sc_lang=en): Tables A4-1 through A4-3 provide detailed breakdowns of West Oakland emissions for 2017, 2024, and 2029 and estimated changes in emissions between 2024/2029 and the 2017 WOCAP baseline.
**Modeling Background (**[**Link**](https://www.baaqmd.gov/~/media/files/ab617-community-health/west-oakland/fifth-year-report-files/five-year-report_v3-pdf.pdf?rev=f7643d088570420c89c96d6cf78681b8&sc_lang=en)**) **
During the development of the WOCAP, the Air District worked with the CSC and CARB to develop a community-scale emissions inventory for local sources in West Oakland. The original emissions inventory was developed for a base year of 2017 and forecast years of 2024 and 2029 (5 and 10 years from the WOCAP adoption year of 2019). Once compiled, the emissions data were combined with meteorological inputs in the AERMOD dispersion model to estimate pollutant concentrations and cancer risk resulting from local sources. This evaluation focused on fine particulate matter (PM2.5)), diesel particulate matter (DPM) and cancer risk, and human exposures and risks were estimated for seven community-identified impact zones that the CSC selected based on analyses of monitoring data. 
As part of the development of this fifth-year report, the 2024 emissions inventory was updated to account for activity changes, plan strategies, and regulatory programs that have been implemented since the adoption of the WOCAP. Emissions changes were also used to adjust prior modeling and exposure results, providing an assessment of progress toward plan targets over the past 5 years. In addition, an updated forecast of 2029 emissions from local sources was developed to assess further progress that is anticipated in the years ahead.
**Future Predictions **
BAAQMD derived a growth factor GF based on EMFAC outputs of total vehicle miles traveled (VMT). The GF was used to scale the 2017 traffic data for forecast traffic activity for 2024 and 2029. See [section 2.3.1](https://docs.google.com/document/d/1zLUNpiASA-_hjKv7GaB_kPaxI0lk5NQkxwThEi4Bgnk/edit?tab=t.0) from Owning our Air Report. 
#### **Traffic Parameter Preparation Procedure**
##### Summary and Open Questions
Essential data: Analysis period, vehicle count by category, average speed, average vehicle size
Attributes irrelevant to OpenFOAM: Route
Questions
❓How do Streetlight quantities compare with AERMOD input ratios provided to us by BAAQMD?
❓Should we put in the effort to model directionality of traffic using Force method? Would also require quantifying X,Y,Z vectors of traffic. The Force method is better but how much?
The Force method injects a constant momentum volume source in the traffic zone to represent the drag force exerted by moving vehicles in the lane(s). This method focuses on replicating the directional impact of vehicle-induced turbulence by applying a force volume source aligned with the traffic flow. For example, if the roadway is aligned along the y-direction zones, northward traffic receives a positive y-momentum source. In contrast, those with southbound traffic have a negative y-momentum source. The magnitude of the force is determined by the drag force of the vehicles in each zone, accounting for vehicle categories such as passenger cars, medium-duty, and heavy-duty vehicles. By incorporating traffic flow direction and vehicle drag characteristics, the Force method provides a more realistic simulation of vehicle-induced turbulence than traditional methods (i.e., the TKE method). This approach allows for a better representation of the aerodynamic impact of moving vehicles on urban air quality without the need for highly refined mesh grids, reducing the computational cost. 
A challenge of the Force method is its reliance on vehicle trajectory directionality, which can complicate the model when roads are not aligned with the primary coordinate axes (x, y, and z). In such cases, the force may have components in all three directions, requiring additional computational handling to resolve these directional forces accurately. Accurately capturing interactions on curved or non-linear roads may add complexity and increase computational demands.
###### *Selection of traffic data sources*
  - Streetlight segments are not volumetric and require assumptions about widths of different segments
  - AERMOD dots can be outlined
|  |
| :- |
| *Figure. Flow chart for proposed steps to calibrate VIT and emissions.* |
| \[image\] |

##### 1\. Obtain Traffic Data from StreetLight
###### *Vehicle Classification *
StreetLight uses a vehicle classification system based on the Federal Highway Administration's (FHWA) categories. These categories are further grouped into light, medium, and heavy-duty classifications, see figure below. Light-duty (LD) includes FHWA categories 1-3, such as passenger vehicles, four-tire pickup trucks, and vans. Medium-duty (MD) encompasses categories 4-6 and includes buses and trucks with up to three axles. Heavy-duty (HD) categories 7-13 include trucks with four or more axles. StreetLight’s Truck Volume Metrics are based on five machine-learning models, which link together to predict total vehicles on a road (sum of LD, MD, and HD) and individual metrics for MD and HD. 
|  |
| :- |
| *Figure StreetLight’s vehicle categories are based on the FHWA classification scheme: light-duty (LD) includes categories 1-3, medium-duty (MD) encompasses categories 4-6, and heavy-duty (HD) are categories 7-13. Figure was retrieved from StreetLight white pages* |
| \[image\] |

###### *Zone Activity Analysis *
StreetLight’s Zone Activity analysis is used to output traffic counts and moving speeds for all vehicles, medium-, and heavy-duty trucks over pre-defined road segments. Note that StreetLight’s All Vehicles Volume Metrics cover all vehicle categories, including LD, MD and HD. An important model constraint is that the sum of volumes for the three vehicle categories equals our All-Vehicles Volume Metric (StreetLight white papers), thus LD counts may be obtain by subtracting the truck count (i.e., MD plus HD counts) from the all vehicles count. Temporal variations are also considered to reflect realistic traffic patterns throughout the day (e.g., hourly data for all days, weekdays, and weekends). Below are the road segments (OpenStreetMap, OSM) selected for the case study in WO. 
  - Select Data Type: Export traffic data using the <comment_start id=kix.orfilc3gwj3p>Zone Activity<comment_end id=kix.orfilc3gwj3p> option in StreetLight. This provides traffic counts and vehicle speeds for all passenger cars and trucks (medium and heavy duty) in the zones selected. 
  - Temporal Variation: The exported data will include a temporal resolution to capture how traffic patterns and vehicle speeds vary over time. These temporal changes in vehicle counts and speeds affect emissions and VIT. There are two categories: Day Type and Day Part. Day Type corresponds to day bins (e.g., All days (M-Su), Monday-Thursday (M-Th), Friday (F-F), and Weekends (Sa-Su). Day Part corresponds to hour bins (e.g., All day (12am-12am), 12 am (12am-1am), 1 am (1am-2am), 2 am (2am-3am), …). 
  - Zones: Use StreetLight's map interface to select road segments within the AOI. These road segments should encompass the areas where VIT and emissions are modeled.
  - Activate Trip Attributes to get averaged travel time, length, speed, and circuity metrics. Select Speed to get the average vehicle speed over the defined road segments. If the speed of moving vehicles is unavailable, one may use the legal speed limit for the road segment as an approximation.  
|  |
| :- |
| *Figure. StreetLight zone set (OSM road segments) for West Oakland case study. * |
| \[image\] |

To calculate the average number of vehicles on a road segment at any given time (N), you will need the following inputs from the StreetLight analysis: the hourly traffic count, the average speed of the moving traffic, and the length of the roadway. The relationship between the hourly traffic count (TC), the average speed of the moving traffic (U), and the traffic density (TD) is used to determine N. The average number of vehicles N on the specified length of the roadway L is given by $N\ =\ TD\times L,$ where $TD\ =TC\ /(T\ \times U)$ and T is the time period (3600 s). Note we can consider specific conditions for a month, day, and hour. 
###### *Roadway Attributes *
The roadway attributes (i.e., road length, road type, and number of lanes) are obtained from the StreetLight analysis and outsourcing maps. The road types (e.g., motorway, ramp, and residential) are matched to corresponding U.S. Federal Highway Administration (FHWA) Road Types to determine roadway widths. The number of lanes is used to determine the total width of the roadway, which is required to set the traffic zone volumes in the CFD simulation.  
###### *Origin-Desination Analysis *
StreetLight’s Origin-Destination (O-D) analysis can determine truck counts specific to an origin-destination, which derives data based on GPS navigation information. For example, in West Oakland, Port Trucks have historically been a significant source of DPM (diesel particulate matter) (California Air Resources Board 2008a). Due to the lack of direct traffic counts for Port Trucks, the port truck portion of HD may be estimated via origin-destination (O-D) data from StreetLight. The Bay Area Air Quality Management District (BAAQMD) conducted this type of analysis in 2019 (see Owning our Air report). The Port area was defined as a zone with 49 gates on various road types to assess traffic volumes and determine the proportion of Port Trucks within the HD category. Using an origin-destination analysis, the port fraction was estimated based on trip volumes, showing that over 75% of HD vehicles are linked to port trucks.
###### *Include Different StreetLight Scenarios for other maps (not simulation inputs)*
1.  Origin-Destination
    1.  Coming from port to either of the freeways north and south 80 (BB did a test in Streetlight)
    2.  Coming from North or south and exiting onto frontage.
##### 2\. Calculate Emission Rates Using EMFAC
The EMFAC web tool (Emissions Inventory) provides emissions from on-road and off-road mobile sources in California. Note that emissions extracted from this web tool are the same as those provided by EMFAC2021 software.
###### *Access the EMFAC Inventory:*
  - Navigate to the EMFAC Page: Visit the official CARB website or directly go to the EMFAC section ([CARB EMFAC](https://arb.ca.gov/emfac/emissions-inventory)).
  - Tool Selection: Consider on-road emissions (emissions and emission rates), providing pre-processed data from the EMFAC model. Select the latest version of EMFAC that is appropriate for the target year and region of the analysis, such as EMFAC2021, for modeling up to the year 2050. 
###### *Define the Scope of the Analysis:*
  - Geographic Area: Select the specific geographic area. EMFAC provides data for different regions within California, including specific counties and air basins. For Oakland, select Alameda. 
  - Vehicle Categories: Choose the types of vehicles you want to analyze, such as passenger cars (LDA), medium-duty, and heavy-duty trucks. See the EMFAC [user manual](https://ww2.arb.ca.gov/sites/default/files/2021-01/EMFAC202x_Users_Guide_01112021_final.pdf) for vehicle categories. 
  - Model: Choose between aggregate data or by model year. 
  - Speed and Fuel Type: Both can be selected in aggregate form or by multiple selections.
  - Period: Define the analysis year or range of years for which you need emission data.
  - Season: Annual, Winter, or Summer 
###### *Select Matching Vehicle Categories:*
Vehicle categories are selected based on the vehicle classifications used in StreetLight to ensure that the emission factors are applied correctly. In EMFAC, vehicle categories are more detailed but generally correspond to the following classifications for light-duty vehicles, medium-duty trucks, and heavy-duty trucks, as StreetLight (see Figure 5.2). EMFAC can provide factors based on three categories: (1) Non-Trucks, which includes passenger cars and motorcycles and other non-truck vehicles; (2) Truck 1, which includes trucks with weight class of GVWR 8,501–14,000 lbs ; (3) Truck 2 which includes trucks with weight class of GVWR \> 14,000 lbs. EMFAC further breaks down the non-truck and truck categories into Motorcylces (MC), Passenger cars (LDA), Light-Duty trucks (LDT1, LDT2), Medium duty trucks with GVWR \< 8,500 lbs (MDV), Motor homes (MH), Motorcylces (MC), busses (SBUS/OBUS/UBUS), Light heavy-duty trucks with GVWR \< 14,000 lbs (LHDT1, LHDT2), Medium heavy-duty trucks (MHDT) with GVWR 14,000 - 33,000 lbs, and Heavy duty trucks (HHDT) with GVWR \> 33,000 lbs. See the table below for further details. 
|  |
| :- |
| *Figure. Vehicle classes modeled in EMFAC, retrieved from EMFAC user guide. * |
| \[image\] |

The EMFAC weight class was matched with the FHWA classes; see the table below. Note that EMFAC Truck 1 category was matched with MD from StreetLight and EMFAC Truck 2 with HD from StreetLight. EMFAC bus classes (SBUS; OBUS; UBUS) were matched with MD from StreetLight.
|  |
| :- |
| *Table. Comparison of vehicle categories (FHWA, StreetLight, and EMFAC). * |
| FHWA Class, StreetLight, EMFAC , FHWA Description    1 , LD , Non-truck (MC), All two or three-wheeled motorized vehicles    2, LD, Non-truck (LDA), Passenger vehicles    3, LD, Non-truck (LDT1; LDT2; MDV; MH), Other Two-Axle, Four-Tire Single Unit Vehicles    4, MD, Non-truck (SBUS; OBUS; UBUS), Buses with two axles and six tires or three or more axles    5-6, MD, Truck 1 (LHDT1; LHDT2) , Two-Axle, Six-Tire, Single-Unit Trucks; Three-Axle Single-Unit Trucks     7-13, HD, Truck 2 (MHDT, HHDT), Heavy duty trucks categorized by axle count and configuration. See FHWA for more details.  |

###### *Apply EMFAC Emission Factors:*
EMFAC provides emission factors for pollutants such as NOx, PM2.5, and CO2, based on vehicle type. These emission factors, expressed in grams per vehicle-mile, are used to estimate emissions based on the traffic data from StreetLight. Below are the emission factors of PM2 for both Gasoline and Diesel fuel types.The EMFAC results can be accessed [here](https://arb.ca.gov/emfac/emissions-inventory/6eba4d4dc44f6974483a7dc33fc297b96cdce782). 
|  |
| :- |
| \[image\] |
| NEED TO UPDATE.  Includes running exhaust factor. Missing brake and tire wear PM emission factors. Add missing vehicle categories.  |

###### *Weighting Emission Factors:*
Adjust the emission factors according to the fleet composition in the AOI (e.g., trucks vs. passenger cars) based on the StreetLight data. This adjustment ensures that the emissions accurately reflect the local vehicle mix and their respective contributions to pollution.
##### 3\. Convert Traffic Data into VIT and Emission Inputs for CFD
  - Estimate VIT from Traffic Data: VIT is influenced by the speed, size, and number of vehicles on a road segment. A higher vehicle count increases turbulence as vehicles disturb the air around them. Heavier vehicles like trucks generate stronger wakes and turbulence, contributing to VIT. Moving speed data from StreetLight is combined with vehicle counts to estimate VIT for each road segment. The size of the vehicles can be estimated based on the vehicle category. 
  - Emissions Source Terms for CFD: Calculate the total emissions for each road segment using the traffic counts from StreetLight and the emission factors from EMFAC. These calculations provide the emission source terms (in g/s). One may consider only pollution from a particular vehicle category, e.g., trucks. 
  - Use tools like Python to process and prepare the data for integration into OpenFOAM or other CFD software.
##### 4\. Set Up Roadway Emission Zones in the CFD Model
  - Define roadway emission zones in the CFD domain. These zones serve as sources of both pollution emissions and VIT.
  - Temporal Emission Profiles: Capture daily traffic fluctuations by creating separate simulations for different times of day (e.g., morning rush hour, noon, and evening). Based on the traffic counts and speeds from StreetLight, these temporal variations allow the CFD model to reflect realistic conditions.
##### 5\. Scenario Analysis and Sensitivity Studies
  - Test Different Scenarios: Examples include changes in vehicle fleet composition, increased traffic volumes, or new emission regulations. This analysis helps assess how different conditions impact pollution dispersion and VIT.
  - Sensitivity Analysis: Perform sensitivity analysis to understand how changes in vehicle counts, speeds, or emission factors influence VIT and pollution levels. This analysis helps identify the most critical factors affecting CFD model outputs.
#### **StreetLight Traffic Data Overview**
StreetLight Data provides valuable transportation insights by using Aggregated GPS (AGPS) data to measure and predict vehicle volumes across U.S. road networks. It captures vehicle trips through data from navigation apps, in-vehicle systems, and mobile sources, creating a representative sample that accounts for about 27% of actual vehicle traffic on average (see StreetLight whitepapers). The system processes this data alongside demographic, road characteristics, and seasonal patterns using machine-learning models, including XGBoost, to estimate Monthly Average Daily Traffic (MADT) and other metrics. With the capability to assess total vehicle volume and specific truck categories (medium- and heavy-duty), StreetLight’s metrics can inform diverse projects, from infrastructure planning and congestion analysis to environmental assessments. 
However, the methodology has some limitations that may influence the CFD analysis. For example, errors are significantly higher on low-volume roads (under 500 MADT) due to limited data, potentially impacting CFD accuracy in low-traffic areas. Additionally, medium-duty (MD) truck volumes can be underrepresented due to classification challenges and fewer data points. Another consideration is the limited precision on high-traffic roads (125,000+ MADT), where some variability remains due to sparse permanent counter data in the highest traffic volumes. Seasonality and day-part accuracy might also vary, as scaling factors are based on monthly averages, which could affect the modeling of specific time-dependent traffic patterns. Despite these considerations, StreetLight provides a reliable and scalable solution for high-level vehicle volume estimates, making it a practical input for CFD simulations when its limitations are acknowledged and accounted for.
  - **Traffic Data:** StreetLight provides real-time traffic data, including vehicle counts, speeds, and road usage for various vehicle types. 
  - **Vehicle Composition:** StreetLight captures detailed traffic activity, distinguishing between light-duty vehicles, medium- and heavy-duty trucks.  
  - **Temporal and Spatial Resolution:** StreetLight offers high-resolution data over time and space, enabling users to capture temporal variations (e.g., hourly, daily) in traffic patterns and vehicle speeds. 
#### **EMFAC Emissions Model Overview**
EMFAC (EMission FACtors) is a tool developed by the California Air Resources Board (CARB) to estimate emissions from on-road vehicles within California. EMFAC compiles data from various sources, including vehicle activity, fleet composition, fuel usage, and atmospheric conditions, to calculate pollutant emission factors. The model generates emission factors across different vehicle categories and fuel types, providing metrics such as grams of pollutant per vehicle-mile, which can be applied to both individual vehicles and aggregate traffic scenarios. These emissions estimates include pollutants like NOx, CO, and particulate matter (PM). EMFAC’s outputs are widely used in environmental impact studies, air quality management plans, and regulatory compliance assessments, making it a fundamental tool for evaluating on-road pollution levels across urban and rural regions in California.
EMFAC provides operational emission factors for pollutants such as NOx, PM2.5, and CO2 based on vehicle type. Operational emissions arise from various sources linked to fuel use and vehicle material wear. These emissions include pollutants from running exhaust, where combustion in the engine releases gases through the tailpipe. Additionally, running loss emissions occur as fuel vapors escape the vehicle’s fuel system during operation. Particulate matter (PM) emissions also result from the physical wear of vehicle components, such as tire wear on road surfaces and brake wear from friction on brake discs. Together, these processes contribute to overall emissions, impacting air quality and necessitating targeted mitigation efforts.
  - **Emission Factors:**  
    EMFAC provides emission factors for pollutants such as NOx, PM2.5, and CO2 based on vehicle type, speed, and operating conditions. 
  - **Vehicle Fleet Composition:**  
    EMFAC includes detailed data on vehicle fleet composition, distinguishing passenger cars, trucks, buses, and other vehicles. This ensures the emissions inventory is tailored to the vehicle categories present.
  - **Scenario Analysis:**  
    EMFAC supports scenario analysis, allowing users to simulate emissions for future years or different regulatory conditions. This functionality is valuable for assessing how emissions regulations or changes in traffic patterns could affect urban pollution.
**EMFAC Links:**
[EMFAC Inventory](https://arb.ca.gov/emfac/emissions-inventory/0b4f00d1e72848281afad12ef5f40eefd04e87b1) 
[EMFAC Web Platform Tutorial: Emissions Inventory](https://www.youtube.com/watch?time_continue=22&v=ln1GvXHnFLU&embeds_referring_euri=https%3A%2F%2Farb.ca.gov%2F&source_ve_path=MTM5MTE3LDI4NjY2)
[EMFAC example results](https://arb.ca.gov/emfac/emissions-inventory/d4b874776545053eb84ce49e7eee5ca23e0ea990)
### Field procedure
Text
### Data
##### Data types and schema
Text
##### Data limitations
Text
## Analysis
##### Preparation
Text
##### Calculations
Text
## Recommendations
## Summary
  - 
### References
       
Adapt Oakland (2016). Website <http://plan.adaptoakland.org/adapt/oakland/1_analyze> retrieved July 26, 2016
Al-Dabbous, Abdullah N. Kumar, Prashant. (2014). The influence of roadside vegetation barriers on airborne nanoparticles and pedestrians exposure under varying wind conditions. Atmospheric Environment (90) 113-124


# Hand-outs (short reports)

# Hand-outs (short reports)
  - Pollutant sources in West Oakland
  - 


# Pollutant sources

# **\[image\]<comment_start id=kix.lj1r3t5m9j1f>Pollutant sources  
in West Oakland<comment_end id=kix.lj1r3t5m9j1f>**
## ***Where does the particulate matter in the air in our community come from?***
We’ve heard about and felt the problem in our community but what can we say about what’s driving this problem? The Bay Area Air Quality Management District has invested in an inventory of pollutants in West \[image\]\[image\]Oakland including particulate matter. \[image\]


# Urban Built Environment Simulations

# **Urban Built Environment Simulations**
Computational fluid dynamic (CFD) simulations have proven invaluable for analyzing the dispersion of pollutants in urban flows (Pantusheca et al., 2022). Meso-scale CFD of urban areas considers the urban heat island effect, regional wind patterns, and pollutant dispersion across broad urban  regions. These simulations typically derive boundary conditions from mesoscale meteorological  models (Lucas et al., 2016). Micro-scale CFD simulations of urban areas delve into the detailed  flow dynamics around individual buildings, streets, and trees. These simulations are crucial for  understanding local variations in pollutant dispersion and the impacts of urban design features  such as buildings, street canyons, and vegetation (Blocken et al., 2016). The study aims to address urban flows at the meter to sub-meter scales, resolving interactions between airflow and urban features, including buildings, trees, and vehicles. 
Structures, particularly tall buildings, can disrupt wind movement, as shown in Figure 1. Depending on their height, shape, and respective location with other structures, they can cause several effects: (1) Downward deflection (downdraft effect); (2) Upward deflection resulting in high wind speed and pressure; (3) Reduced wind speed on the downwind side of the structures; (4) Narrow spaces between buildings can create high wind speed and turbulence (Venturi effect); (5) Effects of reversed or cross-wind directions. These flow patterns are complicated to predict without CFD simulation. 
\[image\]
Figure 1 Basic urban wind effects by structures (e.g., buildings). (a) Wind profile upwind of the building. (b) Upward and downward deflection. (c) Downwind eddy and counter current. (d) Venturi effect (wind speed intensified by a gap). Note that (a)-(c) corresponds to the side view of the building; in contrast, (d) corresponds to a top view. The building is shown in gray. 
In addition to buildings, vegetation (e.g., trees) plays a crucial role in urban environments. As physical barriers, vegetation can reduce pollution through deposition processes, where pollutants settle on their leaves. However, vegetation also interact with wind flow, sometimes creating areas of lower turbulence and trapping pollutants near the ground, which can lead to higher concentrations of pollutants at pedestrian levels.  A plume of pollutants approaching a vegetative barrier will undergo two effects, see Figure 2, that can increase or decrease concentration depending on the porosity of the vegetation, micrometeorology, and pollutant deposition characteristics.  When the plume rises above vegetation, the enhanced dispersion due to increased turbulence often leads to a decrease in concentration compared to flat terrain. Conversely, when the plume passes through dense or less porous vegetation, it encounters less turbulence, which dampens dispersion and leads to higher concentration levels near the canopy. Moreover, vehicle-induced turbulence (VIT), caused by the motion of vehicles, introduces additional complexity to urban airflows. VIT enhances pollutant dispersion but, when combined with the effects of buildings and trees, creates highly intricate and variable flow patterns that require detailed analysis. 
\[image\]Figure 2 Basic urban effects by vegetation. PM deposition on leaves reduces downwind exposure. Figure retrieved from Sheikh et al., 2023: Efficacy of green infrastructure in reducing exposure to local, traffic-related sources of airborne particulate matter (PM). 
Together, the interaction of buildings, trees, and VIT highlights the need for CFD simulations to predict wind movement and pollutant dispersion accurately. These simulations enable urban planners and environmental managers to understand and mitigate the effects of pollution more effectively, accounting for both the man-made and natural elements in the urban environments.


# Log

# Log
## January
## 2025-01-30 | [DF IH JPG modeling modules](https://www.google.com/calendar/event?eid=MWgyNDU5b2pzbzVyZmdhMzgxbnNkOTIxc2dfMjAyNTAxMzBUMTgwMDAwWiBpdmFuQGh5cGhhZS5uZXQ)
Attendees: [Daniel Fleischer](mailto:fletch@hyphae.net) [Juan Penaloza Gutierrez](mailto:juan@hyphae.net) [Ivan Heitmann](mailto:ivan@hyphae.net)
Attached files: [Modeling Development Planning Notes](https://drive.google.com/open?id=1kFWqn8Zkw5p-2wk9bIDVF2f1qs_O0E77RSBi9gpk_-o) 
Conclusions about modeling strategy
1.  Go ahead with 10m high x 8m wide west side buffer model 
2.  Pending design discussion consider modeling 30m tall west buffer because it’s easy to modify geometry and we hope beneficial for health and fletch wants giant redwoods
3.  Discuss and design interruption in east side buffer for next model (default hypothesis is that this will not be very effective unless we add ‘patches’)
4.  Model actual proposal of vegetation on both sides of proposed corridor
## December
### 2024-12-10 IH MV check in
Attendees: Mei & Ivan
Notes:
  - Prescott
      - Want futerfas to do some modeling
      - Mei also wants Ivan and Eric Olson to be working with us 
          - Public works and stormwater
      - Ivans time:
          - Dallas is wrapped so Ivan is mostly working on 
              - Happy to help, tease out what his role should be
                  - Kinda an allocations question…
                  - Take a look at the allocations sheet
          - Ivan on Marin city
              - Technically mostly supposed to have Juan on it
          - Fresno
              - Ivan finds out in february
      - Mei needs to work on allocation
          - Allocate Ivan for 4 months of work
      - Put together 1 pager or summary for the results of Juan’s work
          - Ivan wants some time to put into the narrative
              - Very hard to do good distillation and clarification of the take home messages
              - Want to make sure that is ok
          - 1st step is some bullet points from the meeting: what are the take home messages
          - Turning it into a hand out may actually be somewhat difficult
              - Mei suggests we work together on that
                  - Ivan suggests that I make some comments on the slide
  - Simulations
      - Ivan put together 2 different handouts
      - Relative proportion of the different sources
          - Have a graphic
          - May need it to be cleaned up
      - Could have a list of things worth making into a handout in the handout tab
          - A few paragraphs with the core message
          - 2-3 graphics
      - Maybe make that list of hand outs and then run that by Brent and the community
      - 1st tell woeip what we heard in the meeting and then have a communication strategy to follow up with 
Next Actions
- [ ] Plan part of Hyphae Retreat as a West Oakland sprint
- [ ] Mei and Ivan putting the allocations for road diet plan
- [ ] Following up with WOEIP with bullet point from simulation presentation
- [ ] Planning our hand outs
### 2024-12-05 Presentation of Results to WOEIP
Attendees: Nicole, Meet, Scott, Brian, Brent, Mei, Juan, Ivan
Main takeaway: Need to simplify the conclusions that we share with the community. 
Notes:
Simulations Presentation
  - Brian: what does the team think is relevant to the community
      - Meet: the community is probably most interested in the health improvements and traffic levels
      - Scott: confirms what people already think
          - Good for fundraising and speaking to a scientific audience.
          - Validates what we are doing. 
          - Run the risk of people just saying that we need to get all the trucks off the road. This could justify their thinking of that. 
      - Brian: i understand the intentions to doing a more in depth analysis. A key thing is: at one point it seems like the trucks aren’t as much of an issue, but then later it seems the truck is the biggest part of the problem. 
          - I can’t make a pitch for the community, knowing what their concerns are.
          - Can you give me the bottom line?
  - Brent: this is grounding things in the real data. Allows you to interpret this so that you can use it strategically for policy work. 
  - Brian: if eliminating tailpipes only eliminates 10% of all this, then that is really significant. 
      - This eliminates a lot fo the stuff about vehicle type. It really changes the script, which is a contentious one, and hopefully unifies people.
      - If we can assume that veg buffs can be effective against brake and tire wear, then that allows us to move forward. 
          - That simplifies the discussion… brake and tire wear becomes the enemy. Veg buffs become the ally all across the board. 
  - Ivan: something that has become clear to me is that we have some assumptions about where we are going with this information that isn’t clear in the presentations.
      - It's about what are the levers that we can pull. We want to break things down into these different categories so we can figure out how to have an impact on a large and complex problem.
      - If we can show a breakdown of the relative scale and relative impacts, then that does simplify the narrative. 
          - Which one of these problems can we have a meaningful impact on. 
          - If trucking less of a problem then we think, and veg buffs are a big help, then thats great.
      - So we can present as what the opportunities.
          - If truck traffic goes to zero, what is the impact on the health. That can help recommend policy decisions. 
  - Brian: make it like a popular science article “science suggests —” 
      - Have some specifics ready to go.
      - But many people will be satisfied with us saying its a problem and want to know what the solution is. 
  - Scott: could we have cumulative numbers for break and tire wear instead of percentages. So we can use that to assuage the worries around the trucks. 
### 2024-12-03 Internal Presentation of Results
Attendees: Ivan, Fletch, Mei, Juan, Brent
Meeting purpose:
In preparation for presenting or discussing our modeling results with WOEIP and the community, we'd like to first have an internal presentation of the work that Ivan and Juan have done.
Agenda:
  - Presentation (20 min)
  - Questions/Discussion (20 min)
  - Discussion on what conclusions we want to present to WOEIP
Links:
[Prescott Simulation 2024 (Submittal).pdf](https://drive.google.com/file/d/1-QUYCov0VczzyprgVPouUGTowYq6c5D4/view?usp=drive_link)
[Prescott Simulation 2024 (Submittal)](https://docs.google.com/presentation/d/1C4Z4dI_Tg8H-_F063mION_yykFiGbX_SJwmVmQc3F1E/edit?usp=drive_link)
[WO\_Figures\_Report](https://docs.google.com/presentation/d/1gOMcZB8HaKOxiLKeyL1BlnuHfjYKyzPcZ_ypcazmSPc/edit?usp=sharing)
[Transcript](https://docs.google.com/document/d/1VzXtOdSnUmVOn8hJ9fAi2ibk88-80bSoUlV9v4LQlGc/edit?tab=t.0#heading=h.mf8mox2vmss0)
[Recording](https://drive.google.com/file/d/1uG2ZQ0AS4oEpBiBxRf2BS_bGHORPERR8/view)
Notes:
  - Focusing on tile 1 of the CFD study
  - Main challenges for West Oakland
      - Freeways
      - Port & industrial sources
      - CARE (community air risk evaluation) identified this as a problem community
      - EPA has updated the national air quality standards to 9micro
          - Oakland fails this
  - Owning our air 
      - 50% of the emissions come from streets and highways
          - 23% of that is road dust
              - Our current model does NOT take road dust into account
      - The showed values of 3 microm near highway and roads
          - They show local and regional air quality averages
              - That is what iss being produced locally vs from the larger area
  - Study objectives
      - We are accounting for 20-25% of the local emissions
  - Effects that structures have on wind
      - AERMOD doesn’t account for buildings the way that CFD does
          - Speed profile, downdraft, eddies, venturi effect
      - We have effects from traffic and vegetation
          - Car releases PM, turbulence and mixing from car movement
          - Pollution is being pushed by wind
          - This all encounters the vegetation barrier
              - Can cause lofting
              - Slows down the air as it goes through vegetation
              - Causes dispersion on the vegetation
              - Causes downwind eddies
  - Framework for CFD simulations
      - Inputs: weather data, traffic data, digital twin (3d representation)
      - We are doing a wind simulation to get a wind field
          - That is fed into the dispersion model. That gives us the concentration
      - Models
          - Models used:
              - Turbulence
              - ABL
              - VIT vehicle induced turbulence
              - Vegetation
              - Deposition
          - These are all linked to our simulations (how?)
      - Digital Twin:
          - Buildings, terrain, vegetation
          - We create a mesh and then turn that into small volumes
              - Have larger resolution outside the urban area, and as we get closer to the neighborhood our resolution goes up and the mode gets more accurate
      - Weather data
          - Did a windrose study. Used the Oakland airport weather station
              - Closer ones are less accurate and constant
          - For the most part wind is moving (from??) western direction 
              - Can we put this on the slide, explanation of which direction moving
      - Traffic study
          - Gives us moving speed and count for specific road segments
          - We considered all months of 2021
              - 2022,2024 didn’t have info for medium duty trucks
          - They classify their vehicles into 13 classes, 3 major classes of Light, medium, and heavy duty
          - Breakdown of vehicles traffic on weekdays, fridays, and weekends. 
              - Increasing on the weekends
          - Comparison of medium heavy duty trucks. Medium duty trucks have a higher count. But if you sum these up, they are less than 500
              - Light duty is 5-6x greater than the sum of truck counts
              - Bigger contribution
          - If we plot total truck count
              - Around 1pm is peak for truck counts
              - Greater number overall on the weekend
              - But we will focus on a typical week day
              - 20% of trucks on frontage, 45% on the freeway
                  - Can we get that comparison in a graph?
          - Plotting traffic lanes breakdown
              - Light duty higher proportion on freeway. On frontage the heavy duty higher
      - Emissions
          - EMFAC emission factors model- will give you emission factors. Amount of emissions from a vehicle per mile it travels
              - Assumption that light duty are gasoline, and Medium and heavy are diesel
                  - Diesel emission factors do appear to be higher
              - The first column is tailpipe, breakware and tire wear are the 2nd column
              - Break and tire are the larger proportion
              - Emission factors vary depending on vehicle speed. (faster = more emissions) We are aggregating this
      - Traffic data: streetlight, emissions, VIT per vehicle category…
      - Wind speed near the ground
          - Lighter are faster moving speed
          - You can see how buildings and structures redirects the flow. Slows things down and redirects it
          - If we plot the velocity vectors, you can see how the wind changes compared to the overall movement
          - In the canyon the wind slows, and pollution accumulates
      - Comparing wind speed to the PM2.5 concentration
          - Pollution greatest near the canyon and frontage road..
          - If you select a few points and look at a pie chart, looking at the source of that PM 2.5 
              - Light duty vehicles are contributing 50% or more to the pollution
              - Medium duty trucks are higher than heavy duty
              - But overall it is half and half if you are comparing light duty to both medium and high duty
  - Conclusions:
      - The brake and tire wear are contributing 68% of the pollution
      - Even if you made all light duty vehicles electric, only 10% of PM2.5 are removed
      - If you plot the concentration downwind, 500m from the freeway
          - 3 peaks at freeway and frontage road
              - Biggest accumulation at the street canyon
          - A small bump as well at a street
          - Small dips, we think that is where vegetation is
          - Vehicle categories shown in different colors.
      - Plotting 2.5 concentration. 
          - Gray rectangles are where there are buildings
          - Peaks at frontage, and decreases at a different rate than brake wear
          - Small peak at a street
      - Brake and tire wear biggest contributor
      - Takes 80m for concentration levels to decrease
      - Frontage shows highest concentration
      - BB: put some dots in the figure so it's easier to see where the parts of the cross section are..
  - Future improvements
      - Road dust is excluded from current cfd models and should be incorporated into future simulations because it is a huge part
      - Want to include the vehicle speed and VIT
      - Need to verify the streetlight traffic data.. 
  - Average of the PM 2.5 in community is 0.12 micrograms… ⅕ of the canyon
      - So how does this compare with EPA limit
  - Working on a tile 2 as the next simulation
      - Hopefully will have that tomorrow
  - The standard measurement: you always want to be below 9 micrograms (before it was 12). That is a very big number compared to 0.12(average).
      - Significantly lower because we are not considering the regional emissions. The regional average is 6.9-7 micrograms
          - So the rest is coming from the larger region..
      - So we aren’t looking at ALL the various sources (port, industrial, road dust).
          - So we are actually only accounting for about 25% of all the emissions 
      - Half of the work in owning our air was the emissions inventory.. So we could add in other stuff but it would be a lot of work
      - BB: make sure to explain that in the beginning, but then remind them at the end.. 
  - BB: what is our pollution compared to other communities in Oakland. Put that in there as well. Make sure to see, if we are intervening, does this get us to the Owning our Air equity goals?
  - BB: Back in november the air district presented an update of where we are at (from 2018-now). They reanalyzed some assumptions
      - We should find that report and link to it..
          - Juan did look at it. 
              - The big change is that they originally used the 2017 EMFA 
              - In 2021 the report shows 70% lower PM2.5 emissions from brake wear
          - BB: can you specifically reference that you got this from the old report?
  - BB: should we be talk about what baseline that we should be using? Since it seems like they are moving things around.. Makes it look like there is improvements.
  - BB: Do we really need to use the airport site for windrose? 
      - Can we use the air district source??
          - Can we get that data?
      - JPG: Used iowa tool. Says insufficient data, except for the airport weather station.
          - Can look into the air district source..
          - Only one of them actually meets the standards from monitoring (in owning our air report)
  - BB: speeding up has higher emissions.. Ive read start stop has higher emissions.. Are we comparing that?
      - Can we also have a next steps slide?
  - BB: Heavy trucks not the highest contributor?
      - Just for PM2.5 but what about black carbon
      - JPG: not sure we can get emission factors for black carbon
          - Fletch: in the past to estimate UFP from EMFAC had to make stuff up based on literature.. 
          - Ivan: we’ve found that it is NOT a consistent fraction
          - Fletch: may need to simulate UFP for vegbuffs… may need to go back to normalized factors.. 
  - BB: can we have a side by side comparison of the pollution coming from the freeway, and coming from the road.. 
      - Light duty compared to trucks. Trucks can be aggregated. 
  - The claim is that the truck traffic won’t go up much. But we should look at the truck study.. 
      - Need to do a scenario based on the truck management plan
  - We were hoping also to present the old things that we found
  - Have a transition slide to why we are getting way more intense with our CFD modeling.. 
  - Want to be able to present things to the port and community soon…
      - We are moving faster in January on the design… 
      - Should we just be using the previous models? Or should we 
  - Want to look at the impact of the tile 2 for frontage road diet if we want to pitch a $10 million road redesign project.
Prescott Simulation 2024 
  - This deck is a tightened up version of our internal slides..
  - There is also some material in the miro board where we were working
      - Plan to bring that in to this presentation. 
  - Overview, some methodology slides, then goes scenario by scenario
  - Started with 3 planting scenarios
      - Scenarios:
          - Scenario 1 no veg. 
          - Scenario 2 existing conditions
          - 3  caltrans and immediate planting
          - 4 Road diet + caltrans + immediately plantable
          - 5 road diet only
  - Scenario 3 compared to existing conditions shows a marginal decrease in the neighborhood. 
      - We can probably show all the scenarios 3-4 together and explain that each of them do make the neighborhood better. But there are some differences
      - Improvement at pedestrian height most pronounced at a specific area. The improvement decreases as you get further from the interventions
  - Scenario 4 only includes some of the immediately plantable?
      - Why does scenario 4 look better than scenario 3??
      - WHAT?????
  - Comparison of scenario 4 and scenario 3 attempts to isolate the planting effect in the canyon
      - You get minor changes
          - It looks worse but not fair because of the missing immediately plantable higher up…
      - The soundwall planting is more effective than the road diet
  - Brent wants the diagrams to be clearer, very unclear which of the diagrams is showing which scenario
      - MV: we can use our pictorial diagrams to make it clear which diagrams are which
      - BB: want the plans compared to plans, and sections compared to the sections
      - BB: could we have a line chart comparisons between the scenarios. 
  - Scenario 3 Scenario 4 & Scenario 5 plans compared
      - Caltrans + Immediately plantable
      - Clatrans + Road Diet
      - Road diet by itself
  - Scenario 6 immediately plantable only 
  - Scenario 8 everything
      - Road diet is fully planted all to the right of the road
## November
### 2024-11-27 MV IH check in
Attendees: Mei, Ivan H
Links: [WO\_Figures\_Report presentation ](https://docs.google.com/presentation/d/1gOMcZB8HaKOxiLKeyL1BlnuHfjYKyzPcZ_ypcazmSPc/edit#slide=id.g2d58558950e_0_6)
Notes:
  - Ivan made a slide deck with Juan
      - Getting some good results that are exciting
  - Juan took some proactivity in digging into the air district updates (emissions factors)
      - Ivan wasn’t equipped to have the same analytical precision
      - Juan was able to answer many of our questions by reviewing the materials in depth
          - Slide 17/18: he was able to run the simulation for the different particulate sources
          - So we have traffic types, brake and tire
      - We should get juan to present this information to all of us
          - BB fletch, ivan, mei, woeip, and air district
  - Brent said we need things more digestible..
      - Small documents that makes one point very well
          - Ivan wants to do that: make short documents explaining things
  - In this slide deck we have results that gives us good info re: what would change if we eliminated all heavy vehicles, or changed to an all eclectic fleet
  - When could we put together a presentation for WOEIP?
      - There isn’t necessarily a lot of preparation needed
          - We should schedule an internal presentation for next tuesday
              - Hyphae only
      - Ivan: Part of our issue is we make things too complicated
          - We pile on nuance and tell people not to make conclusions
              - Then they obviously think its inconclusive
          - Juan is really good at keeping things simple
          - Lets try to refine things for our audience, and figure out what core conclusions we can support
              - Workshop internally tuesday and then meet them on friday
                  - Maybe scott, brian, margaret etc can join us. Get them on the same page. 
  - Action: Mei will set up an internal presentation for tuesday. Ivan and Juan will prepare
Next actions:
- [ ] Mei will set up an internal presentation for Tuesday
- [ ] Ivan & Juan will prepare for that presentation
- [ ] Team will discuss which conclusions we can support
- [ ] Mei will set up simulations meeting with WOEIP
## 2024-11-19 | [IH:JG check-in](https://www.google.com/calendar/event?eid=czFja3FjaWF2bzRkdnZjbm00NTQxczdiYWFfMjAyNDExMTlUMTczMDAwWiBqdWFuQGh5cGhhZS5uZXQ)
Attendees: [Ivan Heitmann](mailto:ivan@hyphae.net) [Juan Penaloza Gutierrez](mailto:juan@hyphae.net)
Attached files: [Modeling Development Planning Notes](https://docs.google.com/document/u/0/d/1kFWqn8Zkw5p-2wk9bIDVF2f1qs_O0E77RSBi9gpk_-o/edit) 
Notes
  - Include Tile 1 results in AQ report and slides 
  - Tile 2 computational domain, mesh, boundary conditions are set
  - Traffic zone/lanes creation process for individual links is complicated 
  - Will need to continue manually separating the traffic lanes. 
  - Need to develop simpler insights for modeling results: 2 page reports with a couple of figures and reference
  - Send AQ 2 page report for Tile 1 
Action items
- [x] IH export vegetation for Tile 2
- [x] JPG separate road zones for Tile 2  
- [ ] JPG run wind sim for Tile 2
- [ ] JPG run pollution sims (x6) for Tile 2
- [ ] JPG slides for AQ 
- [ ] IH and JPG collaborate on 2 page report for Tile 1
### 2024-11-08 | [Prescott status update](https://www.google.com/calendar/event?eid=NGpxN2VnaG5xdmZnbnVwYmhiYjgzMzUxNjggaXZhbkBoeXBoYWUubmV0)
Attendees: [Juan Penaloza Gutierrez](mailto:juan@hyphae.net) [Ivan Heitmann](mailto:ivan@hyphae.net)
Notes
  - Need proposed conditions model to compare side-by-side
  - Tile 2 domain geometry
      - vegetation is missing for tile 2 - IH
      - traffic lanes for tile 2 - IH
  - Emissions inventory needs work…
      - (Given that traffic represents only \~10% of pollution)
      - Juan make a very logical flow diagram or outline of what the inventory affects downstream in our process - JH
  - Strategy for modeling
      - Are we going to look at other sources?
Action items
- [ ] Flow diagram / list of emission inventory variables we need to know
- [ ] 
### 2024-11-06 | [IH/MV 1:1](https://www.google.com/calendar/event?eid=cGI4czEyOTNxODRhN3Y4cTRsOGxhc3Y1NTBfMjAyNDEwMDlUMTYzMDAwWiBpdmFuQGh5cGhhZS5uZXQ)
Attendees: [Mei Visco](mailto:mei@hyphae.net) [Ivan Heitmann](mailto:ivan@hyphae.net)
Notes:
  - Updates on what has happened since our last meeting:
      - Not a lot of progress: Juan has been busy with other things
      - Slide deck?
  - Ivan needs to meet with Juan to figure out what is going on and where they are at
      - Juan was putting together exports and visualizations for other grant that was being worked on
          - Made some figures from results, wanted some graphics to include in the grant
  - Almost ready to move on from documentation
  - Worked on air district email with Brent
  - What is available over next 2 months?
      - Ivan will be taking some time in November and December
      - Marin city will be starting up again
      - Someone allocated Ivan to work on stockton
      - Will be trying to help Max make our grant process less insane
      - Field semester need to cut back on putting so many hours
Action items:
- [ ] Juan & Ivan to meet and summarize work completed so far
  - [ ] Update on where we are and where we are going
## October
### 2024-10-11 | [Streetlight data observations](https://www.google.com/calendar/event?eid=NW8yaDZyMWpwaHZwaGYwY2dvNGk5djJwYmogaXZhbkBoeXBoYWUubmV0)
Attendees: [Brent Bucknum](mailto:brent@hyphae.net) [Ivan Heitmann](mailto:ivan@hyphae.net) [Juan Penaloza Gutierrez](mailto:juan@hyphae.net)
Notes
  - Model extreme traffic conditions (worst case scenario). Take data at 1 pm.
  - A thing to try: assume all electric cars and keep the number the same and substitute the emission factors
  - Future consideration: brake and tire wear (emission factors)
  - Prioritize having an advisory committee beyond AQMD {BB}
  - Cross check StreetLight data with other resources. 
  - Anomaly over Frontage Rd (westbound). Proposal: Take data symmetrically based on opposite lanes. 
  - AERMOD data is different from StreetLight. 
  - Owning our air report mentions StreetLight for composition of vehicle fleet 
  - Missing deliverable: cleanup spreadsheet to show counts/percentage 
  - Rodeo refinery impact
      - People are skeptical about Rodeo AERMOD results
      - AERMOD being 2D… but refinery and town are in canyon
      - 
Action items
- [ ] Clean tables of input numbers that go into the model (hopefully with graph/chart)
- [x] Block out time for technical assistance for multiple grants (including cost estimates) (help Max) (Stockton, Rodeo)
- [x] Schedule meeting with IH and JPG to break down time allocations
- [ ] Research on point source CFD and fence-line monitoring data
- [ ] Work with Max to make list of people for committee
- [x] Assign Brent to approve AQMD email
### 2024-10-07 | [IH/MV 1:1](https://www.google.com/calendar/event?eid=cGI4czEyOTNxODRhN3Y4cTRsOGxhc3Y1NTBfMjAyNDEwMDlUMTYzMDAwWiBpdmFuQGh5cGhhZS5uZXQ)
Attendees: [Mei Visco](mailto:mei@hyphae.net) [Ivan Heitmann](mailto:ivan@hyphae.net)
  - Fletch reviewed methodology doc
  - JPG out of office: potentially because of category 5 hurricane
  - Dug through streetlight data, have questions and issues.
  - Want to set up call with Brent
      - Potentially next week, walk him through what JPG and IH have produced
  - In a good position to resume conversation with BAAQMD folks
      - Want to work on taking our internal chat and turning it into a set of questions. 
      - Can get the ball rolling on that before meeting with brent
          - Want their take on emissions factors and stuff. 
          - Should draft email for that
  - IH busy this week
  - Want to start a slide deck 
      - JPG has visuals of winfield from area of interest
      - Want to structure it for broader audiences
  - Currently going over some of the hours estimates
      - Some of the hours can be diverted into R\&D
      - Running up against allocated time on subtasks
      - Mei suggests talking to Brent during the meeting they are planning
          - Figure out how to reel in scope creep
  - IH is worried about the emissions \_\_
      - Don’t think we should use Streetlight as the most accurate version..
          - There are some unknownst/discrepancies
      - In the aermod parameters, frontage had 1/20 of the truck traffic represented by  the freeway. But in streetlight it is 30-40%
          - That is a big difference
      - Streetlight is showing southbound traffic, 1 segment has extremely low number. So it looks like we have way more northbound than southbound traffic.But looking at other segments, its not consistent
          - The analysis will be directly impacted by this question.
          - And how our results compare to AERMOD will be influenced…
      - Has BAAQMD looked at streetlight? Are they aware of it? We should ask them.. 
      - We don’t have to rerun the simulation update pollution numbers. 
          - So process can continue, and we can fine tune emissions in parallel
          - Not wise to continue using Streetlight without interrogating its reliability
Action items
- [x] Meet with Brent regarding Streetlight data
- [ ] Email AQMD regarding emissions
### 2024-10-04 | [chart brainstorming sharing session](https://www.google.com/calendar/event?eid=MmJicjk3c2NqOWk3bHUwbXVyOHNrMHJpODcgaXZhbkBoeXBoYWUubmV0)
Attendees: [Juan Penaloza Gutierrez](mailto:juan@hyphae.net) [Ivan Heitmann](mailto:ivan@hyphae.net)
Notes
Investigate Streetlight Data and Traffic Count Accuracy
  - Investigate if traffic data from Streetlight is accurate or contains errors.
  - Hypothesis: Trucks may be exiting the freeway at Grand Avenue, using frontage roads.
  - Analyze if geometry needs to be split for accurate representation of traffic flow.
  - Compare Streetlight data with other models (e.g., AERMOD) to check inconsistencies.
Methodological Issues and Data Representation
  - Clarify methodological shortcomings, particularly the sharp drop in traffic count.
  - Assess if discrepancies could be due to assumptions made in segmenting the freeway.
  - Present issues to Fletch for insights and additional feedback.
  - Determine if the 50-count data point in the analysis is erroneous.
Narrative and Analytical Focus
  - Craft a compelling narrative for the data to tell a coherent story.
  - Assess whether further data exploration or graph generation is necessary.
  - Consider using origin and destination data to better understand traffic flows, particularly related to the Southbound freeway links.
Emissions Modeling
  - Determine whether to use normalized schemes in ENVI-met based on traffic counts or input specific emissions factors.
  - Evaluate emission factors based on vehicle speed and road types (e.g., freeway vs. surface streets).
  - Assess if separate simulations for various pollution sources (exhaust, tire wear, road dust) should be run.
  - Consider using MFAC data for future emission factors, possibly extending to 2050.
Open Questions and External Validation
  - Prepare an open-ended question for AQMD about assumptions in their updated models and how they handle traffic counts and other factors
  - Investigate how future traffic projections were handled in prior Owning Our Air studies (e.g., 2017-2024 analysis).
Next Steps and Action Items
- [ ] Add to methodology document summarizing data issues 
- [ ] Explain findings to AQMD and ask for feedback
- [x] Reach out to Streetlight Support if the origin of the discrepancy remains unclear.
- [ ] Follow-up meeting with Fletch
- [x] Look at origin/destination data to see if that clears up the question
##### 2024-10-01
###### *Problems with mesh and lots of buildings close together*
CANCELED Try bounding box approach away from aoi
- [x] Try further mesh refinement to 0.25m around buildings close to each other THIS WORKED
- [x] Fletch fix his script THIS ALSO WORKED
- [ ] Updating ENVI-met traffic source parameters
###### *Charts*
What charts can we generate to tell our story?
- [x] Schedule a chart brainstorming session
## September
### 2024-09-25
  - Had to ask fletch to re-run some things, may have completed yesterday
  - BB IH JPG have meeting to discuss emissions
      - Made some good progress
      - Established the central study questions that they will begin with:
          - [Table of Simulations](#heading=h.co1yihc4mui1)
          - 2024a is our previous run
              - 2024b is our next set
                  - Frontage truck route (adding the truck route)
                  - Local traffic (surface streets) + freeway
                      - Trying to understand the relative impact of the frontage road traffic to other pollution sources in the existing condition
                  - Different fleet types
  - Did all the questions get answered in order to proceed productively?
      - Next 2 important meetings:
          - Make sure the simulations they are specifying meet with his expectations
              - Could have the table list more of the parameters, setting the parameters so we are more on the same page
              - May be able to do this asynchronous instead of a meeting
                  - Give him a table to review that he can ask questions about
          - Figure out what elements of the analysis that are not an openfoam question
              - May need IH and JPG to do analysis outside of CFD
                  - Charts
                  - Little maps
                  - Line graphs
              - Some issues that BB is discussing that will be important to continue to define
                  - Some things are better understood by further processing into a graph or things, and so they will need to produce those things
                  - It takes effort through conversation with him to get to a clean analytical scientific question
                      - He has ideas, narrative, and questions that aren’t structured in an analytical way
                      - Define the data needed, how it will be aggregated, and the attributes that they will want to quantify
                      - Can things be done in GIS? MatLab? Spreadsheet? Can streetlight exports be brought into spreadsheet and make a google chart.
                  - Have to think forward a few steps: 
                      - Want to have a chart that we show the public that demonstrates hypothesis 1
                          - What is hypothesis 1? Don’t know
                          - What kind of chart? Don’t know
                          - What does the public want to know? Also don’t know. 
              - This will probably require several back and forth meetings with BB. 
                  - This is time consuming, and not exactly what was scoped 
          - Need to define these tasks, put some hours to them
  - Questions
      - Revision or thought about the emission model
      - Trying to tease out what are the dimensions that we should try to differentiate
          - What is on the x and y axis
          - What is the trend over the next 10 years
              - We know tail pipe emissions going down
              - But break and road dust possibly going up 
              - How do we characterize that and the impact on the exposure?
      - We have question: we have more gentrification. How can we quantify the impact on the different demographics?
          - You could potentially do that with a chart
          - Distance from freeway, location of development, location of disadvantaged neighborhood
          - Can see how line graph
  - Process to get there:
      - Figure out what data inputs we need
      - Figure out what deliverables and figures we are producing
      - What are plotted on x and y axis
      - Are we going to have bar graphs?
  - Need to coordinate with BAAQMD
      - What are their new assumptions
          - How are they quantifying different sources
          - Some coming from EMFAC. what are the updates?
      - Show them our methods & ask specific questions
          - What did they make changes to and why
  - Allocation assumptions
      - Planning this 6h
          - Involves defining questions
          - Brainstorming what processes will help answer those questions
          - Review from brent
      - Creating figures
          - October 12h
          - November 12h
      - BAAQMD
          - Already allocated
  - What are the boundaries?
      - Pretend example: Exposure due to truck traffic will go down 20%
          - But we know that's only the minority of the problem
          - Trucks will be 2x as heavy and will create more brake dust 
      - By making lines of question more precise we can counteract the natural tendencies of scope creep.
          - Figure out what each of these tangents actually will be. 
  - Need to do the homework between meetings to see all that BB brought up and make sure we’ve prepared suggested way to handle these questions
Next actions:
- [x] Need to check in with Fletch
- [x] Need Fletch to review the suggestions on what to include and what to ignore (methodology doc)
- [ ] Brainstorm the questions/processes for additional figures
  - [ ] Track the list of figures in this doc
    - [ ] Can be a table copied in from a spreadsheet
  - [ ] Potentially re-arrange spreadsheet
- [ ] Complete the wind field simulation
- [x] Digital twin revisions
- [ ] Start a presentation
  - [ ] Start outlining
  - [ ] Define what is and isn’t in the simulation, make a placeholder slide on that
### 2024-09-20 MV BB check in
  - Decided to compare the relative contribution of the freeway vs the frontage road itself.
  - Ms. M wondering if the greening is going to have impacts on the community, or if its mostly helping the new housing development. 
  - Many of the things they are comparing they don’t have to necessarily do as many of the complex simulations
  - Already have some interesting insights that can be compiled into a report.
      - What info do we want to present or not? 
      - Can plan to ask for a progress update even if it's not totally finished and conclusive.
  - 
### 2024-09-20 *meeting with Brent, Juan, Ivan*
Understand what the questions are in the community
Unpack the relative impacts given the data that exists
Relative difference of possible plantable area impacts and ROI
Recreating our ENVI-met studies in OpenFOAM
Port argues the traffic won’t go
Questions to study
Quantify relative impacts of frontage road vs. the freeway
Charts of Streetlight data X EMFAC
Academic / Scientific inquiry - How do we compare models of ENVI-met vs. OpenFOAM (results)
###### *Actions*
- [ ] Communicate how and why our models are limited and what information they incorporate (for other audiences including the public)
- [ ] Consider written and video documentation to support explanation of what is calculated in this model
### 2024-09-18
Troubleshooting domain geometry
Juan working on methods docs
BB sick
  - Assigned Juan his task to work on the BAAQMD task
  - Ivan reviewed the doc himself and saw if anything additional needed to be added. Then sent BB the agenda to review this doc. Said to make a note if there were things that needed to be included.
  - Ivan handed off the domain to Juan. He will come up with any problems and they will work together on solving those issues as they come up. 
  - Ivan decided not to assign additional work to Futerfas. 
      - Been very busy on field semester. And may not be a good task for him: more involved. Not just a simple modeling task.
      - Ivan is doing it himself. 
  - Juan was able to run a few tests. Have some blocking issues to surmount. But the tests looked good. 
  - What needs to be completed this week?
  - What needs to be done to reach the first wind solution deadline? (This will lead to a completed wind field that we can look at as a team for the existing condition)
      - Need to revise the building models (to eliminate gaps) IH
      - Hand off existing vegetation IH
      - Need to refine the mesh so that it will converge near the buildings JPG
      - Run the model JPG
  - Currently put hours/budget in to do 2 tiles
      - If we follow the current plan, how much of that budget will we expend
  - Currently focused on the traffic quantity, but that doesn’t require the simulation to be re-run for different quantities, so don’t have the same computational lift if we do 3-4 different traffic scenarios
###### *Allocations / budget*
###### *Actions*
- [x] Compose table of required sims
- [x] Revise building models
- [x] Hand off existing vegetation
- [ ] Mei should find out JPG billing rate
### Beginning of september → 9.11.24
  - Previous Envimet results 
      - Showed previous completed modeling work to Juan
          - He will help with doing some more numerical charts of results
      - Decided to use the same domain boundaries for this round of openfoam 
      - There is a bug in the envimet program, so Ivan will need to produce updated tables before he can proceed
  - Domains
      - Decided to use the same domain boundaries for this round of openfoam 
          - There is a bug in the envimet program, so Ivan will need to produce updated tables before he can proceed
      - Ivan working on the updating domains
          - Have a different process to produce openfoam domains compared to what was used for envimet
              - New geometry is required (triangulated meshes)
      - On track for giving Juan these domains to begin working on this week
      - Ivan wants Eric Futerfas to update the rhino model - need to assign him that
  - Planning
      - Outlined this schedule and the hours required, then got feedback from Brent
      - Decided that we wanted to use only a part of the budget available to us right now
          - Not going to do a WRF model right now
  - Streetlight
      - Juan has successfully started using streetlight and has coordinated with Travis
      - Decided that Juan will continue to export and prepare his own data & use the procedure outlined in this document to prepare the data for use in our simulations
  - Focused on the different truck traffic scenarios
  - Feedback needed from Brent
      - Have proposed a procedure for modeling pollution and on traffic in this documents
          - Brent may have ideas or things he wants addressed
      - Some steps may be required to make sure the steps in this doc are comprehensive
          - Need to show Brent how the parameters of the pollution are being set up and why
      - The doc has been updated, and a table created, this now needs to be digested by Brent so that feedback can be given
      - Had previously had things to talk about but BB asked to do fewer meetings and more asynchronous collaboration
          - So we will schedule review time for him early next week
  - Need to send a methodology doc to BAAQMD 
      - Critical to get this reviewed as soon as possible to give us the proper credibility when showing our results to the Port later
      - Create paper that could be published in a journal
          - Something scientific, doesn’t need to have all the information included in our larger methodology doc
###### *Actions*
- [ ] Make sure rationale for protocol Brent is reviewing is comprehensive
- [x] Write up agenda with specific asks for Friday meeting
- [x] Let Brent know he needs to review this during the monday meeting
- [x] Schedule some review time for BB on tuesday
- [x] Give Juan more instructions on how to update the BAAQMD doc / paper
~~Assign futerfas task~~
Check if completed next week
  - Ivan completed the domains and handed off to Juan
  - Mei checks in w/ Ivan Friday to make sure above actions completed
## August
Mei met with Brent and Ivan and summarized previous notes on how to move forwards.
##### Simulation Plan:
The following is a summary of the next steps that need to take place to advance the simulations, with the goal of having them ready to present to the community in October:
[From 6/21/24 Meeting notes](https://docs.google.com/document/d/1wFkXMxo8N8z1PPsSm1hyOof1FhT_DbJMwE2SViRIVLA/edit#heading=h.rviq4jv46e1v)
  - The freeways and grey infrastructure need to be revised in rhino
  - R\&D about how to tile the simulations
  - Model traffic volumes, the pollution source volumes
  - Create a hypothesis. Pose some study questions.
      - Do we think lofting, or deposition are the governing dynamic. Have more conversations with Venkatram
  - Figure out the workflow for implementing variable LAD in OpenFOAM.
##### <comment_start id=kix.iyv9yfdol4es>Truck inventories<comment_end id=kix.iyv9yfdol4es>
Brent has asked Ivan to begin preparing to include different truck levels into the simulations. 
  - Compare different truck levels
      - With and without trucks
      - Different inventories
      - Current surveyed truck quantities vs. double vs. none
      - Quantify the difference between freeway and frontage for truck emissions
      - Simulate emission changes without veg changes
  - What counts should be used?
      - If we have decided not to use Aermod, what counts should we use?
      - Can find truck inventory inputs from traffic model produced by Kittelson (they did counts)
          - [Screenshots in this presentation from their survey](https://docs.google.com/presentation/d/10UIeLFWe_W8k-DvbE2ElggfB5-6mpE1IXdz5XbM4p9o/edit#slide=id.ge78b90b7f7_0_127)
          - [Kittelson counts website](https://maps.kittelson.com/OaklandCounts)
          - [Kittelson Memorandum on Truck Management Plan](https://cao-94612.s3.amazonaws.com/documents/Truck_Route_Memo_20200601_clean.pdf)
## July
  - Ivan begins preparing the plan
  - Brent & Ivan meeting
## June
  - Meeting defining next round of simulations
      - [From 6/21/24 Meeting notes](https://docs.google.com/document/d/1wFkXMxo8N8z1PPsSm1hyOof1FhT_DbJMwE2SViRIVLA/edit#heading=h.rviq4jv46e1v)
## May
  - Simulations
      - Ivan prepared a report to go into the invoice, which describes some of the progress of our simulations
## April
  - BAAQMD Coordinatioin
      - Met with Steve Reid 4.8.23
          - Ivan got questions answered about BAAQMD data that was provided to us
      - Worked on methodology report for the BAAQMD to review: [Particulate Modeling Methodology ](https://docs.google.com/document/d/1OyeAfZOvdCLvCuEkVcBBUT8O--mF9MtTjBfLKnT2DiI/edit#heading=h.mtix9t3ba8qx)
## March
  - BAAQMD Coordination
      - Had a meeting with BAAQMD district on 3-5-24
          - Had prep meeting before that to create an overall agenda for discussion, summarize our previous discussion, and settle on questions we wanted to ask
          - During the meeting itself there was a lot of discussion within the air district as to what type of data that they were allowed to share with us.
      - After the meeting Fletch re-submitted the data request and they sent the data to us
          - Ivan created [this graphic in Miro ](https://miro.com/app/board/o9J_lvNfKVo=/?moveToWidget=3458764583940456197&cot=14)to depict the data that he received
              - He sent a follow up email to Steve Reid to get a download on the data that he received. 
      - Ivan has also been working on a [simulations methodology document](https://docs.google.com/document/d/1b7oNth9Yw7JwazRIa9A1Y1El4LgcnmijmiyNYPujUNs/edit?usp=sharing) that we want to have reviewed by BAAQMD 
          - He has asked our new CFD modeler Juan Gutierrez to review it, which he will complete in April
## February
  - Collaboration Meeting with BAAQMD
      - Recieved feedback from BAAQMD team. They were very open to assisting us by sharing their data with us. Gave us some feedback on our models/approach. 
      - It was determined that we would need another meeting to figure out the more technical details as to how we would want them to support us in sharing data.
      - [Notes/Transcript from meeting](https://docs.google.com/document/d/1GG6Sy1ium_p9uyyrUWcZ1deJbO2dx2XTH5SYNGr69KY/edit?usp=sharing) (pdf version added to deliverables folder)
  - Modeling
      - Completed more simulations
      - Reviewed modeling results 
## January
  - “Email Alicia @ BAAQMD” Communications established with BAAQMD
      - Set up a meeting with Alicia and team at BAAQMD. This meeting was then postponed by BAAQMD to February 5.
      - In preparation for this meeting our team met to prepare an agenda and a presentation for the meeting. 
          - [Presentation](https://docs.google.com/presentation/d/1utoJlJgSDsff4EresHo9nruto3fCX1UAfensDFZprjM/edit#slide=id.g2669de129f5_0_0)
          - [Proposed Collaboration Scope](https://docs.google.com/document/d/1wmjIdx10VHLWNuTUL6FT0mJGigoC-Gk-MiKApeCsW0k/edit)
  - “Simulation Modeling” Ivan continues to work through simulations, document his findings, and present these to Mei so that they could be input into the community presentation. 


# [Doc Template]

# **How to use this template**
# **Title**
## **Subtitle**
# Heading 1
## Heading 2
### Heading 3
#### **Heading 4**
##### Heading 5
###### ***Heading 6***
### Section Heading
#### **Topic description 1**
This greening plan seeks to utilize academic research for optimizing air quality for health benefits. While there are many benefits that will be studied, this goal drives the design, prioritization, engineering, and weighting of all decisions that went into the greening plan.
#### **Topic description 2**
Est bitters single-origin coffee, air plant distillery brunch before they sold out tacos aliquip nostrud fixie roof party quis quinoa meh. Sint narwhal messenger bag tacos salvia. Humblebrag la croix waistcoat hella in trust fund. Everyday carry anim chambray drinking vinegar. Four loko kale chips snackwave, tempor qui ennui biodiesel dolore subway tile iceland direct trade sed godard. Blue bottle nulla ex echo park butcher ut mumblecore gluten-free in poutine hashtag brooklyn chillwave.. 
##### Sub-topic 1
Lorem ipsum dolor amet live-edge deserunt la croix ea squid art party air plant exercitation tbh mumblecore consequat roof party. Bicycle rights PBR\&B fingerstache, salvia velit ramps poutine stumptown wayfarers lumbersexual activated charcoal helvetica vegan fanny pack. Sartorial kogi taiyaki dolore pariatur slow-carb bespoke prism aute tattooed skateboard franzen trust fund. Vexillologist wolf ipsum elit laboris, humblebrag hella activated charcoal chicharrones lomo raw denim microdosing dolore literally.
   
[**Figure 1**](https://docs.google.com/spreadsheets/d/1G2il45zzM1dii0ZiZUQorIYjjhrXfvDInblstbj0Hu4/edit#gid=0): Distribution of plantability classes as                                              [**Figure 2**](https://docs.google.com/spreadsheets/d/1G2il45zzM1dii0ZiZUQorIYjjhrXfvDInblstbj0Hu4/edit#gid=0): Zoning type of plantable area                                                    percentage of total area in target neighborhood
### Tables
|  |  |
| :- | :- |
| **Table of Items** |  |
| Number | Description |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |




<!-- connector commentThreads: verbatim JSON as returned by read_file_content -->
```json
[
  {
    "commentId": "AAABVEUJ0r4",
    "headPost": {
      "authorName": "Juan Penaloza Gutierrez",
      "content": "https://docs.google.com/document/d/16s2VXUswOjwzMrLMe4Y9Mm7p81hvTwsuqotOH8LUOMU/edit?tab=t.0",
      "modifiedTime": "2024-11-18T20:16:29.397Z",
      "postId": "AAABVEUJ0r4"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABVEUJ0h8",
    "headPost": {
      "authorName": "Juan Penaloza Gutierrez",
      "content": "Updated the email based on the recent updates from BAAQMD",
      "modifiedTime": "2024-11-18T18:29:25.815Z",
      "postId": "AAABVEUJ0h8"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABVEUJ0h0",
    "headPost": {
      "authorName": "Juan Penaloza Gutierrez",
      "content": "@ivan@hyphae.net I am unsure what this means: \"How to integrate it alongside AERMOD quantities\"",
      "modifiedTime": "2024-11-18T18:28:40.166Z",
      "postId": "AAABVEUJ0h0"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABVEUJ0hY",
    "headPost": {
      "authorName": "Juan Penaloza Gutierrez",
      "content": "BAAQMD released updates on Oct 10, 2024. Most of these questions are answered in the reports. I copied some of the relevant updates below.",
      "modifiedTime": "2024-11-18T18:54:58.876Z",
      "postId": "AAABVEUJ0hY"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABWkjOj-g",
    "headPost": {
      "authorName": "Ivan Heitmann",
      "content": "@mei@hyphae.net @brent@hyphae.net @juan@hyphae.net - drafting an email to AQMD",
      "modifiedTime": "2024-10-21T23:58:48.996Z",
      "postId": "AAABWkjOj-g"
    },
    "replies": [
      {
        "authorName": "Ivan Heitmann",
        "content": "@brent@hyphae.net made some updates and cleaned up your additions",
        "modifiedTime": "2024-10-21T23:58:48.996Z",
        "postId": "AAABXDpTqoQ"
      }
    ],
    "status": "OPEN"
  },
  {
    "commentId": "AAABVg4qeIU",
    "headPost": {
      "authorName": "Brent Bucknum",
      "content": "this should still be the focus. hover I feel like further refining emissions assumptions is necessary. also predicting previous vs future scenarios of emissions, ex lss diesel vehicles is important for evaluating the potential impacts of vegetation the future.",
      "modifiedTime": "2024-09-17T21:32:10.526Z",
      "postId": "AAABVg4qeIU"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABVg4qd5c",
    "headPost": {
      "authorName": "Brent Bucknum",
      "content": "while this is one of our focuses we do not want to explicitly say so. we do not politically, necessarily want to get sucked into this battle between residents and port. we're still focused on assessing the possible impacts of vegetated buffers, and some of that may be helpful to port and communities discussion about the truck route",
      "modifiedTime": "2024-11-06T17:26:34.705Z",
      "postId": "AAABVg4qd5c"
    },
    "replies": [
      {
        "authorName": "Ivan Heitmann",
        "content": "reworded",
        "modifiedTime": "2024-09-25T16:34:52.064Z",
        "postId": "AAABV52s0lE"
      },
      {
        "authorName": "Ivan Heitmann",
        "content": "",
        "modifiedTime": "2024-11-06T17:26:34.705Z",
        "postId": "AAABXaKzNqQ"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABVK_B5q8",
    "headPost": {
      "authorName": "Ivan Heitmann",
      "content": "@juan@hyphae.net i think it would be very useful if we could compare the traffic counts from the different data sets / inputs. Probably here neglect diurnal profile and just look at ratios of vehicle types and ratios of street class",
      "modifiedTime": "2024-09-20T18:42:56.767Z",
      "postId": "AAABVK_B5q8"
    },
    "replies": [
      {
        "authorName": "Ivan Heitmann",
        "content": "",
        "modifiedTime": "2024-09-20T18:42:56.767Z",
        "postId": "AAABWHKrI-o"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABU6EgmLU",
    "headPost": {
      "authorName": "Ivan Heitmann",
      "content": "@juan@hyphae.net why are you proposing zone level specificity rather than segment level?",
      "modifiedTime": "2024-09-06T20:53:33.492Z",
      "postId": "AAABU6EgmLU"
    },
    "replies": [
      {
        "authorName": "Juan Penaloza Gutierrez",
        "content": "I am referring to the analysis type option. Zone activity is used to analyze traffic starting in, stopping in, or passing through one group of locations. It can give you a good overview of vehicle density, speed, and types across different parts of your urban area. The group of locations/zones are the road segments the user will select. Streetlight offers other analysis options such as: Turning Movement Counts, Origin-Destination, Top Routes for Zones ...",
        "modifiedTime": "2024-09-06T17:41:48.123Z",
        "postId": "AAABU6EgmMw"
      },
      {
        "authorName": "Ivan Heitmann",
        "content": "",
        "modifiedTime": "2024-09-06T20:53:33.492Z",
        "postId": "AAABU6EgmuA"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdfVJ4bQ",
    "headPost": {
      "authorName": "Ivan Heitmann",
      "content": "@mei@hyphae.net did i ever show you this?",
      "modifiedTime": "2025-02-21T05:16:55.827Z",
      "postId": "AAABdfVJ4bQ"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABU5rEbPk",
    "headPost": {
      "authorName": "Mei Visco",
      "content": "@juan@hyphae.net @ivan@hyphae.net Now that we've overhauled this doc to match our methodology template, you can find some of the more simplified reporting on what our next steps are down here",
      "modifiedTime": "2024-09-20T18:41:48.762Z",
      "postId": "AAABU5rEbPk"
    },
    "replies": [
      {
        "authorName": "Ivan Heitmann",
        "content": "",
        "modifiedTime": "2024-09-20T18:41:48.762Z",
        "postId": "AAABWHKrI-c"
      }
    ],
    "status": "RESOLVED"
  }
]
```
