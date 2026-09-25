---
id: cand-fresno-rfp-hyphae-2024-s8-1
status: candidate
title: High-resolution environmental modeling methodology for urban heat analysis
type: method
summary: Describes a multi-scale modeling approach combining satellite data, local climate zones, and hyper-local 3D digital
  twins to simulate mean radiant temperature and UTCI at 1-meter resolution for heat intervention planning.
words: 507
places:
- Fresno County
orgs:
- USGS
- CBE
projects: []
facts:
- claim: Local climate zones (LCZ) data is calculated at 30 meter resolution
  quote: Local climate zones (LCZ) data is calculated at 30 meter resolution
- claim: LIDAR data from the USGS 3D Elevation program was gathered from 2019-2023
  quote: aerial LIDAR data from the USGS 3D Elevation program gathered from 2019-2023
- claim: Modeling produces 24 hourly estimates of mean radiant temperature at 1 meter grid resolution
  quote: 24 hourly estimates of mean radiant temperature in human occupied elevations on a 1 meter grid
flags: []
quality_notes: Strong technical method with specific tools and resolutions; ready for reuse with site-specific data parameters.
provenance:
  origin: extracted
  source:
    asset: fresno-rfp-hyphae-2024
    sha256: 63d95c433e28d05c93d5c0d728f7fa1bb51a99f796a930a464613e694b9c8bce
    section: s8
    path: part 8
  authors:
  - kind: unknown
    id: Hyphae
    role: wrote
    verified: false
  extracted_by:
    model: claude-haiku-4-5
    prompt: x1
    date: '2026-09-25'
  verbatim: true
---

Other medium resolution data Local climate zones (LCZ) data is calculated at 30 meter resolution for a single time period and reflects 17 categories of local topology concerning feature types (buildings and vegetation) heights (tall, medium, short, none) and spacing (dense, medium, sparse). This can be used to stratify heat data (such as surface temperature) to prioritize where interventions are most likely to be plausible and effective. Similarly we use 100 meter dasymetric population density data and Cropscape crop mapping to estimate where people live or are likely to be working outdoors to adjust risk factors for heat stress estimates at the 30 meter scale. Hyper-local high resolution environmental modeling. After choosing neighborhoods or corridors to target interventions, discussed in task description, we come back to further modeling work where we then utilize our own novel high resolution modeling to develop meter scale simulations. This includes shade and UTCI models at 1-10 meter resolution. This work combines the development of 3d digital twins of trees, buildings, terrain and other features from lidar data and simulation modeling of UTCI variables including air temperature, humidity and radiant temperature. These are novel datasets that we generate from our software pipeline. To conduct a simulation of 1-meter scale mean radiant temperature in the 5 target project areas, we will take aerial LIDAR data from the USGS 3D Elevation program gathered from 2019-2023, and use it to generate 3D models of the target areas, including building heights, and canopy leaf area index. We will then find selected historical days in which there was minimal cloud cover to simulate, which correspond to 2 Jian, H., Yan, Z., Fan, X. et al. A high temporal resolution global gridded dataset of human thermal stress metrics. Sci Data 11, 1116 (2024). https://doi.org/10.1038/s41597-024-03966-x 13 time periods where extreme heat was recorded. We will obtain hourly meteorological data from the nearest weather service stations which include regional wind speed, air temperature, pressure and humidity. We will also obtain estimates of total incoming shortwave radiation from the CBE clima tool. These meteorological data points will be inputted along with the 3D model into the Urban Multi-scale Environmental Predictor (UMEP)'s SOlar and LongWave Environmental Irradiance Geometry model (SOLWEIG) solver3. The outputs of this will be 24 hourly estimates of mean radiant temperature in human occupied elevations on a 1 meter grid for each of the 5 target project areas. These can be combined with estimates of wind speed, humidity and air temperature to produce 1 meter UTCI maps. From these 1 meter grids we can then calculate cumulative heat stress for specific pedestrian routes, discussed more in the pedestrian section. Here we can differentiate the temperature in the middle of the street from those under a tree on the sidewalk. We can see how hot it is on a basketball court vs under a grove of trees. We can also see how the thermal comfort is different at different times and how it changes how temperatures accumulate and radiate over the course of the day. With these models we target
