---
asset_id: nsf-sbir-p1-final-technical-narrative
source_system: gdrive
source_id: 106c6Q81e2k-uP_3aMyBHX-msMlX8wW4l
source_title: "HYPHAE_NSF_SBIR_PHASE1_1938665_FINAL_REPORT_Technical_Narrative_rev3-1_1665615071242_0.pdf"
acquired: 2026-09-25
via: connector-text
tool: google-drive read_file_content (includeComments=false)
truncated: unknown
---

HYPHAE\_NSF\_SBIR\_PHASE1\_1938665\_FINAL\_REPORT\_Technical\_Narrative\_rev3 

NSF SBIR PHASE I PROJECT 1938665: Ecosystem Design Tool

FINAL REPORT BY HYPHAE DESIGN LABORATORY

Introduction: 1

Summary of Research Results: 2 Google Data acquisition and preprocessing: 2 LIDAR data acquisition: 2 Estimation of LAD from LIDAR data: 4 Deep Learning results: 5 Approach 1: grid-based (“chunkwise”) single image regression: 5 Approach 2: Pixelwise whole image regression: 6 Ground-Truth of LAD data: 9 Additional data types for deep learning pipeline: 9 Post Planting Validation: 12 Tree Placement Algorithm: 12 Back-end Data Handling Infrastructure: 13 Front End User Interface: 14

Unexpected Problems Solved: 14

Unexpected Problems Unsolved: 15

Impact of customer discovery on technological development: 15

From phase I to phase II and beyond: 15

Conclusions: 16 Link for full-sized figures: https://drive.google.com/drive/folders/1msrhBy72hPS10Tj5gbf3bSSKnEDbX4eK?usp=sharing

Introduction:

This project sought to develop a deep learning algorithm for estimating leaf area density (LAD) from commonly available street-view imagery. LAD is a meaningful expression of various ecosystem functions, in particular the ability of roadside vegetation to mitigate traffic-sourced air pollution. The inclusion of such LAD data in the ongoing Green Heart environmental clinical study in Louisville (and other environmental health initiatives elsewhere) will enable such data to be used to design ecosystem interventions that can be reasonably expected to reduce health care costs. The end product is a design tool to accelerate the adoption of such interventions. Creating the deep learning algorithm for LAD estimation required gathering concomitant street-view photography and LIDAR point clouds. The point clouds were processed to create an LAD estimate based on Beer’s law. The LIDAR data was then paired with corresponding street-view images to train a deep learning network to estimate the LAD from photographs. To make a usable software prototype, we also developed a user interface and back-end processing and database management system.

Summary of Research Results:

Google Data acquisition and preprocessing:

We developed an automated pipeline that takes an input bounding box from the front end user

interface, acquires roadlines from Open Street Map application programming interface (API), places points every 20 meters along the roadlines, then asks Google’s street view API for all of the street view photographs near each point. The photos are downloaded to our server where a semantic segmentation algorithm (PSPnet trained on ADE20k) segments the images into semantic categories of environmental interest, an example of which is shown in figure 1.

Figure 1: example of PSPnet semantic segmentation

The results are then returned to the user interface as points on a map, each which can be queried to get the results of the analysis and the processed photos. The PSPnet trained on ADE20k segments the images into trees, shrubs, grass, buildings, houses, roads, and 144 other semantic categories. The maps make environmental view indices (EVI) showing the percentage of the scene from that viewpoint which is in the semantic category (see figure 2 for three examples).

Figure 2: EVIs from semantic segmentation. Left, South Louisville tree view index. Right, West oakland tree, sky and grass view indices.

We have also started building training sets to further segment the trees into deciduous and evergreen. While the EVIs are themselves a dataset of interest to our customers which has been associated with health outcomes in the literature (and we have provided this data to health researches for inclusion in ongoing studies), our purpose here is to make the data more ecologically relevant by estimating surface area rather than simple semantic segmentation. To do that we trained a deep learning network on paired street view photographs and LIDAR data.

LIDAR data acquisition:

