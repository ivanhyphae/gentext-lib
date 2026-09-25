---
id: cand-fresno-extreme-heat-analysis-doc-s26-1
status: candidate
title: Hyper-local high resolution environmental modeling for extreme heat analysis
type: method
summary: A methodology for generating meter-scale UTCI and shade models using 3D digital twins derived from LIDAR data, meteorological
  inputs, and the SOLWEIG solver to simulate thermal conditions and evaluate intervention designs.
words: 444
places:
- Fresno County
orgs:
- USGS
- UC Berkeley
projects: []
facts:
- claim: LIDAR data used is from 2019-2023
  quote: aerial LIDAR data from the USGS 3D Elevation program gathered from 2019-2023
- claim: Modeling produces 1-meter resolution grid outputs
  quote: 1 meter grid for each of the 5 target project areas
- claim: 24 hourly estimates of mean radiant temperature are generated
  quote: 24 hourly estimates of mean radiant temperature in human occupied elevations on a 1 meter grid
- claim: SOLWEIG solver is used for irradiance geometry modeling
  quote: Urban Multi-scale Environmental Predictor (UMEP)'s SOlar and LongWave Environmental Irradiance Geometry model (SOLWEIG)
    solver
flags: []
quality_notes: Strong methodological description with specific tools and data sources; ready for reuse with site-specific
  LIDAR and meteorological inputs.
provenance:
  origin: extracted
  source:
    asset: fresno-extreme-heat-analysis-doc
    sha256: c9296faa94c9e16bf7970fdd5895e08b0d85aa624f95c04a2bc570252abd0661
    section: s26
    path: 'D. Detailed Work Plan > Task 3: Extreme Heat Vulnerability Analysis > Approach > Methodology for Extreme Heat Vulnerability
      Analysis > Hyper-local high resolution environmental modeling.'
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

After choosing neighborhoods or corridors to target interventions, discussed in task description, we come back to further modeling work where we then utilize our own novel high resolution modeling to develop meter scale simulations. This includes shade and UTCI models at 1-10 meter resolution. This work combines the development of 3d digital twins of trees, buildings, terrain and other features from lidar data and simulation modeling of UTCI variables including air temperature, humidity and radiant temperature. These are novel datasets that we generate from our software pipeline. To conduct a simulation of 1-meter scale mean radiant temperature in the 5 target project areas, we will take aerial LIDAR data from the USGS 3D Elevation program gathered from 2019-2023, and use it to generate 3D models of the target areas, including building heights, and canopy leaf area index. We will then find selected historical days in which there was minimal cloud cover to simulate, which correspond to time periods where extreme heat was recorded. We will obtain hourly meteorological data from the nearest weather service stations which include regional wind speed, air temperature, pressure and humidity. We will also obtain estimates of total incoming shortwave radiation from the [CBE clima tool](https://clima.cbe.berkeley.edu/). These meteorological data points will be inputted along with the 3D model into the Urban Multi-scale Environmental Predictor (UMEP)'s SOlar and LongWave Environmental Irradiance Geometry model (SOLWEIG) solver. The outputs of this will be 24 hourly estimates of mean radiant temperature in human occupied elevations on a 1 meter grid for each of the 5 target project areas. These can be combined with estimates of wind speed, humidity and air temperature to produce 1 meter UTCI maps. From these 1 meter grids we can then calculate cumulative heat stress for specific pedestrian routes, discussed more in the pedestrian section. Here we can differentiate the temperature in the middle of the street from those under a tree on the sidewalk. We can see how hot it is on a basketball court vs under a grove of trees. We can also see how the thermal comfort is different at different times and how it changes how temperatures accumulate and radiate over the course of the day. With these models we target specific low tree areas of a neighborhood or segments of a corridor for intervention. We also work with communities to see where they live, work and play. Discussed further in the pedestrian section. In addition to running these models for prioritization and opportunity studies of the existing conditions, we will also run prospective intervention design prototypes selected from the 5 project focus areas to run through the simulations to estimate the benefits of designed interventions.