In March 2020 we scanned 88km of roadside vegetation with the Zeb Horizon rental scanner. The Zeb scanner uses a 16 laser LIDAR on a rotating gimbal, with proprietary software that must be processed by the rental agency. The Zeb also does not have 360o field of view, so it can be difficult or impossible to correctly align the scans with each other after they have been processed. This scanner also does not allow for sensor fusion with other sensors (like GPS or RGB cameras) as it sends all data to a proprietary data logger and has no other inputs or outputs. While this produced high quality point clouds that can be used to generate LAD metrics for ground truthing deep learning inference, they can not be used as training data as they are not precisely paired with RGB imagery, and geolocation can be extremely challenging as there is no paired GPS data. To remedy this problem, we acquired an Ouster OS0-64, which has 64 lasers, and 360 by 90 field of view, and has a User Datagram Protocol (UDP) data output that can be integrated with GPS and RGB camera for sensor fusion, image pairing and

geolocation. The decoupling of the sensor head from the data logging infrastructure also allowed us to place the sensor on a vehicle for road scanning or a backpack for closer, slower and more detailed scans of forests or other less accessible vegetation. We acquired a real time kinematic (RTK) GPS unit to allow time synchronized 2cm accurate global positioning with the LIDAR and RGB data.

Figure 3: top left, the Zeb Horizon Scanner. Top middle, Vehicle mounted Ouster LIDAR scanner with RGB 360 camera and RTK GPS. Top right, backpack mounted Ouster LIDAR with RTK GPS. Bottom, SLAMed point clouds from vehicle mounted LIDAR

To generate precise pairing of LIDAR data with RGB imagery requires extrinsic calibration; colocation in time and space of the camera and LIDAR sensors to within a few thousand microseconds. To accomplish this we attached the Garmin VIRB360 camera to the top of the Ouster LIDAR sensor (rig shown in figure 3, top middle), and used Robot Operating System (ROS) to synchronize the timestamps of each video frame (at around 30 frame per second) with the LIDAR frames (around 20 frames per second). It was found that a consistent delay of around 0.9s in the camera data could be compensated for through recalibration in post-processing. Because of the unique method used in the Garmin camera to create equirectangular 360 images from 2 hemispheric lenses, a significant amount of time went into developing a script to align the pixels of the LIDAR scans with the images, but a script was developed to accomplish this with high precision (see figure 4).

Figure 4: Top left, 3D LIDAR frame, top right, equirectangular projection of corresponding 360 RGB photograph. Bottom left, aligned 2D projection of LIDAR range data. Bottom right, LIDAR range data superimposed on RGB image.

Estimation of LAD from LIDAR data:

While the LIDAR to LAD algorithm we use works on each LIDAR frame individually, in order to localize the LAD data with real vegetation it must be oriented in the georeference frame by rotating and translating each frame from its origin while keeping alignment with adjacent scenes, using a process called simultaneous localization and mapping (SLAM). To accomplish this we tested several open-source SLAM frameworks, including Cartographer, HDL-GraphSlam, LIO-SLAM, BLAM, and various lesser known approaches. We found the most consistent and highest quality results using Cartographer, once we had modified it to maintain all sensor and trajectory information to our standards. This results in dense point clouds that can be trajectory matched with the RTK GNSS data and the colocalized 360 RGB photos. The individual LIDAR frames (each formed by a single rotation of the LIDAR sensor’s 64 lasers, which generates 20 frames per second) are then extracted and processed individually to get the LAD estimate. Our voxel based method does not use cubic voxels, but rather view-frustum shaped voxels that each contain a fixed number of laser trajectories, and hence are small near the scanner and large further away. The scanner emanates lasers from a central rotating diode array with a 90° vertical field of view and a 360° horizontal field of view, with 64 vertical lasers pulsing 1024 times per rotation. The metric derived from the LIDAR frames is actually a raw LAD estimator factor (unmodified by plant species), which is estimated from the LIDAR points with the following equation 1:

LADraw= ð 1∑

ðλ ðððº υ Equation 1 Where V is the total volume in question, and υ is the voxel volume, and G is a projection function estimated at 0.5 and, λ ðð is the attenuation coefficient described by the equation 2: λ ðð = − ððð(1−ðð·ð¼)

ζ Equation 2 Where ζ is the mean path length of lasers (the “depth” of the voxel) and RDI is the relative density index described by the equation 3: RDI= ð ð

ð

Equation 3 Where described Ni is the number of points in the by the equation 4:

voxel and N is the number of laser beams that reached the voxel

N = Where wide Lby t-vLp-v10° t is b-S total number of laser beams that could reach high, then Lt can be given by equation 5:

Equation 4 the voxel, for example if the voxel’s profile is 10°

Lt= 90/10 64

\* 1024

360/10 ≈ 200 Equation 5 vtrajectory, p is the number and S total points within of is that skypoints, points path. in Thus previous which the is RDI voxels the is total an along lasers effective the emitted trajectory, absorbance within vb is the measure the voxel’s points as trajectory beyond used in the Beer’s (Lt) voxel minus law,

in the the

which is incorporated into the LAD estimation formula. The estimated LAD for each voxel is assigned as a scalar value to each point in the voxel, and then the resulting cloud is projected into 2 dimensions with each pixel value being the estimated LAD, which can be aligned to the photographs to get an estimated

LAD for each photograph pixel. This method will produce different results for different voxel sizes, as LAD is highly scale-variant, but for this initial proof of concept study we chose 1 voxel size to see if the deep learning algorithm could get anything related from a photograph.

For the following experiments we used a voxel size of 10° wide by 10° tall by 0.5m deep, as this seeks a balance between being small enough to be considering a volume relevant to airflow, while maintaining enough potential points per voxel to provide dynamic range to the measure. A LIDAR sensor with more lasers, or a denser beam pattern will allow smaller voxels, and hence higher resolution data. The Zeb Horizon has 16 lasers with an effective vertical field of view of 270o, hence has a per degree beam density of 0.08% of the Ouster 64 beam that we used for the following experiments.

Deep Learning results:

Two overall approaches to deep learning were utilized; a grid-based sampling approach in which each tree grid cell is treated as a single image with a single LAD value, and a pixelwise regression on every pixel in the images. The grid cell based method assumes that the important thing for estimating the LAD will be the texture of the foliage parts of the image, and that global context will distract the model. The pixelwise method assumes that global context is useful for the model, as it provides a multitude of cues that could relate to LAD, among them the overall tree shape, size, and potentially distance, tree species etc.

Approach 1: grid-based (“chunkwise”) single image regression:

The first approach involved first using PSPnet to do semantic segmentation of the RGB images, using the resulting tree masks to extract tree pixels, and dividing the trees into chunks that resemble the sizes of the 2D projections of the voxels used in the LIDAR LAD estimation. The equivalent chunks were extracted from the LIDAR derived LAD 2D images. The average or sum of pixel values in the LIDAR chunk were paired with the whole RGB chunks, and the pairs used as inputs to the learning models.

To see if range data could be included in the training data for estimating LAD, initial tests were done to infer range only from the images without any other inputs. Using ResNet50 architecture this was found to be possible with a mean absolute percentage error (MAPE) on validation samples of around 25%, given 50000 chunk pairs. While this is encouraging, when using similar models to estimate the LAD, the lowest MAPE achieved after around 200 hyperparameter permutations was 66%. Adding in the average of the first Laplacian edge detection as a variable improved this to 54%. Removing the images and just using a multilayer perceptron to predict LAD from average Laplacian and estimated range gave 51% using 190000 image pairs. In order to get better results from the chunkwise method, we suspect that the preprocessing code must be updated to adjust the individual image chunk sizes to match specific voxels that they overlap with in the LIDAR data. This will be complicated as the 3D voxels overlap each other in 2D projections, so additional rubrics will have to be developed. The projection to 2D might also be enhanced by filtering the voxels by an occlusion measure, to try to only show voxels that would be visible to the RGB camera (mainly the nearest ones). Additional improvements may be had by averaging the voxels from 10 or so adjacent LIDAR frames before creating the 2D images from the voxels. This should reduce representation error in the 2D images. This merging of adjacent LIDAR frames will also allow preprocessing of the points themselves to reduce overall computation time when performing the LIDAR to LAD calculations. For example we developed an algorithm to separate tree trunks from tree foliage in the point cloud that is highly effective when using multiple frames of the LIDAR scan together post-SLAM. This algorithm will not only enable faster LAD estimation when using merged frames, but also provides additional information about the trees (in particular the trunk diameter at breast height (DBH), a key metric in forestry) that can be useful in addition to LAD for measuring ecosystem health.

While we are interested in testing these improvements on the chunkwise approach, as it may have advantages down the road as we scale up, the second, pixelwise approach yielded better than expected results, and so we proceeded to do the rest of the experiments that way.

Approach 2: Pixelwise whole image regression:

The second method used a conditional generative adversarial network (CGAN) called pix2pix trained on whole image pairs. Pix2pix couples a generator with a discriminator to produce images from other images. By training with paired RGB and LIDAR derived 2D images, pix2pix can attempt to

synthesize a LIDAR derived 2D image from an RGB image on which it was not trained. This method proved much more successful, with an average MAPE of 31% and average pixel to pixel coefficient of determination (r2) of 0.82 for a validation set of 100 pairs using a model trained on 3000 pairs. Figure 6 shows 3 RGB photographs in the top row, the actual LIDAR LAD data paired with the photographs on the second row, the CGAN prediction of the LAD in the third row, and the pixel to pixel correlation in the bottom row. The middle and right columns have higher r2 (0.86 and 0.96 respectively), probably due to the favorable conditions caused by solar backlighting. The sun behind the trees strikingly enhances visibility of lower density foliage parts of the crown, while the lower performance in the leftmost column (r2=0.78) sees the dense tree foliage (and also defoliated deciduous trees) in front of a solid building which reads as maximal density when using Beer’s Law on voxels. While the validation images are not included in the training dataset, they are taken from the same neighborhood, and we can expect there to be significant overfitting related to the overall character of the neighborhood; the model as trained will probably perform less accurately in areas with different architecture and different tree species. This can be improved by training the model further on data from different types of places, which is in progress. Also interesting is that the average r2 was 0.93 when estimating RDI rather than raw LAD… the RDI is a simpler range-adjusted point density index that while dependent on voxel size, is unadjusted for it. This suggests that the deep learning algorithm may perform better when using a different voxel size for estimating LAD.

Figure 6: Top row is street view photo (not included in training set), second row is actual LIDAR derived LAD, third row is CGAN LAD predicted from photo. Bottom row shows pixel to pixel correlation between LIDAR and predicted LAD. Global context cues such as backlighting seem to improve performance.

For further interpretation of the data we filter out the LAD predictions on non vegetation pixels, as shown in figure 7. The semantic segmentation itself does not differentiate between different foliage densities, but the LAD estimation deep learning network does. In the left column of figure 7 we see a purpose built dense vegetated air barrier, which is mostly correctly identified as having a high LAD. In this case the effect of distance can be seen where the LAD appears lower for trees that are farther away (due to the scanner used in the training data having a limited range), this may be a useful bias, as trees further from the road have less impact on air pollution. The middle column shows a gradient of tree health from a dense, healthy redwood on the left to an essentially dead redwood on the right, with the LAD tracking with tree health (the hotspot in the 3rd tree from the left is due to the building overlapping in the semantic mask, this type of error can be improved by upgrading to a more modern, higher definition semantic segmentation algorithm). The right column shows a gradient of LAD from very low on the left to medium on the right.

Figure 7: Top row is RGB photograph, middle row is semantic segmentation, and bottom row is our deep learning prediction of LAD. Left column is dense, purpose built vegetated air barrier at Saint Margaret Mary School in Louisville. Middle row shows a gradient in tree health from left to right, with the leftmost tree being healthy and dense, and the rightmost tree almost dead. Right column shows an increasing

gradient of low density foliage from left to right.

Ground-Truth of LAD data:

While the CGAN produces impressive results estimating the LIDAR derived LAD from street-view photographs, the LIDAR derived LAD itself, while adopted from methods validated with ground-truth in the literature, does itself require calibration to different tree species, voxel sizes and LIDAR ranges. Thus to ground truth the inference we have taken physical samples from the trees in the scanned neighborhood and measured their surface area using two methods, the wax dipping method and the photographic method. The photographic method involves spreading the leaves picked from a known volume of canopy on a white sheet with an area standard (red), photographing from a consistent distance and then counting the green pixels to get the single sided leaf area. In brief, the wax dipping method involves weighing the leaves picked from a specific volume of crown, dipping them in molten wax, spinning them in a consistent fashion to reduce the coating to a uniform thickness, and then weighing again to get the weight of wax coating. This can then be used to create an adhered wax weight to surface area ratio by also performing the process on surface area standards. Using wire standards our standard curve has an r2 of 0.942 (see figure 8).

Figure8: left, wax dipping wire standard curve (r20.942). Right, per species surface area.

This wax method was developed for needle-leafed conifers species, as their shape makes their analysis with the photographic method inaccurate. However, the wax dipping standard curve made with wire is probably inaccurate for broadleaf species, so for full utilization of these results we will need to run some wax-dipping standards made of paper or other flat objects for broadleaf species. In any case we made wax dip and photographic pairs of over 1000 foliage samples from throughout the West Oakland neighborhood scanned for training the street-view LAD deep learning network. The association of each sample with a 3D location within the LIDAR point clouds must currently be done manually, and with high spatial precision, (as to avoid undue destruction of trees on public property we limited samples to a 15 x 15 x 15 cm cube). With the sample distance from the trunk, height above ground and compass direction recorded, we are working on an automated procedure to associate each sample with the exact location in the point cloud. This will be possible because our RTK GPS geolocation of the point clouds has an accuracy around 2cm.

Additional data types for deep learning pipeline:

There are two additional data types that we began implementing; leaf area index (LAI) from aerial LIDAR scans and plantable area (PA) from combined aerial LIDAR and 1m aerial normalized difference vegetation index (NDVI). We trained a similar deep learning algorithm as used for the street view images on satellite imagery to predict LAI and PA. LAI from aerial scans is a complementary metric to LAD from terrestrial scans as it includes information about backyards, which is missing from roadway based terrestrial scans. It also includes information about locations of trees with more spatial resolution than Google street-view images taken every 20m along roadways. FIgure 9 illustrates these complementary differences between terrestrial and aerial LIDAR.

Figure 9: top left, terrestrial LIDAR misses backyard information. Top right, terrestrial LIDAR gets high quality near-road understory information (maybe most important info for air quality). Bottom left, aerial LIDAR gets great backyard information. Bottom right, aerial LIDAR misses understory information, trees look like floating blobs.

Through the Green Heart partnership we were able to acquire aerial LIDAR scans of around 65km2 of Louisville, KY. This scan was flown by a contractor at a price of \>$75,000, so the ability to replicate the data derivatives from free satellite images would be very valuable in the future. To estimate the LAI from the LIDAR data we used Beer’s law in a similar way as we did for getting LAD from terrestrial LIDAR, except that each patch of land had a single voxel over it, and the ground plane was used as the measure of how many beams got all the way through the foliage. The script we developed to perform this calculation also removed building roofs, the edges of which would otherwise read as vegetation. Completion of LIDAR data processing resulted in 216 tiles of 301000m2 each, with 1m LAI resolution. These were divided into around 10000 256x256 images for CGAN training, with 1000 left out for validation. The aerial photography used to train the model was from the ESRI WorldMap 30cm free map service. The results were not as good as the results of the terrestrial LIDAR streetview data, (probably because the ESRI photography may be several years out of date), in that the average r2 for pixel to pixel correlation was 0.3 for samples not in the training set, and the model showed limited ability to adapt to diversity in the input data. For example figure 10 shows in the top row the orbital photo (not included in the training set), the middle row the actual LAI derived from aerial LIDAR (normalized to values between 0 and 255 for presentation clarity), the third row the CGAN predicted LAI and the bottom row the pixel to pixel correlation. The left column shows a fully forested tile, very uncommon in the dataset (it is a small park that is represented by around 10 out of 10000 images), with an r2 of 0.014, which may be remedied by having a more expansive training set with more diverse types of vegetation. The right column shows a typical urban setting, which is very common in the dataset, with an r2 of 0.73, which is satisfactory for remote forestry of this type, while the middle column shows an intermediate landscape with an r2 of 0.46. There is clearly some error happening where the model correctly predicts an LAI value but puts it in the wrong place, or correctly places vegetation but gets the wrong LAI value. The most likely reason for this is that the ESRI orbital photography is not contemporaneous with the LIDAR acquisition, in fact it could be several years old in some places, so trees may have grown or been cut down between the photographs and the LIDAR. This can be remedied by using a contemporaneous dataset. We have found a commercial provider that can get summer 2019 30cm satellite data from around the same time as the LIDAR was flown for around $800, so we are pursuing that to retrain the model and see if it improves. Having more total data will also help, as the r2within the training set was 0.83 on average, so in future runs data augmentation (rotations and moving-window sub-sampling) will be used to increase the size of the training set.

Figure 10: top is Orbital 30cm imagery (not in training set), middle is LIDAR derived LAI, 3rd row is CGAN LAI predicted from orbital imagery, bottom is pixel to pixel correlation between LIDAR and CGAN output.

The other type of data that we are estimating from satellite photography is the plantable area. Plantable areas are places where planting new trees is possible due to lack of existing tree cover, permeable ground surface, and other factors such as municipal setback regulations, distance to overhead utility lines/underground utilities. To make a large training set, we again used the aerial LIDAR and NDVI data from the Green Heart project, in this case to separate the ground-plane high-NDVI (grass) from the above-ground features (trees and buildings) and ground-plane low-NDVI features (roads, parking-lots etc). This method produced plantable area maps for the entire neighborhood that can be used as training data for the deep learning inference from satellite imagery. Like the LAI experiments, we believe that we

will get better results by purchasing satellite data that is contemporaneous with the LIDAR acquisitions, and will commence training once that data is acquired.

Post Planting Validation:

Due to the COVID-19 pandemic, the Green Heart team’s plan to plant several miles of freeway-adjacent vegetated air barriers followed by detailed air-pollution monitoring was delayed for almost a year. While we will still take advantage of that process when it occurs, in the meantime we have begun fluid dynamic modeling to estimate the effects of LAD on particulate pollution deposition and dispersion. Intuitively, higher LAD is expected to be better for deposition and dispersion of particulates. However, there are some who wonder if too-high LAD might deflect air too much, minimizing deposition. If this is the case, then there may be a sweet-spot of LAD. To investigate this we used ENVImet, a commercial software for fluid dynamic simulations of vegetation and pollution. ENVImet allows the user to create 3D models of vegetation with adjustable LAD, buildings, ground surfaces, terrain and pollution sources and subjects them to a fluid solver, and enables visualization of pollution concentrations and deposition. The results of the first two simulations are visualized in figure 11 (as a section perpendicular to the roadway), and suggest that LAD=10 is far superior to LAD=3. More experiments will perhaps provide more insights and guide vegetation design for the design tool product. Indeed the integration of fluid dynamics simulations into our product is being considered for phase II.

Figure 11: ENVImet simulation of traffic source pollution with vegetated air barriers of different LAD

Tree Placement Algorithm:

While our previous automated tree placement algorithm was more general purpose and packed trees into plantable areas according to a density per sector rubric (where sectors near roads were assigned a high density and sectors far from roads a lower density) we are now working on an improved method that specifically generates roadside vegetated air barriers. Given the plantable areas generated by our plantable area algorithm, our new plant placement algorithm finds the nearest road to each plantable area, establishes the parallel direction to the road that coincides with the plantable area’s long axis, and places trees row by row starting from the side nearest the road, as illustrated in figure 12.

Figure 12: improved automatic tree placement algorithm

The trees thus placed can be prioritized according to the results of the LAD and LAI analysis of the area, yielding the highest returns for green infrastructure investment. We are also incorporating an automated prioritization mapping process that includes information on sensitive receptors and where people spend time outside, a prototype output of which is illustrated in figure 13.

Figure 13. Prototype outputs of automated prioritization layer

Back-end Data Handling Infrastructure:

In order to obtain requests from users on a front-end user interface, process the environmental data on a backend server, and then provide the results back to the user we had to create a back-end data handling system. The environmental index tool is built on industry standard open source software platforms designed for scalability and resilience. We have implemented a geospatial stack (see figure 14) which serves standard application programing interfaces (APIs) in multiple interfaces. The data structure is built on PostgreSQL as its underlying database engine. The database runs on a Debian based virtual machine which is hosted on Amazon Web Services (AWS). For geospatial applications this provides excellent stability and performance. The PostGIS database extension package adds geospatial classes and functions to the database. Our server runs a Java based geospatial server called Geoserver which is also open source and well established. That application interfaces with the database and serves data and dynamic derivatives to the web. Geoserver uses the Open Geospatial Consortium standards for map services. Raw data is inserted directly into the database by python functions, after which it is stored and retrieved on demand. Geoserver creates caches of map tiles which it serves on the common mapbox standard via an http connection.This system does not use any licensed or enterprise software such as ESRI products, but it is nevertheless scalable. PostgreSQL is highly efficient and the data is relatively lightweight. The data product can be cached and could be served by additional Geoserver instances if needed.

Figure 14: geospatial database architecture

Front End User Interface:

The front-end prototype (available here: https://www.hyphae.net/adapt-os/streetscape-ecology to login without registering use email: guest@hyphae.net and password hyphae2021) currently shows the user where already calculated data exists, and allows them to select an area to calculate new data. This then communicates with our back-end script which measures the total length of roadways within the selection, and produces a crude price estimate for analysis within the selection. The current data shown and prices estimated are for semantic image segmentation for producing environmental view indices of google street-view photos and deep learning inferred leaf area density. Also shown are plantable area, NDVI, prevailing wind direction and traffic volumes for major roadways. Figure 15 shows some screenshots of the interface.

Figure 15: user interface screenshots

Unexpected Problems Solved:

The Zeb Horizon scanner, which ultimately costs \~$4000 per week to rent, and has technical issues around sensor fusion and total resolution discussed above, also required SLAM to be done by the rental agency, which was not always well done, with many scans having grievous alignment problems. We solved this problem by purchasing (using funds not acquired through this grant) the Ouster OS0-64 scanner ($8000). While the Ouster scanner provides for sensor fusion and allows us to do SLAM ourselves, Ouster does not provide any SLAM software or helpful guidance for tuning SLAM. Thus there was a significant amount of time spent developing and tuning SLAM for the Ouster and developing a LIDAR to image alignment system, which paid-off in data flexibility and customization of datastreams for our highly specific purposes. This also allowed us to rescan areas with different configurations as needed, which would not be possible with the rental scanner.

The original grid based deep learning approach did not work well. We solved this problem by switching to a CGAN based architecture that was highly successful.

The free 30cm orbital imagery was out of date and limited the accuracy of training our orbital LAI estimator. We think we solved this by finding commercial data that matched the scanning dates.

Unexpected Problems Unsolved:

One deliverable identified at the beginning of the project was to adapt our LIDAR-LAD voxel algorithm to use graphical processing units (GPUs) instead of central processing units (CPUs). There were several delays in starting this process, as described in the transition from the Zeb to the Ouster scanners above; the whole LAD from LIDAR algorithm had to be substantially altered to go between the original (built for a stationary Faro scanner), to the Zeb (a mobile 16 laser scanner with 2 simultaneous but perpendicular axes of rotation) to the Ouster (mobile 64 lasers with 1 axis of rotation). However we did ultimately get the algo running on GPU, however the performance gains were limited (or even negative) by the need to jump between GPU grid and main system memory as each voxel’s situation with regard to its LAD is dependent on all of the other voxels within its radial trajectory segment. This did not impact the

outcome of the project, as we were able to process enough data on CPUs to train the deep learning system. This problem may yet be solved by adopting more aggressive changes in the overall approach to assigning data to the GPU, but it was seen as a low priority given the overall objective of the project. While the tool we are generating is valuable in its own right, it will become far more valuable when the metrics are validated with health and air monitoring data, and we remain well positioned to do that validation as we have so much data on the Green Heart neighborhood where an interventional study is underway. However, the COVID-19 pandemic caused yearlong delays in Green Heart tree planting and air monitoring, so no such validation has taken place yet. We are trying to fill this gap both with fluid dynamic modeling and reaching out to other providers of health and air quality data to perform non-intervention studies on existing conditions, and “reverse-intervention” studies (for example in places with health and air quality data where large numbers of trees were cut down or died from disease).

Impact of customer discovery on technological development:

During customer discovery activities we learned several key insights about the desired attributes of the technology. Firstly, many potential customers have lower expectations for data quality and utility than we are producing, mainly due to lack of awareness about what is possible. For example, healthcare workers need simpler metrics (than LAD) like distance to parks, NDVI, or the EVIs for a patient or area, and we were able to easily add these to the tool without modifying our overall work-plan. We also found that people in research fields and health insurance industries were more interested in the analytical aspects of the tool rather than the automated design in the short term. This is because both groups are interested in further establishing the relationship between nature and health, which will later be used to justify actual interventions. Consequently we focused more on building up the analytical aspects of the tool for customer testing rather than the automated design components. Customer discovery also pointed us towards another aspect of the analytical platform that can be based on individual location data; rather than just looking at the ecosystem structure of an area, we can follow an individual patient or consumer and add up their exposure to various geolocated ecosystem parameters, and provide personalized health predictors and actionable intelligence for individuals. These personal geotracking functions will be added to the tool in phase II.

From phase I to phase II and beyond:

Phase II will build upon the work done in phase I in several ways: In phase II we will expand the data collection and algorithm training to make the tool more accurately generalizable to different types of neighborhoods and climates. We will also optimize the user interface and data types based on user testing. This will result in deployment of a commercial product at the end of Phase II. Additional functionality to be considered for inclusion in the phase II tool includes personal exposome tracking functions, and fluid dynamic modeling of proposed intervention designs. Phase II will also overlap with several implementations of ecosystem interventions that we have planned and so will include air monitoring to evaluate the efficacy of the interventions and feed those results back into the design tool’s optimization schema.

The software components we are developing have been used on two active projects this year and are either contracted or in pipeline to be used on at least three additional projects in 2021. While completing our phase II application in the coming months, we're going to leverage the fact that we have a working prototype to engage 10 to 20 additional pilot users for feedback and further direction in developing the product offerings. To date the components of the software tool have been included as a greening metric for evaluation before and after on one of the first clinical trials on urban greening in the world. It has also been used by transportation planning and traffic engineers on a 6-mi long major corridor transportation study, both in Louisville Kentucky. We are also now in contract to utilize these tools to do analytics work for the Greenspine, a 4-mi greenbelt through the medical district of Dallas, between February and July. We're in discussion with large not-for-profit foundations in the urban greening and Environmental Health fields who are interested in utilizing our analysis and metrics in tools and dashboards they utilize for projects and funding prioritization. We have also been working with environmental justice communities in the Cities of Oakland, Richmond, and Stockton, California on AB617, a state mandate for local air districts to work with communities to develop plans to resolve air quality injustices.

Conclusions:

This phase 1 project sought to develop a deep learning pipeline for estimating leaf area density from street view photographs based on training data derived from mobile terrestrial LIDAR scans. This was successful; with an average r2 value of 0.82 for LIDAR-LAD prediction from street view photographs, and 0.93 for predicting RDI. We also built a prototype system for delivering this data to customers by implementing a back-end server to retrieve Google street view photos, perform the deep learning inference on the photos, cache them in a geodatabase, and serve them to a front-end user interface. The front end user interface also serves other relevant data, including publicly available wind, traffic and land use data as well as additional custom data sources that we have developed such as LAI and plantable area derived from satellite imagery using our new deep learning pipeline. We improved our automated tree placement algorithm to produce more functional planting structures, and have overall created a strong foundation for building a powerful design, analytics and modeling tool. This supports a phase II proposal for taking the product from the prototype to the deployment stage, optimizing the concepts proven in phase I, developing new models for additional features, and performing new (and integrating with ongoing) environmental health studies. During phase 1 in addition to scientific research and development we also engaged in dozens of customer interviews. One outcome of these interviews was to prioritize adding additional data streams (beyond just street-view derived LAD, such as aerial LAI) to our platform over emphasizing automated tree planting plans, as many in the field are currently more interested in proving the relationships between ecosystem parameters and human health than on planting trees alone. However, we still worked on automated tree planting plans because it will be the first thing required to value-engineer interventions when those are finally implemented. We have also initiated several new collaborations with potential customers for health studies, ecosystem service evaluation and intervention designs, with active partnerships in 10 American cities and one nation (we may process all of the Netherlands). In conclusion, we are pleased with the results of our research, and excited to take the next steps in commercialization.

[\#1](#1)   
[\#1](#1)   
[\#1](#1)   
[\#1](#1)   
[\#1](#1)   
[\#1](#1)   
[\#2](#2)   
[\#2](#2)   
[\#4](#4)   
[\#4](#4)   
[\#5](#5)   
[\#5](#5)   
[\#5](#5)   
[\#5](#5)   
[\#5](#5)   
[\#5](#5)   
[\#8](#8)   
[\#8](#8)   
[\#8](#8)   
[\#8](#8)   
[\#11](#11)   
[\#11](#11)   
[\#11](#11)   
[\#11](#11)   
[\#12](#12)   
[\#12](#12)   
[\#12](#12)   
[\#12](#12)   
[\#13](#13)   
[\#13](#13)   
[\#13](#13)   
[\#13](#13)   
[\#14](#14)   
[\#14](#14)   
[\#14](#14)   
[\#14](#14)   
[\#15](#15)   
[\#15](#15)   
<https://drive.google.com/drive/folders/1msrhBy72hPS10Tj5gbf3bSSKnEDbX4eK?usp=sharing>   
<https://www.hyphae.net/adapt-os/streetscape-ecology>   