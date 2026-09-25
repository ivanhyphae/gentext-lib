---
asset_id: nsf-scc-tamu-2025
source_system: gdrive
source_id: 1fidMYELx1bhy6ZvJsDjJoaXze6HNRQrcZMNpjgo30jA
source_title: "NSF S&CC TAMU"
acquired: 2026-09-25
via: connector-text
tool: google-drive read_file_content (includeComments=true)
truncated: unknown
---

# START HERE

fucUse the tabs at left (\[image\]) to navigate the material
  - PROPOSAL (ONLY) *tab is the draft text for submission*
  - Stuff from other projects *tab is copy/paste of grant text from other related projects. It also includes many links to relevant materials although they may have more restrictive permissions and require requesting view access.*
  - Proposal coordination *is meeting notes, checklists, and internal hyphae discussion*


# Pre-Proposal Only

SCC-IRG Preliminary Proposal: Closing the Heat Gap – Precision Heat Modeling for Community-Driven Cooling Interventions
 
**Project Summary**
Overview
Extreme heat is driving rising healthcare costs across the United States, contributing to an estimated $100 billion annually in direct medical expenses. Indirect costs, such as lost productivity and increased insurance burdens, are expected to drive this figure to $500 billion per year by 2050.\[1\] The rise is fueled by more frequent and severe extreme heat events, the intensification of urban heat islands from expanding sprawl and declining green spaces, an aging population more vulnerable to heat stress, and rising healthcare costs. To fully understand the impact of extreme heat, however, we must move beyond the public health literature’s overreliance on census-tract-level analyses, as these often obscure critical variations in individual exposure.\[2\] Submeter-scale factors—such as pavement type, shade coverage, wind direction, building shape, and building materials—directly shape how individuals experience heat exposure, yet are often overlooked in these broader-scale assessments.
 
Our project will bridge this gap by using cutting-edge geospatial and machine learning techniques to analyze how modifiable built-environment features influence extreme heat exposure across a large American population. We will complement this analysis with pre- and post-monitoring of heat exposure in targeted, community-driven pilot interventions to validate the causal benefits of scalable, evidence-based heat mitigation strategies.
 
Intellectual Merit
While the dangers of extreme heat are well known and built environment interventions are widely embraced, their efficacy is often underexamined. Many communities rely on dashboards that map heat risk by census tract, guiding interventions such as tree planting in high-risk areas. While trees provide shade and cooling in principle, our high-resolution modeling and monitoring confirm that without precise placement, these efforts can be ineffective.
 
For example, a high-risk census tract might have residents experiencing the bulk of their heat exposure at bus stops. Yet a well-intentioned tree-planting initiative may focus on a nearby park, providing shade where it isn’t needed. To address this misalignment, we use submeter radiant temperature modeling, agent-based simulations of pedestrian and worker activity, and mobility tracking to pinpoint heat exposure hotspots. This process enables targeted, high-impact interventions—such as the implementation of greening and other shade structures, cool pavements, or air-conditioning rebates—maximizing mitigation funds and minimizing waste. By integrating pre- and post-intervention monitoring of both heat exposure and health outcomes, we validate effectiveness, ensuring replicable solutions for other communities.
 
Broader Impacts
This project will generate substantial societal benefits by developing and disseminating practical strategies to reduce extreme heat exposure, particularly in high-risk communities. Partnering with local stakeholders, the team will translate research insights into evidence-based tools that help communities lower healthcare costs and improve public health.
 
Communities will gain hands-on experience applying geospatial analyses to design effective heat mitigation strategies. The project will promote widespread adoption of best practices through open-source data sharing, case studies, and public workshops. By equipping communities with scalable solutions, this work will strengthen resilience to extreme heat across the United States and inform urban planning and policy for long-term climate adaptation.
 
**Project Description**
Vision and Goals
This project aims to conduct a 1 meter-scale extreme heat study for the City of Houston, culminating in a green infrastructure pilot project designed to mitigate urban heat exposure along the City’s transportation network. The study will integrate meter-scale heat mapping, public health data, and infrastructure interventions, setting a replicable framework for comprehensively improving community transportation networks in future funding cycles.
 
The pilot intervention may include heat interventions at a bus stop or a set of bus stops, followed by pre- and post-monitoring to assess efficacy. This evidence-based approach will provide a data-driven model for cooling interventions, demonstrating how localized modifications to the built environment can significantly reduce heat exposure and improve health outcomes.
 
The high-risk, high-reward aspect of this study is its unprecedented level of granularity, correlating individual address-level heat exposure with public health outcomes, such as emergency room visits and ambulatory care data. Current research, including the Harris County Public Health (HCPH) 2019–2024 heat study, has only assessed heat impacts at the zip-code level. Our work will pioneer a finer-scale analysis, producing actionable data for heat mitigation strategies.
 
Integrative Research Approach
Our project seeks to surpass the current state of the art in extreme heat research by shifting from census-tract-level heat analysis to meter-scale assessments. We integrate advanced geospatial analysis, engineering solutions, machine learning, and social science methodologies to provide high-resolution, community-driven interventions.
 
*Methodology*
High Resolution Heat mapping:  We will make a one-meter scale three-dimensional digital twin of the City of Houston using publicly available aerial lidar data, which takes into account the terrain, buildings and vegetation. This will be used to perform a 1-meter scale Solar and LongWave Environmental Irradiance Geometry (SOLEWIG) estimation of mean radiant temperature (MRT) for a typical summer day.\[3\] The model will be validated and supplemented with the deployment of a network of low-cost MRT, humidity, and wind sensors that can provide discrimination between the human-scale effects of different modifiable landscape elements; for example some sensors will be placed out in the open over pavement, or grass, while some will be in the shade of a large tree, or a small tree or building. Our previous research has shown that while air temperatures between such features may vary by only a few degrees, the MRT (which more accurately reflects the human experience of heat stress) can vary by up to 25 degrees between shady and sunny areas. While some sensors will be stationary, gathering data 24 hours per day from one location, others will be mobile, traveling with community agents to determine the heatscape of the human occupied activity-space while it is in use.
 
Health Data Correlation: We will access address-level and census block-level health outcomes from Texas A\&M Research Data Center, which provides access to individual death records. This can then be analyzed against a variety of covariates with the heat simulation and monitoring data using distributed lag non-linear models (DLNM), to investigate causal relationships between heat, modifiable built-environment parameters, and health outcomes. A particular outcome will be neighborhood-to-neighborhood comparisons of mortality, which will allow us to determine if some neighborhoods are more vulnerable to extreme heat and humidity.
 
Community-led Intervention Pilot: Equipped with monitoring, modeling, and health data, we will work with community stakeholders (e.g., Super-neighborhood councils, community development organizations, public health experts) to co-design and implement a pilot intervention. The intervention will be optimized to improve health outcomes by reducing heat exposure/heat stress in a testbed community with high heat related health problems. The pilot intervention may be relatively small, like providing greening or shade structures to a set of bus-stops. However, the monitoring will allow pre- and post- measurement of reductions in heat exposure, improved thermal comfort, and potentially changes in health indicators. TAMU and HARC will work with community partners to ensure this intervention is within community interest and will serve as a true benefit.
 
Scalability & Replicability: The framework proposed here; modeling heat, designing an intervention informed by feedback from modeling, and monitoring the benefits of the intervention with pre-post assessments, provides a replicable technology that can be generalized both across the rest of the city of Houston, and to any other location in the United States that suffers from extreme heat. This project can then serve as a model for infrastructure planning with evidence-based design.
 
Interdisciplinary Integration: This project aligns with NSF’s requirement to integrate at least two disciplines, drawing from: Geosciences (47.050): Heat mapping, climate modeling; Engineering (47.041): Green infrastructure implementation; Computer & Information Science (47.070): Machine learning, geospatial data analytics; Social & Behavioral Sciences (47.075): Community engagement, public health impact assessment.
 
Broader Impacts
Our project advances NSF Smart & Connected Communities (S\&CC) priorities by developing an evidence-based, community-led approach to urban heat mitigation.
 
Community-Led Research & Implementation:
·    Stakeholders (potentially Houston Metro, HCPH, Gulfton Super Neighborhood e.g.) co-design interventions to ensure relevance and long-term adoption.
·    The public health sector will use our findings to inform future heat mitigation policies.
Capacity Building for Long-Term Impact:
·    Our research will equip communities with tools and training to design and implement their own interventions.
·    STEM education and workforce development components will enhance local skill-building in climate resilience and urban sustainability.
Scalability Beyond Houston:
·    Our methodologies can be replicated in other heat-vulnerable cities, extending the project’s impact nationwide.
·    Work will be shared with policymakers via policy briefs, white papers, and application to ongoing climate adaptation plans led by the City of Houston, Harris County.
 
This research positions Houston as a national leader in extreme heat mitigation by demonstrating a scalable, data-driven, and community-led model that can be expanded citywide and beyond.
 
 
 
-----
\[1\]  Atlantic Council, 2021,[ https://www.atlanticcouncil.org/wp-content/uploads/2021/08/Extreme-Heat-Report-2021.pdf](https://www.atlanticcouncil.org/wp-content/uploads/2021/08/Extreme-Heat-Report-2021.pdf)
\[2\]  Ho et al. 2015, A Spatial Framework To Map Heat Health Risk at Multiple Scales. International Journal of Environmental Research and Public Health, December 2015 12(12)
\[3\]  Fredrik Lindberg, C.S.B. Grimmond, Andrew Gabey,
Bei Huang, Christoph W. Kent, Ting Sun, Natalie E. Theeuwes, Leena Järvi, Helen
C. Ward, I. Capel-Timms, Yuanyong Chang, Per Jonsson, Niklas Krave, Dongwei
Liu, D. Meyer, K. Frans G. Olofson, Jianguo Tan, Dag Wästberg, Lingbo Xue, Zhe
Zhang, Urban Multi-scale Environmental Predictor (UMEP): An integrated tool for
city-based climate services, Environmental Modelling & Software, Volume 99,
2018, Pages 70-87, ISSN 1364-8152, https://doi.org/10.1016/j.envsoft.2017.09.020.
Project Personnel and Partner Institutions
Andrew Dessler; Texas A\&M University; PI (Professor of Atmospheric Sciences, Director, Texas Center for Climate Studies)  
Stephanie Piper; Houston Advanced Research Center (HARC); Co-PI (Research Associate, Community Development and Resilience)  
Daniel Fleischer; Hyphae Design Lab; Subawardee (Chief Science Officer)  
Brent Bucknum; Hyphae Design Lab; Subawardee (Principal)  
Juan Penaloza Gutierrez, PhD; Hyphae Design Lab; Subawardee (Modeling Expert)  
Ivan Heitmann; Hyphae Design Lab; Subawardee (Modeling and Design Lead)
-----
Texas A\&M University
Dr. Andrew Dessler is a climate scientist specializing in climate change impacts, global climate physics, and atmospheric chemistry. As Director of the Texas Center for Climate Studies, his research informs resilience and adaptation strategies. A fellow of AGU and AAAS, he serves as President of AGU’s Global and Environmental Change section. His work has advanced understanding of climate feedbacks, extreme weather, and infrastructure stress. Formerly a Senior Policy Analyst at the White House Office of Science and Technology Policy, he has written extensively on climate science and policy, including in *The Science and Politics of Global Climate Change* (2005) and *Introduction to Modern Climate Change* (2011). Dr. Dessler holds a Ph.D. from Harvard University and a B.A. from Rice University.
 
Houston Advanced Research Center (HARC)
HARC applies science to support policies that address environmental challenges while promoting social and economic equity. It engages communities in defining problems and co-developing solutions, partnering with Superneighborhood councils, development groups, and environmental nonprofits to build trust and collaboration. A key focus is reducing environmental disparities, such as extreme heat, through initiatives like urban tree planting. Dr. Stephanie Piper, Co-PI, is a Research Associate at HARC specializing in community resilience, urban ecology, and science policy. She leads outreach efforts to integrate community priorities into research and climate adaptation strategies. Previously a Science Policy Fellow with the National Academies of Sciences, Engineering, and Medicine’s Gulf Research Program, she earned a Ph.D. in Plant Biology from UC Riverside, researching urban air pollution patterns, and an M.S. and B.S. in Ecology and Evolutionary Biology from Tulane University.
 **Hyphae Design Lab  
**Led by **Brent Bucknum**, an urban ecologist specializing in environmental health and infrastructure resilience, and **Daniel Fleischer**, an applied scientist and engineer advancing environmental monitoring and intervention technologies, **Hyphae Design Lab** is a leader in evidence-based environmental design. The firm develops adaptive solutions that enhance human health, support biodiversity, and mitigate risks such as extreme heat, air pollution, and flooding.
With over 15 years of experience supporting environmental justice communities, Hyphae collaborates with academic institutions and community partners to integrate research into practice. The firm has secured funding from the **National Science Foundation** and **National Institutes of Health** to develop **adaptOS**—a platform integrating aerial, satellite, and ground-level data to create high-resolution, hyperlocal 3D maps of environmental risks, model intervention scenarios, and implement design solutions that improve urban resilience. In partnership with the **University of Louisville**, Hyphae is leading the largest clinical trial to date on the effects of urban greening on air quality and neighborhood health. Working nationwide, Hyphae applies data-driven design to create equitable, scalable solutions for environmental health challenges


# Pre-proposal guidelines

### **V. Proposal Preparation And Submission Instructions**
#### **A. Proposal Preparation Instructions**
Preliminary Proposals *(required)*: Preliminary proposals are required and must be submitted via Research.gov, even if full proposals will be submitted via Grants.gov.
Preliminary proposals are required for SCC-IRG and SCC-LSR proposals only and are required to be eligible to submit a full SCC-IRG or SCC-LSR proposal. Full proposal submissions for both proposal categories that did not provide a preliminary proposal will be returned without review. The NSF decision made on the preliminary proposal is advisory only (encourage or discourage submission) and may include feedback on proposed activities, including anticipated budgets.
Proposers should carefully note the target dates for both preliminary and full proposals. If you plan to submit a full proposal by the April 2025 target date, make sure to submit your preliminary proposal by its February target date. If you’re aiming for the November target date for full proposals, submit your preliminary proposal by its September target date. And in 2026, if you plan to submit a full proposal by the March 2026 target date, make sure to submit your preliminary proposal by its January target date. This timing helps NSF give you feedback on whether to proceed with your full proposal within 30 days of the April or November target dates for full proposal submissions.
Required components of preliminary proposals are given below. Page limitations given here will be enforced, and preliminary proposals that are not compliant will be returned without review. If there are multiple organizations involved in a project, a single preliminary proposal should be submitted and that should come from the lead organization.
Preliminary proposals consist of four elements:
1.  Cover Sheet;
2.  Project Summary;
3.  Project Description; and
4.  Project Personnel and Partner Institutions.
Preliminary Proposal Set-Up: Select "Prepare New Preliminary Proposal" in Research.gov. Search for and select this solicitation title in Step One of the Preliminary Proposal wizard. Select "Single proposal (with or without sub-awards). Separately submitted collaborative proposals will be returned without review.
Title: The Proposal Title should begin with "SCC-IRG Preliminary Proposal" or “SCC-LSR Preliminary Proposal", followed by a colon, followed by the project title.
Project Summary (1-page limit): The project summary may not exceed one page and must consist of three clearly labeled sections:
1.  Overview: A summary of the challenge to be tackled and its importance, how the project integrates different fields and partners, and how it builds research capacity-building and community engagement*;*
2.  Intellectual Merit: Provide a brief summary of the intellectual merit of the project, describing potential outcomes and fundamental and integrative research advances; and
3.  Broader Impacts: Provide a brief summary of the broader impacts of the proposed project, including potential impacts on the targeted community, society writ large, the economy, and science and/or engineering.
Project Description (2-page limit): The Project Description of the preliminary proposal is limited to two pages and must consist of the following headings and associated text:
1.  Vision and Goals: Describe the vision and goals of the proposed research. Briefly describe how the project will contribute to scientific and technical advancements and its potential impacts on the engaged community.
2.  Integrative Research Approach: Describe the project’s plan for integrative research and community engagement. Provide a discussion on the novelty of the proposed work, how the expected outcomes go beyond today’s state of the art, and the generalizability of its outputs beyond addressing an application domain problem. Additionally, identify the disciplines to be integrated and the relevance of the research to the funding directorates and divisions for the S\&CC program. Define the community and associated stakeholders and list the various disciplines needed to address the challenge being undertaken. Discuss how the community will be incorporated into the project plan and research. Briefly describe the approach for evaluation and metrics to be employed.
3.  Broader Impacts: Describe the anticipated and planned broader impacts of the proposed project, including potential impacts on the targeted community, society writ large, the economy, and science and/or engineering.
Project Personnel and Partner Institutions (1-page limit): Provide current, accurate information for all personnel and organizations involved in the project. Follow the same format as described for Project Personnel and Partner Institutions in the Full Proposal Preparation Instructions below. Submit as a supplementary document.
The following sections are not required for preliminary proposals and must not be included: "Results from Prior NSF Support"; "Budget and Budget Justification"; "Facilities, Equipment and Other Resources"; “Biographical Sketches”. “Current and Pending (Other) Support”; "Collaborators and Other Affiliations Information", "Synergistic Activities", "Data Management and Sharing Plan", and "Mentoring Plan". Preliminary proposals containing items other than those required above will be returned without review
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Project Summary (1-page limit): The project summary may not exceed one page and must consist of three clearly labeled sections: 
 
1.  Overview: A summary of the challenge to be tackled and its importance, how the project integrates divergent fields and partners, and how it builds research capacity-building and community engagement; There are no restrictions or limits. There are no restrictions or limits. For the S\&CC program, during any contiguous 12-month period, an individual may not participate as PI, co-PI, or Senior/Key Personnel in more than two proposals across all proposal categories. This limit will be applied beginning with this solicitation and will continue to apply to future versions of this solicitation, unless noted otherwise. 
2.  Intellectual Merit: Provide a brief summary of the intellectual merit of the project, describing potential outcomes and fundamental and integrative research advances; and 
3.  Broader Impacts: Provide a brief summary of the broader impacts of the proposed project, including potential impacts on the targeted community, society writ large, the economy, and science and/or engineering. 
 
Project Description (2-page limit): The Project Description of the preliminary proposal is limited to two pages and must consist of the following headings and associated text: 
 
1.  Vision and Goals: Describe the vision and goals of the proposed research. Briefly describe how the project will contribute to scientific and technical advancements and its potential impacts on the engaged community. 
2.  Integrative Research Approach: Describe the project’s plan for integrative research and community engagement. Provide a discussion on the novelty of the proposed work, how the expected outcomes go beyond today’s state of the art, and the generalizability of its outputs beyond addressing an application domain problem. Additionally, identify the disciplines to be integrated and the relevance of the research to the funding directorates and divisions for the S\&CC program. Define the community and associated stakeholders and list the various disciplines needed to address the challenge being undertaken. Discuss how the community will be incorporated into the project plan and research. Briefly describe the approach for evaluation and metrics to be employed. 
3.  Broader Impacts: Describe the anticipated and planned broader impacts of the proposed project, including potential impacts on the targeted community, society writ large, the economy, and science and/or engineering. 
 
Project Personnel and Partner Institutions (1-page limit): Provide current, accurate information for all personnel and organizations involved in the project. Follow the same format as described for Project Personnel and Partner Institutions in the Full Proposal Preparation Instructions below. Submit as a supplementary document.


# Proposal Guidelines

Title: The title of the proposal must begin with “SCC-DG”, “SCC-IRG”, or “SCC-LSR” depending on the proposal category. The rest of the title should be a concise representation of the project and its goal(s) The title should be suitable for use in the public press. 
Project Description: Project Descriptions for SCC-IRG and SCC-LSR proposals are limited to 15 pages, 
All proposals must include sections required by the PAPPG, including a separate section labeled “Broader Impacts” and Results from Prior NSF Support. 
The Project Description must provide details on an integrative research approach and describe how the community engagement components infuse and support the proposed research. 
In addition to the sections required by the PAPPG, it must include separate bold headed sections as described below under Project Description Components. 
1.  Integrative Research: SCC-DG, -IRG, and -LSR proposals The Integrative Research section is the intellectual heart of the Project Description. The section should outline the interdisciplinary research to be undertaken, the fields involved, and the fundamental scientific or engineering contribution the work will make that are relevant to the NSF Directorates and Divisions listed as sponsoring the program. Proposals should articulate the nature of the high-risk/high-reward research to be undertaken and address potential risks and mitigation approaches. The potential for transformative scientific and societal impact should also be discussed, if the project is successful. Proposals should be motivated by challenging and important research areas that blend critical needs of communities and expertise from fields represented by the sponsoring NSF Directorates.
1.  S\&CC Research Focus is required where the PI must identify the two or more primary research areas and disciplines in which the novel and foundational research contributions are being made. This is not intended to be a list of areas but a focused discussion, clearly describing the focus and relevance to the program and its participating funders. Note that the scope of research will vary by proposal category: For SCC-DG proposals, integrative research may be more exploratory, focusing on early-stage concepts that require further refinement and scoping through project activities. For SCC-IRG and SCC-Large proposals, the research is expected to be well-reasoned, mature in its conception, strongly integrated across disciplines, and supported with clearly defined aims for achieving scientific and technological impact that support critical community needs. 
1.  Community Engagement: SCC-DG, -IRG, and -LSR proposals Proposals should clearly identify and define the targeted community and the participating stakeholders. Proposals should also describe activities that reflect meaningful community engagement, considering community stakeholders and their participation and input as integral to success of the research. Investigators and community stakeholders should work closely to develop, implement, and evaluate creative approaches to accomplish the goals of the proposed research and overcome a compelling community challenge. 
    1.  **Community stakeholders may involve any of the following: residents, neighborhood or community groups, nonprofit or philanthropic organizations, businesses, health and social services agencies, and municipal entities that could include libraries, museums, public works departments, and/or educational institutions.** Community stakeholder engagement can **leverage partnerships with regional stakeholders including local, county, state, and tribal governments and departments, and/or regional cooperative initiatives**. 
    2.  The **budget should take into consideration community interactions and demonstrate that community participants, as appropriate, are being equitably compensated for their contribution**. Note that the nature of the community engagement will vary by proposal category: For SCC-DG proposals, community engagement should be co-design in planning and establishing research direction-setting and may include activities that build and strengthen trust and additional community engagement. For SCC-IRG and SCC-Large proposals, the community engagement piece is expected to be **mature, substantive, and robust**. 
1.  Evaluation Plan: SCC-IRG and -LSR proposals only The proposal Evaluation Plan should clearly define the methods and metrics for evaluating success of the proposed research activities and goals. In this section, the proposers should clearly describe how research hypotheses will be confirmed. This should be considered as an important section whereby the PI demonstrates their insights into the proposed research by clearly describing how the research hypotheses will be confirmed and demonstrated through realistic in-context experiments. The Evaluation Plan should include details on how both the research and its outcomes will be validated and demonstrated through testing and implementation within controlled environments and/or real-world contexts through full or sub-scale prototypes and/or simulations. This section should include project milestones and timelines, with details of the specific evaluation metrics, methodologies and criteria that will be employed to determine process and/or project success. 
1.  Management Plan: SCC-IRG and -LSR proposals only Researchers from diverse fields and community stakeholders are expected to work collaboratively and interdependently to create a shared vision of the project and to accelerate the rate of discoveries. Each SCC-IRG and SCC-Large proposal must contain a Management Plan that specifies the roles and responsibilities of the collaborating PI, co-PIs, other Senior Personnel, paid consultants, and stakeholder participants. It must also describe the expertise of team members undertaking the research. A list of key personnel is required. This includes their name and job title, their institutional /organizational affiliation, and the role the key community participants play. The plan must address communications between partner entities and fields as well as how the project will be managed across institutions, and community entities. It should also identify collaboration mechanisms that enable integration of the entire team. The plan must include a timeline showing principal tasks, milestones, and interactions between the various team members. Supplementary Documents: 13 
1.  Project Personnel and Partner Institutions: Provide information for all organization or partnering entities involved in the project and provide a list of all associated personnel, including their institutional/organizational affiliation. This list of personnel must be numbered, grouped according to associated institution/organization, and conform to the below format: Keisha Johnson; XYZ University; PI Neil Gupta; University of PQR; Senior/Key Personnel Xavier Brown; XYZ University; Postdoc Marc Garcia; ABC Inc.; Funded Consultant Bob Adams; HHH Community organization, Funded Consultant Maria White; XYX Govt organization; Unfunded Collaborator Lucy Wang; ZZZ University; Subawardee 
1.  Letters of Collaboration: For all substantial collaborations and engagements (included or not included in the budget) with partner organizations including communities described in the Project Description, Letters of Collaboration are strongly encouraged. These should be provided in the Supplementary Documents section of the proposal and follow the recommended format specified in the PAPPG. Letters of Collaboration should not contain endorsements or evaluation of the proposed project. Collaborative activities that are identified in the budget should follow the instructions in the PAPPG. Any substantial collaboration with individuals not included in the budget should also be described in the Facilities, Equipment and Other Resources section of the proposal and documented in a Letter of Collaboration from each collaborator. B. Budgetary Information Cost Sharing: Inclusion of voluntary committed cost sharing is prohibited. Budget Preparation Instructions: Budgets for all projects must include funding for one or more designated S\&CC project representatives (PI/co-PI/Senior Personnel or NSF-approved replacement) to attend annual S\&CC PI meetings during the proposed lifetime of the award and are encouraged to include funding for attendance of one community stakeholder (see Section II of this program solicitation). Proposers are also encouraged to consider including funding for community stakeholder participation in the project as part of the project budget or explain why this does not make sense or is not possible.
**From the PAPPG:**
**Sections of the Proposal**
The sections described below represent the body of a research proposal submitted to NSF. Failure to submit the required sections will result in the proposal not being accepted[\[10\]](https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ftn10), or being returned without review. See Chapter IV.B for additional information.
A full research proposal must contain the following sections[\[11\]](https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ftn11). Note that the *NSF Grants.gov Application Guide* may use different naming conventions, and sections may appear in a different order than in Research.gov, however, the content is the same:
1.  Cover Sheet
2.  Project Summary
3.  Table of Contents
4.  Project Description
5.  References Cited
6.  Budget and Budget Justification
7.  Facilities, Equipment and Other Resources
8.  Senior/Key Personnel Documents
      - (i) Biographical Sketch(es)
      - (ii) Current and Pending (Other) Support
      - (iii) Collaborators and Other Affiliations (see also Chapter II.D.1 for additional information on submission of single copy documents
      - (iv) Synergistic Activities
9.  Special Information and Supplementary Documentation[\[12\]](https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ftn12)
      - (i) Mentoring Plan (if applicable)
      - (ii) Data Management and Sharing Plan
The proposal preparation instructions for Planning, RAPID, EAGER, RAISE, GOALI, Ideas Lab, FASED, Conference, Equipment, Travel, Center, and Research Infrastructure proposal types may deviate from the above content requirements.
All proposals submitted to NSF will be reviewed using the two NSB-approved merit review criteria described in greater length in Chapter III.
### **a. Cover Sheet**
There are seven components of the Cover Sheet. The Cover Sheet data elements are as follows:
  - Requested Start Date and Proposal Duration  
    The proposed duration for which support is requested should be consistent with the nature and complexity of the proposed activity. The Foundation encourages proposers to request funding for durations of three to five years when such durations are necessary for completion of the proposed work and are technically and managerially advantageous. The requested start date should allow at least six months for NSF review, processing, and decision. PIs should consult their organization’s SPO for unusual situations (e.g., a long lead time for procurement) that create problems regarding the proposed start date. Specification of a desired start date for the project is important and helpful to NSF staff; however, requests for specific start dates may not be met.
  - Related Letter of Intent (LOI)  
    If an LOI was submitted, enter the LOI ID number that was issued upon submission.
  - Related Preliminary Proposal  
    If a preliminary proposal was submitted, and the organization was either invited or encouraged/discouraged to submit a full proposal, provide the Preliminary Proposal Number.
  - Prime Organization  
    The information on the Awardee Organization is prefilled on the Cover Sheet based on the login information entered. NSF uses the legal business name and physical address from the organizations’ SAM registration.  
    The awardee organization name, address, NSF organization code, UEI, and Employer Identification Number/Taxpayer Identification Number are derived from the profile information provided by the organization or pulled by NSF from the SAM database and are not entered when preparing the Cover Sheet.  
    Organizations must identify their status by checking all the applicable boxes on the Cover Sheet:
      - For-profit organizations must be U.S.-based commercial organizations, including small businesses, with strong capabilities in scientific or engineering research or education and a passion for innovation. See Chapter I.E.3 for additional information.
      - A small business must be organized for profit, independently owned, and operated (not a subsidiary of, or controlled by, another firm), have no more than 500 employees, and not be dominant in its field.
      - A minority business must be: (i) at least 51 percent owned by one or more minority or disadvantaged individuals or, in the case of a publicly owned business, have at least 51 percent of the voting stock owned by one or more minority or disadvantaged individuals; and (ii) one whose management and daily business operations are controlled by one or more such individuals.
      - A woman-owned business must be at least 51 percent owned by a woman or women, who also control and operate it. "Control" in this context means exercising the power to make policy decisions. "Operate" in this context means being actively involved in the day-to-day management.
  - Primary Place of Performance  
    The Primary Place of Performance (PPoP) information will default to the organization’s physical address. If the project will be performed at a location other than the awardee organization, provide the following information (where applicable).
      - Organization Name (identify the organization name of the primary site where the work will be performed, if different than the awardee);
      - Country
      - Street Address;
      - City;
      - State/Territory; and
      - 9-digit Postal Code.
  - Note that not all fields listed above are required. Research.gov specifies the fields that are required for projects that will be performed at locations other than that of the proposing organization.  
    For research infrastructure projects, the project/performance site should correspond to the physical location of the asset. For research infrastructure that is mobile or geographically distributed, information for the primary site or organizational headquarters (as defined by the proposer) should be provided.
  - Other Federal Agencies  
    If the proposal is being submitted for consideration by another Federal agency, the abbreviated name(s) of the Federal agency(ies) must be identified in the space provided.
  - Other Information  
    If any of the following items on the Cover Sheet are applicable to the proposal being submitted, the relevant box(es) must be checked.
      - Beginning Investigator (See Chapter II.E.2) (Note: this box is applicable only to proposals submitted to the Biological Sciences Directorate.)
      - Disclosure of Lobbying Activities (See Chapter II.D.1.d)
      - Proprietary or Privileged Information (See Chapter II.D.1.c and II.E.1)
      - Special Exceptions to the Deadline Date Policy (See Chapter I.F.3)
      - Historic Places (See Chapter II.D.2.i(vii))
      - Live Vertebrate Animals[\[13\]](https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ftn13) (See Chapter II.E.4)
      - Human Subjects[\[14\]](https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ftn14) (See Chapter II.E.5)
      - Funding of an International Branch Campus of a U.S. IHE (See Chapter I.E.1) – If this box is checked, the proposer also must enter the name of the applicable country(ies) in the International Activities Country Name(s) box described below.
      - Funding of a Foreign Organization or Foreign Individual (See Chapter I.E.2) – If this box is checked, the proposer also must enter the name of the applicable country(ies) in the International Activities Country Name(s) box described below.
      - International Activities Country Name(s) – each proposal that describes an international activity, proposers should list the primary countries involved. An international activity is defined as research, training, and/or education carried out in cooperation with international counterparts either overseas or in the U.S. using virtual technologies. Proposers also should enter the country/countries with which project participants will engage and/or travel to attend international conferences. If the specific location of the international conference is not known at the time of the proposal submission, proposers should enter “Worldwide”. (See Chapter II.E.8)
      - Potential Life Sciences Dual Use Research of Concern (DURC) (See Chapters II.E.6 and XI.B.5)
      - Off-Campus or Off-Site Research – For purposes of this requirement, off-campus or off-site research is defined as data/information/samples being collected off-campus or off-site, such as fieldwork and research activities on vessels and aircraft. (See Chapter II.D.1.d(viii) and II.E.9).
      - Potential Impacts on Tribal Nations – (See Chapter II.E.10)
### **b. Project Summary**
Each proposal must contain a summary of the proposed project not more than one page in length. The Project Summary consists of an overview, a statement on the intellectual merit of the proposed activity, and a statement on the broader impacts of the proposed activity.
The overview includes a description of the activity that would result if the proposal were funded and a statement of objectives and methods to be employed. The statement on intellectual merit should describe the potential of the proposed activity to advance knowledge. The statement on broader impacts should describe the potential of the proposed activity to benefit society and contribute to the achievement of specific, desired societal outcomes.
The Project Summary should be informative to other persons working in the same or related fields, and, insofar as possible, understandable to a broad audience within the scientific domain. It should not be an abstract of the proposal.
### **c. Table of Contents**
A Table of Contents is automatically generated for the proposal. The proposer cannot edit this form.
### **d. Project Description (including Results from Prior NSF Support)**
#### **(i) Content**
The Project Description should provide a clear statement of the work to be undertaken and must include the objectives for the period of the proposed work and expected significance; the relationship of this work to the present state of knowledge in the field, as well as to work in progress by the PI under other support.
The Project Description should outline the general plan of work, including the broad design of activities to be undertaken, and, where appropriate, provide a clear description of experimental methods and procedures. Proposers should address what they want to do, why they want to do it, how they plan to do it, how they will know if they succeed, and what benefits could accrue if the project is successful. The project activities may be based on previously established and/or innovative methods and approaches, but in either case must be well justified. These issues apply to both the technical aspects of the proposal and the way in which the project may make broader contributions.
The Project Description also must contain, as a separate section within the narrative, a section labeled "Broader Impacts", and "Broader Impacts" must appear as a heading on its own line. This section should provide a discussion of the broader impacts of the proposed activities. Broader impacts may be accomplished through the research itself, through the activities that are directly related to specific research projects, or through activities that are supported by, but are complementary to the project. NSF values the advancement of scientific knowledge and activities that contribute to the achievement of societally relevant outcomes. Such outcomes include, but are not limited to: full participation of women, persons with disabilities, and underrepresented minorities in science, technology, engineering, and mathematics (STEM); improved STEM education and educator development at any level; increased public scientific literacy and public engagement with science and technology; improved well-being of individuals in society; development of a diverse, globally competitive STEM workforce; increased partnerships between academia, industry, and others; improved national security; increased economic competitiveness of the U.S.; use of science and technology to inform public policy; and enhanced infrastructure for research and education. These examples of societally relevant outcomes should not be considered either comprehensive or prescriptive. Proposers may include appropriate outcomes not covered by these examples.
Plans for data management and sharing of the products of research, including preservation, documentation, and sharing of data, samples, physical collections, curriculum materials and other related research and education products should be described in the Special Information and Supplementary Documentation section of the proposal (see Chapter II.D.2.i for additional instructions for preparation of this section).
For proposals that include funding to an International Branch Campus of a U.S. IHE or to a foreign organization or foreign individual (including through use of a subaward or consultant arrangement), the proposer must provide the requisite explanation/justification in the project description. See Chapter I.E for additional information on the content requirements.
#### **(ii) Page Limitations and Inclusion of Uniform Resource Locators (URLs) within the Project Description**
Brevity will assist reviewers and Foundation staff in dealing effectively with proposals. Therefore, the Project Description (including Results from Prior NSF Support, which is limited to five pages) may not exceed 15 pages. Visual materials, including charts, graphs, maps, photographs, and other pictorial presentations are included in the 15-page limitation. PIs are cautioned that the Project Description must be self-contained, and that URLs must not be used because: 1) the information could circumvent page limitations; 2) the reviewers are under no obligation to view the sites; and 3) the sites could be altered or deleted between the time of submission and the time of review.
Conformance to the 15-page limit will be strictly enforced and may not be exceeded unless a deviation has been specifically authorized. (Chapter II.A contains information on deviations.)
#### **(iii) Results from Prior NSF Support**
The purpose of this section is to assist reviewers in assessing the quality of prior work conducted with prior or current NSF funding. If any PI or co-PI identified on the proposal has received prior NSF support including:
  - an award with an end date in the past five years; or
  - any current funding, including any no cost extensions,
information on the award is required for each PI and co-PI, regardless of whether the support was directly related to the proposal or not. In cases where the PI or any co-PI has received more than one award (excluding amendments to existing awards), they need only report on the one award that is most closely related to the proposal. Support means salary support, as well as any other funding awarded by NSF, including research, Graduate Research Fellowship, Major Research Instrumentation, conference, equipment, travel, and center awards, etc.
The following information must be provided:
  - (a) the NSF award number, amount and period of support;  
    (b) the title of the project;  
    (c) a summary of the results of the completed work, including accomplishments, supported by the award. The results must be separately described under two distinct headings: Intellectual Merit and Broader Impacts;  
    (d) a listing of the publications resulting from the NSF award (a complete bibliographic citation for each publication must be provided either in this section or in the References Cited section of the proposal); if none, state “No publications were produced under this award.”  
    (e) evidence of research products and their availability, including, but not limited to: data, publications, samples, physical collections, software, and models, as described in any Data Management and Sharing Plan; and  
    (f) if the proposal is for renewed support, a description of the relation of the completed work to the proposed work.
If the project was recently awarded and therefore no new results exist, describe the major goals and broader impacts of the project. Note that the proposal may contain up to five pages to describe the results. Results may be summarized in fewer than five pages, which would give the balance of the 15 pages for the Project Description.
#### **(iv) Unfunded Collaborations**
Any substantial collaboration with individuals not included in the budget should be described in the Facilities, Equipment and Other Resources section of the proposal (see Chapter II.D.2.g) and documented in a letter of collaboration from each collaborator. Such letters should be provided in the supplementary documentation section of Research.gov and follow the format instructions specified in Chapter II.D.2.i. Collaborative activities that are identified in the budget should follow the instructions in Chapter II.E.3.
#### **(v) Group Proposals**
NSF encourages submission of proposals by groups of investigators; often these are submitted to carry out interdisciplinary projects. Unless stipulated in a specific program solicitation, however, such proposals will be subject to the 15-page Project Description limitation established in Section (ii) above. PIs who wish to exceed the established page limitations for the Project Description must request and receive a deviation in advance of proposal submission. (Chapter II.A contains information on deviations.)
#### **(vi) Proposals for Renewed Support**
See Chapter V for guidance on preparation of renewal proposals.
### **e. References Cited**
Reference information is required. Each reference must include the names of all authors (in the same sequence in which they appear in the publication), the article and journal title, book title, volume number, page numbers, and year of publication. (See also Chapter II.D.2.d(iii)(d)) If the proposer has a website address readily available, that information should be included in the citation. It is not NSF's intent, however, to place an undue burden on proposers to search for the URL of every referenced publication. Therefore, inclusion of a website address is optional. A proposal that includes reference citation(s) that do not specify a URL is not considered to be in violation of NSF proposal preparation guidelines and the proposal will still be reviewed.
Proposers must be especially careful to follow accepted scholarly practices in providing citations for source materials relied upon when preparing any section of the proposal. While there is no established page limitation for the references, this section must include bibliographic citations only and must not be used to provide parenthetical information outside of the 15-page Project Description.


# Proposal Only

SCC-IRG Preliminary Proposal: Closing the Heat Gap – Precision Heat Modeling for Community-Driven Cooling Interventions
1.  ~~Cover Sheet~~
2.  Project Summary
3.  Table of Contents
4.  Project Description
5.  References Cited
6.  Budget and Budget Justification
7.  Facilities, Equipment and Other Resources
8.  Senior/Key Personnel Documents
      - (i) Biographical Sketch(es)
      - (ii) Current and Pending (Other) Support
      - (iii) Collaborators and Other Affiliations (see also Chapter II.D.1 for additional information on submission of single copy documents
      - (iv) Synergistic Activities
9.  Special Information and Supplementary Documentation[\[12\]](https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ftn12)
      - (i) Mentoring Plan (if applicable)
      - (ii) Data Management and Sharing Plan
Project Description sections (15 total pages)
  - Broader Impacts 
  - Results from Prior NSF Support
  - Integrative Research
  - S\&CC Research Focus
  - Community Engagement
  - Evaluation Plan
  - Management Plan
Supplementary Documents
  - Project Personnel and Partner Institutions
  - Letters of Collaboration 
  - Budgets
Hyphae supplemental documents
 
~~Budget in RR format~~
~~Budget Justification(pdf format in accordance with PAPPG)~~
~~<comment_start id=kix.pp5i23s4yt7o>Subrecipient Commitment Form (pdf, please let me know if another copy of this document is needed)<comment_end id=kix.pp5i23s4yt7o>~~
~~<comment_start id=kix.6n2z4z48kxhz>Scope of Work (word doc or pdf)<comment_end id=kix.6n2z4z48kxhz>~~
~~Senior Personnel Documents~~
1.  ~~<comment_start id=kix.6gzzyegj2r19>SciENcv Biosketch (pdf)<comment_end id=kix.6gzzyegj2r19>~~
2.  ~~<comment_start id=kix.nptdmq7az85f>SciENcv Current and Pending (pdf)<comment_end id=kix.nptdmq7az85f>~~
3.  ~~COA (excel)~~
4.  ~~Synergistic Activities(pdf)~~
~~<comment_start id=kix.4hhu7fwwc4gh>IDC Rate Agreement<comment_end id=kix.4hhu7fwwc4gh>~~


# Project Summary



# Proposal + references

# SCC-IRG: Closing the Heat Gap: Precision Heat Modeling for Community-Driven Cooling Interventions
### Introduction
Improving our understanding of urban areas is a high priority for the scientific community. Urban regions are where most people live and are well known to be warmer than surrounding rural areas, a fact generally referred to as the Urban Heat Island (UHI) {see review by \\Qian, 2022 \#3000}. The UHI occurs due to various factors {Arnfield, 2003 \#3100;Stewart, 2011 \#3083}, such as the materials used in construction, e.g., concrete and asphalt, which have a high thermal mass, absorbing and storing heat during the day and releasing it at night. Waste heat from human activities, including heat from buildings, vehicles, HVAC, and industrial processes, is also a contributor. 
 
The risk of heat-related illnesses and mortality is expected to increase with increasing temperature {Gasparrini, 2015 \#2969;Kovats, 2008 \#3052;Ebi, 2021 \#3054}, but it will not be spread evenly.  It will be exacerbated by the UHI and, within urban regions, disproportionately affect vulnerable populations such as the poor, the young and the elderly, and those with pre-existing health conditions {Hajat, 2009 \#3613;Hsu, 2021 \#2949;Yin, 2023 \#3002}.  For example, 30% of deaths in one Arizona study were in mobile homes {Charley, 2023 \#3610}. Some of this difference in vulnerability is a relic of segregationist housing policy, where hotter neighborhoods with higher UHI were more likely to have formally been “redlined” areas {Hoffman, 2020 \#3049}.
 
The economic repercussions are also becoming increasingly evident. A decline in productivity is one such outcome {e.g.\`, \\Lai, 2023 \#3625}. Elevated temperatures make both manual labor and cognitive tasks more challenging due to heat-induced fatigue, diminished focus, and a higher rate of mistakes. This is especially true for industries that involve outdoor work, or in areas where air conditioning is not prevalent.  Heat waves also put a strain on energy infrastructure {Lee, 2022 \#2970}, causing costs to rise \<\<Dessler ref\>\>. These challenges cumulatively lower overall productivity and hamper economic growth, with a more significant burden placed on low-income communities and regions. 
 
Despite extensive research on urban heat islands and their impacts, critical gaps exist in our understanding of heat exposure at fine spatial scales. Current heat studies, including the Harris County Public Health 2019-2024 heat study {Harris County Public Health, 2024 \#3982}, have only assessed impacts at large scales. This coarse resolution obscures crucial variations in heat exposure that occur within neighborhoods or even smaller space scales — variations that can mean the difference between comfort and danger for vulnerable populations. Our project pioneers a transformative approach by shifting to meter-scale heat analysis, providing unprecedented insight into how microclimates within urban environments affect human health and comfort.
 
Transportation networks are particularly challenging environments for heat exposure, as they often feature extensive impervious surfaces, limited shade, and concentrated human activity. Bus stops and other transit hubs can become dangerous hot spots during extreme heat events, with waiting passengers experiencing prolonged exposure in potentially dangerous conditions. This disproportionately affects transit-dependent populations who may already be vulnerable to heat stress. By focusing our research on neighborhoods containing transportation infrastructure in Houston, we address the critical intersection of infrastructure, public health, and social equity concerns.
Urban parks and recreational spaces present a complex dynamic in the context of urban heat. While these green spaces can serve as “cooling islands” within the urban heat landscape, their effectiveness varies dramatically based on design, vegetation density, and maintenance. Well-designed parks with mature tree canopies can be several degrees cooler than surrounding urban areas, providing essential relief during heat events {Yin, 2024 \#3984}{Razzaghmanesh, 2021 \#3985}.  But they tend to increase humidity, which can offset some of the benefits of cooler temperatures {Du, 2021 \#3983}.
Many recreational spaces in underserved communities feature minimal shade, extensive paved surfaces, and inadequate irrigation—paradoxically becoming heat traps rather than refuges. This disparity in park quality creates inequitable access to cooling resources, as vulnerable populations with the greatest need for heat relief often have access only to degraded spaces offering minimal cooling benefits. 
Our proposal will … \[put in statement about how we’re addressing these issues\] Our meter-scale analysis will quantify these variations within and between parks, enabling targeted improvements to maximize their cooling potential. By understanding the thermal performance of different recreational space configurations, we can transform these community assets into effective components of a comprehensive heat mitigation strategy that provides equitable access to cooling resources across Houston's diverse neighborhoods.
The high-risk, high-reward nature of our approach lies in its integration of multiple innovative elements: meter-scale heat mapping, deployment of low-cost sensor networks, correlation with address-level health outcomes, and community-led intervention design. While any one of these components represents significant advancement, their integration creates the potential for transformative impact. By developing a replicable framework that communities can use to identify, measure, and mitigate extreme heat exposure, we aim to establish Houston as a national leader in climate resilience planning.
 
Our project embodies the goals of the NSF Smart and Connected Communities program by synergistically integrating intelligent technologies with the natural and built environments to improve quality of life. Working closely with community stakeholders—including Houston Metro, Harris County Public Health, and the Gulfton Super Neighborhood Council—we will co-design interventions that are both scientifically sound and responsive to community needs. This collaborative approach ensures that research findings translate directly into actionable strategies for reducing heat exposure among Houston's most vulnerable populations.
The interdisciplinary nature of our work brings together expertise from geosciences (heat mapping, climate modeling), engineering (green infrastructure implementation), computer science (machine learning, geospatial data analytics), and social and behavioral sciences (community engagement, public health impact assessment). This integration enables us to address the complex, multifaceted challenge of urban heat in ways that would be impossible through a single disciplinary lens. By combining these diverse perspectives, we create opportunities for novel insights and solutions that can be scaled and transferred to other urban environments facing similar challenges.
**Integrative Research**
This research will combine research in geosciences and in social and behavioral sciences.  
1.  ### <comment_start id=kix.s6xchnmvjpvu>Geoscience component<comment_end id=kix.s6xchnmvjpvu>
For the geosciences research, we will produce a high-resolution estimates of the temperature field over \[region? Houston? A particular neighborhood?\] … 
**3D digital twin (neighborhood-wide existing conditions)**: We will gather aerial LIDAR point cloud data, meter-scale digital elevation model rasters and concomitant multispectral (4 band) aerial imagery of the Houston area from the Texas Geographic Information Office. We will also collect building footprint geospatial polygons from OpenStreetMap.  These four datasets will be merged to yield a multispectral point cloud which we will segment into ground, above-ground vegetation, and buildings. The data will also be used to generate a 60-cm land cover dataset that distinguishes pavement  and grassy areas. 
The segmented point cloud and land cover data will be converted to raster layers suitable for inputs to UMEP SOLWEIG, which computes skyview and building aspect indices for solar path analysis, and uses land cover and vegetation data for heat storage, reflection and emission modeling. The terrain, vegetation and building data will also be converted to 3D watertight triangular mesh geometry suitable for input into OpenFOAM computational fluid dynamics software. 
**<comment_start id=kix.vi64k3o1gr0s>UMEP SOLWEIG**<comment_end id=kix.vi64k3o1gr0s>: We will gather meteorological data from a time period corresponding to hot summer conditions concomitant with sensor deployments. We use the [<comment_start id=kix.j0vdqin8i0pj>Iowa Environmental Mesonet (IEM)](https://mesonet.agron.iastate.edu/) <comment_end id=kix.j0vdqin8i0pj>website for extracting historical data and generalizing and binning wind directions to find the most common wind direction and speed. We will gather additional input from local airport weather service stations which include regional air temperature, pressure and humidity. We also obtained estimates of total incoming shortwave radiation from the [CBE clima tool](https://clima.cbe.berkeley.edu/). These data will be gathered in hourly increments for each of several 24 hours periods in the duration of the study. The SOLWEIG solver takes the digital twin and the meteorological inputs and produces outputs of mean radiant temperature estimates at the meter scale. 
**Computational Fluid Dynamics: **Once pilot intervention sites have been identified by the community design process, these sites (at the scale of a several city block radius) will be simulated in OpenFOAM to develop estimations of wind speed and direction at the submeter scale. The trimesh 3d digital twins will be discretized into the OpenFOAM dynamic mesh, using a fine resolution (0.5 m) cell size in several layers near the terrain and building surfaces, and progressively coarser cell sizes (up to 12 m) further from obstacles. Again using the same meteorological inputs as for SOLWEIG, we will set boundary conditions for the domain with wind input speed and direction and compute the Reynolds Averaged Navier Stokes solution to convergence. This will result in a wind field for the domains that can be mixed with the SOLWEIG mean radiant temperature data to get a universal thermal comfort index (UTCI) or other metrics of heat stress that incorporate air temperature, radiant temperature, humidity and wind speed.
To advance the state of the art in urban climate modeling, we propose to extend our existing OpenFOAM-based urban wind flow pipeline to incorporate coupled thermal processes—including surface energy exchange, radiative heating, and moisture dynamics—at high spatial resolution. This extension will enable predictive simulation of surface and air temperature dynamics under varying material and design scenarios and support the assessment of thermal comfort metrics such as Mean Radiant Temperature (MRT).
Our current pipeline is capable of resolving complex urban geometries, turbulent airflow, and pollutant dispersion using Reynolds-Averaged Navier–Stokes (RANS) equations. To simulate thermal behavior, we will introduce additional scalar transport equations for air temperature and humidity, using the Boussinesq approximation to model buoyancy-driven flow. Material-dependent surface properties—including albedo, emissivity, thermal conductivity, specific heat capacity, and moisture retention—will be incorporated to represent the thermophysical behavior of urban surfaces such as asphalt, concrete, white and black roofs, trees, and vegetated ground. These properties will be embedded into a surface energy balance model that accounts for absorbed solar radiation, longwave radiative exchange, sensible (convective) and latent (evaporative) heat fluxes, conduction, and transient thermal storage.
To compute solar gains at each surface, we will leverage existing OpenFOAM tools such as the solarLoad class and built-in radiation models (e.g., view-factor-based longwave models), while remaining open to integrating external solar analysis tools. The solarLoad model computes direct solar irradiance based on solar geometry and surface orientation, but does not account for shading caused by surrounding buildings or vegetation. To address this limitation, we will incorporate spatially varying surface irradiance fields derived from external tools such as UMEP/SOLWEIG (e.g., sky view factors) and Radiance (e.g., solar exposure maps). These inputs can be mapped onto the surface mesh as boundary heat flux fields or used as correction factors to the solarLoad output. This approach enables the integration of directional shading effects, diffuse sky radiation, and urban occlusion into the surface energy balance. The influence of urban morphology—including canyon geometry, surface orientation, and vegetation—on solar access and radiative trapping will thus be represented directly in the simulation through the 3D mesh and spatially distributed solar input fields.
Mean Radiant Temperature (MRT) will be derived directly from CFD outputs, using surface temperature fields, view-factor-based radiation exchange models, and external shortwave irradiance inputs. MRT will be computed as a post-processed quantity by combining longwave emissions from surrounding surfaces with directional shortwave solar gains, allowing high-resolution spatial mapping of thermal exposure. This approach leverages existing CFD fields and supports thermal comfort analysis without requiring additional equations to be solved during runtime. We will consider both simplified (longwave-only) and full MRT formulations, depending on available solar data and the intended use case.
We will reuse and adapt components from existing OpenFOAM solvers: buoyantSimpleFoam (for buoyancy-driven airflow), chtMultiRegionFoam (for multi-region heat transfer), and hamFoam (for moisture transport in porous materials). These components will be combined into a modular solver architecture that enables flexible material assignment, surface-type resolution, and energy budget closure. This framework is conceptually aligned with the urbanMicroclimateFoam solver developed by ETH Zurich, which integrates airflow, radiative heat transfer, and hygrothermal behavior in urban materials. The resulting model will support scenario testing of urban design interventions, such as cool roofs, reflective pavements, and green infrastructure, by directly linking material and form to heat exposure outcomes.
**Sensor network: **We will install 36 sensor nodes. Each node consists of a 6” copper black globe temperature sensor, an air temperature sensor, a humidity sensor,  an anemometer, and a people-counter. Each node has a LORAWAN radio enabling long range, low-bandwidth communication with a central LORAWAN gateway hub. With direct line-of-sight the LORAWAN nodes can communicate to the hub up to 300 miles away, however in realistic urban environments where line of sight is broken up by buildings and reflections are more common, we typically want a hub placed every few miles to bridge signal areas. For this study we will deploy up to six such hubs to get good coverage. The sensors push readings every 20 minutes through the gateway, which connects to the internet via cellular or wifi if available at the gateway site. The sensor readings are forwarded from the gateway to a LORAWAN Network Server in the cloud, which publishes the readings on an MQTT broker, which our backend subscribes to to collect the readings in an influxdb time-series database. 
**Sensor Locations:** To get a spread of radiant temperature readings we will place the sensors in a matrix of landscape conditions. The conditions of interest pertain to land cover and shade provision; for land cover there is grass and pavement, while for shade there is exposed and shaded. With 9 sensors in grass/shade, 9 sensors in grass/exposed, 9 sensors in pavement/shade, and 9 sensors in pavement/exposed we will be able to discern the impacts of each landscape feature on the thermal comfort metrics. These locations will be decided in coordination with the community design process to provide before and after sensor readings for the heat mitigation intervention pilot. During the site selection process we will also vet property owners to get permission for attaching sensors to poles, trees, signposts and buildings as needed. Where the study design calls for attaching to city-owned utility poles we will coordinate with city transportation and public works departments to get necessary permissions and right-of-way permits for sensor installation. 
**Simulation Validation with Sensors:** The simulation of existing conditions concomitant with sensor readings will allow us to validate the simulation results using the sensors as ground-truth. For each hour simulated, sensor readings from corresponding timestamps will be pulled from the time-series database and matched with the geolocation of the sensors within the simulation domain. The R2 and RMSE will be calculated to determine the fidelity of the simulation with the actual conditions. 
1.  ### Social science component
**3D digital twin (pilot interventions): **While the digital twin of existing conditions will be derived from the datasets described above, we will also develop new digital twins for each of various intervention designs developed with the community for heat mitigation. These will be at a smaller scale and involve computing 3D raster and trimesh geometries from designs developed in the community design process. These can then also be fed into the physics simulations to estimate the impacts of the interventions.
**Agent-based simulations**: SOLWEIG and OpenFOAM outputs give us gridded maps of heat and wind at the meter scale over the entire simulation domain. However, exposure will occur only where people gather, walk or cycle, so the key transportation networks will be mapped using tile2net deep learning algorithm from commercially available 15cm aerial imagery. These networks can be queried within the heat and wind maps to develop an agent-based model of how much thermal stress exposure people will experience walking, biking or gathering throughout the study area. These maps can be used to assist with site prioritization for interventions, and also be used to guide placement of sensors. 
**Pre intervention modeling and monitoring: **Sensors will be deployed in the vicinity of potential interventions to determine the effect of the interventions on the heat-stress metrics. This, combined with people-counter pre/post data will allow estimation of overall exposure change in the community. The pre and post simulations can be validated with the sensor data, enabling generalizability of the modeling approach to other communities.  
Health impact modeling: The primary goal of this part of the proposal is to examine how heat-related mortality risk varies at neighborhood scales within a city and to determine the extent to which interventions will reduce mortality. To the best of our knowledge, this is an entirely novel analysis.  Most previous extreme-heat mortality studies have analyzed much larger geographic regions (e.g., city, state, country) and rely entirely on daily average air temperature.
We will analyze mortality and temperature data for Houston spanning from 2010 to 2024.  Fine-scale mortality data will be obtained from the **Census Bureau’s Research Data Center (RDC) at Texas A\&M University**.  We will use the standard method of estimating mortality from extreme heat, the **Distributed Lag Non-Linear Model (DLNM)**, which incorporates the delayed effects of extreme heat.  Code to do this calculation is available in an R package.
After determining the risk-ratio curves for each neighborhood, we will bring in socioeconomic and other datasets in order to determine the factors that cause some neighborhoods to be more vulnerable than others.  Examples of explanatory factors we will investigate include the amount of vegetation in a neighborhood (which lowers temperature) or median income (which correlates with accessibility to air conditioning). 
#### **Novelty and Granularity of Research**
  - Highlight the innovative shift from conventional census tract-level analysis to detailed meter-scale heat mapping.
  - Clearly describe the methodological advancement of correlating meter-scale heat exposure data with individual address-level public health outcomes.
  - Emphasize the transformative potential of this detailed scale of analysis.
### **Community Engagement**
#### **Stakeholder Participation**
  - Identify the target community and stakeholders involved (residents, community groups, municipal entities).
  - Emphasize meaningful co-design, co-implementation, and co-evaluation of the pilot interventions.
#### **Pilot Intervention**
**Intervention Design**: Community stakeholders already involved with ongoing intervention designs will be engaged to incorporate monitoring and modeling into their design process. For example Ultra Barrio transit shade structures are in the conceptual design phase for the greener Gulfton project; we can model the structures, estimate the impacts of design features through iterative modeling, and place heat sensors at potential shade structure sites to gather pre-implementation data. Pending completion of the intervention, post-intervention data will also be gathered to evaluate impacts. 
We have developed software with NSF funding that takes greening intervention designs, simulates their growth over time and the resulting impacts on mean radiant temperature. This can be used to optimize community designs. 
**<comment_start id=kix.r4ap8ljszeej>Intervention Implementation:<comment_end id=kix.r4ap8ljszeej>**
Final determination of cooling intervention design and location will come after engagement through community outreach and workshops. Because the final schedule of community interventions may be beyond the scope of this project funding, we will work with communities to site sensors near their interventions, and provide a platform for continued use of project data for future implementation phases. 
The team identified an area in the center of the Gulfton neighborhood as a potential location for cooling intervention. Though the specifics of this area may change, the community partner works within Gulfton and other neighborhoods which include similar locations that would benefit from a cooling intervention. Figure X shows an example of the type of potential intervention design that could be discussed with the community and eventually implemented with pre and post monitoring and simulation guided design. The planting of shade trees along sidewalks would reduce heat exposure for pedestrians. This can be enabled both by cutting new tree wells in the sidewalk (the paved portion of which is far wider than necessary) and by transitioning the adjacent parking lots from 90 degree parking to 45 degree parking, which would open up a triangle of pavement for removal and tree planting. The existing bus stop could be outfitted with a cool bus shelter. 
Gulfton St and Rampart St
  - Very developed area
  - In center of neighborhood
  - High heat observed in eat mapping and in community measurements
  - Do we need Gulfton response before picking this, or can it work as an example?
\[image\]
Figure X: Example of the type of potential intervention strategy that could be vetted by the community. Top, vicinity of Gulfton St and Rampart St existing conditions. Bottom, example shade tree planting, green circles are new shade trees planted in new sidewalk tree-wells or triangular cutouts enabled by conversion of parking lots to 45 degree angled parking. The green rectangle is a cool bus shelter. 
\[image\]
\[image\]
Infrared images from this intersection:
\[image\]\[image\]\[image\]\[image\]
**<comment_start id=kix.dgphbegb9c8p>Pre and Post implementation monitoring**:<comment_end id=kix.dgphbegb9c8p>
Pre and post implementation thermal metrics monitoring can be used to determine the efficacy of the intervention. This can be coupled with health indicator analysis derived from the larger scale high resolution heat simulations to estimate the health benefits of the interventions. We will have installed sensors in locations  directly impacted by the intervention and sensors at other locations which can act as a before-after impact control, which we can analyze as a Difference in Differences (DiD). In addition to DiD for thermal stress metrics of the environment, we will also use the people counter data to evaluate the socio-behavioral changes to pedestrian activity brought about by the intervention relative to the control areas. 
  - Describe methods to monitor efficacy through pre- and post-implementation measurements (heat exposure, thermal comfort, health indicators).
  - Solicit community feedback post implementation 
### **Evaluation Plan**
  - Clearly outline methodologies leveraging high-resolution data (meter-scale heat maps and address-level health outcomes).
  - Detail metrics and statistical approaches (e.g., distributed lag non-linear models) to assess impacts pre- and post-implementation.
  - Include specific project milestones, timelines, and success criteria for validation of outcomes.
### **Scalability and Replicability**
  - Highlight how the project’s methodologies and findings can be generalized and replicated across other communities.
By validating high resolution heat simulations with heat monitoring and health outcomes before and after community designed interventions, we can more confidently generalize the simulation optimized design process to other communities beyond the Houston area to all parts of the United States of America. We see this as a virtuous cycle, with data from Houston being used to help optimize designs of interventions in other communities, and the data from those being used to even greater effect elsewhere.  
  - Address the broader application beyond Houston, emphasizing nationwide scalability and policy influence.
### **Management Plan**
1.  **Roles & Responsibilities**:
Andrew Dessler (Professor ot Atmospheric Sciences, Texas A\&M Univ.) is the PI of this proposal and is responsible for overall management.  He will focus on the neighborhood-level mortality studies, building on previous work in this area \[Lee and Dessler reference\].  
Stephanie Piper (job title, organization) is the senior person responsible for community and stakeholder engagement.  \[put expertise and demonstration of ability to execute here\]
Hyphae is the group responsible for the heat modeling of the neighborhood being studied.  \[put names of individuals, along with job titles, add Hyphae’s expertise and demonstration of ability to execute here\].  
1.  **Details Communication & Coordination Mechanisms**:
Our team will hold biweekly virtual meetings involving all groups (heat, mortality, community engagement), ensuring regular updates on project progress, facilitating data sharing, and aligning on deliverables. Each month, the meeting will include community stakeholders to validate progress and discuss community insights.
Annual meetings will take place at HARC’s offices in Houston, where the team will meet in person along with community stakeholders.
Our project will use Slack for daily communication and quick updates and a centralized Google Drive for shared access to datasets, preliminary findings, and meeting documentation. Regular training sessions will ensure all partners are comfortable using these tools.
1.  **Includes a Timeline with Milestones**:  
      - Provides a **timeline** that includes principal tasks, milestones, and interactions between team members.
      - Breaks down the phases of the project, demonstrating **clear and achievable objectives** over the funding period.
1.  **Addresses Institutional Collaboration Challenges**:  
      - Identifies potential challenges in coordinating multiple institutions and offers solutions.
      - Details how different institutions will work together effectively and how responsibilities will be divided.
### **Best Practices for a Strong Management Plan**
  - **Be Specific**: Clearly define roles and collaboration methods rather than providing general statements.
  - **Plan for Regular Meetings**: Specify the frequency of **team meetings**, **progress reviews**, and communication strategies.
  - **Establish Conflict Resolution Strategies**: Define how disagreements or issues in collaboration will be resolved.
  - **Ensure Stakeholder Engagement**: Outline how community partners will participate and be compensated, if applicable.
  - **Scalability Consideration**: If applicable, explain how the project will scale beyond the initial timeframe and locations.
This structured approach ensures that the **Management Plan** strengthens the overall proposal and increases its competitiveness for NSF funding.
**Broader Impacts**
  - Explicitly outline anticipated broader impacts on public health, community resilience, and quality of life.
  - Highlight contributions to STEM education, local capacity building, and workforce development.
  - Describe methods for disseminating findings to policymakers and broader scientific communities through policy briefs, white papers, and integration into climate adaptation plans.
### Results from prior NSF support
###### *Dessler*
NSF Award Number: AGS-2243602
Project Title: Towards an Improved Mechanistic Understanding of Dangerous Heat Extremes Affecting US Cities in the Historical Records and Future Climate Projections
Period of Support: 7/23-6/26
Total Amount of the Award: $591,203
Project’s Intellectual Merit: This project advances our understanding of extreme heat events by defining them based on excess mortality rather than arbitrary temperature thresholds. Using a combination of high-resolution climate datasets, statistical models, and machine learning techniques, we will identify key meteorological factors contributing to extreme heat and their connections to large-scale climate circulation patterns. By testing these relationships in climate model simulations, we aim to improve predictive capabilities at seasonal and decadal timescales, providing crucial insights into the physical drivers of heat extremes and their future evolution.
Broader impacts: The findings of this project will support climate adaptation efforts by identifying the most impactful extreme heat events and their underlying causes. The results will inform urban planning and public health initiatives, particularly for vulnerable communities at high risk. Publicly available datasets and analytical tools will enhance research and decision-making for climate resilience. Additionally, this project will train two graduate students in statistical modeling, data visualization, climate modeling, and science communication, equipping them with critical skills for addressing climate risks.
Publications: {Lee, 2023 \#3905;Chao, 2024 \#3741;Lee, 2024 \#3724}
NSF Award Number: AGS-1841308
Project Title: Using large ensemble simulations from multiple global climate models to quantify the internal decadal climate variability
Period of Support: 3/19-2/22
Total Amount of the Award: $520,107
Project’s Intellectual Merit: This project advanced our understanding of the interplay between decadal climate variability and anthropogenic forcing mechanisms, particularly aerosols. By quantifying how decadal climate patterns influence the frequency, intensity, and distribution of global climate extremes, this research provided critical insights into the drivers of long-term climate variability. Additionally, the project extended its scientific contributions by analyzing the downstream effects of these climate variations, establishing clear connections between climate extremes and their impacts on public health and energy consumption patterns.
Broader impacts: This includes the training of two graduate students in interdisciplinary climate science methods, equipping them with valuable skills in climate variability analysis and its societal applications. The research findings were disseminated through peer-reviewed publications, contributing to the broader scientific community’s understanding of climate variability and its consequences. By linking climate extremes to real-world impacts, this project provides valuable information for policymakers, public health officials, and energy sector stakeholders working to mitigate climate-related risks.
Publications: {Zhou, 2021 \#2934;Chao, 2022 \#2963;Lee, 2022 \#2970;Yao, 2022 \#3582;Xu, 2022 \#3975;Da, 2022 \#3978;Banks, 2022 \#3976;Li, 2022 \#3977}
###### *Hyphae*
NSF Award Number: 2218499
Project Title: SBIR Phase II: Ecosystem Design Tool
Duration: 02/23-08/25
Total Amount of the Award: $999,592
Project's Intellectual Merit and Broader Impact: The broader impact of this SBIR Phase II project is to enable communities impacted by air pollution and extreme heat to design and implement solutions to these problems in a fast and cost-effective way. This project is developing a design tool to ensure that built environment interventions can produce maximum benefits at the lowest possible costs and shortest timelines.  This creates opportunities for communities to profit financially from improving their health and the environment. Local businesses can use this tool to make sure that they get paid fairly for reducing health care cost burdens of health insurance companies, governments and pollution producers, while making communities and the environment more resilient.
Relation to the Proposed Work: The design tool will be used to assist communities in intervention design, while also being improved by innovative research and cyclical feedback.


# Stuff from other projects

# PREVIOUS MATERIAL
<comment_start id=kix.gwogskujdby2>[Fresno Extreme Heat Analysis](https://docs.google.com/document/d/1DJkKB_EVFkRuvPayBu6GObWo7vTLbH_bvSI690HEtr8/edit?tab=t.t99jvw3m4fjm#heading=h.uby7oekw2ex9)<comment_end id=kix.gwogskujdby2>
[EHCRP\_Common\_Supliment.pdf](https://drive.google.com/file/d/10THmauePUyDnRma6yJ5d_94MlnbwypV5/view?usp=drive_link)
[EHCRP Budget workbook (2).xlsx](https://docs.google.com/spreadsheets/d/1XQMj4I54cFG6nbEg20w2KSTdXGWixWPH/edit?usp=drive_link&ouid=107498729360351714914&rtpof=true&sd=true)
[Submission\_ California Environmental Justice Coalition - California Microclimate Observatory (CAMO).pdf](https://drive.google.com/file/d/1EzPgvL42UyIKPoB4LgeIop2-Ead6d-Ol/view?usp=drive_link)
[Dallas SWMD](?tab=t.6wfo8thmiq#heading=h.jihv6zh5ulhv)
[Boyle Heights](?tab=t.6wfo8thmiq#heading=h.bf4d9kbewvkx)
[Ambrose Park](?tab=t.6wfo8thmiq#heading=h.v99fnq7h6lks)
[Hyphae Materials](?tab=t.6wfo8thmiq#heading=h.fqm97z5bky4t)
[BH-EPA-Grant EDITED](?tab=t.6wfo8thmiq#heading=h.v6vmbu1k9f49)
[Approach](?tab=t.6wfo8thmiq#heading=h.qu42iw1v4hpr)
[Project Focus:](?tab=t.6wfo8thmiq#heading=h.1rgxj8ueo7dd)
[The Need and the Challenge](?tab=t.6wfo8thmiq#heading=h.vp53l9o3ke47)
[Community-driven Design](?tab=t.6wfo8thmiq#heading=h.ukgz7urukzj)
[Evidence-based Design](?tab=t.6wfo8thmiq#heading=h.juhcgyypvtrc)
[The Science Team](?tab=t.6wfo8thmiq#heading=h.4m83cmxsbnao)
[The Approach: Measurement & Modeling](?tab=t.6wfo8thmiq#heading=h.wfs5r8r3kdxy)
[Strategies](?tab=t.6wfo8thmiq#heading=h.o1x38zcwnpf2)
[Strategy 1: ROW Tree Planting](?tab=t.6wfo8thmiq#heading=h.6gnuloo4a0i7)
[Strategy 2: Private Tree Planting](?tab=t.6wfo8thmiq#heading=h.9tou60vq75ma)
[Strategy 3: Agency Vegetated Buffers](?tab=t.6wfo8thmiq#heading=h.icfg3e5345g)
[Strategy 11: Complete Streets in Industrial Community](?tab=t.6wfo8thmiq#heading=h.v5hf38fel5mh)
[Traffic Analysis and Technical Assistance](?tab=t.6wfo8thmiq#heading=h.h2fvnlu05jxj)
[Strategy 12: Showcase Greening Projects](?tab=t.6wfo8thmiq#heading=h.8mmhxqemsk5u)
[Strategy 13 – Community Air Quality Monitoring, Training, and Education](?tab=t.6wfo8thmiq#heading=h.rvc9xowd7u3z)
[Sensor Deployment Plan](?tab=t.6wfo8thmiq#heading=h.b81zzrkg3y1p)
[Scope Table](?tab=t.6wfo8thmiq#heading=h.g0yxog2w35j4)
[MAPS](?tab=t.6wfo8thmiq#heading=h.ggw7fm9ueein)
[Green\_Spine\_Design\_Coordination\_Hyphae\_Scope\_and\_Schedule](?tab=t.6wfo8thmiq#heading=h.l6hjuufb1ium)
[Introduction](?tab=t.6wfo8thmiq#heading=h.86xkahbnjw3p)
[Background](?tab=t.6wfo8thmiq#heading=h.jizxk7lt1h03)
[Phasing](?tab=t.6wfo8thmiq#heading=h.n8t1xntmjebu)
[Design coordination](?tab=t.6wfo8thmiq#heading=h.9vsfvi8lpzn)
[Baseline Model](?tab=t.6wfo8thmiq#heading=h.did2ki7drpub)
[Benchmarking goals and studies](?tab=t.6wfo8thmiq#heading=h.ssr7tq8jkmsc)
[Design evaluation](?tab=t.6wfo8thmiq#heading=h.r8vc0dvie15o)
[Design optimization](?tab=t.6wfo8thmiq#heading=h.xwgup8fqq7kc)
[Impact Estimation of Final 30% Design Development Plans](?tab=t.6wfo8thmiq#heading=h.v9166r8oa78k)
[Research](?tab=t.6wfo8thmiq#heading=h.nwpkt9cbzody)
[Future Phases Post 30% Engagement \[NOT IN PRESENT BUDGET\]](?tab=t.6wfo8thmiq#heading=h.3r526ynfkupv)
[Harry Hines Evidence-based design methodology report](?tab=t.6wfo8thmiq#heading=h.n6xwpvigvs1v)
[Executive summary](?tab=t.6wfo8thmiq#heading=h.byp9xjyj7cbz)
[Introduction](?tab=t.6wfo8thmiq#heading=h.b8paf1h4lx6q)
[Design Process, Collaboration and Iteration](?tab=t.6wfo8thmiq#heading=h.wh6xosjia022)
[Monitoring and pre-post study](?tab=t.6wfo8thmiq#heading=h.5wy4kx294c7z)
[Brief Literature review](?tab=t.6wfo8thmiq#heading=h.ubcvlykvucdg)
[Strategies for air pollution](?tab=t.6wfo8thmiq#heading=h.twijpx2uudnp)
[Urban Vegetation for Air Quality Improvement:](?tab=t.6wfo8thmiq#heading=h.aqodxp1qv647)
[Vegetated Air Barriers for Roadside Pollution Mitigation:](?tab=t.6wfo8thmiq#heading=h.iv03k47wnq3m)
[Urban Trees for Ambient Pollution Mitigation:](?tab=t.6wfo8thmiq#heading=h.4h0rljpyksd4)
[Strategies for Heat Mitigation](?tab=t.6wfo8thmiq#heading=h.dwh9bfj65q1n)
[Strategies for Biodiversity](?tab=t.6wfo8thmiq#heading=h.dj4lvp7tefig)
[Monitoring](?tab=t.6wfo8thmiq#heading=h.m0ehr7lbo5kh)
[Sensor Hardware](?tab=t.6wfo8thmiq#heading=h.mlhdtlwxiyrg)
[Sensor Placement](?tab=t.6wfo8thmiq#heading=h.izop2ubrhdl9)
[Pre/Post & Cross-Sectional Study Methodology](?tab=t.6wfo8thmiq#heading=h.9mdql2yc0kvr)
[The cross-sectional hypotheses are:](?tab=t.6wfo8thmiq#heading=h.rsbqfcofo94h)
[The longitudinal hypotheses are:](?tab=t.6wfo8thmiq#heading=h.68aol84rjxgj)
[Quantitative methods](?tab=t.6wfo8thmiq#heading=h.smjma9gghglr)
[Qualitative studies](?tab=t.6wfo8thmiq#heading=h.id3y5o1dy04d)
[IRB approval](?tab=t.6wfo8thmiq#heading=h.ptjr151ks8t1)
## Dallas SWMD
[Green\_Spine\_Design\_Coordination\_Hyphae\_Scope\_and\_Schedule](https://docs.google.com/document/d/1rjLWnWYy-2Vy80-5FDGFUZKCM8VPwrh1TV7bNl2qDh0/edit?tab=t.0)
[Harry Hines Evidence-based design methodology report](https://docs.google.com/document/d/1pjgqG3wJG3j3V4w3kpBcz6cwrEsE_ZMVqWDp1iUnlqE/edit?tab=t.0#heading=h.mtix9t3ba8qx)
[Green Spine Process Documentation - Narrative \[HYPHAE DRAFT NOT FOR EXTERNAL USE\]](https://docs.google.com/document/d/1x1UlYQFFUlDFcNDKl0621Ehbg0VDbDBIC5BVpHYIBBw/edit?usp=sharing)
[Harry Hines Green Spine\_ Proposal Content - April 10, 10\_30 AM.odt](https://drive.google.com/file/d/1T6kgLxbsHEPl-EO1IPQKplimYJIUf5WQ/view?usp=drive_link)
[GreenSpine\_Hyphae\_SOW (original)](https://docs.google.com/spreadsheets/d/1_gIdZ8xAEEEt6lm06r-BwDA8M4tIIpClU4MYEU9U1pY/edit?gid=1400601326#gid=1400601326)
[TTF-twopager](https://docs.google.com/presentation/d/1MUNEgl5dk9v__lxOnTtEltrec23eUCCR7q8raJcYtAs/edit#slide=id.p)
## Boyle Heights
[ARLA Boyle Heights Grant ](https://docs.google.com/document/d/1qx5nj4zSlkB-cO-O5dz7l-cqJ_mjvK0lNbJkw0U1oUM/edit?usp=sharing)
[Boyle Heights Buffer Zone Project Partners](https://docs.google.com/document/d/1AC5sJD7Ty-PEHuHC4Pt2lG5d4KPLhU26dTUp6Ru1Csk/edit?usp=sharing)
[Boyle Heights: Community Driven Design](https://docs.google.com/document/d/1zX5AwttrYVUAdi-yFISdtmoLIoDEfImQthoGThLeaG4/edit?usp=sharing)
[BH-EPA-Grant](https://docs.google.com/document/d/1YdZRG7tx2Ji1_7NrmzRRTM940g562PqRTS2o7Ons-NI/edit?usp=sharing)
[ARLA Scopes](https://docs.google.com/spreadsheets/d/14FAQaenwJs8IawEizjBFCP5CgCpr60900-pIux6NlOc/edit?gid=1049340145#gid=1049340145)
EHCRP
[Submission\_ California Environmental Justice Coalition - California Microclimate Observatory (CAMO).pdf](https://drive.google.com/file/d/1EzPgvL42UyIKPoB4LgeIop2-Ead6d-Ol/view?usp=drive_link)
## Ambrose Park[Submission\_ California Environmental Justice Coalition - California Microclimate Observatory (CAMO).pdf](https://drive.google.com/file/d/1EzPgvL42UyIKPoB4LgeIop2-Ead6d-Ol/view?usp=drive_link)
[EPA San Francisco Bay Water Quality Improvement Fund narrative.pdf](https://drive.google.com/file/d/1PlloR5pF3vZUqKyI5KES8qVB4zSxrxQ6/view?usp=drive_link)
[EPA San Francisco Bay Water Quality Improvement Fund narrative](https://docs.google.com/document/d/1MvX4zkb6MPA_mX3xVcMty-VPFUEeWorHdGel7j97nSM/edit?usp=sharing)
[LoS final compiled.pdf](https://drive.google.com/file/d/13aGPI7AnGuOwjAhX0T4dSBHVsJTgNNO4/view?usp=drive_link)
[Ambrose Recreation and Parks District](https://docs.google.com/presentation/d/1AyJvKcK4vHczYVkhjdUDkxMIabf8BylwZd-G-IUgKHY/edit#slide=id.g1247a97f598_4_36)
[Ambrose Center Park Green Infrastructure Enhancements\_Additional Funding](https://docs.google.com/document/d/1_vvsviJbFmPg8-He3cFtWJ7Zu-M7u_vAAT3o9d1oUNw/edit?tab=t.0)
Project Map: <https://drive.google.com/drive/u/0/search?q=Ambrose>
Language on bike and trail access: <https://drive.google.com/drive/u/0/search?q=Ambrose>
[CCRCD\_Attachment2\_Workplan\_01262023.docx](https://docs.google.com/document/d/1Qwgo6IAQxALXml9yzidlM6WwUmQLl_QY/edit)
EPA San Francisco Bay Water Quality Improvement Fund Narrative: <https://drive.google.com/drive/u/0/search?q=Ambrose>
## ONLY PUT TEXT HERE THAT IS DRAFTED FOR SUBMISSION
# Overview
## **Scope of work description**
Hyphae will support TAMU staff in structuring and implementing the community engagement tasks, as well as on capacity building and training tasks as technical assistants. Hyphae will contribute experience in community engagement as well as documentation of outcomes. Hyphae staff will also install and train TAMU students and community members in installation, maintenance, and data collection for sensors.
Hyphae specialists will extend an existing digital twin model to include the Arlington Park area in order to conduct thermal comfort computational modeling to establish existing conditions in typical seasonal conditions. Results of this analysis will be shared in report form along with data insights showing results of microclimate and occupancy fixed sensor arrays.
Hyphae designers will assist in co-design process with community members through a series of charrettes culminating in conceptual drawings of proposed designs. They will generate plans, sections, and perspectives as appropriate to communicate the primary outcomes of the design sessions. A master plan level illustrative drawing will be made public to show the connectivity and place-based interventions proposed for both limited tactical interventions and longer term civic scale upgrades for neighborhood resilience.
## **Budget**
[HYPHAE: EPA-COMMUNITY CHANGE](https://docs.google.com/spreadsheets/d/1YhAGhA52q9-MGuODry2l8-ORuH9rfx4UaE5oIVTJUYc/edit?gid=1934813080#gid=1934813080) table location
\[image\]
## **Budget Justification**
Hyphaes Budget is broken into two categories Evidence Based Design and Sensor Deployment. Evidence Based Design is for consulting, design, engineering and management services, while Sensor Deployment is primarily fixed costs to purchase equipment, or operational costs to install the fixed sensors and operate mobile sensors such as LIDAR for periodic data collection campaigns. The sensor deployment scope also includes IT and software developer time to manage and maintain and debug data collection pipelines and databases of data storage during the project lifecycle
### Evidence Base Design 
**Project Importance **
This budget is critical to the overall management of the project. It is a key piece that connects the data collection, research, design, and community process. Hyphae Design Laboratory has unique experience working at the interface of community lead design process, with rigorous scientific analysis and design. They have experience with filling this unique role in other projects, in Dallas, Louisville Kentucky, Boyle Heights community of Los Angeles, CA, Richmond CA, Stockton, CA, and Oakland, CA, working in partnership with Community Partners, Academics, and Agencies.
**Roles & Responsibilities**
  - Brent Bucknum - Principal
  - Ivan Heitmann- Project Manager, Landscape Designer, GIS Specialist
  - Merissa MacDonald- Certified Arborist, Community Forest Expert
**Timeline**
The first year will include baseline data collection from GIS sources as well as sensor deployment. The first year will also include development of a community coalition and initial community meeting development. The second year will focus on developing community strategies and fast tracking short term projects like tree planting and pavement repairs and prioritization of longer term projects that require further detailed design and coordination with permitting officials. The final year will include 
**Evidence Based Design Oversight **
This budget includes time to manage the Evidence Based Design Process and to complete the technical roles and responsibilities of the community participatory design and engineering work.
Evidence based, Community participatory design process requires a principal, project manager, and Arborist, Community Forestry expert to travel to the neighborhood on multiple occasions as well as manage the project in collaboration with TAMU and TTF throughout the life of the project.
*Task Items:*
  - Project Management: 4 hours per week for 4 years
  - 6 meetings during the first 2 years
  - Principal Oversight: 1 hour meeting twice per month 
**Community-Based Design**
Active Transportation Connectivity Plan includes geospatial mapping of walking, biking and alternative transportation routes through the community as well as surveying community members and doing community mapping. Community Greening Strategies includes developing greening plans for shade, stormwater management along pedestrian and bike corridors including plant selection and plan development. It also includes tree planting for residential properties identified by the community and for planting plans on 3-4 community parcels as defined by the community, for example, schools, parks, community centers. Stormwater & Flooding Strategies include analysis of current and future flooding scenarios, and conceptual development of flood mitigation and habitat enhancement and nature based solutions in partnership with the community to present to community stakeholders and officials from ACOE and Dallas.
*Task Items:*
  - Community listening sessions and surveys
  - Community capacity building
      - Training+certification as community health workers
  - Community model and data literacy learning sessions and materials
  - Pedestrian mobility study
      - Creek access
      - Missing links
      - Cool corridors
      - Refuge and egress
      - Access to area assets like the new Green Park
  - Community co-design process
  - Master plan (connectivity, green infrastructure, greening prioritization)
  - Tactical interventions (including construction budgets)
      - Tree planting
      - New trail segments
      - Temporary pedestrian+bike mobility measures
  - Municipal infrastructure proposals
      - Sidewalk plan
      - Typical creekside section
      - Tree planting for shade and aq mitigation
**Measurement & Modelling Data Analysis**
This section includes to to process data coming from both Geospatial analysis as well as data collected from the network of sensors throughout the corridor and neighborhood. This includes work to analyze the findings and develop design insights from geospatial data collected by our team, TAMU’s team as well as the sensor data. It also includes time to write reports of insights.. Costs to deploy fixed sensors and operate mobile sensors and manage the data are included in the separate sensor deployment budget.
This scope also includes developing a digital twin for the project to develop models for prioritizing locations and optimizing designs for various heat island mitigation interventions, such as tree planting, vine planting, cool surface treatments and pedestrian route planning.  With support from NSF SBIR Grant \#2218499, Hyphae Design Laboratory, a mission-driven social enterprise, has developed software pipelines to build 3D digital twins, computational fluid dynamics models, and sub-meter microclimate simulations using open source data inputs like aerial lidar data, using openfoam CFD and UMEP and other simulation tools.
*Task Items:*
  - Climate and traffic risks geospatial analysis and social mapping
      - Community implemented traffic counting campaigns
  - Thermal comfort modeling (GIS based)
  - Integration of sensor data
  - Baseline report of above
  - Impact evaluation
      - Quantitative changes to thermal comfort
      - Projected changes to air quality
      - Physical activity data, health outcomes data, stress and mental health outcomes data
      - health equity and environmental justice indicators (longitudinal)
      - Conduct pre- and post-intervention assessments to evaluate changes in mobility, heat exposure, and flood resilience.
### Sensor Deployment
**Roles & Responsibilities**
  - Daniel Fleischer (Chief Scientist)
  - Ivan Velev (Software & Hardware Programmer)
  - Jaqueline Kelly (Software Programmer)
**Project Importance **
The sensor network is central to the Evidence Based Design methodology, allowing for before and after evaluation of the effectiveness of the Greening and Active transportation improvements  and therefore a critical piece to the success of this project's mission.
**Cost Basis**
Sensor Deployment costs are based on real costs to deploy the first round of sensors in the corridor. This budget includes the expansion of the existing microclimate sensor network to include the entire corridor, beyond the initial pilot zone, as well as into the Arlington Park Neighborhood. This will allow the expansion of microclimate sensors, as well as the addition of occupancy sensors and air quality sensors. Hyphaes Team, with support from TAMU students will deploy stationary sensors and ground-based mobile monitoring runs based on initial monitoring runs and community feedback. Sensors will be attached to infrastructure at the appointed locations and configured to send data to the cloud databases.
*Task Items:*
  - Microclimate sensor deployment
  - Environmental indicator sensing and analysis (meteorology,, aq)
  - Occupancy sensing (ped counters, bike counters)
**Timeline**
Sensors will be deployed at the beginning of the project, to gather existing conditions data and last throughout the life of the project. Sensors will be strategically placed to attempt to keep the same locations throughout the construction of the interventions but some sensors will have to be moved and reinstalled if construction activity overlaps. Additional Funding is being sought to maintain sensors for an additional 5-10 years after the project completion to continue to study the change in the environment.
**Equipment & Direct Costs**
*Data Telemetry  & Storage*
LORAWAN, Long Range Wireless Receiver Hubs have been installed in the corridor and can communicate with individual LORAWAN Nodes. Data is collected on a time series database and maintained with two mirrored backups on different cloud servers. The cost of physical sensors as well as the cloud server hosting and management costs are included. The LORAWAN hub connects over the internet to a cloud service running a LORAWAN network server which routes sensor messages via ‘MQ’ Telemetry Transport (MQTT) protocol to our cloud MQTT clients, which decode the LORAWAN packets and store the sensor readings in several time-series databases. 
*Microclimate Sensors*
This budget includes For stations where power is not available, a 30w solar panel, charge controller are 10ah sealed AGM battery. It also includes Barani MeteoWind IOT anemometer with solar panel and battery and LoRaWAN radio. It includes Black Globe sensor developed for the project by Hyphae Design Laboratory. The budget includes two overall types of microclimate sensors predominantly; temperature sensors and wind sensors. The temperature sensors employ a LORAWAN radio-module and microcontroller based on the Dragino LSN50-V2 module, which provides a unified communications platform to which we can attach a variety of sensor types. The LSN50-V2 has a battery which can last up to 10 years if messages are configured to be transmitted only every 20 minutes, as we have done for our temperature sensors. To the LSN50-V2 module we attach 2 cables, one of which connects to a SEN0385 weatherproof SHT31 temperature and humidity sensor, which we immobilize underneath a white radiation shield. The second cable attaches to a waterproof DS18B20 which we affix inside a 6 inch diameter hollow copper sphere, which is painted matte black. The DS18B20-based “globe sensor” provides radiant temperature measurements, while the SHT31 provides air temperature and humidity measurements. Our wind sensors are Barani Meteowind IoT Pro units, which have a small solar panel, battery, LORAWAN radio, elliptical-cup anemometer and direction vane. The wind sensors send data every 10 minutes, including average wind speed, peak wind speed, average and peak wind direction, minimum and maximum wind speed,  and direction confidence interval. Images of a couple of the sensors are shown in figure 3 below.
\[image\]\[image\]
\[image\]\[image\]
*Figure 3. Examples of sensors placed along the Harry Hines Corridor for this project.*
*Occupancy Sensors*
These sensors include a purchase price, as well as a data management price form the supplier, currently being specified as EcoCounter.com. A final vendor will be selected, after awarding of the contract to meet the specifications and 
*Air Quality Sensors*
For fixed sensors we will be using QuantAQ MODULAIR-PM monitors designed for use by trained non-specialists. These sensors include four gas-phase measurements (CO, NO, NO2, and O3) in addition to PM1, PM2.5, and PM10 estimates as well as number concentrations for particles between 0.35 µm and 40 µm. It is also coupled with a Sonic Anemometer.  To install them, community air leaders will receive online training from hyphae and QuantAQ. These sensors have been successfully used on many similar initiatives throughout the United States and beyond, offering significant ease of use, quality, and price. They have been chosen for their relatively low cost, but higher quality than other low cost sensors like Purple Air, as well as the more advanced machine learning and data calibration capabilities. They have also been chosen for their increasing use in EPA and other funded projects. We believe in the value of utilizing similar methods and protocols across different projects in different regions, so that hopefully insights can be compared more broadly between them. His also increases the power of the insights
*Mobile Sensing*
The combined data set, along with aerial, satellite, and ground-based LiDAR scans, will be integrated to generate 3D models of the chosen area.  Troubleshooting in the field will be handled via collaboration between our participants in the field and our technology partners. Participants will be trained in how to handle common issues such as network disconnection, power loss, and spurious data readings, receiving automatically generated prompts from our chosen technology platform when they need to take action. 
# Narrative project description
  - Complete streets analysis
  - Master plan
  - Getting Arlington people to and from the park
  - Extend thermal sensor network into neighborhood
  - Occupancy: add pedestrian / biking sensors, data analysis goes to TAMU grad student?
  - Sidewalk improvements
  - Tree planting areas
  - Evidence-based design outreach process
  - Prioritized greening locations
  - Air, heat, pollution driven analysis
  - Pedestrian studies
  - Creek access improvements
  - Community engagement strategy
## **Project need**
### Safety and Resilience Challenges in Arlington Park
The sources describe several problems impacting the safety and resilience of residents in the Arlington Park neighborhood of Dallas, Texas:
  - **Lack of Pedestrian Infrastructure and Connectivity:** Arlington Park has inadequate pedestrian infrastructure, with sidewalks that are discontinuous and frequently absent entirely, making it unsafe to walk or bike within the neighborhood. Residents have expressed safety concerns and a desire for better connectivity, including safer crossings and access to existing parks and creeks. For example, there's no safe way to get from Arlington Park to the planned green park in the nearby medical district, even though it’s just a few blocks away. This lack of connectivity isolates residents and limits their access to essential services, recreational opportunities, and employment centers.  
  - **Flooding:** The neighborhood experiences significant flooding problems, which threaten residents' safety and property. Flooding events can disrupt daily life, damage homes, and lead to health risks. There is an urgent need to identify flood-prone areas and develop green infrastructure solutions to mitigate the impacts.  
  - **Industrial Corridor Impacts**: Arlington Park is located near industrial zones and faces challenges related to its proximity to these areas. Residents are likely exposed to higher levels of air and noise pollution from industrial activity and traffic, which can negatively impact their health and well-being. Additionally, the aesthetic appeal of the neighborhood may be diminished due to its proximity to industrial sites.  
  - **Heat Island Effect**: Like the Southwestern Medical District adjacent, this area experiences a significant heat island effect, with temperatures in built-up areas being considerably higher than surrounding areas. The lack of green spaces and tree cover in Arlington Park exacerbates this problem, creating a less comfortable and potentially dangerous environment for residents, particularly during hot summer months.  
  - **Limited Access to Green Space**: The limited green space within Arlington Park further reduces its resilience to climate change impacts like heat and flooding. Access to green spaces offers residents a respite from urban stressors, provides opportunities for recreation and social interaction, and contributes to overall well-being. The planned green park in the medical district offers potential benefits, but its accessibility is currently limited for Arlington Park residents due to the aforementioned connectivity issues.  
These interconnected problems underscore the need for interventions that address both the built environment and social factors contributing to resilience and safety in Arlington Park. The proposal suggests that solutions should prioritize community engagement, evidence-based design principles, and a holistic approach that considers the interplay of these various challenges.
### Maps for the Arlington Park neighborhood
##### Land use and POI visitation
### \[image\]
##### Property value (Dollars per square-feet)
\[image\]
### Socio-Demographics characteristics of Arlington Park neighborhood
|  |  |  |  |  |
| :- | :- | :- | :- | :- |
| **Socio-Demographic Characteristics** | **Arlington Park neighborhood** | **City of Dallas** |  |  |
| **Total Population** | 1,358 |  | 1,300,642 |   |
|   |  |  |  |   |
| **Race/Ethnicity** |  |  |  |   |
| Hispanic or Latino | 482 | 35.5% | 551,447 | 42.4% |
| Non-Hispanic White Alone | 424 | 31.2% | 368,673 | 28.3% |
| Non-Hispanic Black or African American Alone | 440 | 32.4% | 302,925 | 23.3% |
| Non-Hispanic Asian Alone | 0 | 0.0% | 46,801 | 3.6% |
| Non-Hispanic Other | 12 | 0.9% | 30,796 | 2.4% |
|   |  |  |  |   |
| **Age** |  |  |  |   |
| 17 Years or Younger | 554 | 40.8% | 317,057 | 24.4% |
| 18-64 Years old | 771 | 56.8% | 840,093 | 64.6% |
| 65 Years or Older | 33 | 2.4% | 111,826 | 8.6% |
|   |  |  |  |   |
| **Travel time to Work** |  |  |  |   |
| less than 10 minutes | 53 | 13.6% | 48,584 | 8.4% |
| 10 to 29 minutes | 112 | 28.6% | 295,967 | 51.4% |
| 30 to 44 minutes | 205 | 52.4% | 145,416 | 25.2% |
| 45 to 59 minutes | 5 | 1.3% | 44,223 | 7.7% |
| 60 or more minutes | 16 | 4.1% | 41,746 | 7.2% |
|   |  |  |  |   |
| **Means of Transportation to Work** |  |  |  |   |
| Drove Alone/Carpooled | 351 | 89.8% | 533,611 | 92.7% |
| Public Transportation | 0 | 0.0% | 17,857 | 3.1% |
| Other (Walk, Bicycle, Work at Home, etc) | 40 | 10.2% | 24,468 | 4.2% |
|   |  |  |  |   |
| **Household Type** |  |  |  |   |
| Married-couple family | 77 | 17.4% | 184,347 | 35.4% |
| with related children | 38 | 8.6% | 79,985 | 15.3% |
| Male householder, no spouse present | 31 | 7.0% | 27,584 | 5.3% |
| with related children | 0 | 0.0% | 11,428 | 2.2% |
| Female householder, no spouse present | 276 | 62.3% | 74,113 | 14.2% |
| with related children | 196 | 44.2% | 40,494 | 7.8% |
| Living alone | 51 | 11.5% | 191,742 | 36.8% |
| Nonfamily, but not living alone | 8 | 1.8% | 43,361 | 8.3% |
|   |  |  |  |   |
| **Household with 65+ years old** | 33 | 7.4% | 108,150 | 20.8% |
| **65+ years old living alone** | 20 | 4.5% | 44,276 | 8.5% |
|   |  |  |  |   |
| **Educational Attainment 25 Years +** |  |  |  |   |
| Less than High School | 190 | 23.6% | 169,347 | 19.8% |
| High School Graduate (includes equivalency) | 230 | 28.6% | 185,351 | 21.7% |
| Some college | 299 | 37.2% | 145,262 | 17.0% |
| Bachelor's degree | 43 | 5.3% | 233,465 | 27.4% |
| Master's Professional Doctorate degree | 42 | 5.2% | 119,985 | 14.1% |
|   |  |  |  |   |
| **Annual Household Income** |  |  |  |   |
| Less than $25,000 | 55 | 12.4% | 94,769 | 18.2% |
| $25,000 to $49,999 | 268 | 60.5% | 110,314 | 21.2% |
| $50,000 to $74,999 | 58 | 13.1% | 95,604 | 18.3% |
| $75,000 to $99,999 | 5 | 1.1% | 61,395 | 11.8% |
| $100,000 to $199,999 | 57 | 12.9% | 101,949 | 19.6% |
| $200,000 or more | 0 | 0.0% | 57,116 | 11.0% |
|   |  |  |  |   |
| Median Household Income | $45,313 |  | $63,985 |   |
| Percent of Houston's Median | 70.8% |  | \- |   |
|   |  |  |  |   |
| Households with self-employment income | 111 | 25.1% | 59,582 | 11.4% |
| Households with interest, dividends, or net rental income | 0 | 0.0% | 72,039 | 13.8% |
|   |  |  |  |   |
| Households with Social Security income | 58 | 13.1% | 104,123 | 20.0% |
| Households with Supplemental Security Income (SSI) | 75 | 16.9% | 19,335 | 3.7% |
| Households with public assistance income | 0 | 0.0% | 9,395 | 1.8% |
| Households with cash public assistance or Food Stamps/SNAP | 196 | 44.2% | 65,115 | 12.5% |
| Households with retirement income | 5 | 1.1% | 62,972 | 12.1% |
|   |  |  |  |   |
| Population whose Income Below Poverty | 192 | 14.1% | 225,553 | 17.5% |
|   |  |  |  |   |
| **Housing Units** |  |  |  |   |
| Occupied | 443 | 84.9% | 521,147 | 90.0% |
| Vacant Housing Units | 79 | 15.1% | 57,849 | 10.0% |
|   |  |  |  |   |
| **Tenure** |  |  |  |   |
| Owners | 75 | 16.9% | 218,575 | 41.9% |
| Renters | 368 | 83.1% | 302,572 | 58.1% |
|   |  |  |  |   |
| **Persons per Household** |  |  |  | 5 |
| Owner occupied | 1.61 |  | 2.75 |   |
| Renter occupied | 3.36 |  | 2.26 |   |
|  |  |  |  |  |
| Housing costs as a percentages of household income  |  |  |  |  |
| Owned units |  |  |  |  |
| Over 30% | 0 | 0.0% | 53,018 | 24.3% |
| Over 50% | 0 | 0.0% | 24,158 | 45.6% |
| Rented units |  |  |  |  |
| Over 30% | 306 | 83.2% | 136,302 | 45.0% |
| Over 50% | 55 | 14.9% | 64,233 | 21.2% |
|   |   |   |   |   |
| 2018-2022 American Community Survey 5 years Estimates |  |  |  |  |

### Demographics charts
[Arlington Park Dallas, TX Overview: Weichert.com](https://www.weichert.com/search/community/neighborhood.aspx?hood=51906)
\[image\]
\[image\]
## **Community Co-Design Approach**
Our environmental justice approach aims to empower communities to advocate for themselves using data, science, and evidence. For over a decade, Hyphae Design Laboratory has supported grassroots organizations by providing technical assistance, environmental monitoring, and design solutions that empower impacted communities. By collaborating with activists, researchers, government agencies, and local stakeholders, Hyphae has helped these groups achieve significant policy advancements in pollution reduction, climate resilience, and green infrastructure.
Using advanced tools for hyperlocal mapping and data collection, Hyphae identifies environmental threats such as air, soil, and water contamination, as well as health risks like extreme heat. The evidence gathered through this monitoring and modeling will drive hyperlocal design interventions, ensuring that solutions are precisely tailored to the needs of the community. The Arlington Park Neighborhood Association will utilize Hyphae’s adaptOS platform to design and simulate environmental interventions—such as urban greening, rerouting heavy vehicle traffic, or building digital tools to protect vulnerable populations. Insights from the community will form a crucial part of the evidence base, integrating local knowledge and lived experiences into the scientific analysis to ensure solutions are both effective and community-driven. This approach puts scientific tools and data directly in the hands of the community, shifting the balance of power from regulatory agencies to the people most affected by pollution.
However, challenges persist, particularly in modeling and simulating urban air quality. Tools like Computational Fluid Dynamics (CFD) are still underdeveloped for community-level use, making it challenging for grassroots groups like the Arlington Park Neighborhood Association to provide definitive data to influence policy effectively. Estimating dynamic air quality conditions in complex urban environments remains a methodological gap. Addressing this gap is crucial for making informed decisions about where and how to intervene. Hyphae's approach demonstrates that, with the right tools, communities can hold decision-makers accountable and compel industries and agencies to implement necessary changes.
This proposal seeks to enhance air quality modeling capabilities, enabling the Arlington Park Neighborhood Association to better predict the outcomes of their advocacy and environmental actions. Strengthening these modeling tools could set a national precedent by expanding this participatory environmental justice framework. With improved tools, the Arlington Park Neighborhood Association and other local groups will be better positioned to evaluate the costs and benefits of interventions, thereby accelerating their efforts to secure environmental improvements.
Hyphae's success is rooted in strategic partnerships—connecting community groups like the Arlington Park Neighborhood Association with local governments, academic experts, and other stakeholders. Their track record includes collaborations with various environmental justice organizations committed to reducing pollution exposure in vulnerable areas. Coalition-building is a fundamental aspect of this strategy: it creates a comprehensive ecosystem where grassroots data collection directly informs government policy and regulatory action.
The proposed strategy involves using successful pressure campaigns as templates for new regions. By building coalitions that unite community members, environmental scientists, and local governments, Hyphae has demonstrated how to push for stricter emissions standards, more effective air quality monitoring, and increased investment in green infrastructure. Empowering communities like the Arlington Park Neighborhood Association to collect their own data and advocate for change—backed by advanced modeling capabilities—can facilitate significant environmental justice achievements nationwide.
## **Evidence-Based Design Approach**
Hyphae Design Laboratory's evidence-based design (EBD) approach is a comprehensive process that integrates scientific analysis, community engagement, and innovative design solutions to address environmental challenges and enhance community well-being. The approach emphasizes:
  - **Understanding the Problem**: Hyphae begins by conducting thorough research and analysis to understand the specific environmental health challenges facing a community. This often involves:
      - Reviewing existing literature and data on relevant topics like heat stress, air pollution, and biodiversity.
      - Collecting data on environmental indicators, such as temperature, humidity, and air quality, using sensors and other monitoring tools.
      - Developing spatial models and simulations to understand the dynamics of environmental factors and their impact on human health.
  - **Engaging the Community**: Hyphae believes that effective design solutions must be grounded in community needs and priorities. They actively engage residents through:  
    Community meetings and workshops to gather input, present findings, and co-design solutions.
      - Developing accessible and engaging communication materials, including visualizations, to help community members understand complex data and participate in decision-making.
  - **Developing Innovative Solutions**: Hyphae employs a creative and iterative design process to develop solutions that address the identified environmental challenges while considering community preferences and site constraints. This includes:
      - Exploring a wide range of greening interventions, from traditional approaches like tree planting to more novel solutions like green walls, car canopy trellises, and bioswales.
      - Utilizing advanced modeling and simulation tools to evaluate the effectiveness of different design scenarios in mitigating heat stress, improving air quality, and enhancing biodiversity.
      - Developing detailed design plans and specifications, incorporating feedback from community members and technical experts.
  - **Measuring Impact**: Hyphae prioritizes data collection and analysis to evaluate the effectiveness of their interventions and document their impact on environmental health and community well-being. This includes:
      - Implementing pre- and post-intervention monitoring to track changes in environmental indicators and human health outcomes.
      - Analyzing data to assess the performance of different interventions and identify areas for improvement.
      - Disseminating findings through reports, presentations, and publications to share lessons learned and promote broader adoption of evidence-based design practices.
### Key Elements of Hyphae's EBD Approach
  - **Adaptive Management**: Hyphae recognizes that environmental conditions and community needs are constantly evolving. Their approach is iterative and flexible, allowing for adjustments based on new data, feedback, and changing circumstances.
  - **Collaboration**: Hyphae works closely with a diverse range of stakeholders, including community members, researchers, designers, engineers, and government agencies, to ensure that projects are informed by multiple perspectives and expertise.
  - **Transparency**: Hyphae believes in open and transparent communication throughout the design process. They make data and findings accessible to community members and involve them in decision-making.
  - **Replicability and Scalability**: Hyphae aims to develop solutions that can be replicated and adapted in other communities facing similar challenges. They document best practices and develop resources to facilitate knowledge transfer.
### Benefits of Hyphae's EBD Approach
  - **Improved Environmental Health Outcomes**: By grounding design decisions in scientific evidence and community priorities, Hyphae's approach leads to interventions that effectively address environmental health challenges and improve the well-being of residents.
  - **Increased Community Engagement and Ownership**: Hyphae's participatory design process empowers community members to contribute their knowledge and perspectives, fostering a sense of ownership and increasing the likelihood that projects will be supported and maintained in the long term.
  - **Enhanced Sustainability**: By focusing on data collection, analysis, and adaptive management, Hyphae ensures that projects are designed for long-term effectiveness and can be adjusted to changing conditions.
  - **Greater Cost-Effectiveness**: Hyphae's use of modeling and simulation tools allows them to test different design scenarios and optimize interventions before implementation, reducing the risk of costly mistakes and maximizing the impact of limited resources.
### Examples of Hyphae's EBD Approach in Action
  - **Harry Hines Green Spine Project**: This project exemplifies Hyphae's comprehensive approach, integrating extensive data collection, modeling, community engagement, and iterative design refinement to create a health-promoting and ecologically beneficial corridor. The project also serves as a "living laboratory" for testing and refining EBD principles.
  - **Boyle Heights EPA Grant Project**: This project demonstrated the effectiveness of Hyphae's community-driven design process, resulting in tangible improvements to sidewalks, tree canopy, and pedestrian safety in a disadvantaged neighborhood.
  - **Prescott Neighborhood Greening Project in West Oakland**: This showcase project exemplifies Hyphae's ability to work collaboratively with community organizations, government agencies, and research institutions to address complex environmental justice issues. The project combined innovative design solutions like vegetated buffers and road dieting with rigorous data collection and analysis to demonstrate the effectiveness of the interventions.
Hyphae's evidence-based design approach is a powerful tool for creating healthier, more resilient, and more equitable communities. By prioritizing scientific rigor, community engagement, and innovative design solutions, Hyphae is helping to transform urban environments and improve the lives of residents in communities disproportionately impacted by environmental challenges.
### Measurement of environmental indicators
The monitoring approach encompasses a multi-phased strategy that uses a variety of sensors and data collection methods to track environmental conditions before, during, and after interventions.
#### **Phase 1 Monitoring**
Phase 1 monitoring focused on a pilot deployment of a central monitoring hub and 30 sensor nodes placed in a specific area. The sensor locations were strategically chosen based on previous data and to capture variations in conditions. The data collected in this phase would help validate models and guide decisions for the next phase.
#### **Phase 2 Monitoring**
Phase 2 expands on the initial monitoring efforts by incorporating additional sensors and data collection methods:
  - **Expanded Thermal Comfort Sensor Network**: Phase 2 increases the number of thermal comfort sensors to gather more data on the impact of landscape features on variables like temperature, humidity, wind, and radiant heat.
  - **Air Pollution Monitoring Campaign**: Recognizing the need to monitor air pollution, Phase 2 includes a mobile air monitoring cart that measures pollutants like PM1, PM2.5, PM10, ultrafine particulates, black carbon, NO, NO2, as well as temperature, sound, and video. Passive samplers are also deployed to collect data on NO, NO2, O3, and VOCs.
  - **Biodiversity Monitoring**: Acoustic sensors are incorporated to detect and identify birdsong, bat calls, and other sounds related to biodiversity. These sensors are placed in locations that represent habitat corridors and potential disruptors.
  - **Pedestrian Usage Monitoring**: Pedestrian counting sensors are placed at key locations to monitor pedestrian activity and assess the impact of interventions on pedestrian usage patterns.
#### **Phase 3 Monitoring**
Phase 3 involves continued monitoring and evaluation after the intervention. This phase aims to track long-term changes and the effectiveness of the interventions.
#### **Data Collection Methods**
The monitoring approach employs several methods to gather data:
  - **In-Situ Monitoring**: Sensors are placed in the environment to passively collect data on various parameters.
  - **Mobile Monitoring**: A mobile cart equipped with sensors is used to collect data along specific routes or areas.
  - **Pre- and Post-Intervention Monitoring**: Data is collected before and after interventions to assess their impact.
  - **Cross-Sectional Studies**: Monitoring data is used to compare different locations or conditions and understand the influence of specific factors.
  - **Longitudinal Studies**: Monitoring data is collected over time to assess changes and trends.
#### **Data Analysis and Modeling**
The data collected through the monitoring process is used to:
  - **Validate Simulation Models**: Real-world data helps calibrate and verify the accuracy of the models used to predict the impacts of interventions.
  - **Identify Pollution Hotspots**: Monitoring data can pinpoint areas with high pollution levels.
  - **Assess Intervention Effectiveness**: Comparing pre- and post-intervention data allows for evaluation of the effectiveness of implemented solutions.
  - **Inform Future Design Decisions**: Monitoring results can inform the design of future interventions and improve their effectiveness.
The monitoring approach is integral to the evidence-based design process. By continuously collecting data and analyzing the results, the project aims to create interventions that are data-driven and effectively address the environmental health challenges in the Arlington Park neighborhood.
\[image\]
### Modeling
The project aims to use evidence-based design to inform the development of interventions that benefit the environmental health of the community. Modeling plays a crucial role in this process, serving as a bridge between data collection and the design of effective interventions. The modeling process leverages data collected from various sources to simulate the impact of different design choices on the environment, allowing for a more informed and strategic approach to community improvement.
#### Data Collection: The Foundation of the Model
The accuracy and effectiveness of the modeling process rely heavily on the quality and scope of the data collected. The project employs a diverse range of tools and techniques to gather comprehensive information about the existing environmental conditions in Arlington Park. These include:
  - **LiDAR**: This technology creates highly detailed 3D maps of the area, capturing the shape and elevation of the terrain, buildings, and vegetation.
  - **Google Street View 360 cameras**: These provide a street-level view of the neighborhood, documenting the existing infrastructure and urban design elements.
  - **Aerial thermal imagery**: This data helps in understanding the distribution of heat across the area, identifying hotspots and areas susceptible to the urban heat island effect.
  - **Fixed and mobile air quality monitors**: These measure the concentration of various pollutants in the air, providing insights into the sources and patterns of air pollution.
  - **Microclimate sensors**: These record localized weather conditions such as temperature, humidity, wind speed, and direction.
This data is then used to create a "digital twin" of the physical environment, a virtual representation that serves as the basis for the simulation models.
#### Modeling: Simulating Interventions and Predicting Impacts
The modeling stage involves using specialized software and computational techniques to simulate how different design interventions would impact the environment. This involves:
##### 1\. Developing a Range of Models
Different types of models are used to capture various aspects of the environment and provide a comprehensive understanding of the potential impacts of the interventions:
  - **Mesoscale models**: These models cover a larger geographical area and simulate regional weather patterns and air pollution dispersion. They provide context and background information for the more localized microscale models.
  - **Microscale models**: These focus on a smaller area, like the Arlington Park neighborhood, and provide a more detailed analysis of specific interventions. They can simulate the impact of tree planting, cool pavement installation, and traffic flow modifications on factors such as air quality, heat distribution, and pedestrian comfort.
  - **Computational Fluid Dynamics (CFD) models**: These simulate airflow patterns around buildings and vegetation, helping to understand how these elements affect pollutant dispersion and heat transfer.
##### 2\. Calibrating and Validating the Models
Before being used to test scenarios, the models need to be calibrated and validated using the collected data. This involves adjusting the model parameters and inputs to ensure that they accurately represent the existing conditions in Arlington Park. The ongoing monitoring data is crucial for this validation process, providing real-world feedback on the model's performance.
##### 3\. Testing Different Scenarios
Once calibrated and validated, the models are used to test various design scenarios and evaluate their potential impacts. This allows the design team to compare different approaches and identify the most effective solutions for achieving the project goals.
  - **Impact of tree planting**: The models can simulate the effect of planting different types and sizes of trees in various locations on factors like shade provision, air pollution removal, and wind patterns.
  - **Effectiveness of cool surfaces**: The models can evaluate how cool pavement and roofs would mitigate the urban heat island effect and improve thermal comfort.
  - **Optimization of pedestrian corridors**: The models can help in designing pedestrian-friendly streets that provide shade, reduce exposure to traffic pollution, and create a safe and comfortable walking experience.
#### Outcomes
This modeling approach provides several benefits for the Arlington Park project:
##### 1\. Evidence-Based Decision-Making
The models provide a scientific basis for design decisions, going beyond intuition and assumptions. This helps in selecting interventions that are most likely to be effective in addressing the community's environmental health challenges.
##### 2\. Optimization of Interventions
The models allow for fine-tuning the design of interventions to maximize their positive impacts and minimize any potential negative consequences. For instance, they can help determine the optimal placement, size, and density of trees to balance air quality improvement with shade provision and wind flow considerations.
##### 3\. Cost-Effectiveness
By testing various scenarios virtually, the modeling process can help identify the most cost-effective solutions. This allows for allocating resources efficiently and achieving the greatest impact within the project budget.
##### 4\. Community Engagement
The modeling process can be used to communicate the potential impacts of the project to the community in a visually engaging and understandable way. This fosters transparency and encourages community involvement in the design process.
While the modeling approach provides valuable technical insights, it's crucial to integrate it with community engagement to ensure that the proposed interventions align with the community's vision and needs. The sources emphasize the importance of involving the Arlington Park community throughout the project, from the initial planning stages to the final design development. This can be achieved through:
  - **Community meetings and workshops**: Providing opportunities for residents to share their concerns, priorities, and ideas for improving the neighborhood's environmental health.
  - **Participatory mapping**: Using mapping tools and activities to allow residents to identify areas of concern, propose locations for interventions, and visualize the potential impacts of the project.
  - **Feedback mechanisms**: Establishing channels for ongoing communication and feedback, allowing residents to provide input on the evolving design and ensure that their voices are heard.
The combination of robust data collection, sophisticated modeling techniques, and meaningful community engagement forms the foundation for the evidence-based design approach used in the Arlington Park project. This holistic approach aims to create a healthier, more sustainable, and resilient community that reflects the aspirations of its residents.
## **Active Multimodal Connectivity Planning**
A key component to reduce GHG’s and increase community wellbeing and social cohesions is to have a community that has active transportation which include multimodal means of circulating through and between neighborhoods including walking, biking, and public transportation.
In meetings about Greenspine park and corridor improvements, the Arlington Park community members have communicated that it is unsafe to walk and bike within their own community and also to to get from their community to the planned medical district greening improvements, even though it is only a few blocks away. A preliminary connectivity study was conducted and is included here and as the basis of the proposal. These preliminary studies will be further developed in partnership with community ambassadors and surveys and meetings with the community to prioritize the most critical locations for initial interventions. These will then be coordinated agencies and designs developed with the relevant agencies, including parks and recreation, Public Works and other agencies.
Existing connectivity in this region of Dallas is really bad. Freeways and lack of historic pedestrian design provide a barrier along these corridors and to the medical district from neighboring communities. Much of Dallas and the Arlington Park community specifically has poor pedestrian infrastructure. Sidewalks start and stop midblock. Many critical corridors don't have sidewalks at all or large scale infrastructure like channelized flood protection streams freeways block access. Many corridors don't have adequate tree cover over sidewalks that do exist.
Record Crossing Road, and Inwood Drive flank the community of Arlington Park and are used by people getting to and from the Medical district and the freeway, through the community, but the safety of the residents and activation of these corridors for the people who actually live there is overlooked.
\[image\]
Arlington Park Census Block Group, Greenspine and Connectivity opportunity
\[image\]
Map showing Inwood and Record Crossing Cut through and red polygons show areas of pedestrian impasse do o freeway underpasses 
\[image\]
Existing Sidewalks and paths are fragmented
\[image\]
*Creeks and waterways could provide a means of ecological and human connectivity through the community and to harry hines blvd in addition to along it. *
\[image\]
Strategic new sidewalks and creek trails could provide safe access to existing greenspace and critical commercial areas like the medical district (purple: new or improved creek trails, green: new sidewalks)
Existing parks
\[image\]
[Connect | Sleepy Hollow Park Unveiling and Celebration Held in Dallas TFS](https://tfsweb.tamu.edu/content/article.aspx?id=33428)  
The Sleepy Hollow Park in Dallas’s Arlington Park Estates was revitalized through a greening initiative honoring the late Congresswoman Eddie Bernice Johnson. This project addressed environmental equity issues by planting trees, adding ADA-compliant amenities, and distributing trees to residents. A collaboration between the City of Dallas, Texas Trees Foundation, and Texas A\&M Forest Service, the initiative aimed to enhance community health, recreation, and green space access, leaving a lasting legacy in a historically underserved neighborhood.
<https://felt.com/map/Greenspine-saved-to-hyphae-rgaHEg4LQ1i9AVoZ0h8igEB?loc=32.81778,-96.852309,15.29z>
## **Showcase greening projects**
These limited shovel-ready interventions aim to demonstrate innovative and impactful greening solutions specifically tailored to the unique challenges of under-resourced neighborhoods like Arlington Park. The projects will focus on creating tangible improvements while also serving as a model for future greening efforts in similar communities. This approach aligns with the EPA's focus on community-driven solutions and creating replicable models.
### Key Strategies Inspired by the Boyle Heights Project
This project draws inspiration from the successful strategies employed in the Boyle Heights project:
  - **Complete Streets Analysis**: Conduct a thorough analysis of the existing street infrastructure in Arlington Park, focusing on pedestrian safety, accessibility, and connectivity. Identify areas for improvement, such as adding sidewalks, crosswalks, and traffic calming measures. The Boyle Heights project demonstrates the value of such analysis.
  - **Sidewalk Improvements**: Prioritize the development and implementation of sidewalk improvements to enhance pedestrian safety and encourage walking. This aligns with the emphasis on pedestrian connectivity in the Boyle Heights project and the overall goal of safe access to green spaces and essential services.
  - **Tree Planting Areas**: Identify strategic locations for tree planting, focusing on areas with high heat exposure, limited shade, and potential for air quality improvement. The Boyle Heights project successfully integrated tree planting as a key component of its greening strategy.
  - **Prioritized Greening Locations**: Utilize data analysis and community input to identify and prioritize locations for greening interventions. Consider factors such as heat vulnerability, air pollution levels, pedestrian traffic, and community needs. The sources highlight the importance of data-driven prioritization in both the Boyle Heights and Arlington Park projects.
### Addressing Unique Challenges and Community Needs
The Showcase Greening Project will go beyond replicating the Boyle Heights strategies by incorporating novel elements specific to Arlington Park:
  - **Showcase Greening Projects**: This project will highlight innovative greening solutions tailored to the specific challenges of the community. For instance, where traditional street trees might not be feasible, explore options like hedgerows, car canopy trellises, living walls, and shrub trellises. This approach addresses the need for adaptable solutions in communities with limited space and resources.
  - **Community Participatory Design**: Integrate the Arlington Park community into every stage of the design process, from identifying priorities to selecting interventions. This participatory approach ensures that the project reflects community needs and values and fosters ownership and long-term sustainability.
  - **Creek Access Improvements**: Given the presence of creeks in Arlington Park, prioritize improvements that enhance access to and enjoyment of these natural assets. This could involve developing trails, creating seating areas, and improving the ecological health of the creek corridors.
### Measuring and Evaluating Impact
To demonstrate the effectiveness of the Showcase Greening Project, implement a robust monitoring and evaluation plan:
  - **Pre- and Post-Intervention Data Collection**: Collect data on key environmental indicators, such as air quality, temperature, and pedestrian activity, before and after the interventions are implemented.
  - **Community Surveys**: Conduct surveys to assess community perceptions of the project's impact on their health, well-being, and quality of life.
  - **Publicly Available Reports**: Compile the findings into publicly available reports and presentations to share the lessons learned and inspire other communities to adopt similar approaches.
### Integrating with the Green Spine Project
This project can be integrated with the ongoing Green Spine Project to create a more comprehensive approach to improving environmental health in the broader area. The Showcase Greening Project in Arlington Park can serve as a model for expanding greening efforts to adjacent neighborhoods and demonstrate the benefits of integrating community-scale interventions with larger-scale infrastructure projects.
# Extracted from meetings
Here are Chanam's suggestions distilled into tasks for the proposal, keeping in mind brevity as requested:
  - ~~**Community-Led Design:**~~~~ Design interventions for protected green connectors and shelters, prioritizing safety and comfort for pedestrians.~~
  - **Phased Implementation:**
      - Year 1: Focus on community engagement and baseline assessments
      - Year 2: Implement interventions by Texas Trees Foundation
      - Year 3: Conduct assessment
  - **Place-Based Benefits:** Emphasize research and assessment focused on place-based benefits, including play spaces, physical activity, and health outcomes, particularly related to stress.
  - **Spatial Analysis:** Leverage spatial analysis to inform community engagement, co-design, assessments, and equity considerations like green gentrification.
  - **Air Quality Considerations:** Integrate air quality considerations into planting design for both air purification and microclimate benefits.
Here are Brent’s suggestions from the meeting on 11/14/2024, distilled into tasks for the proposal:
  - **Pedestrian Connectivity to Park:** Prioritize safe pedestrian access from Arlington Park to the planned green park, focusing on sidewalk improvements and potentially a new path through the channel. This will require coordination with the City of Dallas.
  - **Pedestrian Improvements Within Arlington Park:** Develop a plan for pedestrian improvements within Arlington Park itself, including sidewalks and tree-lined corridors to mitigate heat. This may also require working with the City of Dallas.
  - **Address Flooding**: Use existing GIS data to identify flooding-prone areas within Arlington Park and develop green infrastructure-based solutions to mitigate flooding.
  - **Evidence-Based Design**: Employ evidence-based design principles and tools, incorporating occupancy and heat sensors, and drawing on existing materials from previous projects like the Boyle Heights and Harry Hines proposals. This should include community meetings to gather input and present ideas to the community.
  - **Leverage “Measure, Modify, Manage” Framework:** Consider adapting the “Measure, Modify, Manage” framework for the proposal, emphasizing data collection, intervention design, and ongoing management strategies.
  - **Clarify Budget Allocation**: Determine the appropriate budget allocation for Arlington Park versus the Green Spine corridor, ensuring funding for both community interventions and research activities.
  - **Consider Air Quality**: Carefully consider the inclusion of air quality improvements in the proposal, given potential contradictions with certain interventions and limitations in measuring the impact of greening on air quality.
  - **Define Roles and Responsibilities**: Clearly delineate roles and responsibilities between Hyphae and Texas A\&M, particularly regarding design, data analysis, and community engagement. Decide who will be responsible for leading design charrettes, conducting data analysis and modeling, and managing community engagement.
These tasks reflect Brent’s suggestions, taking into account feasibility within the project timeline and budget.
## Hyphae Materials
[adapt OS narrative](https://docs.google.com/document/d/1TOP8NqhALUf3fTVfasGWsmJr4qM-Z933kueTwj7LqRc/edit?usp=sharing)
[Hyphae Bios (TexasTrees)](https://docs.google.com/document/d/1hZvOug411dZEnyVyDicNWEyjvu5JzZveNaTuMAW-k9k/edit?usp=sharing)
[BB\_CV\_2024.docx](https://docs.google.com/document/d/1tuC8XWegZuMWGOy1aOQpP5L9awZN-I5F/edit)
[IH\_CV.docx](https://docs.google.com/document/d/1Rqdj160XWCLt4K3L08JO-HXs2W8V3tVz/edit)
[EO\_CV\_2024.docx](https://docs.google.com/document/d/1zcajLkGRsfXNv7r0V0uw4UpudtgqFZjZ/edit)
[DF\_CV\_2024.docx](https://docs.google.com/document/d/10bRDnVewMiIGNHI7LzhPKT-MCaA3UJ6F/edit)
JPG CV: [Copy of Copy of JuanPenalozaCV.pdf](https://drive.google.com/file/d/1VRznw4HytHUh8OaX-AehYsyTvnQzBrZQ/view?usp=drive_link)
[Mei\_2020\_Resume.pdf](https://drive.google.com/file/d/1Gg50cfbZyphXn67_9yD1-KjS7Tz1P-u-/view?usp=drive_link)
[resume 2024 MM.docx.pdf](https://drive.google.com/file/d/16lEBWIx_lfhms6W6EaF-7Vq43rt6ZADZ/view?usp=drive_link)
Good material on HYphae history of Community Engagement here: [EPA AQ final submission.pdf](https://drive.google.com/file/d/1GbfpxBOGlIb-Rtmprf0XFwu88n2Ia4AE/view?usp=drive_link)
[JH\_Hyphae\_resume.pdf](https://drive.google.com/file/d/1Vefvn047ckTsUdFLNsOdyptyiS5jskRg/view?usp=drive_link)
These Categories are addressed in each of the two budget subcategories
  - **Project roles and tasks**: Include the project roles of each employee, the tasks they will perform, and the percentage of effort required. 
  - **How the costs benefit the project**: Describe how the expense or service relates to and benefits the project. 
  - **Anticipated cost**: Include the estimated cost for each budget line item. 
  - **Time period**: The desi 
  - **Supplies and materials**: Describe the supplies and materials that make up the costs. 
  - **Equipment**: Provide a cost analysis of the equipment and explain the specific need for it. 
  - **Other direct costs**: Explain the need for each cost item in this category and describe how the expenses were estimated.
  - 
# AirSense grant
From EPA AQ w/ Andres
Community Engagement Plan
Introduction
AB 617, California’s landmark environmental justice bill of 2017, mandated the
implementation of community-led air quality monitoring and emissions reduction programs,
placing environmental data and scientific tools into the hands of community organizers that had
formerly been handled exclusively by experts. Long before AB 617, however, Hyphae Design
Laboratory, founded by Brent Bucknum in 2008, had been practicing this collaborative,
community-driven, evidence-based form of environmental justice advocacy. Hyphae has provided
technical assistance to dozens of local community-based organizations in collecting data,
implementing environmental design solutions, and advocating for their communities before state
regulatory agencies. For almost fifteen years, from West Oakland to Stockton, Los Angeles, and
the country at large, their partners have fought to address unfair pollution burdens faced by low-
income communities and communities of color. By coordinating activists, technical assistants,
academic researchers, air districts, city governments, and federal agencies, they have transformed
their environments and achieved significant policy changes in pollution reduction, green
infrastructure, and climate resilience.
Using hyperlocal mapping and measurement tools developed with funding from the National
Science Foundation and the National Institute of Health, Hyphae helps CBOs identify air, soil, and
water contamination in their communities, as well as other risks to human health such as extreme
heat. These groups then deploy Hyphae’s software-based adaptOS platform to simulate, design,
and implement environmental mitigation solutions in response. Such interventions range from
urban greening to truck-rerouting to the design of software applications protecting sensitive
receptors during extreme heat events. A persistent weakness hampers the optimal implementation
of their combined environmental justice vision, however: the lack of reliable modeling tools.
Although low-coast commercial air sensors can now be reliably calibrated by co-locating them
with reference monitors, estimating the state of a dynamic system from a series of noisy
measurements using techniques like Kalman filtering still lags. Furthermore, the integration of
Computational Fluid Dynamics (CFD) tools for reliable urban airflow modeling and simulation is
not yet fully developed, hindering the accurate prediction and analysis of air quality in urban
environments. University of South Florida (USF), in collaboration with its contracted partner
Hyphae, submits this proposal to the Environmental Protection Agency (EPA) to address these
critical methodological gaps. Hyphae’s methods, combining outreach with technical expertise,
have already secured for CBOs an empirical foundation from which to advocate for fair
regulations, standards, and codes. But without adequate urban air quality modeling and estimation
tools, communities and air districts cannot effectively assess the costs and benefits of given
interventions. That weakness slows down environmental remediation at all stages of the process,
and casts doubt on our collective capacity to resolve our present climate crisis. By redressing this
computational liability, the EPA stands to expand California’s participatory environmental justice
approach to a nation-wide scale, thus extending the State’s legacy of leading the nation in the
formation of ecological policy.
Our partnership structure in this proposed project unites Hyphae’s oldest partners, the West
Oakland Environmental Indicators Project (WOEIP) with newer collaborators in Little Manila
Rising (Stockton, California) and Climate Resolve (Boyle Heights, Los Angeles). All three
organizations actively monitor air quality with in-house sensor networks, united in their goal to
effect lasting policy changes through their local air districts and the California Air Resources Board
(CARB). But only WOEIP has so far successfully pressured local transportation authorities to
make environmental concessions. We thus recommend applying WOEIP’s successful strategy in
West Oakland to South Stockton and Boyle Heights. The EPA can rely on the Hyphae coalition’s
proven track record of addressing unfair pollution burdens to achieve regulatory goals. Should our
collaboration prove successful, it could serve as a case study for CBOs across the nation in this
new chapter of environmental justice.
Hyphae’s partnership with WOEIP has grown to include an ensemble of community actors
ranging from tree-planting organizations, youth education groups, neighborhood associations,
climate resilience activists, local churches, and schools. Together with regulatory agencies, air
districts, city governments, and CARB, this Hyphae-assisted coalition is now implementing a
multi-year, multi-million-dollar urban planning endeavor that combines vegetated buffers, road
dieting, and truck rerouting in the Prescott neighborhood of West Oakland. In addition to the
Prescott project, Hyphae and WOEIP are also collaborating on West Oakland’s Sustainable
Transportation Equity Project (STEP), another CARB initiative aimed at protecting residents from
pollution by reducing transportation emissions. After years of vigorous evidence-based advocacy
from environmental justice groups, the Oakland Department of Transportation (OakDOT) and the
Oakland Parks and Recreation Foundation (OPRF) finally ceded to community demands and
agreed to participate in the project’s urban planning.
Underlying both projects is a conception of West Oakland as a comprehensive ecosystem
linking community-based organizations with academic researchers, state and federal agencies, and
the private sector. Beyond CARB, the coalition’s most immediate regulatory partner is the Bay
Area Air Quality Management District (BAAQMD), the entity tasked with enforcing the Bay
Area’s portion of AB 617’s mandate. Having served on the region’s Technical Advisory Group
since 2017, Brent Bucknum has worked tirelessly to shape its policy agenda while curating its
research goals and slate of funding proposals.
Since 2017, in quarterly WOEIP-led meetings convened in the context of the Prescott grant,
Hyphae modeling expert Ivan Heitmann has been presenting Hyphae’s pollution measurement
analyses and remediation simulations to a combined audience of community organizations and air
district officials. High-ranking air district allies include Stephen Reid, Senior Advanced Projects
Advisor of the Assessment Inventory and Modeling Department, Song Bai, of the Assessment
Inventory and Modeling department, and David Holstius, Ph.D., Senior Advanced Project Advisor
in the Planning and Climate Protection department. Over time, these figures have been
progressively integrating Hyphae’s models with those of the air district. Meanwhile, the CBOs
directed the next phase of the pressure campaign to force the Department of Transportation and
CalTrans to take seriously the pollution risks posed to residents by the Port of Oakland and adjacent
freeways.
The West Oakland coalition was finally vindicated with the 2019 passing of the West Oakland
Community Air Action Plan (WOCAP) which compelled CalTrans, the Department of
Transportation, the Port of Oakland, and local refineries to make substantial regulatory
concessions. These included stricter emissions controls on trucks and other heavy-duty vehicles,
as well as a mandate to enhance air quality monitoring and invest in green infrastructure to mitigate
pollution impacts. Furthermore, the WOCAP obliged future transportation-related projects to
incorporate community feedback into their planning processes.
The Plan advanced a list of eighty-nine proposed pollution-mitigating strategies, ranging from
urban greening to truck re-routing, optimized building envelopes, and clean electrification. But
due to persistent skepticism among many scientists regarding the accuracy of modeling, the
steering committee still lacks an empirical basis by which to effectively simulate which of these
proposed solutions would have maximum impact and highest benefit-to-cost ratio. More effective
modeling could effectively demonstrate at a hyperlocal level exactly how tree canopy, vegetation,
traffic, and shade could be optimally configured to protect environmental health.
In this grant application, we propose to use WOEIP’s successful pressure campaign as a
template by which to compel transportation authorities elsewhere. Currently, Hyphae is serving
five other AB 617 communities, all of which encounter similar skepticism when presenting models
of proposed environmental mitigation scenarios to decision makers. These include Little Manila
Rising and Climate Resolve, who together with WOEIP complete the triad of CBOs included in
this grant proposal, as indicated through their letters of support. All three have suffered
disproportionate pollution burdens due to California’s history of racist environmental policy.
\[...\]
# [BH-EPA-Grant](https://docs.google.com/document/d/1YdZRG7tx2Ji1_7NrmzRRTM940g562PqRTS2o7Ons-NI/edit?usp=sharing) **EDITED**
## Approach
Our project has a number of core overarching missions and project philosophies. 
**Overview**
Historically, industrial corridors have disproportionately affected low-income communities of color, with the Arlington Park community in Dallas being no exception to this industrial encroachment. Residents are exposed to a multitude of pollution sources, exacerbating the challenges posed by climate change and the absence of green spaces. Together, Texas Trees Foundation, Texas A\&M University, Arlington Park Neighborhood Association, and the engineering firm, Hyphae Design Laboratory, are developing a community-driven design for an urban “buffer zone” project that incorporates both gray and green infrastructure options and protects residents from the industrial corridor impacts. The project’s overarching objective is not just to establish a protective buffer zone, but to ignite enduring change in the intersection of environmental justice and community well-being. 
A Community Plan was developed by the city of Dallas during \[timeframe\]. Based on that plan, light industrial and heavy industrial land uses will remain in Arlington Park. The purpose of this project is to fully understand the environmental exposure from those impacts and develop community adaptation solutions to mitigate the impact and exposure to residents and workers.
### Project Focus:
The focus of the project is on residential & commercial communities impacted by the industrial corridor, as well as workers in the industrial corridor. The plan is to first focus on one community in this industrial corridor. The community was chosen in collaboration with community members and shown in green.
The hope is that the community-driven, evidence-based approach from this project can then be replicated to additional adjacent impacted communities in both Arlington Park to the North and East LA to the West, as EJ impacts are not defined by political boundaries\! The eventual hope is that these industrial strength green infrastructure solutions could also be shared and adopted by other industrial corridor communities in LA like Commerce, Compton, etc.
### The Need and the Challenge
It is extremely difficult and expensive to mitigate climate impacts such as air pollution, stormwater and heat islands in a city because infrastructure is extremely expensive.  It is even harder to do so in industrial fenceline environmental justice communities, because of very little plantable area caused by the predominance of small/dense residential lots, due to socio-economic conditions, as well as, excessive pavement associated with historical and/or active industrial land uses. Concrete removal and other infrastructure interventions are required at high relative costs. 
Therefore, interventions must be targeted and optimized to maximize cost benefit ratios to place interventions where impacted populations are most active, which is not only driven by population density, sensitive receptor locations, activity spaces (like parks and schools), but also the active transportation corridors most utilized by pedestrians. 
### Community-driven Design
Community-driven design in partnership with scientific processes is critical. We have been working for over a year with the community to assess these critical corridors.
*Language for Laura to insert elsewhere:*
Our engineering partner, Hyphae Design Laboratory, furnishes community organizers with the data and scientific tools they need to practice evidence-based environmental justice advocacy. The firm has fifteen years of experience coordinating activists, other technical assistants, academic researchers, air districts, city governments, and federal agencies in To redressing unfair pollution burdens faced by low-income communities and communities of color. Acting mainly through the legislative framework of AB 617, their partners have transformed their built environments and achieved significant policy changes in pollution reduction, green infrastructure, and climate resilience.
In Arlington Park, Texas Trees Foundation and Arlington Park Neighborhood Association are partnering with Hyphae to plant vegetated buffers, implement a truck re-routing plan, and depave a section of the neighborhood. \[What is the funding source for this grant?\] Through a NASA Grant, Coordinating with the Jet Propulsion Laboratory, the project integrates aerial and satellite imagery with Hyphae’s LiDAR scanning and Texas Trees Foundation’s ground-level heat sensors to identify heat stress at a submeter level. Trusted Arlington Park Neighborhood Association messengers will then carefully track where sensitive receptors gather, collecting door-to-door canvassing information that cannot be gleaned from maps. Hyphae will then combine all four data sets to map the area and generate a series of extreme heat mitigation scenarios. 
### Evidence-based Design
Max’s text: 
Using hyperlocal mapping and measurement tools developed with funding from the National Science Foundation and the National Institute of Health, Hyphae helps CBOs identify air, soil, and water contamination in their communities, as well as other risks to human health such as extreme heat, flood risk, noise pollution, wildfires, and vector-borne diseases. Partners can then deploy Hyphae’s software-based adaptOS platform to simulate, design, and implement environmental mitigation solutions in response. Such interventions range from urban greening to truck-rerouting to the design of software applications protecting sensitive receptors during extreme heat events. 
The adaptOS platform iteratively cycles through a five-stage process of measurement, simulation, implementation, assessment, and refinement. After mapping a given geographical area, the platform models potential mitigation scenarios prior to construction. Once design solutions are implemented, the same tools are used to evaluate and assess the net environmental impact of those designs, providing empirical evidence of their effectiveness and sustainability, and allowing for corrections as needed. 
Brent’s text:
The community-led design and implementation process is also grounded in an evidence-based, scientific,  adaptive management framework. Evidence-Based design utilizes scientific basis for community adaptation. It goes beyond doing research with or for a community, which can often occur adjacent to the community empowerment work they are doing to embedding scientific within our community design decisions. 
In the Adapt evidence based design process, we do analysis and design, then do measurement and modeling to inform the design, prioritize implementation locations and measure their effects. It also de-imperializes science, as a tool that can be used by all, and not subject to academia and PHDs. Our core philosophy is in fact that community members are often the best scientists, as they inherently experience, observe and evaluate their community more than academics. 
### The Science Team
As Technical Consultant, Hyphae Design Laboratory will spearhead the evidence-based design process. bridging the collaboration between the community groups and the scientific and technical and agency specialists. They will help the team do the environmental measurement, modeling, engineering and design required to optimize infrastructure solutions, pedestrian and vehicle infrastructure optimization, as well as regarding tree planting and cool pavement installation (inclusive of Strategies 1,2,3,5,11, and 12). Hyphae will also lead coordination with the various research partners, including Altro Status, and Jet Propulsion Laboratory, and other partners. Hyphae will ensure that the science conducted is in alignment with the community goals and implementation projects and is shared with community members throughout the grant period. 
With support from NSF SBIR Grant \#2218499, Hyphae Design Laboratory, a mission-driven social enterprise, has developed software pipelines to build 3D digital twins, computational fluid dynamics models, and sub-meter microclimate simulations using open source data inputs like aerial lidar data, using openfoam CFD and UMEP simulation tools, to develop models for prioritizing locations and optimizing designs for various heat island mitigation interventions, such as tree planting, vine planting, cool surface treatments and pedestrian route planning. 
NASA's Jet Propulsion Laboratory (JPL) brings advanced thermal imaging and data analysis capabilities to the collaboration with Texas Trees Foundation, Arlington Park, and Hyphae Design Laboratory. JPL’s ECOSTRESS satellite data and HyTES airborne thermal sensors provide high-resolution data crucial for evaluating the effectiveness of environmental mitigation efforts, such as cool pavement coatings in Dallas. This thermal data helps secure additional funding and guides the design of urban buffer zones that integrate gray and green infrastructure to mitigate industrial impacts. JPL’s expertise in thermal infrared remote sensing and its collaboration with Hyphae ensures data-driven, effective solutions for reducing extreme heat and improving community resilience.
Altostratus, is a leader in mesoscale modeling in both the research and implementation arena. Altostratus Inc., founded in 2003 and based in California, specializes in multi-scale atmospheric modeling for climate, emissions, air quality, and urban heat island studies. They utilize advanced meteorological tools to generate fine-resolution weather forecasts and emissions modeling, aiding in urban and environmental planning. The firm famously developed the Urban Heat Island Index for California and has collaborated extensively with CalEPA and the SMAQMD. Their work supports decision-making for urban development and sustainability initiatives.
USC
### The Approach: Measurement & Modeling
An adaptive, measurement, design and modeling workflow permeates, drives and ties together all of the other more specific projects.
  - Collect data on Heat, air quality, greenness, demographics.
  - Uses data to validate models and use models to expand on resolution of environmental analysis beyond data collection.
  - Use data to drive prioritization of locations for additional sensors
  - Use sensors and models to to optimize design interventions and locations
  - Use sensors to measure intervention effects.
We first survey the physical environment using lidar and Google Street View 360 cameras to develop a high resolution, sub-meter resolution digital twin of the physical environment. We conduct these physical surveys before, during and after project construction. They both serve as environmental measurement baseline as well as a modeling environment for simulating existing and future meteorological conditions and air pollution concentrations.
The synthesis of aerial thermal imagery and high resolution modeling can provide a showcase with societal impact beyond this project. In addition to heat stress and thermal comfort implications, these pipelines can model and inform the co-benefits of intervention impacts on air pollution, stormwater management, and biodiversity. 
For air quality measurement, we're going to combine a network of medium-cost fixed air quality monitors with a regular seasonal collection regime of mobile high-resolution ultrafine particle sensing. The reason and methodology is further discussed in detail in the Section titled *Strategy 13 – Community Air Quality Monitoring, Training, and Education*
We are also going to couple microclimate sensors with the air quality grid including mean radiant temperature, wind speed and direction anemometers and temp and humidity. We are also working with JPL and NASA through a separate grant to fly high resolution thermal data over the community before and after interventions. Increasingly research is finding the microclimate conditions including the shapes of buildings, topography and local conditions like the temperature of the road surfaces can impact AQ dynamics significantly. 
Simulation modeling can further detail these phenomena. Hyphae and AltoStratus will implement simulation models to both understand existing conditions in further detail as well as simulate various alternatives to optimize intervention scenarios for the target neighborhood of Arlington Park. These high-resolution models will also be calibrated with on-the-ground microclimate sensors for validation. 
We will develop mesoscale as well as microscale models that will be coupled and also validated with the JPL data for heat as well as the WRF-Chem CMAS, for regional and mesoscale modeling and done by altostratus. Openfoam CFD models will use forcing data from the mesoscale models but allow fine resolution modeling of specific interventions. 
## Strategies
While we intend to advocate for reduced emissions, the primary focus of this project is to develop community solutions that can be implemented immediately and over the medium term to mitigate exposure of residents to industrial impacts by leveraging multiple interrelated urban planning interventions that range from vehicle and pedestrian routing to gray and green infrastructure like urban greening, cool surfaces, building climate upgrades.
\[Compilation map
Add Boundary of the project\!\]
Strategy 1 — Public Right of Way Tree Planting
**Strategy 2 — Private Property Tree Planting (draw a boundary for prioritization)**
Strategy 3 — Agency Tree Planting Design  
Strategy 4 — Public Right of Way Cool Pavement
Strategy 5 — Private Property Cool Pavement (draw a boundary for prioritization)
Strategy 6 — Parks Improvements
Strategy 7 — Creek Improvements
Strategy 8 — Cool Roofs and Solar (draw a boundary for prioritization)
Strategy 9 — Community Art: Cool Paints/Solar Reflective Murals (draw a boundary for prioritization)
Strategy 10 — Metro Bike Share (Integrate Paula’s maps)
Strategy 11 — Traffic Analysis and Technical Assistance 
**Strategy 12 — Private Property Greening **
Strategy 13 – Community Air Quality Monitoring, Training, and Education
### **Strategy 1: **ROW Tree Planting 
### **Strategy 2: **Private Tree Planting
Prioritization for public right-of-way and private planting will be driven by environmental analysis and modeling. They will also be driven by already underway and ongoing community-based research that identifies critical community corridors and hubs.
Hyphae will provide property level and street level prioritization maps for Northeast trees to optimize outreach to most critical need streets and properties. Hyphae will coordinate with streets La and develop necessary drawings for Northeast trees where concrete removal is needed. Northeast trees will conduct the majority of Street tree and private property planting. Hyphae will assist Northeast trees and Texas Trees Foundation to develop planting designs for more specific properties such as schools and private property along the freeway that may require vegetative buffers.
### Strategy 3: Vegetated Buffers
Planting in \[agency\] right-of-way provides significant potential for the integration of near road vegetated buffers for air filtration; the closer you can get to the pollution source, the more potential you may have to remove particulates, or dissipate them. 
We have met with and worked with \[agency\] in this project area and they're open to planting pending more detailed plan submittal with stewardship plans and traffic control plans. The design and modeling and permitting logistics for \[agency\] are more complex than some of the other project areas, but it's also more important to spend time in these critical times to design the buffers effectively.
We will spend 2 years of this grant developing detailed designs to optimize pollution removal and also develop Encroachment Permits needed by \[agency\] including detailed planting designs, stewardship plans for \[agency\] from which we will leverage other funding to implement planting. This grant provides critical bridge funding to develop the drawings to a level of detail for technical aerodynamic design and \[agency\] approval.
Our consult, hyphae design laboratory, has over 15 years of experience researching and designing vegetated buffers. Hyphae is currently working in partnership with \[agency\] and communities across California to address near road pollution, to permit similar projects in Oakland, Richmond and Stockton. They have also worked with vegetative buffer experts from EPA like Rich Baldauf for over a decade, and are collaborating with Professor Akula Venkatram from U.C. Riverside who is contracted with \[agency\] to build vegetated buffer buffer models and was critical to developments of AERMOD other other near road models.
Hyphae Design Laboratory StreetsLA, Northeast Trees and Texas Trees Foundation will conduct the assessment and identification of suitable planting locations for 100 trees (size 15-gallons) and other vegetative cover as well as the necessary watering systems on \[agency\] properties. Hyphae will work with the relevant professionals including, but not limited to, Traffic Engineers and Landscape Architects to conduct the necessary LiDAR scanning and technical analysis of relevant data to develop planting designs. Hyphae will also update designs to reflect the feedback offered by relevant stakeholders and offer fully vetted designs for future grant opportunities. 
### **Strategy 11: **Complete Streets in Industrial Community 
#### Traffic Analysis and Technical Assistance
HIstorically Complete Streets work has occurred in residential and commercial corridors. We are working with the StreetsLA to develop a model for how to develop Complete Streets in industrial communities. The community of Arlington Park has identified Olympic Boulevard and Soto Boulevard as critical community corridors that are also, unfortunately, interfaces between industrial and residential land uses. Developing sensitive streetscape plans that address critical traffic safety issues in the neighborhood and address truck management plans that direct traffic away from community resources is a critical air quality and pedestrian safety concern. Because of these conditions, designing effective streetscapes in our industrial communities requires a different approach to historic Complete Street design.
This work takes nuanced modeling, design and coordination and policy work. This grant will fund the critical resources for collaborating with the city on policy and infrastructure, and hiring the necessary environmental civil landscaping, geotechnical resources and multimodal design. 
We will work with the community and the city to advance design concepts to 30% to a cohesive collective design concept for integration into planned City sidewalk and Road improvements as well as submission for Capital improvement Project or other Grant submittals. 
For a similar project in Oakland, Hyphae is working with the Port of Oakland, the City of Oakland, the Bay area Air Quality Management district with funding from the Metropolitan transportation commission, to develop a complete Street Road diet and vegetated buffer plan for a truck corridor in West Oakland. This work will require sensitive design and modeling of pollution Dynamics for sensitive integration of residential and community commercial corridors adjacent to active industrial ones.
Direct coordination with StreetsLA for which includes the assessment for the installation of community desired bicycle infrastructure and other safe pedestrian infrastructure within the project area. Additionally, Hyphae Design Laboratory will coordinate with other relevant professionals, including but not limited to Traffic Engineers and Planners, to develop designs for proposed greening improvements along Olympic Boulevard, such as vegetated street medians, protected bike lanes, and other traffic-calming measures to ensure alignment with any LADOT initiatives in the project area. 30% designs will then be proposed to LADOT for feedback and approval for their capital infrastructure program. Moreover, Hyphae Design Laboratory will also coordinate with other relevant professionals to develop additional designs for proposed green infrastructure such as bioswales, rain gardens and bulb outs, to mitigate the impacts of runoff and stormwater pollution as close to its source as possible using permeable materials and drought tolerant plants, and to ensure alignment with other City initiatives in the project area. 
### **Strategy 12: **Showcase Greening Projects 
Particularly in existing and informer industrial neighborhoods as well as neighborhoods that have lower income and property values, the typical environmental justice communities that we try to Target, integrating greening strategies that are used in more Suburban contexts is not always possible. In some properties or streets, typical Street trees can't be planted or people's whole property is paved with the driveway. In these conditions, there are nonetheless interesting and novel and even vernacular strategies for greening and cooling and air quality. For example, planting hedgerows only requires a narrow space and can still accommodate cars and trucks needed to park in working communities. Also car canopy vegetated trellises can provide cooling, protect one's vehicle and also provide a street facing family gathering space. 
These types of novel greening solutions are often not typically funded with standard Street tree and urban greening grants. We're setting aside a portion of funding to Pilot these unique solutions and hopefully integrate them into more policy in the future.
Hyphae will provide direct supervision of Strategy 12 Private Property Greening, which includes coordinating outreach efforts to identify interested homeowners/private property owners, conduct property assessment, and strategically plan and propose greening options such as living walls, shrub trellises, and rain gardens depending on property conditions. Installation of greening will be done in collaboration with a local landscaping contractor, maintenance will be conducted by the corresponding property owner and materials will be purchased from local nurseries and garden supply stores, where possible. 
### Strategy 13 – Community Air Quality Monitoring, Training, and Education
To develop local and community-based actionable interventions, we must first gather hyper-local air quality as well as environmental spatial data (through LiDAR) to identify the main sources of pollution. In some places, pollution may be freeway, but in others it may be a point source, such as a refinery. Our combination of fixed and mobile sensors will identify these pollution hotspots. Mobile sensing will be deployed to provide an initial data picture as fixed monitoring locations are coordinated and deployed. This data will also be used to locate fixed sensors, which will then give more temporal data quality. The combination of fixed and mobile sensors can help improve the shortcomings of each as recently shown by Apte Lab, a research partner in Oakland.
For fixed sensors we will be using QuantAQ MODULAIR-PM monitors designed for use by trained non-specialists. These sensors include four gas-phase measurements (CO, NO, NO2, and O3) in addition to PM1, PM2.5, and PM10 estimates as well as number concentrations for particles between 0.35 µm and 40 µm. It is also coupled with a Sonic Anemometer.  To install them, community air leaders will receive online training from hyphae and QuantAQ. These sensors have been successfully used on many similar initiatives throughout the United States and beyond, offering significant ease of use, quality, and price. They have been chosen for their relatively low cost, but higher quality than other low cost sensors like Purple Air, as well as the more advanced machine learning and data calibration capabilities. They have also been chosen for their increasing use in EPA and other funded projects. Additionally, and for the same reasons, Aethlabs, Black Carbon sensors will be deployed, as a secondary means of data collection for side by side comparison and for the ability to capture the truck related pollution from this heavily truck trafficked neighborhood and health impact data associated with BC. We are also using these sensors because they are EPA validated and used across many projects including partnership with our own in Oakland, Stockton and Marin City. We believe in the value of utilizing similar methods and protocols across different projects in different regions, so that hopefully insights can be compared more broadly between them. His also increases the power of the insights
Mobile sensing will then further enhance the fixed data layer by refining the data picture and validating the medium-cost sensors through co-location. Mobile sensors will be deployed to collect upwind and downwind transects near pollution sources. To achieve this, Hyphae will use a Brechtel ACCESS 9403 Advanced Mixing-based Condensation Particle Counter (aMCPC) to gather highly accurate measurements of PM2.5, NO, NO2, NOX, BC, and Ozone. Similar to the QuantAQ sensors, these are being chosen because they are being used on other similar projects that include interventions. In collaboration with Turner Lab at Washington University, they are being used on the first NIH funded clinical trial  in Louisville Kentucky, they are also being used on a Hyphae project in Marin City, Dallas, and Stockton and Oakland, other AB617 communities.
These sensors are being used because in intervention based studies, higher resolution and accuracy with  lower error range are critical to parsing out smaller scale changes that come about from interventions. For example a plow cost purple air, or even QuantAQ sensor may have an error range of 10-25%, while the impact of greening may be in the range of 5-30%, making it indistinguishable by lower cost sensors but non-the-less impactful to the community. These sensors also strike a balance between extremely expensive sensors and low cost sensors, while $30-50,000, they are still attainable by larger community level projects. 
The higher resolution mobile sensors data will be used to validate the low-cost sensors by co-locating them with them or periods of time. Both the low cost and UFP sensors will also be integrated and colocated with and government reference monitors, as well as other low cost sensor networks in and around the neighborhood (A Carlity network is deployed at schools through LAUSD and is sharing data with OpenAq and SCAQMD). See Maps attached
The combined data set, along with aerial, satellite, and ground-based LiDAR scans, will be integrated to generate 3D models of the chosen area.  Troubleshooting in the field will be handled via collaboration between our participants in the field and our technology partners. Participants will be trained in how to handle common issues such as network disconnection, power loss, and spurious data readings, receiving automatically generated prompts from our chosen technology platform when they need to take action. 
#### Sensor Deployment Plan
This project will consist of the following milestones:
  - \[Start Date\]: Consultation of our community members begins from the outset of the project. We will make sure community members know what we aim to achieve through monitoring and how it can help them make informed decisions about how to adapt their environment. 
  - Initial zones have been chosen based on previous Aclima mobile monitoring data and to collect a range of upwind and downwind conditions in proximity to industrial sites, highways, and other sources of pollution such as truck depots and warehouses. 
  - This period of consultation and awareness-raising is designed to ensure that the community is on board with our project and that we have buy-in when recruiting participants.
  - \[Start Date + 1 month\]: Participant recruitment and community onboarding begins. In exchange for stipends, we will be looking for community members and agencies to help install the sensors, to maintain the sensors, to annotate sensor data, and to receive the daily and monthly air quality reports. Our participants will be recruited from our stated areas of interest. We will also begin a community outreach campaign designed to raise awareness about the program and to rally our aligned community-based partners.
  - \[Start Date + 3 months\]: Hyphae will begin the first of eight mobile sensing trips. They will drive a car equipped with a camera, a thermal sensor, a LiDAR scanning device, and an ultrafine particle sensor (UFP) through the target neighborhoods, taking measurements to reflect the change in seasons and time of day. During that time, they will also attend three community meetings to translate their research to the community, present their findings, and disseminate the models they will have created to visually depict pollution hotspots and flow.
  - \[Start Date + 6 months\]: Selection of specific air quality monitoring locations, e.g., streets, resident homes, and equipment ordering. Hyphae will attend the first of six community outreach meetings, laying out their contribution to the project and inviting community members to think creatively about how they would like to use the data to restructure the urban landscape with urban greening and road diets, or to contain pollution emanating from local industrial sites.Hyphae will also work with SCAQMD to begin the process of co-locating low-cost sensor data with the state’s reference monitors.       
  - \[Start Date + 9 months\]: First monthly air quality insight report produced and shared with the community. Hyphae attends its second meeting and presents its preliminary models.   
  - \[Every subsequent month\]: Monthly air quality insights shared with the community.
  - \[Every quarter post-deployment\]: Project check-in with volunteers to get feedback, recognize community contribution, discuss findings, and answer questions. 
  - \[Yearly \]: Annual report summarizing findings to date, including community observations, along with recommendations for remediation. 
  - Monthly, quarterly, and annual reporting activities continue in subsequent years. 
  - \[Years 2 and 3\]. Hyphae and will collaborate in validating each other’s data sets by co-locating the low-cost sensors with the measurements of the more refined instruments as well as with the government reference monitors. Hyphae will appear periodically at the scheduled community meetings to translate the evolving air monitoring data picture and crowd-source community designs for subsequent rounds of funding and the direction they wish to take the project.   
  - \[Final Quarter of Year 3\]: Hyphae will prepare a detailed report of the air quality in the designated areas, complete with graphics and visualizations that can be used by community members to mobilize popular support for remediation, pressure decision makers for change, and apply for future rounds of grant funding.  
## Scope Table
\[image\]\[image\]
[HYPHAE: EPA-COMMUNITY CHALLENGE](https://docs.google.com/spreadsheets/d/1YhAGhA52q9-MGuODry2l8-ORuH9rfx4UaE5oIVTJUYc/edit?gid=1934813080#gid=1934813080)
LINK TO LIVE BUDGET
## MAPS
 
Prioritization
**Thematic Maps**
  - Parcel Priority
      - Air Quality
      - Extreme heat
      - Flooding
  - Community Priority Maps
      - 
  - All compilation map for Comms team
      - Boundary of the project, fresh new map
      - 
All compilation map for Comms tea
# [Green\_Spine\_Design\_Coordination\_Hyphae\_Scope\_and\_Schedule](https://docs.google.com/document/d/1rjLWnWYy-2Vy80-5FDGFUZKCM8VPwrh1TV7bNl2qDh0/edit?tab=t.0)
**Health-Impact Driven Ecosystem Modeling **
## Introduction
Texas Trees Foundation is spearheading the Green Spine corridor intervention in the South West Medical District (SWMD) of Dallas, Texas. The Harry Hines corridor between Market Center and Mockingbird is to be re-landscaped, potentially with modifications to traffic flow. The cloverleaf interchange between Inwood and Harry Hines is to be replaced with a park. The goal is to use evidence-based design to facilitate a health-improving intervention, and set up the area as a living laboratory for sustainable design. Hyphae has been engaged to model and monitor the district to support the design basis and facilitate before and after studies of the health impacts of the intervention.
 Thermal comfort was chosen as a primary endpoint for two reasons: 1) extreme heat is a pervasive problem in the district and 2) there is a plausible chance that we can measurably change the thermal comfort in the district using landscape interventions, in particular the planting of trees. Air pollution is another endpoint which appeals because there is significant traffic in the corridor, with pedestrian focussed infrastructure unbuffered from traffic-sourced pollution. Tree planting is also a potentially effective intervention for reducing air pollution exposure for users of the district, although effective monitoring for air pollution impacts of vegetation is more expensive than for thermal comfort, and potentially less likely to be improved significantly. 
## Background
 Throughout 2021 TTF organized a visioning collaborative that produced preliminary concepts for traffic changes and landscape improvements. During this phase we produced some small in-silico models of a few prototypical locations in the district to perform thermal comfort and air pollution modeling. A summary of the results of the preliminary baseline existing thermal comfort modeling, and the air pollution modeling of selected sections from the visioning design plans can be found here: [Green Spine Simulation Results](https://docs.google.com/presentation/d/14pa6ST4NVTzvjlFdc9XA70qCvX56Pv8PQl_aQWTMGUM/edit?usp=sharing).   While some insights from these models can be used to guide design decisions, modeling of specific design scenarios is necessary to optimize the best design. Furthermore, to ground-truth the models and establish a baseline for before-and-after efficacy analysis, it is necessary to start monitoring conditions in the district prior to the intervention taking place. Thus a 3 phase modeling and monitoring project was initiated.
## Phasing
1.  Phase 1 monitoring was envisioned as a pilot deployment of a central monitoring hub on the rooftop of Parkland Hospital, which could route LORA radio signals from 30 battery or solar powered sensor nodes to the cloud for analysis. The 30 sensors would be placed throughout the district, but confined to a pilot area between Butler and Medical District Drive, because it was chosen as the most likely primary intervention location. Phase 1 modeling began in this zone, to begin validating those models to the sensor data and to evaluate the design proposals from the visioning phase for feedback into further design processes.  Phase 1 is nearing completion, and in preparation for phase 2 we are proposing the following design coordination scope.
2.  Phase 2 of monitoring will explore the data from phase 1 and determine if additional sensors are required elsewhere in the district. Phase 2 of modeling will be the modeling of design iterations developed with the designer (JCFO). This is the subject of the present document, and will be discussed in detail in the section below entitled Design Coordination. 
3.  Phase 3 will involve continued monitoring, modeling and evaluation into the post-intervention and longitudinal domains and installation of additional sensors if needed, and will not be discussed further in the present document.
## Design coordination
Hyphae’s monitoring and modeling work will inform the basis for design toward stated outcomes established in concert with the primary landscape design team. We describe here a protocol for close collaboration with design and engineering efforts that aims to reliably connect design decision making to environmental modeling results. This involves stages of work beginning with bringing all model inputs up to date (including monitoring data, surveys, outputs from the engineering team, and current assumptions of the designers), then establishing baseline conditions, setting benchmarks, and finally making predictions about the performance of various design proposals. The targeted outcome supported by this process will be 30% design schematics that are vetted through computational simulations for their predicted environmental metrics. 
### Baseline Model
Beginning this design coordination scope Hyphae is building upon baseline simulations started last year and taking advantage of new inputs as they become available, such as monitoring data, traffic counts and improved surveys. We will move forward on these while the collaboration is initialized with the new design team. Hyphae plans to run models for air quality based on traffic inputs, as well as potential changes to speed profiles or stop frequency. We will also study ROW median variations for AQ impact more in detail following our preliminary results. 
We are looking forward to receiving materials from the engineers as well as any new documentation of existing conditions, including tree survey. The preferred traffic alignment is especially important for simulating corridor scenarios. As these studies are completed Hyphae will provide a report, as well as maps, and presentations, with annotated insights. 
### Benchmarking goals and studies
While we complete baseline existing conditions models and proposed lane and traffic updates, we are also developing benchmarking simulations: for example on the impact of a maximal planting scenario, investigating evergreens vs deciduous and small vs large trees. These benchmarks will be useful because the impact of detailed design scenarios can be compared to reference impact ranges. 
We believe this first benchmarking will allow the collaborative team including JCFO and TTF and other research partners to engage in a practical, achievable goal-setting exercise that establishes performance metrics in accordance with some of the previous modeling, current literature and expert input. A design charrette will be instrumental in orienting the team around these goals. At that time we will also set research objectives for later academic literature contributions. 
### Design evaluation
We propose a choreographed collaboration schedule to avoid one team waiting for the other with the exact sequence to be refined as part of the collaboration.  For example, Field Operations might start by prioritizing the corridor design in areas Hyphae has already generated model results, while Hyphae completes baseline models of the extended corridor and park and works on baseline studies.
When certain design options and sections of the corridor are drafted we can begin modeling them while JCFO tackles other segments of the corridor or moves to the park for example. When their designs are ready for modeling we will have results for the first group of designs to pass back to them for iteration. 
We will repeat this hand-off procedure again and then recapitulate our goal-setting exercise for any useful changes made clear during the work to date. 
We will also provide interim recommendations based on the first course of simulations in each condition. These will be sketches and design recommendations as well as analytical exhibits. Additionally, we can ad hoc jump in to run quick models when needed for example if JCFO is considering a few different solutions and want feedback.
### Design optimization
We will revise our models based on iterations provided to us by the design team and refine our queries to target the particular dynamics interesting to the team. We will run models for a second round of design iterations on both corridor and intersection urban conditions, including the park area as needed. We will provide results in preliminary/raw form along with revised sketch recommendations for the designers to incorporate in their 30% design documents. These sketches might be scaled hand drawings, 3D massing models, illustrated sections, or any format which is most effective in communicating an intervention typology. 
### Impact Estimation of Final 30% Design Development Plans
A third round of simulations will be necessary to project the impact of the final design decisions at both the corridor and the intersection scale. The results of this  will be used to formulate targets for future longitudinal studies in future project phases.  
### Research
We will continue to analyze data from sensors deployed in phase 1 to provide insights for design and modeling. We will develop plans for expanding monitoring and analysis for the longitudinal study encompassing the pre- and post- construction phases. Methodology for longitudinal analysis will be developed to understand the scope and funding requirements for additional sensor installation and analysis.  If necessary we will repair, replace and maintain any already deployed sensors. This may include upkeep of the wireless network, sensor calibration and battery replacement if necessary. 
We will collaborate with TTF to develop a framework for health and environmental research to to conduct detailed assessments of change for longitudinal research protocols. 
Will also assist with integrating the monitoring and modeling data into ongoing protocols for qualitative research and subjective perceptions of health and environmental conditions in the district. 
We will also support grant writing efforts for raising additional funding for expanding research initiatives and developing new studies. 
## **Future Phases Post 30% Engagement **\[NOT IN PRESENT BUDGET\]
Subsequent to the submittal of 30% design, in our experience, there are still many decisions to be made that can significantly affect the performance of the design. First, value engineering from the 30% set requires redesign and strategic decision making. Additionally as projects get bid and built, many changes come for example in plant species and size availability which also affects the design and the performance.
Hyphae would like to make ourselves available for responding to Requests for Information with clarification, drawings, models, or additional simulation as requested. We will also want to review designs before each submittal for fidelity to the agreed performance objectives.  However, this is not included in the present scope, which concludes with 30% design. 
Beyond this ongoing design assistance, Hyphae will be prepared to work on authorship of paper(s) for submission to academic fora on whatever topics we, with the client, deem promising.
We are eager to begin working with you and propose setting a time in the coming days to discuss some of the basic details of how we will share information and keep open communication.
# [Harry Hines Evidence-based design methodology report](https://docs.google.com/document/d/1pjgqG3wJG3j3V4w3kpBcz6cwrEsE_ZMVqWDp1iUnlqE/edit?tab=t.0)
## Executive summary
### Introduction
This document presents the methodologies employed during the evidence-based design process of the Harry-Hines redevelopment project in Dallas, TX. The evidence-based design process seeks to make use of evidence from literature, environmental simulations, and environmental monitoring campaigns to inform the design process to maximize the potential benefits, and minimize the potential harms of the built-environment interventions. While these goals apply to the Harry-Hines redevelopment project itself, they are also integrating that project into a platform for generalizing the learnings of the project to other communities. This platform is visualized in figure 1.
\[image\]
*Figure 1: Evidence-based design for environmental health.*
Evidence from previous projects is used to inform design of interventions and studies, which are then implemented, monitored (before and after), and the results fed back into the process. 
 In the case of the Harry Hines corridor, the benefits and harms that we focus on primarily are those that relate to heat stress and air-pollution exposure. From review of the literature we are aware that heat stress can be impacted by shade, where more shade in the summer can reduce heat stress, and less shade in the winter can reduce cold-stress. Wind is also an important component of thermal comfort, with higher winds in the summer reducing heat stress, and lower winds in the winter reducing cold stress. The literature on the effects of built-environment interventions on air pollution exposure is more complex. While interventions such as increasing the distance between a pollution source and the exposed person (receptor), or reducing the amount of pollution produced by the source are relatively uncontroversial approaches, there are also interactions between the structure and form of the built-environment and pollution transport & deposition which have been studied and may be of use, although the exact dynamics are not well defined enough to be certain that a particular type of intervention will necessarily be beneficial. For example tree and shrub foliage placed along a roadway may be able to act as a sort of sponge for airborne particulate matter, providing both a momentum sink and a high surface area, thereby facilitating the collection of pollution on leaf surfaces and thus preventing it from proceeding past the “vegetated buffer”. While this approach is potentially a low-cost, high-benefit design strategy, there are some caveats. For example, trees can also slow down the wind, which would otherwise blow the air pollution away from the ground and up into uninhabited atmospheric strata. This possibility of vegetation trapping air pollution at ground level where people will be more exposed makes it important not to simply plant trees without thought to the aerodynamic consequences… at least when an air pollution source is nearby.
The combination of the heat and air pollution rubrics gleaned from the literature leave designers with a bit of contradictory guidance: Tall canopy trees provide shade, which is good for reducing heat stress, but will potentially trap air pollution near ground level, endangering people’s health. Roadside vegetated buffers may be effective for remediating traffic sourced air pollution, but may slow the wind down (which increases heat stress), and may also reduce sightlines necessary for traffic engineering. To get beyond this limitation of qualitative rubrics, we employ environmental physics simulations to try to find the “sweet spots” where the benefits and harms of intervention design can be balanced to the overall benefit of the community. These simulations enable us to weigh the relative merits of different responses of the design to the constraints of the site, of regulations, and of other stakeholder preferences. By way of some examples; if a pedestrian path must be directly downwind from a highly trafficked roadway, then we might propose a roadside vegetated air barrier. However, we know from the literature that roadside vegetated air barriers are most effective when they are maximally tall (the taller the better) and thick (the thicker the better). However, the plantable area only allows a certain thickness, and the sightline requirements of the transportation regulators call for no more than a 4 foot high buffer. Through simulations, we can see if there is an appreciable difference (on air pollution) between a 4 foot tall buffer and a 12 foot tall one, and if there is, can we still make the buffer useful, for example by adding trees to the median across from it? Similarly, if we are trying to maximize the shade from new trees, we might want to plant lots of tall canopy trees along the pedestrian path. However, if the pedestrian path is right next to a busy roadway, will the shade benefits of the trees outweigh their pollution trapping effects? If they are tall enough, will they create a “wind-tunnel” effect that actually reduces pollution overall in the pedestrian zone? By iterating these potential design scenarios *in silico*, we can compare the relative merits of various design solutions and try to pick the most promising approaches. These approaches can be fed back to the stakeholders, and revised and re-simulated during the design process. 
While the simulations discussed above can provide important insights into the potential health consequences of design decisions, and provide guidance on how to improve specific design scenarios, simulations are inherently not real. The degree to which simulations faithfully represent actual or potential reality can be measured, tested, and validated. In our case the simulation of environmental parameters related to heat stress and air pollution can be measured in the existing environment, and the measurements compared to a simulation of the existing environment. The fidelity of this comparison can give some insight into how reliable a simulation of a hypothetical design might be, even if it cannot itself be verified until after construction. We have deployed a network of 30 low-cost thermal comfort sensors throughout the phase 1 area of the Harry Hines corridor between Butler and Medical District Drive. We have used these sensors to validate the fidelity of the thermal comfort simulations. However, air pollution sensors are more expensive and require greater effort to use effectively, so we are planning to deploy them in future phases. In addition to providing direct insights into the effects of built-environment features on heat and air pollution, and enabling validation of simulation results, the monitoring campaign will allow a pre/post evaluation of the performance of the design once it is installed. In combination with health studies on the users and inhabitants of the corridor, the sensor data will also allow longitudinal studies on the health benefits of the intervention, the results of which can be used to help design effective interventions in other communities. 
## **Design Process, Collaboration and Iteration**
The explicit goal of this work is to improve human health in our study areas. Our process includes planting design and engineering completed at hyphae as well as ongoing collaborative design with cooperating engineers and architects. The specifics of these cooperative procedures are fluid and the subject of our efforts to optimize and manage for maximal real world impact.
Courses of simulations are defined collaboratively with the goal of documenting guidelines and informing an understanding of the essential physical dynamics which impact environmental conditions. The objective is to contrast plausible scenarios in an iterative manner that isolates and optimizes variables that are possible for design intervention.
The procedure is inherently iterative in that each course of simulations reveals unexpected results or questions which are targeted for further interrogation.
The culmination of this collaboration is a set of predictions regarding the measures of key physical parameters following the preferred design option. As supporting data, this process produces expected values for thermal comfort and air quality variation over space and time. If the predictions are born out when experimentally verified then a positive impact is supported and the design can conclusively be called evidence-based.
## **Monitoring and pre-post study**
Our first phase of monitoring has revealed significant benefits of large, mature trees in reducing environmental variables that contribute to heat-stress. Peak mean radiant temperature (MRT) reductions of 24 degrees are seen between the shade of a large established tree and sun-exposed areas. Average summer afternoon globe temperatures are almost 8 degrees lower in the shade of large trees than out in the sun. Small trees also have such an effect, but smaller (only 3.5 degrees cooler on average) and over a much smaller area. Bus shelters are shown to have much higher air temperatures than even out in the sun, although more study is needed to determine the effect of this on total thermal comfort. Correspondence between sensor readings and concomitant simulation results are encouraging, and will be improved by updating models with new LIDAR data created in September 2023. 
Provocative results of air pollution simulations suggest a need for air pollution monitoring in addition to thermal comfort monitoring, and a phase 2 monitoring program is proposed to include this as well as biodiversity monitoring, and studies of human health and experience in the corridor.  A set of cross sectional and longitudinal hypothese are presented on the impacts of the intervention on the environment and human health for further studies which will establish the corridor as a high-performance intervention, and as a living laboratory for validation of evidence-based design principles.
## Brief Literature review
### Strategies for air pollution
#### Urban Vegetation for Air Quality Improvement:
 The use of vegetation as an urban air pollution mitigation strategy has focused on two general categories of observed mitigation scenarios that are addressed below; roadside vegetated air barriers and ambient removal by dispersed trees. In both cases the mechanism of mitigation can proceed through both deposition of pollutants on the surfaces of vegetation, and by dispersion of pollutants by vegetation-induced turbulent mixing of polluted ground level air with cleaner air from higher altitudes (Janhäll 2015). Additional air quality improvements by vegetation from heat island mitigation (for example by reduction of heat-induced ozone formation) are well documented (Akbari, 2005), and this is potential synergy of design strategies that focus on heat reduction.
#### Vegetated Air Barriers for Roadside Pollution Mitigation:
 The design of roadside vegetated air barriers for effective air pollution mitigation has been discussed in Fuller et al. (2009). The primary design rubric is to facilitate a high surface area of vegetation to engender particulate deposition, with no gaps in the buffer to allow unmodified polluted air to pass through. This can be implemented with dense plantings of tall coniferous genera such as Thuja, Abies, Pinus, Taxus, and Juniperus, although species selection should be appropriate to a given site. In locations where a clear-zone is required by the side of the road, these large trees can be planted outside the clear-zone, while the clear zone can be planted with allowed species, such as tall grasses and shrubs with thin branches posing no threat to off-course automobiles.  The reduction in pollution concentration near the source of pollution by nearby vegetation has been studied under different conditions (see for example, Baldauf et al. 2008 & 2013, Bowkler et al. 2007, Brantley et al. 2014, Fuller et al. 2009, Gallagher et al. 2015, Hagler et al. 2011, Islam et al. 2012, Jeanjean et al. 2015, Steffens et al. 2012),
Studies on air pollution mitigation by roadside vegetated air barriers have found that as much as 37% of road sourced ultra-fine particulates can be captured or dispersed during crosswind conditions when the trees are planted close together and have dense foliage (Al-Dabbous & Kumar 2014). However, when vegetation is sparse and the vegetated buffer discontinuous, inconsistent effects are seen (Hagler et al. 2012). Tong et al. (2016) simulated particulate dispersion and deposition on roadside vegetated air-barriers, and found increased performance with increasing buffer depth and leaf area density, with 12 meter deep buffers performing much better than 6 meter deep buffers (where depth is the horizontal dimension perpendicular to the roadway length). Fuji et al. (2008) conducted wind tunnel experiments with different species of tree foliage and found lower particulate capture broadleaf species than by conifers.. Hwang et al. (2011) posit that needle-leaved species (such as conifers) are better at remediating air pollution than broad leaves. Taking these factors into consideration, the US Environmental Protection Agency has developed design guidelines for roadside vegetated buffers (Baldauf 2017) that we have incorporated into our methodologies.
#### Urban Trees for Ambient Pollution Mitigation: 
The reduction of ambient pollution by urban vegetation has been studied extensively (see for example Bealey et al. 2007, Beckett et al. 1998 & 2000, Buccolieri et al. 2009 & 2011, Escobedo & Nowak, 2009, Escobedo et al. 2008 & 2011, Freer-Smith et al. 1997, Irga et al. 2015, Jim & Chen 2008, McDonald et al. 2007, Nowak 2006, Nowak et al. 2006 & 2013 & 2014, Setälä et al. 2013, Speak et al. 2012 and Yang et al. 2005). However it can be appreciated that further from the source of pollution, the pollution will be less concentrated, and hence filtration will be less effective. Hence roadside vegetated air barriers are generally more cost effective (per kg of pollution removed from the atmosphere) than targeting ambient pollution with dispersed vegetation. 
### Strategies for Heat Mitigation
A systematic review found that from 308 studies on the effectiveness of urban greening on air temperature or thermal comfort, urban trees consistently reduce daytime air temperatures and improve thermal comfort indices (Knight et al. 2021). The same study found evidence that trees can have a humidifying effect, and that grassy areas tend to be cooler than non-grassy areas, but that shading from trees was likely a key driver of temperature reductions. The overall average air temperature under urban trees distilled by Knight et al. (2021) was 0.8 °C cooler. While this may seem like a small change, in the context of existing epidemiological literature it is not. For example, Santamouris & Osmond (2020) did a meta-analysis of 55 studies and concluded that a 0.1 °C reduction in peak temperature decreases heat-related mortality by 3%. 
### Strategies for Biodiversity
The benefits of trees for air pollution mitigation and thermal stress reduction are discussed above, however there are additional benefits that may be supported by design rubrics. For example, greenness measured by NDVI was found to correlate with lower cancer mortality, with a minimum of confounding due to PM2.5 exposure (Coleman et al. 2021), suggesting the possibility of non air-pollution mechanisms for protective effects of vegetation. Some such mechanisms have been putatively identified, for example plant biodiversity has been linked to a decreased risk of asthma, where overall greenness measured by NDVI increased risk, when controlling for air pollution as a covariate (Donovan, Landry, & Gatziolis, 2021). Plant biodiversity was strongly correlated with decreased childhood leukemia (Donovan et al. 2021), with a hypothesized mechanism involving immune system regulation via the biodiversity hypothesis of inflammatory disease, which posits that decreased microbiome diversity contributes to chronic inflammatory and autoimmune disease through undereducation of the immune system (Haahtela et al. 2013). The leaf surface area metrics (like LAD and LAI) that our design rubrics emphasize intuitively relate to such hypotheses by providing the substrate for the foliar microbiome (Stone et al. 2018), and indeed leaf area has been correlated with biodiversity in general (Peng et al. 2017). Other structural properties of vegetation (vertical stratification and complexity), have been shown to strongly correlate with nearby airborne microbial biodiversity (Robinson et al. 2021). Indeed, diversity of street-tree species has recently been shown to correlate with reduced risk of cardiovascular and stroke mortality (Giacinto et al. 2021).  Thus in addition to optimizing designs around air pollution mitigation and thermal comfort our evidence-based design strategies also seek maximization of biodiversity, which beyond maximizing surface area includes facilitating structural diversity, species and genera diversity, and, to further ensure both structural diversity and resilience, diverse ages of plants to encourage continuous succession.
There are several methods of increasing biodiversity beyond maximizing leaf area. With regards to plant species diversity in the landscape, simply choosing to plant a diverse palette of species may be sufficient to garner the benefits described in Giacinto et al. (2021). The commonly cited 10/20/30 benchmark proposed by Frank Santamour (2004) states that urban forests should be comprised by no more than 10 % of any particular species, 20 % of any genus or 30 % of any single family, although more recently many cities are changing this to a more stringent 5/10/15 rule (Galle et al. 2021). A list of species existing or proposed can be used to calculate metrics of diversity, such as the Shannon Diversity Index, which is used to assess the health of urban forests (Love et al. 2022).  Similar attention must be paid to the structural diversity of the forms of the plants to address the mediators discussed by Robinson et al. (2021). 
Beyond species selection and specimen form, the importance of habitat connectivity cannot be understated. Biodiversity over many scales and trophic levels is supported by interconnections of different types of habitat, and higher metrics of connectivity have been associated with higher biodiversity (Kong et al. 2010). Connectivity metrics are many and varied, but several have gained traction as ecologically important in the context of urban forestry. The methods of Saura & Torne (2009) use graph theory to derive several metrics of connectivity between habitat patches, and that paper has been cited at least 450 times in the ecological literature. Other graph based metrics also consider the habitat patches or diversity supporting elements (such as pixels weighted by LAI) as nodes in a graph, and by network analysis on the graph, for example by computing the eigenvector centrality (discussed in the landscape ecological context by Estrada & Bodin 2008), we can assign relative importance to each node. In the design context, this means that we score the habitat patches and prioritize their size and position by moving them around and changing their size to optimize their local connectivity. There are also global connectivity measures for subregions that could be increased using the iterative patch placement algorithm of Clauzel et al. (2015). 
## **Monitoring**
### Sensor Hardware
 We installed a Long Range Wide Area Network (LORAWAN) hub on the rooftop of the 18th floor of the Parkland Memorial Hospital. This provides line-of-sight radio communication across the whole corridor from Market Center to Mockingbird. The LORAWAN hub connects over the internet to a cloud service running a LORAWAN network server which routes sensor messages via ‘MQ’ Telemetry Transport (MQTT) protocol to our cloud MQTT clients, which decode the LORAWAN packets and store the sensor readings in several time-series databases. We deployed two overall types of sensors predominantly; temperature sensors and wind sensors. The temperature  sensors employ a LORAWAN radio-module and microcontroller based on the Dragino LSN50-V2 module, which provides a unified communications platform to which we can attach a variety of sensor types. The LSN50-V2 has a battery which can last up to 10 years if messages are configured to be transmitted only every 20 minutes, as we have done for our temperature sensors. To the LSN50-V2 module we attach 2 cables, one of which connects to a SEN0385 weatherproof SHT31 temperature and humidity sensor, which we immobilize underneath a white radiation shield. The second cable attaches to a waterproof DS18B20 which we affix inside a 6 inch diameter hollow copper sphere, which is painted matte black. The DS18B20-based “globe sensor” provides radiant temperature measurements, while the SHT31 provides air temperature and humidity measurements. Our wind sensors are Barani Meteowind IoT Pro units, which have a small solar panel, battery, LORAWAN radio, elliptical-cup anemometer and direction vane. The wind sensors send data every 10 minutes, including average wind speed, peak wind speed, average and peak wind direction, minimum and maximum wind speed,  and direction confidence interval. Images of a couple of the sensors are shown in figure 3 below.
\[image\]\[image\]
\[image\]\[image\]
*Figure 3. Examples of sensors placed along the Harry Hines Corridor for this project.*
### Sensor Placement
Temperature sensors were placed on landscape features throughout the corridor with the goal of capturing a variety of thermal conditions brought about by built-environment features. In particular 23 temperature sensors were placed in relatively sun-exposed areas to capture the dangerous unmitigated thermal stress so common in the area. 15 temperature sensors were placed in the direct shade of a large, mature tree. This will help us capture the maximal benefits of tree planting. 7 temperature sensors were installed in the direct shade of small, immature or recently planted trees. This will help us understand the relative merits of different tree sizes, and assess the cost benefits of planting larger trees during the intervention implementation. 
Wind sensors, because they rely on solar panels for power, could not be placed in the direct shade of trees. However, we did employ a wind simulation to find locations for wind sensor deployment that would capture a range of wind speeds and directions, with areas predicted to have high wind, low wind, and turbulent wind chosen. The higher costs of the wind sensors meant that we could only deploy 6 of them. In addition to the Harry Hines Corridor, some of the sensors were placed in the Pegasus Park property nearby, to enable data gathering during the long logistics coordination phase with the property owners of the sensor locations. Two maps showing the sensor location are shown in figures 4 and 5 below.
\[image\]
*Figure 4: Harry Hines sensor locations*
\[image\]
*Figure 5: Pegasus Park Sensor Locations*
## **Pre/Post & Cross-Sectional Study Methodology**
In order to create an evidence base for this and other designs, the high impact variables that can be adjusted by the intervention must be monitored and modeled before and after the intervention. Such a pre-post study design requires both planning data collection prior to the construction phase and also maintaining data collection after construction. In addition to pre-post studies, other types of longitudinal studies can be conducted that assess the impact of change on the environment and the health of the community over time as a result of the intervention. Furthermore, in service of the design process itself in the pre-construction phase, we can conduct cross-sectional studies using monitoring and modeling data to determine the relative impacts of different built-environment features and intervention typologies. Based on the goals of the designers and the scope of monitoring and modeling plans, we have established the following set of cross-sectional and longitudinal hypotheses.
### The cross-sectional hypotheses are:
1.  Landscape features will have an effect on thermal comfort parameters. Specifically the shade trees will reduce daytime radiant temperature, but also wind speed, resulting in a balancing act between the cooling effects of shade and the warming effects of wind velocity reduction. Additionally the thermal comfort will be impacted by various other surface materials, for example we hypothesize that radiant temperatures will follow an increase in proximity to grass \< cement \< asphalt.
2.  Landscape features will have an effect on air pollution. Specifically roadside lollipop trees will increase roadside air pollution concentrations by trapping traffic sourced emissions at pedestrian level. Buffer-shaped trees will increase concentrations on the traffic side, and reduce them on the other side.  
3.  The simulation results will be associated with the monitoring results. The simulation results will include wind speed and direction, as well as radiant temperature levels for each sensor location on specific dates at specific times, allowing the accuracy of the model to be tested.  
4.  Landscape features will have an effect on biodiversity; with bird, bat and insect populations being more diverse in areas with higher leaf area, more terrestrial-aquatic ecotones, and higher habitat patch connectivity. 
5.  Pedestrian behavior and perceptions will be associated with landscape features. Pedestrians will report more comfortable walking in areas with lower summer UTCI, which is mediated by landscape features according to hypothesis \#1 above. Where pedestrian routes show equivalent utility (for example given two paths that connect the same destinations with equal length) pedestrians will more frequently take the path with lower UTCI in the summer. 
### The longitudinal hypotheses are:
1.  The intervention will have measurable impacts on thermal comfort (**pending intervention design**). Before and after measurement of thermal comfort parameters will reveal that the intervention reduces extreme heat in the summer, and reduces extreme cold in the winter. 
2.  The intervention will have an impact on air pollution (**pending intervention design**), and while it is unlikely to be measurable using PM1, PM2.5 or PM10 as a proxy for traffic pollution, it may be detectable by measuring ultra-fine particulates and NO2, and possibly black carbon.
3.  The intervention will have measurable impacts on bird, bat and insect biodiversity (**pending intervention design**), with before and after measurements indicating an increase in biodiversity after the intervention, possibly with a lag period depending on how much construction of the intervention disrupts the existing ecosystem.
4.  The intervention will have a measurable impact on pedestrian activity and perceptions (**pending intervention design**). A larger percentage of pedestrians will report an enjoyable pedestrian experience, and a larger number of people will use pedestrian routes to traverse the district after the intervention vs before.
5.  The intervention will have a measurable impact on human health outcomes (**pending intervention design**). These may be physiological (for example cardiovascular disease, asthma, heat stress) or psychological (for example stress, anxiety, depression). 
### Quantitative methods 
 The cross sectional hypotheses are already being addressed in the pre-construction phase and are discussed in the results section. These studies will form the basis of the pre component of the pre-post longitudinal studies. The ongoing cross-sectional monitoring work is based on the roughly 30 temperature sensor locations being studied. These are yielding results into cross-sectional & longitudinal hypotheses \#1, that landscape features will impact the atmospheric variables related to thermal comfort, and cross-sectional hypothesis \#3, that simulation results will be correlated with measurements, although only in the case of thermal comfort related metrics, as no air-pollution monitoring has been commenced. In order to address the remaining hypotheses a second phase of monitoring is envisioned. This second phase will employ a larger number of thermal comfort sensors to improve statistical power enough to resolve the effects of trees on wind, and the effect of surface materials on radiant temperature, and the effect of building-sourced shade. The categorization of phase 2 thermal comfort sensor locations is shown in table 1. Unlike in phase 1, where only 4 of the 27 temperature sensor locations on the corridor also having a wind sensor, the sensors in phase 2 locations shown in table 1 will all have the principle low cost thermal suite (globe temperature, air temperature, humidity), while 3 locations in each of the 12 categories (36 total)  will also have wind speed / direction and light sensors. 
|  |  |  |  |  |
| :- | :- | :- | :- | :- |
|  | Shade of large tree | shade of small tree | sunny exposed | shade exposed (afternoon building shadow) |
| Over grass | 9 | 9 | 9 | 9 |
| over cement | 9 | 9 | 9 | 9 |
| over asphalt | 9 | 9 | 9 | 9 |
|  |  |  |  |  |
| total | 108 |  |  |  |

*Table 1. Thermal Comfort sensor location typology matrix*
In addition to the categorical variables shown in table 1, the viewshed of each sensor’s specific location will be analyzed immediately prior to installation using a 360 spherical camera and semantic segmentation to determine each sensor’s exposure to different surface materials. This will allow sky-exposure, grass-exposure, asphalt-exposure, cement-exposure, tree-exposure and dozens of other potential exposures to be quantified and used as continuous variables in the analysis of the sensor’s measurements with respect to built-environment features. These measurements may be used to determine which of the categorical variables apply to each sensor, as many locations are near both grass and pavement, and so ad hoc thresholds or unsupervised cluster analysis may be used on the viewshed data to help with location characterization.
To address cross-sectional hypothesis \#4 and longitudinal hypothesis \#3, 18 locations will have acoustic sensors with edge-computing capability to detect birdsong, bat calls and traffic / insect noise. These sensors will speciate birds and bats to quantify biodiversity within audible range of the sensors. These sensors will be placed in transects with respect to biodiversity hotspots and coldspots detected during a pre-deployment trial period, in which sensors will be deployed on a pilot basis and moved several times to find the optimum locations to monitor habitat corridors and habitat disruptors. While some of these sensors will be colocated with thermal comfort sensors, others may be uniquely focused on other biodiversity-pertinent locations which relate to connectivity metrics which will be calculated for the neighborhood. The connectivity metrics, such as probability of connectivity (PC), interaction flux (IF), and eigenvector centrality (EC) quantify the importance of the habitat patches for facilitating interaction across the habitat surface. A sub-hypothesis that habitat patches that have higher calculated connectivity have higher biodiversity can be tested, and the results use to improve calculations of the benefits of design decisions that impact connectivity. 
While bird and bat biodiversity, and total insect and traffic noise are key performance indicators of the intervention, the collection of this data will also allow research on the interaction between these variables to help understand the mediators between built-environment features and biodiversity. For example, while increasing total canopy coverage may provide direct habitable space for birds and bats, increasing pollinator gardens and diverse shrub and groundcover conditions might increase insect populations which may enhance bird and bat habitat by providing more food sources. 
In addition to the thermal comfort and biodiversity monitors, phase 2 will also include an air pollution monitoring campaign to address cross sectional and longitudinal  hypotheses \#2. An air monitoring cart will be walked through the pedestrian accessible areas of the corridor at regular intervals (6 runs per season, 3 during rush hour and 3 at night). The cart will carry measurement equipment for PM1, PM2.5 and PM10 mass (optical sensor), ultra-fine particulates (UFP) counts (condensation particle counter), black carbon (BC), NO, NO2, temperature, GPS coordinates, sound and video. Passive samplers will also be deployed throughout the neighborhoods to collect NO, NO2 and O3 and certain VOCs from 30 stationary sites. Point and line pollutant source predictors will be geographically represented with the air monitoring data and built-environment measurements to perform spatiotemporal modeling starting with land use regression (LUR) modeling. LUR is a predictive modeling approach that enables estimation of intra-urban air pollution spatial contrasts from air monitoring data gathered at a limited number of locations within the area (Hoek et. al 2008). The resulting LUR model can be associated with the outputs of the evidence-based design process to establish an impact of the design on air quality. 
To address cross-sectional hypothesis \#5 and longitudinal hypotheses \#4 & \#5, which relate to pedestrian usage, satisfaction and health, we will employ both quantitative measurements and qualitative assessments. Quantitative measurements will employ both pedestrian counting sensors, survey instruments and biomarkers. Pedestrian counting sensors will be used to determine cross-sectional impact of microclimate on usage patterns & longitudinal change in usage patterns due to changes in built-environment parameters. The pedestrian counting sensors will be placed at key locations on pedestrian paths, including the most common destinations (hospital entrances & exits, bus-stops, major pedestrian road-crosswalks) and paths between destinations. A total of 12 pedestrian sensors will be used for this purpose. 
Studies of the effects of the intervention on people will target both in-situ participants and prescriptive participants. In-situ participants are exposed to environmental parameters naturally as they go about their normal lives. Prescriptive participants are instructed by experimenters to go to particular locations at particular times to create a standardized exposure surface for study. In both cases we will employ a control condition, which can be both temporal and spatial. For example, in pre-post studies, the pre-intervention condition can serve as a temporal control. In both pre-post and cross-sectional studies we will also use spatial controls, where a group of in-situ participants who are not exposed to the intervention naturally can also be studied. Similarly in prescriptive studies, a group of participants can be sent to a placebo exposure site, or there can be a cross-over design where participants are measured after exposure to both an intervention site and a placebo site.
 Survey instruments will be used to quantify the human experience of working and living in the corridor cross-sectionally as well as before and after the intervention. Survey parameters will include long-term assessments of health, quality of life, and satisfaction with the environment, as well as short term metrics of mental health and cognition. Long-term parameters such as depression scales, and anxiety scales can be used both as direct measures of intervention or cross-sectional feature efficacy, as well as covariates for short-term metrics. Short term metrics can include both subjective responses to the circumstance via likert scales of mood, anxiety, depression etc., as well as indirect measures via psychometric tests, for example using cognitive reaction time or memory recall tests as a proxy for stress. These studies will be coordinated by academic project partners who specialize in each method.
Where participants are enrolled in in-situ or prescriptive study, we may also collect biomarkers and other clinical metrics to assess the physiological impacts of the intervention. This data may include patient health evaluations and biomarkers, for example blood pressure, arterial stiffness, circulating epithelial progenitor cells, cortisol, volatile organic compound metabolites, catecholamine metabolites, and microbiome diversity. For all participants we will address available covariates as potential confounders or mediators (and use them to establish synthetic controls), for example age, race, smoker/nonsmoker/never-smoker, alcohol drinking, socioeconomic status (income, parental occupation/education level, marital status) for both respondents and their geographic population unit median, body mass index, exercise frequency/duration/intensity (normalized to metabolic equivalents if possible) & sedentary behavior, self-reported social engagement duration/frequency, and estimated exposure to air pollution, thermal stress, and other built-environment parameters that are salient to the intervention (which, pending the final design, likely also include biodiversity, vegetation, traffic noise, wind, and shade). Pending development of sample sizes and power calculations, we plan on using difference in differences (DD) methods to quantify the impact of the interventions on longitudinal parameters. In the cross-sectional analysis we will use Generalized Linear Mixed Models (GLMM) to associate differences in built-environment parameters with health outcomes. 
### Qualitative studies
Qualitative assessments of thermo-spatial perception will be conducted  using learning circles and phenomenological interview series, cognitive mapping and sensewallking as reviewed by Lenzholder et al. (2018). Study participants will be drawn from populations that work and live in the district. Participants will be studied in situ, with researchers engaging in extensive relationship building to establish trust and comfort in communication with study participants. This qualitative research will be conducted by graduate students in medical anthropology at local universities, in partnership with a team of advisers in the field. 
### IRB approval
For all human subjects research (related to cross-sectional hypothesis \#5 and longitudinal hypotheses \#4 & \#5) an initial planning stage will be coordinated with all of the research partners involved in those experiments prior to any experimentation beginning. This planning process will result in sufficient information to produce the required human subjects documentation for the Institutional Review Board (IRB). When research is conducted by academic partners, then their institution’s IRB may be engaged. However, if University IRB’s present logistical challenges that are not compatible with overall project timelines, then we may use a commercial IRB. We have identified an independent, commercial firm that offers IRB services (WGC IRB) and will include contingency for their fees in human subjects research budgets as needed. 


# Proposal coordination

|  |  |
| :- | :- |
| **NSF Smart and Connected Communities** |  |
| **Deadline for preliminary proposal ** | **2/20/2025** |
| **Deadline for full proposal** | **4/4/2025** |
| **Total Funding Amount** | **$23,260,000** |
| **Total Projects funded** | **Development Grants: 10 to 20**    **Integrative Research Grants: 10 to 20**    **Large-Scale Research Grants: 1** |
| **Minimum amt per project ** | **$750,000** |
| **Grant length (months)** | **Set by applicant** |
| **Grant start date** | **Set by applicant** |
| **Purpose for Funding** | The purpose of the NSF Smart and Connected Communities (S\&CC) program solicitation is to accelerate the creation of novel intelligent technologies and concepts through high-risk/high-reward research that addresses major challenges and issues faced by communities across the US. A “smart and connected community” is defined as a community that synergistically integrates intelligent technologies with the natural and built environments and with the functions of civic institutions and organizations. Proposals submitted to the program should be designed to advance one or more of the following community priorities: economic opportunity and growth; safety and security; human and environmental health and wellness; accessibility of critical services and resources; and the overall quality of life for those who live, work, learn, or travel within the community. To meet the goals of the program, researchers should work with community stakeholders to identify and define challenges the community faces, using that interaction and input to generate high-impact, use-inspired, basic research that advances science and engineering.** ** |

|  |
| :- |
| Grant Guidelines:     [**RFP link**](https://nsf-gov-resources.nsf.gov/files/nsf25527.pdf?VersionId=AdRVQy4CNupILLRwMad4gbikIGo8LG_f)    [**Program description**](https://new.nsf.gov/funding/opportunities/scc-smart-connected-communities/nsf25-527/solicitation)    Other relevant documentation:    [**Dear Colleague Letter**](https://nsf-gov-resources.nsf.gov/files/nsf24_1.pdf?VersionId=ImnVCR.NDkOKTGKuDHHmterZQY3cXEDn) (w/ full proposal guidelines)   |
| [**Webinar**](https://players.brightcove.net/679256133001/NkgrDczuol_default/index.html?videoId=6367894973112)** ** |
| **MEETING NOTES (If any): ** |
| **PORTAL FOR APP: **    [**www.research.gov**](http://www.research.gov) |

[Email Follow-Up (2/11/2025)](?tab=t.0#heading=h.f75txkhqhlta)
[AD @ TAMU to Team](?tab=t.0#heading=h.d3nhkqzdbpq1)
[MP @ Hyphae to Team Response](?tab=t.0#heading=h.4b4g0fsres8a)
[Feb 11, 2025 | Andrew Dessler (TAMU) x Hyphae re: NSF](?tab=t.0#heading=h.xcszpd4dbcgy)
[Summary of meeting:](?tab=t.0#heading=h.9h5nvjotqnz5)
[Notes from meeting](?tab=t.0#heading=h.w13jbfkpjiuq)
[NSF S\&CC Webinar Takeways](?tab=t.0#heading=h.v2flzwvayvv)
[Tues Feb 11, 2025](?tab=t.0#heading=h.ueosnlxjkshj)
[Jan 24, 2025 | Hyphae x TAMU NSF Extreme Heat](?tab=t.0#heading=h.ddm1sa1tdjtn)
[DF-MP Post-meeting discussion](?tab=t.0#heading=h.g8621u6f9lzm)
[Follow up email (sent 2/4/25)](?tab=t.0#heading=h.pjeu1hpjoy7o)
[NSF Office Hours (1/22/25)](?tab=t.0#heading=h.5uunp27iuuwy)
[NSF Smart and Connected Communities (S\&CC) webinar (1/24/25)](?tab=t.0#heading=h.eckalj1z6gsv)
In total the documents that are still needed are the following:
1\) Budget in RR format (sent from Savannah Steffen)
2\) Budget justification (see attached template)
3\) <comment_start id=kix.ydh5kng483w3>Scope of work<comment_end id=kix.ydh5kng483w3>
4\) IDC rate agreement
5\) Signed subrecipient form (Savannah Steffen has copies of this form)
6\) Personnel documents for all key personnel (biosketch, current/pending (will require total budget from this proposal), COA, synergistic activities) – Karen Thum can assist with these as needed
7\) Facilities, Equipment, Other Resources (see attached template)
## Mar 19, 2025 | [BB-MP-Stephanie (HARC)](https://www.google.com/calendar/event?eid=NDFxZDlkcHMyOWp1ZzlucjhyZjIwczA5cGwgbWF4QGh5cGhhZS5uZXQ)
Attendees: [Stephanie Piper](mailto:spiper@harcresearch.org) [Brent Bucknum](mailto:brent@hyphae.net) [Maxwell Pingeon](mailto:max@hyphae.net)
Agenda:
  - BB and SP share notes on potential Houston contacts 
  - Expand on list below: idea is to dovetail our proposed research with an existing project  
  - ~~Develop a target site and CBO to be the point of contact for the grant~~
      - ~~I.e. to demonstrate communities have decision-making power  ~~
  - Examine how much of HARC budget can go to paying the community  
**Revisiting the Project Approach and Integration with Existing Work**
  - MP recapped the last internal discussion: instead of pitching a new implementation project, the team will dovetail research with an existing project. SP confirmed her alignment with this approach.
  - SP mentioned a Metro conversation—Metro is overwhelmed with bus stop designs and not seeking more, which aligns serendipitously with project direction.
-----
**Identifying Project Contacts, Target Sites, and Community Decision-Making**
  - MP suggested gathering contacts, expanding the project list, and identifying a target site/CBO to demonstrate community decision-making in the narrative and explore how HARC’s budget could support this.
  - BB agreed but warned against overly leaning on a single community group given the late stage of the process. Instead, suggested letters from a few groups would strengthen the proposal.
  - BB raised the question of focusing on greening interventions, bus stops, or both. He cited research showing perceived wait times at bus stops reduced when trees, rather than structures, were present.
  - SP confirmed widespread interest in shade structures and the importance of parsing community preferences between trees and other cooling interventions. She noted communities might prefer non-tree solutions.
-----
**IV. Potential Collaborators, Letters of Collaboration, and Community Groups**
  - SP listed outreach done for letters of collaboration:
      - **Super Neighborhood** (Gulfton and A-Leaf) – pending response.
      - **Alief Votes** – willing to sign.
      - **Metro** – hard to nail down.
      - **SWA Group** – interested due to heat internships.
      - **Precinct 4** – active in tree planting and heat mitigation.
      - **Texas Forest Service** – involved in plantings.
  - SP clarified Alief leadership is in transition; past president Barbara Quatro, "the tree queen of Alief," is in hospice.
  - Nature Conservancy’s past involvement noted. Jaime Gonzalez is now with SCA (Student Conservation Association). SP connected with him on other projects.
-----
**Discussion of Precinct 4’s Role, Tree Planting Strategy, and Funding Approach**
  - SP confirmed that Precinct 4 planners are involved due to their "Healthy Parks Plan" and investment in increasing green space.
      - <https://cp4.harriscountytx.gov/healthy-parks#:~:text=As%20part%20of%20the%20Healthy,park%20access>
  - BB suggested possibly keeping a planting budget in scope, even if small, for flexibility. 
      - The tricky negotiation we often face is the choice to plant young trees that take a long time to grow vs planting fully grown trees that are expensive to install, e.g. Louisville project that spent $9M on tree planting.
  - SP described HARC’s $20K/year budget line for a community group/intervention. Cited Alief planting 350 trees for $25K due to local connections and reduced water truck costs.
  - BB referenced the "Alief Linear Forest" led by Barbara Quatro, aiming to replace grass esplanades with trees.
-----
**VI. Data and Prioritization for Planting**
  - BB questioned whether the grant should fund prioritization since urban forest master plans are typically too crude (census-level).
  - SP cited the Healthy Parks plan but was unsure if detailed planting prioritization exists.
  - BB described a "cool corridors" project in Dallas focusing on safe routes to schools and targeting hottest areas.
  - SP noted most vegetation maps, including the tree portal, are census-tract level. DOT has planted everywhere allowed; Harris County Flood Control focuses on riparian areas.
-----
**VII. SWA Heat Internship and "Cool Loop" Concept**
  - SP explained SWA’s "cool loop" idea modeled on Houston’s inner/outer freeway loops, and Downtown Houston’s underground tunnels. Downtown Houston Plus is working to revamp downtown with similar design concepts.
-----
**VIII. Demographic Considerations, Outreach Models, and Super Neighborhoods**
  - BB raised the "promotoras" model and the importance of understanding community demographics.
  - SP described the Gulfton Super Neighborhood as majority Hispanic; Alief is “slightly different.” Outreach funding could support tree planting or workshops.
  - Gulfton’s Super Neighborhood acts like a neighborhood council but varies in activity levels citywide.
-----
**IX. Nature Conservancy’s Role and Shifts in Focus**
  - BB noted potential Nature Conservancy (NC) retreat from urban work, citing Dallas dynamics and donor-driven shifts. SP observed NC’s reduced presence in Houston.
  - BB mentioned the firm "Tecolotl" from the Greener Gulfton report, focusing on multilingual capacity building and community planning. SP had not worked with them but recognized leadership.
      - <https://www.tecolotl.org/team>
-----
**X. Additional Groups and Institutional Partners**
  - <comment_start id=kix.xu1d9gzerkt1>SP and BB listed other key groups:
      - **TEPRI (Texas Energy Poverty Research Institute)** – SP collaborates with them.
          - Little overlap with project goals
      - **Trees for Houston** – active planting group.
          - Connected with Texas Forest Service
      - **Texas Forest Service** – supports small plantings.
          - Sent us LOC\!
      - **Texas by Nature** (Laura Bush funded).
          - SP does not have a contact
      - **Texas Children in Nature** – Austin-based.<comment_end id=kix.xu1d9gzerkt1>
          - SP does not have a contact, just on their mailing list
-----
**XI. Mapping, Data Layers, and Technical Planning**
  - Discussion shifted to defining scale and developing a compiled map.
  - BB emphasized aligning health data with heat sensing, LiDAR, and identifying diverse urban morphology (local climate zones - LCZs).
  - SP agreed and will share snapshot heat data (done following the CAPA model).
      - [<comment_start id=kix.hydl4bqq3bdh>https://www.forustreehtx.org/search?groupIds=5737b46445c14cecbdabc6a123bb3e6b](https://www.forustreehtx.org/search?groupIds=5737b46445c14cecbdabc6a123bb3e6b)<comment_end id=kix.hydl4bqq3bdh>
  - BB suggested integrating higher-resolution tree canopy data from Fletch/DF and other sources like PlanITGeo and aerial LiDAR.
  - SP clarified HARC’s data is limited but awaiting new Landsat data.
  - BB mentioned having a contact at Precinct 4: Luis Guajardo, Director of Planning, who responded positively to SP’s invite.
-----
**XII. Tree Planting Locations and Control**
  - BB inquired about control over where trees are planted.
  - SP explained:
      - Depends on the planting group—flood control is limited to riparian areas.
      - Some giveaways depend on recipients (American Youth Works crews).
      - HARC tracks trees on the forestry portal and city/county plotters.
-----
**XIII. Air Quality Considerations and Future Collaboration**
  - BB raised air quality as a possible addition for future funding; SP noted it is an issue; MP added that for this project, we did not budget for air sensors.
  - SP has expertise (dissertation chapter) on air quality and trees.
  - BB discussed his work in Louisville planting green belts as vegetative buffers along freeways and suggested future collaboration.
  - Both agreed a follow-up session on air quality could be productive.
-----
**XIV. Closing and Next Steps**
  - BB mentioned presenting at Rice’s Nature and Health Conference; 
      - SP invited him to visit HARC’s net-zero building in the Woodlands.
  - MP summarized next steps:
      - <comment_start id=kix.1z866e5mugdo>Compile the mapping layers.
      - Overlay data to narrow down a potential corridor.
      - Focus the narrative on demonstrating statistical impact.
  - BB offered to share national datasets (CO2, PM models, warehouse proximity to schools) and explore collaborative opportunities on child health and the built environment.<comment_end id=kix.1z866e5mugdo>
  - SP expressed interest, mentioning related conversations about schools and health.
-----
**II. Action Items & Responsibilities**
- [ ] Finalize and send drafted letters of collaboration, ensuring specificity per NSF guidelines (i.e. NSF preference that LoC reflect their specific role and expertise in the project, not a boiler-plate letter) – <comment_start id=kix.rz8nzkpttskd>Stephanie Piper<comment_end id=kix.rz8nzkpttskd>
- [ ] Reconnect with Gulfton Super Neighborhood and Luis Guajardo at Precinct 4 – <comment_start id=kix.vbawu4kx0gly>Stephanie Piper<comment_end id=kix.vbawu4kx0gly>
- [ ] Overlay local climate zones and snapshot heat data to create a compiled map – DF
- [ ] For same mapping task, gather high-resolution tree canopy data and explore integrating LiDAR – DF
- [ ] Determine potential corridor location for statistical impact demonstration in the narrative 
- [ ] Share national datasets (CO2 emissions, PM models, schools, warehouses) for possible integration 
- [x] Locate and confirm access to City of Houston Tree Plotter data – <comment_start id=kix.pc7e1nja0rg2>Stephanie Piper<comment_end id=kix.pc7e1nja0rg2>
  - [ ] <https://pg-cloud.com/HoustonTX/> 
## Mar 13, 2025 | [\[moveable\] IH-MP NSF budget ](https://www.google.com/calendar/event?eid=M20ybm5tNmZmN3RvZGVncXR1c2YwbWlzMTcgbWF4QGh5cGhhZS5uZXQ)
Attendees: [Ivan Heitmann](mailto:ivan@hyphae.net) [Maxwell Pingeon](mailto:max@hyphae.net)
Notes
Convo re: applicability or need for CFD in cases where we are looking at an urban scale and the environmental risk of interest is heat and \*not\* air quality.
<comment_start id=kix.53nz1nlv955b>IH<comment_end id=kix.53nz1nlv955b>: my opinion that CFD should not be assumed part of our standard offering.
  - Bec too much area for us to realistically do 
  - So we would have to choose sample spots 
  - That windfield then fed into a different model to get thermal info 
  - You can get a windfield that’s coming out of meteorological models rather than CFD 
  - CFD just gets you a better resolved windfield rather than thermal analysis  
  - ^^ better to use this money for health data correlation   
Feasibility of large area analysis
  - Man hours vs compute 
  - In theory, w/ enough compute it’s possible 
      - Compute costs scale with area
      - Qu of how much of your budget you want to spend on compute   
Political boundaries discussion
  - Option instead of relying on political boundaries 
      - Pull NASA data to draw a boundary based on heat severity (that transcends political boundaries)
  - Empirical question:
      - What is the extent of the LIDAR dataset that we would use?
          - Entire metropolitan area or just city limits, county limits?
      - Might be worth extra effort to follow the heat maps instead of the political maps
Action items
- [ ] 
## Mar 14, 2025 | [BB-MP-DF NSF TAMU budget and scope discussion](https://www.google.com/calendar/event?eid=M3M2ZnJkMmM0dXJzaWNrdWdoM2YxNmE0a3YgbWF4QGh5cGhhZS5uZXQ)
Attendees: [Brent Bucknum](mailto:brent@hyphae.net) [Daniel Fleischer](mailto:fletch@hyphae.net) [Maxwell Pingeon](mailto:max@hyphae.net)
Notes
  - Cost-benefit analysis of a low margin project
  - Potential BB contacts:
      - Gulfton Neighborhood (“Greener Gulfton” project)
          - Also funded by Nature Conservancy 
          - In collaboration with Asakura Robinson
              - <https://asakurarobinson.com/projects/greener-gulfton/> 
          - Ultra Barrio has ongoing projects
              - <https://www.ultrabarrio.com/greener-gulfton-shade-structures>
              - <https://www.houstonpublicmedia.org/articles/news/health-science/2023/07/20/457262/gulfton-is-the-hottest-neighborhood-in-houston-whats-being-done-about-it/> 
              - Marcus Martinez BB contact
              -  
  - Need 30% of community engagement needs to go to CBO liaisons 
      - Houston Land Trust  
  - Do we book a session with BB to enhance CBO profile 
  - Do we have the Metro connections to do a bus stop?
      - DF: Not the scope accounts for finding those connections and facilitating 
  - Question of piggy-backing on other ongoing interventions that we can monitor vs building something ourselves 
      - Could be bus stop, corridor planting, or even a cool roof project
      - Leave it open so that we don;t have to have an agreement in place with a city agency 
      - BB: But then how to budget for it in the scope if not defined 
      - DF: the community design process will have to work with the not-to-exceed x amount of budget    
  - BB: put a bunch of money to gear (gear?)
      - DF: want to add people counters
  - BB: what are we doing vs Andrew
      - DF: health analysis 
      - BB: can we uncover more of the detail re: health information, and targeting the information around that?
      - DF: trying to avoid project getting foisted onto NIH, tf not looking at people
          - AD looking at hospitals and neighborhood-level 
      - BB: then whats the intervention
      - DF:
          - We reduce temp by this amount \_\_\_\_
      - BB: why do interventions, not just put out more sensors and say if/then re: effects 
      - DF: the solicitation calls for robust community engagement
          - Would have to shift to more sensor-driven approach
      - BB: value-to-impact of $ spent 
          - We’re going to sample data in broad range of typologies 
          - Integrate this where people are already doing community-driven greening 
      - DF
          - We did try that w/ NIH grant 
          - “If you’re not in control of those projects, you’re not doing science”
              - Need to control the variables 
              - Not a controlled experience     
      - BB
          - Calibrate the instrument 
          - It is interventional bec working on ongoing projects 
              - Validating the people’s take on what’s actually going in these projects 
              - Enriched dataset and validation of what they’re doing 
      - DF
          - SP approach would be amenable to that 
          - But needs a list of ongoing projects that we can study 
              - Whatever is happening over next few years     
      - Return to orally drafted email draft in transcript
          - Using Greening Gulfton as an example 
          - The Land Bank should have ongoing projects 
          - Dovetail an intervention: link up SP and BB to share notes 
Action items
- [x] Find a list of ongoing projects that we can study 
- [x] Schedule a meeting between BB and SP 
- [x] Find out more detail on available health data  
## Mar 14, 2025 | [MP-ED NSF Budget convo ](https://www.google.com/calendar/event?eid=MDBwM2p2YmpwNGVvZXBlb2cyb2ZwNDgwdDIgbWF4QGh5cGhhZS5uZXQ)
Attendees: [Eric Dorfman](mailto:ericd@hyphae.net) [Maxwell Pingeon](mailto:max@hyphae.net)
Attached files: [Hyphae\_AdaptOS\_Platform\_Budgets](https://docs.google.com/spreadsheets/d/1szR85wo6CH5BNqR7lDKAp7_LP588OXMeIw100GfTgr4/edit?disco=AAABe65V2R4) 
Notes
  - 
Action items
- [ ] 
1.  Need to know what our current NSF overhead rate calculation 
2.  If we are obligated to use it
3.  And if the alternative is to our advantage:
    1.  Alternative a: the de minimis 10% of total    
From PAPPG, re: indirect cost billing rates  
 
“NSF does not negotiate rates for organizations that are not direct recipients of NSF funding (e.g., subrecipients). Consistent with 2 CFR § 200.332, NSF recipients must use the domestic subrecipient’s applicable U.S. Federally negotiated indirect cost rate(s). If no such rate exists, the NSF recipient must determine the appropriate rate in collaboration with the subrecipient. The appropriate rate will be: a negotiated rate between the NSF recipient and the subrecipient; a prior rate negotiated between a different pass-through entity and the same subrecipient, or the de minimis indirect cost recovery rate of 10% of modified total direct costs.” 
## Mar 12, 2025 | [\[moveable\] Quick check-in about TAMU and WPF budgets](https://www.google.com/calendar/event?eid=M203cWc0ajc3bzVidDJiN2FhcDgzc290aW0gbWF4QGh5cGhhZS5uZXQ)
Attendees: [Daniel Fleischer](mailto:fletch@hyphae.net) [Maxwell Pingeon](mailto:max@hyphae.net)
Notes
  - If you take the total labor cost, and then divide by half, that’s all you can charge.
  - Not good, but better than 10%
  - Negotiated rate is a long process that we don’t have time for  
  - <comment_start id=kix.2a9cot8ge5t>Questions for Eric<comment_end id=kix.2a9cot8ge5t>:
      - Since we are using a 50% labor cost for SBIR, does that constitute an already negotiated federal govt rate that we can use in this grant application?
          - See section on budgets for subawards (p. II-19) in PAPPG <https://nsf-gov-resources.nsf.gov/files/nsf24_1.pdf?VersionId=ImnVCR.NDkOKTGKuDHHmterZQY3cXEDn>  
      - When they say in PAPPG 10% of “modified total direct cost,” what are they referring to?
          - If it includes a bunch of costs besides direct labor costs, then does that allow us to include health insurance and rent e.g. or R\&D overhead? 
          - Need to know which is a better deal: our 50% labor costs or the 10% modified labor costs that is standardized in the PAPPG. 
  - If it is 50%, then I need to get the SBIR rates from Eric?
      - No, says DF
      - Just get the actual pay rates from Eric 
      - Then add 50% in indirect 
      - Revisit the Fresno scope 
  - Assumptions and scope 
      - Lorwan (6)
      - Heat (30)
      - Wind (9)
          - Scale?
              - Same sensor amount as for Dallas
              - INcrease installation costs (over a wider area, closer to $100k in labor)
              - PM 
                  - Design charrettes  
                  - 1 PM
                  - IH, JPG, JH involved
Action items
- [x] Ping ED re: PPAPG guidelines 
 
## Mar 7, 2025 | [NSF SCC proposal meeting](https://www.google.com/calendar/event?eid=MTUyMGllbjdwMHRjaGZlZ28xbTJwcWs2dHYgbWF4QGh5cGhhZS5uZXQ)
Attendees: [Daniel Fleischer](mailto:fletch@hyphae.net) [Stephanie Piper](mailto:spiper@harcresearch.org) [Andrew Dessler](mailto:adessler@tamu.edu) [Brent Bucknum](mailto:brent@hyphae.net) [Maxwell Pingeon](mailto:max@hyphae.net) [](mailto:karenthum@tamu.edu)
*Agenda*
  - Assess proposal lift
  - Assign sections to team members
  - Assess how many meetings we need to schedule to complete proposal on time 
  - Schedule meetings 
  - Determine asynchronous workflow for working in the document 
*Notes*
  - Budget discussion 
      - Total grant: $1.5M for entire period (not $1.5M per year as initially thought)
      - Breaks down to \~$500k/year for 3 years
      - A\&M overhead rate: 52.5-54%
      - Rough budget allocation discussed:
          - A\&M portion (\~$100k/year): 1 month PI salary + 1 grad student
          - HARC portion (\~$100k/year): Stephanie + potential support staff
          - Remaining funds (\~$300k/year) for Hyphae analysis/implementation
      - CBO budget unknown…
  - Technical Scope
  - Hyphae team to lead:
      - Solar radiation modeling to get the MRT simulated for whole city 
      - Install MRT sensor network to validate simulation and provide direct measurement of landscape features 
      - Track interaction of shade trees, wind, land cover 
          - Design interventions
              - Hypothetical scenarios (1-3 bus stops?)
                  - Vetted and produced with community help
                  - Fed back into model to estimate impact 
              - Ideally build one and do pre- and post- monitoring 
                  - Show the iterative process and reliable transferability 
          - One way to demonstrate high reward is providing reliable, scaleable, replicable costing for such projects 
              - Reliable tree planting costs do not exist, SP says, for instance, and are in high demand 
                  - Possibly explore 3D printing for scalable solutions
  - Community Engagement 
      - Stephanie (Hark) recommended focus on Precinct 4 in Houston:
          - High heat neighborhoods
          - Active community groups
          - Existing tree planting initiatives
      - Community participation components:
          - Annual community meetings (w/ more scheduled in final year)
          - Participant support costs (gift cards, food)
              - Explore budget options for paying a CBO point-person
          - Development of public-facing materials
          - Iterative community feedback on analysis
  - Outstanding scope questions
      - How much can Hyphae get done for $300k/year?
      - How much can we pay CBOs?
      - Which CBOs would be willing to participate and provide letters?
      - What is our target location?
      - What scale is the area we are trying to map?
      - Can we get maps to start to develop the concept? 
      - Equipment and compute costs  
  - High-risk, high-reward nature of project still undefined.
  - Writing:
      - Err on more rather than less: easier to cut than to add  
  - Cast of Characters 
      - <comment_start id=kix.xbs1knsxpn5w>Precinct 4: high-heat neighborhoods 
          - SW Houston
          - Superneighborhoods  
      - Abundant CBOs actively tree planting<comment_end id=kix.xbs1knsxpn5w> 
  - 4-wk timeline 
      - Need to be submitted to TAMU SRS by March 31st (gives them 5 days buffer)
      - Send reasonable drafts in a week (Fri 3/14)
          - Intellectually complete if still pieces missing 
      - AD can then massage pieces into coherent piece (3/21-3/31) 
*Points of emphasis from solicitation*
**Granularity and Novelty**: Highlight the innovative aspect of the work.
**Interdisciplinary Integration**: Clearly articulate the integrated
methodologies involving Geosciences (heat mapping, climate modeling),
Engineering (green infrastructure), Computer & Information Science
(machine learning, geospatial analytics), and Social & Behavioral
Sciences (community engagement, public health impacts).
**Community-led Intervention**: Emphasize the active and meaningful
participation of local community stakeholders in co-designing and
implementing pilot interventions, showing that community input is
integral, not peripheral, to your research.
**Evaluation Methodology**: Detail your robust evaluation plan that
leverages high-resolution data and health outcome comparisons to
rigorously measure intervention impacts pre- and post-implementation.
**Scalability and Replicability**: Underline the generalizability and
replicability of your approach for broader application beyond Houston,
emphasizing potential nationwide impact and policy implications.
**Broader Impacts**: Clearly articulate impacts on public health,
community resilience, climate adaptation policy, STEM education, and
workforce development to demonstrate extensive societal value and
NSF's mission alignment.
*Action items*
- [ ] TAMU Budget
- [ ] HARC Budget
- [ ] Hyphae Budget   
- [ ] CBO Budget 
- [ ] SRS TAMU Paperwork 
- [ ] Assign writing tasks
  - [ ] AD: Intro 
  - [ ] SP: 2-3 pp community engagement, broader impacts  
  - [ ] DF-MP: technical analysis/implementation plan
  - [ ] MP: assist with community engagement, broader impacts
  - [ ] KT: assist with gathering materials 
  - [ ] KT question: Letters of Collaboration required for subawardees?  
  - [ ] SP: identify CBOs
- [ ] CVs
- [ ] Spreadsheet of collaborators
- [ ] Synergistic activities (all in special format - on a web page that’s formatted into PDF)
- [x] Get a map of target from [Stephanie Piper](mailto:spiper@harcresearch.org)
  - [ ] [<comment_start id=kix.8954747eig1p>https://cp4.harriscountytx.gov/Portals/cp4/hcp4/Explore/Maps/Super%20Neighborhoods%20Map.pdf?ver=88pQeaH2vSd6wBiz3-lUmw%3d%3d](https://cp4.harriscountytx.gov/Portals/cp4/hcp4/Explore/Maps/Super%20Neighborhoods%20Map.pdf?ver=88pQeaH2vSd6wBiz3-lUmw%3d%3d) <comment_end id=kix.8954747eig1p>
Additional Precinct 4 context
  - Range of socioeconomic data 
  - Superneighborhoods include: Addick Park Ten, Afton Oaks/River Oaks Area, Alief, Braeburn, Brays Oaks, Briar Forest, Eldridge/West Oaks, Fairbanks/Northwest Crossing, Greater Uptown, Greenway/Upper Kirby, Gulfton, Langwood, Lazybrook Timbergrove, Memorial, Meyerland, Mid-West, Sharpstown, Spring Branch Central, Spring Branch East, Spring Branch North, Spring Branch West, Washington Ave Coalition/ Memorial Park, Westbury, Westchase, Westwood 
  - Alief, Gulfton, Sharpstown, Spring Branch all came out as hot spots in 2024 heat mapping 
  - River Oaks – neighborhood where Ted Cruz lives 
  - Greenway/Upper Kirby, Memorial, Meyerland also richer
## Email Follow-Up (2/11/2025)
### AD @ TAMU to Team
 
Hi Stephanie (cc Max): I wanted to summarize the next steps from our
recent meeting to ensure we're all aligned:
1\. Draft Proposal: Max et al. will work on drafting the two-page
project summary. They aim to have a draft with placeholders ready by
Thursday or Friday. We will then iterate and refine it.
2\. Stakeholder Contacts: You and I will start compiling a list of
potential stakeholders in Houston. We'll need verbal or email
confirmations from them to include their names on the proposal's last
page.  Can you start asking your contacts in Houston (e.g., Metro,
neighborhood groups) if they are willing to be involved.  I don't
think we need anything other than an email saying they're willing to
do it at this point.  We should aim to finalize the list by early next
week.
Please let me know if there's anything you'd like to add or adjust.
Looking forward to collaborating on this.
Andy
### MP @ Hyphae to Team Response
Thanks Andy for putting this together. And thank you Stephanie for joining us\!
 
[I added some detail from the webinar in the google doc](https://docs.google.com/document/d/1fidMYELx1bhy6ZvJsDjJoaXze6HNRQrcZMNpjgo30jA/edit?disco=AAABdpj48EM) that answers some of our questions from this morning such as the budget range of the middle tier ($1.5M for up to 4 years). I’ve also included the meeting minutes and [summary](https://docs.google.com/document/d/1fidMYELx1bhy6ZvJsDjJoaXze6HNRQrcZMNpjgo30jA/edit?disco=AAABdpj48Xc).  
 
Stephanie, to recap, here are the action items we discussed in the meeting: 
1.  Let us know if HARC is still able to submit as lead, that you are willing to serve as PI on the project (with Andy as co-PI and Hyphae as a sub-award).  
2.  Is there someone else in the HARC community resilience and sustainability team whom we should include that could complement the urban greening interventions with social science analysis? (Social science is not required in the solicitation but it is one of the overlapping disciplines and would strengthen the proposal I think.) We had flagged your colleague Jennifer Irving as a potential add to the team for instance.
3.  Re: the potential stakeholders to contact, we had discussed:
    1.  CBOs in Houston, the Gulfton super superneighborhood association (sp?) for instance 
    2.  Transportation authorities  
    3.  County and Municipal authorities (we could propose to contrast our proposed analysis with the 2019-2024 Norris County heat study)
    4.  Harris County Public Health officials
    5.  Tree-focused non-profits
    6.  The Texas Forest Service, headquartered at TAMU   
 
Looking forward to carrying over this over the finish line with you all\! 
 
Since it’s due on the 20th, we should submit on the 19th given that the proposal needs to be submitted on Research.gov and we don’t want to risk getting snarled up in any last-minute technical difficulties with the platform.    
 
Next week, we have openings Tuesday (2/18) from 2:30 to 4:30 PM CT if we want to have a final check-in for submitting. If you propose an alternate time, we can likely accommodate. Just a head’s up that I will be out of office Monday February 17.  
 
More soon, all the best, 
 
Max 
 
 
## Feb 11, 2025 | <comment_start id=kix.ug3mn0nznlr9>[Andrew Dessler (TAMU) x Hyphae re: NSF ](https://www.google.com/calendar/event?eid=N3JhN2VraTY4b2xjY2hsNTIwczh2ZTR0dGkgbWF4QGh5cGhhZS5uZXQ)<comment_end id=kix.ug3mn0nznlr9>
Attendees: [Daniel Fleischer](mailto:fletch@hyphae.net) [Andrew Dessler](mailto:adessler@tamu.edu) [Brent Bucknum](mailto:brent@hyphae.net) [Maxwell Pingeon](mailto:max@hyphae.net) <spiper@harcresearch.org>
### Summary of meeting:
After discussion, we landed on submitting for a middle tier Integrative Research Grant (IRG) proposing to do a heat study for the city of Houston that culminates in a green infrastructure pilot project. Options include greening a bus stop or a set of bus stops for instance, and doing pre- and post- monitoring analysis to assess its efficacy, and thus providing a replicable framework to comprehensively green the city transportation network in future rounds of funding. <comment_start id=kix.dmvnicgrm9uo>The high-risk, high-reward nature of the project is that such a city-wide heat plan has never been attempted at neighborhood scale<comment_end id=kix.dmvnicgrm9uo>, i.e. correlating extreme heat at the level of individual addresses with public health data such as emergency room visits and ambulatory care. The idea is that the current state of the art (which S\&CC program is trying to supersede) correlates extreme heat to census tract level analysis only. These measurements cannot provide an accurate sense of how extreme heat impacts human health from block to block. Our analysis could be used to contrast the recently completed Norris County heat study (2019-2024) which is done at census-tract scale (<comment_start id=kix.3zyqit4ymlnq>confirm<comment_end id=kix.3zyqit4ymlnq>) with our own more detailed analysis. It would be community-led from start to finish with HARC facilitating, potentially involving a team member with an MPH or related degree to ground the results in mature social science analysis. 
Our proposal would also fulfill NSF guidelines to combine “2 or more” disciplines identified in the solicitation. These are: 
47.041 --- Engineering
47.050 --- Geosciences
47.070 --- Computer and Information Science and Engineering
47.075 --- Social Behavioral and Economic Sciences
47.076 --- STEM Education 
To demonstrate “robust community engagement,” we should underscore how the community is guiding the research and implementation trajectory to meet community needs, and is equipped to use the research and design interventions after the lifecycle of the grant has elapsed.
Feel free to add as needed. We can use this material in the Project Summary when the time comes.            
### Notes from meeting 
  - Question of scale 
  - Question of tier: 1-3
  - Question of purpose:
      - Analysis towards design strategies
      - Community-led 
      - Of benefit to the community 
  - Need a coalition of stakeholders to begin with 
      - Grassroots organizations benefit 
      - They direct what they need 
      - Give them the tools they need 
  - Stakeholders
      - Have contacts in each city 
      - Austin, San Antonio 
      - Stephanie knows CBOs in Houston
      - HARC about to release heat mapping data in Houston 
          - One of those neighborhoods in particular 
          - Stephanie’s program gave temperature sensors to individuals to drive around Houston
              - Goes back to the sensors of buses project
              - High resolution measurements along bus routes 
              - Potential cooling interventions at bus stops 
              - At “Metro” for instance, they are already collecting data 
  - Lot of data out there 
      - EV may be already logging temperature 
      - What are the unexpected sources of data 
      - Companies from smart cars may be a useful addition to complement the existing data     
  - Norris County heat study 
      - 2019-2024 study 
  - CBOs in Houston, Gulfton super superneighborhood association (sp?) for instance
  - Transportation authorities  
  - County and Municipal authorities (we could propose to contrast our proposed analysis with the 2019-2024 Norris County heat study)
  - Harris County Public Health officials
  - Tree-focused non-profits
  - The Texas Forest Service, headquartered at TAMU       
  - Greening a bus stop or two 
  - Pre- and post- monitoring 
Action items
- [ ] Pick the middle tier: place the story in Houston 
- [ ] Identify CBOs
- [ ] Gulfton superneighborhood 
- [ ] Norris County public health  
- [ ] Get email OKs from people: no letters needed 
- [ ] What is the scope and the target budget? 
- [ ] Reach out to Stephanie and catch her up on end of meeting: confirm her role as lead
- [ ] Andrew and Stephanie will gather a list of names for potential stakeholders
- [ ] Ask if Jennifer Irving, MPH or other social science person at HARC can boost the cast of characters
- [ ] Or Rose Jones, our medical anthropologist from Dallas (https://www.linkedin.com/in/rosecjones/)
Links
<https://publichealth.harriscountytx.gov/Portals/hcph/Documents/Reports/REPORT_Heat-2024-FINAL.pdf> 
## NSF S\&CC Webinar Takeways
## Tues Feb 11, 2025
  - S\&CC solicitation no longer focused, as in previous iterations, on interaction of social and technical science, what it formerly called "sociotechnical research.”
      - More expansive now:
          - It now simply blends 2 or more disciplines relevant to the primary funders of the program: 
              - E.g. AI/ML + Civil Engineering “would be acceptable” to the new NSF funder which is the Directorate of Geosciences 
  - Tiers
      - Lower tier = Development Grants (formerly Planning Grants) 
          - 1 year ($150k)
          - Award between 20 and 30
      - <comment_start id=kix.6po1ucp6rtsl>Middle Tier = Integrative Research Grants (IRGs)
          - Up to 4 years for max budget of $1.5M
          - Estimating awarding between 8 and 12 awards per fiscal year <comment_end id=kix.6po1ucp6rtsl>
      - Upper tier = Large-Scale Research 
          - Up to 5 years (up to $5M)
          - 1 - 2 awards 
  - Note that “areas of interest” identified in webinar vary slightly from the language of the solicitation.
      - Solicitation identifies relevant overlapping disciplines as:
          - 47.041 --- Engineering
          - 47.050 --- Geosciences
          - 47.070 --- Computer and Information Science and Engineering
          - 47.075 --- Social Behavioral and Economic Sciences
          - 47.076 --- STEM Education
      - Webinar identifies 
          - Computer and Information Sciences   
          - Civil and Mechanical Engineering
          - Geosciences 
          - Social, Learning, and Behavioral Sciences
      - I will follow up with Barbara Ransom to clarify 
  - Note the Full Proposal Components (might be good to signal that we are thinking about these things in the pre-proposal)
\[image\]
## Jan 24, 2025 | [Hyphae x TAMU NSF Extreme Heat](https://www.google.com/calendar/event?eid=M2VzZGNmYmg3cmtlYjF1bzQyOTFxNXZnOTQgbWF4QGh5cGhhZS5uZXQ)
Attendees: [Daniel Fleischer](mailto:fletch@hyphae.net) [Andrew Dessler](mailto:adessler@tamu.edu) [Maxwell Pingeon](mailto:max@hyphae.net)
Notes
  - MP Intro:
      - Grew out of West Oakland EJ struggle
      - Work with communities in Richmond, Marin City, Boyle Heights, Stockton, and the wider Central Valley
      - As well as in Dallas, Louisville, Philadelphia   
          - In 2020, and again in 2023, we were awarded an NSF SBIR funding to develop a suite of tools that synthesizes aerial and satellite data in novel ways to produce highly accurate neighborhood scale environmental maps of the built environment and then simulates design solutions
              - Work primarily directed towards AQ and Extreme Heat
              - Which we can treat with tree planting, road diets, depaving, and other methods
                  - We have extensive experience with green infrastructure for stormwater and biodiversity challenges  
  - Andrew Dessler (AD) current project:
      - Trying to get health care data for the neighborhood scale to correlate heat and mortality
      - Ok to do city-scale, but more granular studies violate privacy concerns 
      - Wants to do temperature at city scale but was interested in    
      - Compare the regression curves from this neighborhood to that neighborhood 
      - Imagined the city-wide project would be too expensive (only 20% of the project can go towards this supplement)
  - Diff project: put sensors on buses
      - Get high resolution heatmap of in-situ data 
      - Seeking seed funding to look at the data for a proof of concept
      - Could imagine recruiting us for that 
  - DF gave advice for correlating heat and health data 
      - AD interested in subtleties of LST vs MRT 
  - DF approves bus concept
      - Add a globe sensor 
      - And a fast GPS
  - Discussion of CFD and fires
      - CFD could assess the threshold at which point a manageable fire gets out of control 
      - Do we ever do that?
          - DF we do submeter CFD and particulate transport from vehicular transport
          - We don’t model the combustion process
          - But for forest fires, a colleague is looking at the elasticity of the branches as they bend and how they behave when on fire 
          - AD: not a linear process, 
  - Large research project for for S\&CC
      - We would like to synthesize all the data streams into a single project
      - To which Andrew’s heat-mortality project would make a nice fit 
      - Andrew willing to take a look at S\&CC and share thoughts 
      - Texas A\&M has a census bureau research center (that’s where health care data is coming from)
          - Relatively inexpensive $10,000 flat fee to get a seat in the data center (for unlimited data)
          - You get address-level data (not census block)
          - “Master Beneficiary File” includes SS, address, and then you cross-link to “Death File” and other data sets that you need to painstakingly fuse together  
  - Houston Project
      - Pick a few Texas cities 
      - Develop a software program that can replicate it in different settings
      - 98% is getting the first one started 
          - We could provide data sets
          - mediators : what impacts health in the environment other than heat 
      - Risk-ratio curve : how the risk of mortality increases with temperature
          - Correlating to class and wealth 
      - Indoor temp: studies on that?   
### DF-MP Post-meeting discussion 
Project pitch could be a high resolution model for the entire city of Houston, the whole state of Texas, or a cluster of metropolitan areas.
  - Use high-res data 
  - Multiple high-resolution studies of diversity of places
  - Propose health mitigation solutions 
  - AD: What’s the temp
  - DF: But we’re like traffic, trees, other modifiable factors etc   
Action items
- [ ] ~~Thank Barbara Ransom ~~
- [ ] ~~Send emails to academic partners advising them to apply for NSF funds (hopefully with us)~~
- [ ] ~~Email people on call to keep us in mind ~~
  - [ ] ~~Dressler~~
  - [ ] ~~Jisung Park~~
- [ ] 
#### Follow up email (sent 2/4/25)
Dear Andrew (If I may), 
Thanks for a great meeting last Friday (1/24/25)\! I’m looking forward to us staying in touch about all things extreme heat. 
To recap: 
  - We talked about your NSF work correlating heat and mortality at the neighborhood scale and how our hyperlocal mapping and modeling tools might contribute, if not on this project, then on the next one.
  - We also discussed your upcoming proposal to equip public transport buses with globe temperature sensors in Houston
  - As well as other projects coming up, including the Smart and Connected Communities (S\&CC) program. 
One thing to keep in mind about the S\&CC in regard to your ongoing heat-health research is that NSF is interested in “high risk, high reward” projects that are both scientifically innovative and community-led. A large extreme heat research project proposing to synthesize high-resolution data across multiple metropolitan areas could be competitive. Especially given the range of climate adaptation interventions that such a neighborhood-scale data set could enable. Let’s keep talking about it\!
To answer your question about Hyphae, our team includes scientists, urban planners, arborists, ecologists, civil engineers, landscape architects, even a History PhD (me\!) to do the grant-writing and communication. Our strength lies in bringing together diverse stakeholders to address complex environmental challenges. As our name suggests, we draw inspiration from mycelium fungi, whose underground networks connect and sustain seemingly separate trees, creating a unified forest ecosystem.    
Looking forward to future conversations,
Max 
## NSF Office Hours (1/22/25)
w/ Barbara Ransom of Geoscience Directorate
  - Andrew E. Dressler (Texas A\&M, Dept of Atmospheric Sciences)
Extreme heat - Mortality at a neighborhood level
  - Ransom recommends sending a “concept outline”
      - To: <geohealth@nsf.gov>
  - RCN is 500k for 5 years (sent all at once)
  - Wants to see numbers: Geoscientists together + health and medical people
  - List a steering committee of 3-4 that can reach out more broadly to rope other people in 
  - Just got $1.5 – got money to blow 
  - Bridge medical and non-medical - even if something has material impact on human health
  - [Barbara Ransom](https://new.nsf.gov/staff/bransom)   
  - You can also pitch a conference proposal for under $100k ($99.99) - for $50k she doesn’t even need to ask her colleagues 
  - Idea with this “seed money” is to lay the foundation of actors involved who can coordinate on larger projects when “big money” comes through 
  - COC needs to include medical people: either public health or MD or group of doctors 
  - \+ geoscientist  
  - Has to get rid of $5 mm 
  - Has office hours every week now…
  - 9/27 at 1PM ET, 2/24 at 
  - R. Jisung Park Extreme Heat and worker deaths and workplace injuries 
      - Environmental economist by training
      - Would go up to SBE - social behavioral and economic scientists  
      - New center at Penn on Climate Adaptation and Resilience 
      - Industry University cooperative research centers (<https://iucrc.nsf.gov/>)
          - Only 10% of industry money can go to admin costs  
 ^^ currently coordinating a meeting
  - Def of Geoscience = “Earth, atmosphere, water”
  - Pick a funding vehicle in the DCL
  - RCN requires a merit justification component 
  - “Tell me how much money you want” in the letter
  - Active NSF award can be “supplemented” 
      - But can only ask for 20% of the award amount 
      - This is the “easiest way to move $” 
  - EAGER up to $300k but goes to IHE 
  - Tech, Innovation, and Partnerships has programs for which private companies can apply 
      - “NSF TIP Directorate”
  - Smart and Connected Communities 
  - CIVIC innovation challenge 
  - Barbara recommended we sign up as private sector reviewers in CIVIC and S\&CC:
      - Read previously awarded proposals to see what speaks to the review panels 
      - Suss out which proposals are successful or not 
  - Email re: webinar on S\&CC email Barbara and bring your buddies 
## NSF Smart and Connected Communities (S\&CC) webinar (1/24/25) 
Program goal is to reward “high risk/high reward” proposals
  - Want an “element of risk in the hypothesis”
  - Not needing a “slam dunk” or “baking a cake”
  - Think of the “risk categories,” what might fail, show that “there is a research plan that really describes how I will achieve that.” 
  - Risk to research not  = risk to community lol 
  - Make clear what is the innovation:
      - An existing idea of yours in a new environment e.g.?
      - Panel needs to see where the innovation is. 
          - Can’t be just replicating what you’ve already published on 
Said that they personally hate when the LoS are ghost written (letters “that all say the same thing” – added that they always want letters of collaboration and “never” LoS.) 
Reviewers are multidisciplinary  
Don’t wait for February 20 to submit prelim proposal
Industry cooperation welcomed
  - Still a research program 
  - But that research is integrated with community needs throughout its life cycle 
  - Collaborators funded through sub-awards
Pitfalls to avoid:
  - Make sure you are eligible, registration info 
  - Think of the questions that you might ask of your own proposal 
  - Don’t submit a data management plan for another program
  - Proof-read everything, sometimes sections are missing, returned without review
  - Don’t submit proposals that are not well-written (grammatical and other errors)
NSF Grants
Nesting dolls of funding streams somewhat inchoate, but NSF launching a [Capacity Building to Catalyze Collaborations to Address Climate Change Impacts on Human Health](https://links-2.govdelivery.com/CL0/https:%2F%2Fwww.nsf.gov%2Fpublications%2Fpub_summ.jsp%3Fods_key=nsf24013%26utm_medium=email%26utm_source=govdelivery/1/01010193e0aae6ef-7daa015e-74e7-4c8c-a6ab-c595c1b8c7c8-000000/sCBauq-k0qMpm_GT3c-MUnr9miMAi2jn_-lmsCfleOo=384) (C2H2) program.
Program builds off NSF’s most recent Dear Colleague Letter (DCL) referring grant applicants to existing NSF programs committed to addressing “**climate-triggered human health issues **through interdisciplinary collaboration.”
These include:
<https://new.nsf.gov/funding/opportunities/civic-civic-innovation-challenge>
<https://iucrc.nsf.gov/>
Research Coordination Networks ($500k approx–rolling deadline)
<https://new.nsf.gov/funding/opportunities/research-coordination-networks>
“*NSF Research Coordination Networks (RCN) are designed to foster communication and promote new collaboration among scientists, engineers and educators with diverse expertise and who share a common interest in a new or developing area of science, engineering or technology translation. By encouraging the formation of new groups and networks, the RCN program will advance elds and create novel directions and opportunities for fundamental and applied research as well as science education.*” 
Our mission is to coordinate researchers that are often working in silos, and to pair that research with action, using data to build resilient and equitable urban spaces. Beyond the medical vs. non-medical silo, even our geospatial partners often aren’t sharing information effectively. Meanwhile, it's getting very hot around here\!
SCC: Smart and Connected Communities
Preliminary Proposals Due February 20th, 2025   
<https://new.nsf.gov/funding/opportunities/scc-smart-connected-communities/nsf25-527/solicitation>
<https://nsf-gov-resources.nsf.gov/files/nsf25527.pdf?VersionId=AdRVQy4CNupILLRwMad4gbikIGo8LG_f>
Average award for proposals estimated to range from approximately **$567,000 to $1,107,000**, depending on the number of awards distributed across the three grant categories, with the potential for the **Large-Scale Research Grant** to exceed **$5 million**
Early-concept Grants for Exploratory Research (EAGER)
<https://new.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ch2F5>
^^ see PAPPG Chapter II.F.3.
~~Early-concept Grants for Exploratory Research (EAGER)~~
[~~https://new.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation\#ch2F5~~](https://new.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ch2F5)
~~^^ see PAPPG Chapter II.F.3.~~
Grant Opportunities for Academic Liaison with Industry (GOALI) Proposal
<https://new.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation#ch2F5>
^^ see PAPPG Chapter II.F.5
“*GOALI is a type of proposal that seeks to stimulate collaboration between IHEs and industry. Under this proposal type, academic scientists, and engineers request funding either in conjunction with a regular proposal submitted to a standing NSF program, unsolicited proposal, or as a supplemental funding request to an existing NSF-funded award *
*\[...\] *
*Special interest is focused on affording opportunities for:*
  - *Interdisciplinary IHE-industry teams to conduct collaborative research projects, in which the industry research participant provides critical research expertise, without which the likelihood for success of the project would be diminished;*
  - *Faculty, postdoctoral scholars, and students to conduct research and gain experience in an industrial setting; and*
  - *Industrial scientists and engineers to bring industry's perspective and integrative skills to academe.*”
GEO = Directorate for Geosciences
  - This directorate supports research in **Earth, atmospheric, ocean, and polar sciences**.
  - Areas of focus include topics like climate change, natural disasters, environmental systems, and geophysical processes.
  - Relevant for projects involving geoscientists addressing issues like climate-triggered health effects.
SBE = Directorate for Social, Behavioral, and Economic Sciences
  - This directorate supports research in **human behavior, societal systems, and economic dynamics**.
  - It covers disciplines like sociology, anthropology, psychology, and economics.
  - Relevant for projects exploring how human health is affected by social, economic, and behavioral factors, particularly in the context of climate change.


# 1-page Concept-vision (Laura Burnham)



# Letters

Potential collaborators as of 3/17
**Letter of collaboration**: A letter of collaboration documents a collaboration between a principle investigator (PI) and other entities whose contributions are significant to a proposal. There are two types of collaborations: An unfunded collaboration is “any substantial collaboration with individuals not included in the budget.” These contributions must be documented in a letter of collaboration from each collaborator. Each letter should contain only the statement of collaboration described below – letters that include additional information will be omitted from the proposal. Unfunded collaborations should also be described in the Facilities, Equipment and Other Resources section of the proposal. A funded collaboration is one where a collaborative activity is identified in the proposal budget. Refer to Chapter II.D.3 in the PAPPG for instructions on how to complete the budget. 
  - Gulfton superneighborhood - emailed 
  - Role: assist with community engagement workshops, connect with community members 
  - Potential funded partner 
  - Alief superneighborhood – change in leadership, connect with new president 
  - Role: assist with community engagement workshops, connect with community members 
  - **Alief Votes – willing to sign LOC**
  - Role: assist with community engagement workshops, connect with community members 
  - Could potentially be the funded partner, can ask if needed
  - Metro – emailed, setting up meeting next week 
  - Role: provide access to data collected by Metro, provide feedback on potential interventions 
  - Unfunded, LOC 
  - **SWA - willing to sign LOC**
  - Role: share data from heat internship programming, attend community workshops, share heat intervention ideas for community feedback 
  - Unfunded, LOC 
  - Harris county office of county administration - emailed 
  - Role: advertise community workshop, help disseminate 
  - Unfunded, LOC 
  - **Precinct 4 - willing to sign LOC**
  - Role: advertise community workshops, collaborate for location and details on pilot cooling intervention 
  - Unfunded, LOC 
  - **Texas Forest Service - willing to sign LOC**
  - Role: attend community workshops, share tree planting/heat intervention expertise for feasibility 
  - Unfunded LOC 
Letters of Collaboration received: Texas Forest Service
Waiting on: Precinct 4, 
1.  CBOs in Houston, the Gulfton super superneighborhood association (sp?) for instance 
2.  Transportation authorities  
3.  County and Municipal authorities (we could propose to contrast our proposed analysis with the 2019-2024 Norris County heat study)
4.  Harris County Public Health officials
5.  Tree-focused non-profits
6.  The Texas Forest Service, headquartered at TAMU   
Dear Barbara,
We are participating as sub-awardees on at least two proposals for the S\&CC grant. I have a clarifying question regarding the disciplinary areas of interest—specifically, how the focus outlined in the webinar compares to the language in the solicitation.
The solicitation identifies relevant overlapping disciplines as follows:
  - 47.041 --- Engineering
  - 47.050 --- Geosciences
  - 47.070 --- Computer and Information Science and Engineering
  - 47.075 --- Social Behavioral and Economic Sciences
  - 47.076 --- STEM Education
But the webinar identifies them thusly:
 
  - Computer and Information Sciences   
  - Civil and Mechanical Engineering
  - Geosciences 
  - Social, Learning, and Behavioral Sciences
Can you clarify the discrepancy? In particular, we wanted to know how social science analysis is weighted into the review process. Vishal and David mentioned that social science was less integral to the research vision of the grant than in previous years but I wanted to clarify. 
Thanks for your support.  


# Scraps

# **SCC-IRG Preliminary Proposal: Closing the Heat Gap: Precision Modeling & Community-Driven Cooling Interventions**
[SCC-IRG Preliminary Proposal:](?tab=t.8x57mnjnrbtp#heading=h.ekxct433w214)
[Project Summary](?tab=t.8x57mnjnrbtp#heading=h.tf6b5zq7rvu9)
[Overview](?tab=t.8x57mnjnrbtp#heading=h.l816a2hozj5k)
[Intellectual Merit](?tab=t.8x57mnjnrbtp#heading=h.ugbm1usxfux2)
[Broader Impacts](?tab=t.8x57mnjnrbtp#heading=h.h1vv11g7xen)
[Project Description](?tab=t.8x57mnjnrbtp#heading=h.bo4moomodrdj)
[Vision and Goals](?tab=t.3bfqc41amuf9#heading=h.oyqy855matl3)
[Integrative Research Approach](?tab=t.3bfqc41amuf9#heading=h.8refoguklxpn)
[Broader Impacts](?tab=t.3bfqc41amuf9#heading=h.m9cqyeoiv0tv)
# Project Summary
## **<comment_start id=kix.wysyjt6pngo3>Overview**
Extreme heat is driving rising healthcare costs across the United States, contributing to an estimated $100 billion annually in direct medical expenses. Indirect costs, such as lost productivity and increased insurance burdens, are expected to drive this figure to $500 billion per year by 2050. The rise is fueled by more frequent and severe extreme heat events, the intensification of urban heat islands from expanding sprawl and declining green spaces, an aging population more vulnerable to heat stress, and rising healthcare costs. To fully understand the impact of extreme heat, however, we must move beyond the public health literature’s overreliance on census-tract-level analyses, as these often obscure critical variations in individual exposure. Submeter-scale factors—such as pavement type, shade coverage, wind direction, building shape, and building materials—directly shape how individuals experience heat exposure, yet are often overlooked in these broader-scale assessments.
Our project will bridge this gap by using cutting-edge geospatial and machine learning techniques to analyze how modifiable built-environment features influence extreme heat exposure across a large American population. We will complement this analysis with pre- and post-monitoring of heat exposure in targeted, community-driven pilot interventions to validate the causal benefits of scalable, evidence-based heat mitigation strategies.
## **<comment_start id=kix.1x84hjejsp14>Intellectual Merit**
While the dangers of extreme heat are well known and built environment interventions are widely embraced, their efficacy is often underexamined. Many communities rely on dashboards that map heat risk by census tract, guiding interventions such as tree planting in high-risk areas. While trees provide shade and cooling in principle, our high-resolution modeling and monitoring confirm that without precise placement, these efforts can be ineffective.
For example, a high-risk census tract might have residents experiencing the bulk of their heat exposure at bus stops. Yet a well-intentioned tree-planting initiative may focus on a nearby park, providing shade where it isn’t needed. To address this misalignment, we use submeter radiant temperature modeling, agent-based simulations of pedestrian and worker activity, and mobility tracking to pinpoint heat exposure hotspots. This process enables targeted, high-impact interventions—such as the implementation of greening and other shade structures, cool pavements, or air-conditioning rebates—maximizing mitigation funds and minimizing waste. By integrating pre- and post-intervention monitoring of both heat exposure and health outcomes, we validate effectiveness, ensuring replicable solutions for other communities.
## **<comment_end id=kix.1x84hjejsp14>Broader Impacts       **
<comment_end id=kix.wysyjt6pngo3>This project will generate substantial societal benefits by developing and disseminating practical strategies to reduce extreme heat exposure, particularly in high-risk communities. Partnering with local stakeholders, the team will translate research insights into evidence-based tools that help communities lower healthcare costs and improve public health.
Communities will gain hands-on experience applying geospatial analyses to design effective heat mitigation strategies. The project will promote widespread adoption of best practices through open-source data sharing, case studies, and public workshops. By equipping communities with scalable solutions, this work will strengthen resilience to extreme heat across the United States and inform urban planning and policy for long-term climate adaptation.
# <comment_start id=kix.o8f0vziynyq6>Project Description<comment_end id=kix.o8f0vziynyq6>
## **<comment_start id=kix.p34si7oziy0i>Vision and Goals**
This project aims to conduct a 1 meter<comment_start id=kix.xnzcovwzrplg>-scale extreme<comment_end id=kix.xnzcovwzrplg> heat study for the City of Houston, culminating in a green infrastructure pilot project designed to mitigate urban heat exposure along the City’s transportation network. The study will integrate meter-scale heat mapping, public health data, and infrastructure interventions, setting a replicable framework for comprehensively improving community transportation networks in future funding cycles.
The pilot intervention may include heat interventions at a bus stop or a set of bus stops, followed by pre- and post-monitoring to assess efficacy. This evidence-based approach will provide a data-driven model for cooling interventions, demonstrating how localized modifications to the built environment can significantly reduce heat exposure and improve health outcomes.
The high-risk, high-reward aspect of this study is its unprecedented level of granularity, correlating individual address-level heat exposure with public health outcomes, such as emergency room visits and ambulatory care data. <comment_start id=kix.5ggvmy8htzl>Current research, including the Harris County Public Health (HCPH) 2019–2024 heat study, has only assessed heat impacts at the zip-code level.<comment_end id=kix.5ggvmy8htzl> Our work will pioneer a finer-scale analysis, producing actionable data for heat mitigation strategies.
## **Integrative Research Approach**
Our project seeks to surpass the current state of the art in extreme heat research by shifting from census-tract-level heat analysis to meter-scale assessments. We integrate advanced geospatial analysis, engineering solutions, machine learning, and social science methodologies to provide high-resolution, community-driven interventions.
Methodology:
**High Resolution Heat mapping: ** We will make a 1 meter scale three-dimensional <comment_start id=kix.j6nm1f9kmzrs>digital twin<comment_end id=kix.j6nm1f9kmzrs> of the city of Houston using publicly available aerial lidar data, which takes into account the terrain, buildings and vegetation. This will be used to perform a 1-meter scale Solar and LongWave Environmental Irradiance Geometry (SOLEWIG) estimation of mean radiant temperature (MRT) for a typical summer <comment_start id=kix.82kwd5j8xjvp>day<comment_end id=kix.82kwd5j8xjvp>. The model will be validated and supplemented with the deployment of a network of low-cost MRT, humidity, and wind sensors that can provide discrimination between the human-scale effects of different modifiable landscape elements; for example some sensors will be placed out in the open over pavement, or grass, while some will be in the shade of a large tree, or a small tree or building. Our previous research has shown that while air temperatures between such features may vary by only a few degrees, the MRT (which more accurately reflects the human experience of heat stress) can vary by up to 25 degrees between shady and sunny areas. While some sensors will be stationary, gathering data 24 hours per day from one location, others will be mobile, traveling with community agents to determine the heatscape of the human occupied activity-space while it is in use.
**Health Data Correlation: **We will access address-level and census block-level health outcomes from Texas A\&M Research Data Center, which provides access to individual death records. This can then be analyzed against a variety of covariates with the heat simulation and monitoring data using distributed lag non-linear models (DLNM) , to investigate causal relationships between heat, modifiable built-environment parameters, and health outcomes. A particular outcome will be neighborhood-to-neighborhood comparisons of mortality, which will allow us to determine if some neighborhoods are more vulnerable to extreme heat and humidity.
**Community-led Intervention Pilot: **Equipped with monitoring, modeling, and health data, we will work with community stakeholders (e.g., Superneighborhood councils, community development organizations, public health perts) to co-design and implement a pilot intervention. The intervention will be optimized to improve health outcomes by reducing heat exposure/heat stress in a testbed community with high heat related health problems. The pilot intervention may be relatively small, like providing greening or shade structures to a set of bus-stops. However, the monitoring will allow pre- and post- measurement of reductions in heat exposure, improved thermal comfort, and potentially changes in health indicators. TAMU and HARC will work with community partners to ensure this intervention is within community interest and will serve as a true benefit.
**Scalability & Replicability: **The framework proposed here; modeling heat, designing an intervention informed by feedback from modeling, and monitoring the benefits of the intervention with pre-post assessments, provides a replicable technology that can be generalized both across the rest of the city of Houston, and to any other location in the United States that suffers from extreme heat. This project can then serve as a model for infrastructure planning with evidence-based design.
Interdisciplinary Integration:
This project aligns with NSF’s requirement to integrate at least two disciplines, drawing from:
  - Geosciences (47.050): Heat mapping, climate modeling.
  - Engineering (47.041): Green infrastructure implementation.
  - Computer & Information Science (47.070): Machine learning, geospatial data analytics.
  - Social & Behavioral Sciences (47.075): Community engagement, public health impact assessment.
## **Broader Impacts**
Our project advances NSF Smart & Connected Communities (S\&CC) priorities by creating an evidence-based, community-led approach to urban heat mitigation.
  - Community-Led Research & Implementation:
      - Stakeholders (e.g., Houston Metro, HCPH, Gulfton Super Neighborhood) co-design interventions to ensure relevance and long-term adoption.
      - The public health sector will use our findings to inform future heat mitigation policies.
  - Capacity Building for Long-Term Impact:
      - Our research will equip communities with tools and training to design and implement their own interventions.
      - STEM education and workforce development components will enhance local skill-building in climate resilience and urban sustainability.
  - Scalability Beyond Houston:
      - <comment_start id=kix.57m0u18lyncq>Our methodologies can be replicated in other heat-vulnerable cities, extending the project’s impact nationwide<comment_end id=kix.57m0u18lyncq>.
      - Work will be shared with policymakers via policy briefs, white papers, and application to ongoing climate adaptation plans led by the City of Houston and Harris County.
      - <comment_start id=kix.3g2pmt1qoeip>The data framework, intervention strategies, and policy recommendations will be openly shared for broader adoption.<comment_end id=kix.3g2pmt1qoeip>
      - Findings will be shared with the City of Houston, Harris County, Harris County Public Health, and Texas Commission on Environmental Quality for broader application.
This research positions Houston as a national leader in extreme heat mitigation by demonstrating a scalable, data-driven, and community-led model that can be expanded city-wide and beyond.<comment_end id=kix.p34si7oziy0i>
# Project Personnel and Partner Institutions
 
Project Personnel and Partner Institutions
Andrew Dessler; Texas A\&M University; PI (Professor of Atmospheric Sciences, Director, Texas Center for Climate Studies)  
Stephanie Piper; Houston Advanced Research Center (HARC); Co-PI (Research Associate, Community Development and Resilience)  
Daniel Fleischer; Hyphae Design Lab; Subawardee (Chief Science Officer)  
Brent Bucknum; Hyphae Design Lab; Subawardee (Principal)  
Juan Penaloza Gutierrez, PhD; Hyphae Design Lab; Subawardee (Modeling Expert)  
Ivan Heitmann; Hyphae Design Lab; Subawardee (Modeling and Design Lead)
-----
Texas A\&M University
Dr. Andrew Dessler is a climate scientist specializing in climate change impacts, global climate physics, and atmospheric chemistry. As Director of the Texas Center for Climate Studies, his research informs resilience and adaptation strategies. A fellow of AGU and AAAS, he serves as President of AGU’s Global and Environmental Change section. His work has advanced understanding of climate feedbacks, extreme weather, and infrastructure stress. Formerly a Senior Policy Analyst at the White House Office of Science and Technology Policy, he has written extensively on climate science and policy, including in *The Science and Politics of Global Climate Change* (2005) and *Introduction to Modern Climate Change* (2011). Dr. Dessler holds a Ph.D. from Harvard University and a B.A. from Rice University.
 
Houston Advanced Research Center (HARC)
HARC applies science to support policies that address environmental challenges while promoting social and economic equity. It engages communities in defining problems and co-developing solutions, partnering with Superneighborhood councils, development groups, and environmental nonprofits to build trust and collaboration. A key focus is reducing environmental disparities, such as extreme heat, through initiatives like urban tree planting. Dr. Stephanie Piper, Co-PI, is a Research Associate at HARC specializing in community resilience, urban ecology, and science policy. She leads outreach efforts to integrate community priorities into research and climate adaptation strategies. Previously a Science Policy Fellow with the National Academies of Sciences, Engineering, and Medicine’s Gulf Research Program, she earned a Ph.D. in Plant Biology from UC Riverside, researching urban air pollution patterns, and an M.S. and B.S. in Ecology and Evolutionary Biology from Tulane University.
 
Hyphae Design Lab
Hyphae Design Lab is a leader in evidence-based environmental design, specializing in adaptive interventions that enhance human health, support biodiversity, and mitigate risks such as extreme heat and flooding. With over 15 years of experience supporting environmental justice communities, Hyphae collaborates with academic institutions and community partners to integrate research into practice.
 
Hyphae has secured funding from the National Science Foundation and the National Institutes of Health to develop adaptOS—a platform integrating aerial, satellite, and ground-level data to create high-resolution, hyperlocal 3D maps of environmental risks. In partnership with the University of Louisville, Hyphae is leading the largest clinical trial to date on the effects of urban greening on air quality and neighborhood health. The firm partners with community-based organizations nationwide to improve environmental health through data-driven design solutions.
 
<comment_start id=kix.4k8ith5tkic4>
<comment_end id=kix.4k8ith5tkic4>
Other HARC personnel -<comment_start id=kix.gcpxb1343ueq> Yaneth Barton potential<comment_end id=kix.gcpxb1343ueq>
1.  CBOs in Houston, the Gulfton and alief super super-neighborhood association for instance - can discuss funded vs un-funded partners
    1.  Coalition for Environment, Equity, and Resilience (CEER) - could connect with their ambassadors
    2.  Student Conservation Association?
    3.  If looking for full city can include other areas
        1.  Greater East Houston Redevelopment Corporation
        2.  Fifth Ward
        3.  Buffalo Bayou Partnership
2.  Transportation authorities  
3.  County and Municipal authorities (we could propose to contrast our proposed analysis with the 2019-2024 Norris County heat study)
4.  Harris County Public Health officials
5.  Tree-focused non-profits
    1.  Trees for Houston?
6.  The <comment_start id=kix.h97ma982y6k4>Texas Forest Service<comment_end id=kix.h97ma982y6k4>, headquartered at TAMU   
Andrew Dessler, PI (Professor of Atmospheric Sciences, Director, Texas Center for Climate Studies, TAMU)
Stephanie Piper, Co-PI (Research Associate, HARC)
Daniel Fleischer, subawardee (Chief Science Officer, Hyphae Design Lab) 
Brent Bucknum, subawardee (Principal, Hyphae Design Lab)  
Juan Penaloza Guttierrez, PhD, subawardee (Modeling Expert, Hyphae Design Lab)  
Ivan Heitmann, subawardee (Modeling and Design Lead, Hyphae Design Lab) 
Dr. Andrew Dessler is a climate scientist specializing in climate change impacts, global climate physics, and atmospheric chemistry. As Director of the Texas Center for Climate Studies, his research informs strategies for resilience and adaptation. A fellow of the AGU and AAAS, he serves as President of AGU’s Global and Environmental Change section.
His work has advanced understanding of climate feedback mechanisms, extreme weather, and infrastructure stress. Formerly a Senior Policy Analyst at the White House Office of Science and Technology Policy, he has written extensively on climate science and policy, including *The Science and Politics of Global Climate Change* and *Introduction to Modern Climate Change*.
Dr. Dessler holds a Ph.D. from Harvard University and a B.A. from Rice University.
Houston Advanced Research Center (HARC) has a history of community engaged research in the greater Houston area and will connect that network to this program in order to ensure interventions are within community interest and need. HARC’s mission is to use science and research to support the deployment of policies, programs, and practices that will effectively address the environmental concerns while leveraging work with communities to provide sustainable, just, social, and economic opportunities for all. Past work in community research and analysis supports a participatory approach to inform problem definition and co-development of solutions. Community engagement practices involve robust outreach to build a trusting and effective working relationship with community groups and community members. Potential partners include Superneighborhood councils, community development groups, community ambassadors, and local tree planting non-profits. HARC is committed to leverage investments to rectify environmental disparities, like those associated with extreme heat.
With over 15 years of experience supporting environmental justice communities nationwide, Hyphae is a recognized leader in evidence-based design. In collaboration with communities and academic partners, Hyphae has secured funding from the National Science Foundation and the National Institutes of Health to develop adaptOS—an adaptive management platform that integrates aerial, satellite, and ground-level data to generate high-resolution, hyperlocal 3D maps of the built environment and associated risks to air, water, and soil.
In collaboration with communities and academic researchers, Hyphae designs adaptive environmental interventions that enhance human health, support biodiversity, and mitigate risks such as extreme heat and flooding. Currently, in partnership with the University of Louisville, Hyphae is leading the **largest clinical trial to date** examining the impact of urban greening on air quality and neighborhood-scale health outcomes.
Hyphae Design Laboratory is a mission driven environmental analysis, design and evaluation firm. Hyphae has partnered with community base organizations throughout the United States to improve environmental health outcomes through evidence-based design.


# Cover Letter + Abstract

**Cover Letter**
 
Andrew Dessler  
Professor of Atmospheric Sciences  
Texas A\&M University, Department of Atmospheric Sciences  
\[Your Address\]  
adessler@tamu.edu  
\[Your Phone Number\]  
Tuesday February 18, 2025
 
NSF Smart & Connected Communities Program  
National Science Foundation  
2415 Eisenhower Ave
Alexandria, VA 22314
 
Re: SCC-IRG Preliminary Proposal – Closing the Heat Gap: Precision Heat Mapping for Targeted Cooling Interventions
 
Dear NSF Review Committee,
 
I am pleased to submit our preliminary proposal for Closing the Heat Gap: Precision Heat Mapping for Targeted Cooling Interventions under the Smart & Connected Communities (S\&CC) program. This interdisciplinary research project brings together experts in climate science, geospatial analysis, urban planning, and public health to address extreme heat exposure through high-resolution mapping and targeted mitigation strategies.
 
Extreme heat is a growing public health crisis, exacerbated by urban heat islands, aging infrastructure, and inequitable access to cooling resources. Current heat risk assessments often rely on census-tract-level analyses, missing critical submeter-scale variations that directly impact individual exposure. Our project will bridge this gap by integrating advanced geospatial modeling, community-driven interventions, and pre- and post-monitoring of heat exposure to validate scalable mitigation strategies.
 
Led by Texas A\&M University in collaboration with the Houston Advanced Research Center (HARC) and Hyphae Design Lab, this project aligns with NSF’s mission by advancing smart and connected solutions for climate adaptation. Our research will empower communities to implement data-driven cooling interventions, reduce heat-related health risks, and establish a replicable framework for urban resilience nationwide.
 
We appreciate the opportunity to submit this proposal and look forward to the potential to contribute meaningful research and solutions in extreme heat mitigation. Please do not hesitate to contact me if you require any additional information.
 
Sincerely,
 
\[Online signature\]  
Prof. Andrew Dessler  
Texas A\&M University
 
**Project Description Abstract** (176 words)
 
Extreme heat exposure is a growing public health crisis, yet most heat risk assessments rely on census-tract-level data that fail to capture critical submeter-scale variations in individual exposure. This project integrates high-resolution heat mapping, mobility tracking, and machine learning to identify heat exposure hotspots and develop targeted, community-driven interventions. Using a one-meter-scale digital twin of Houston, we will analyze how built-environment factors—such as pavement type, shade coverage, building shape, and wind flow—affect heat exposure. In collaboration with local stakeholders, we will co-design and implement cooling strategies, such as shade structures, targeted greening, and cool pavement technologies. Pre- and post-monitoring of heat exposure and health outcomes will validate the effectiveness of these interventions, creating a replicable model for urban heat mitigation. Led by Texas A\&M University in partnership with the Houston Advanced Research Center (HARC) and Hyphae Design Lab, this interdisciplinary project advances NSF Smart & Connected Communities (S\&CC) priorities by equipping communities with data-driven tools to address extreme heat. Findings will inform policy, guide infrastructure investments, and provide scalable solutions for heat-vulnerable cities nationwide.  


# Rough notes

3/19/25
Rough Notes
  - On 3/14 
      - Hyphae Team had discussed ongoing projects in Houston area that we could measure for this grant
          - Gulfton Neighborhood (“Greener Gulfton” project)
              - Also funded by Nature Conservancy 
              - In collaboration with Asakura Robinson
                  - <https://asakurarobinson.com/projects/greener-gulfton/> 
                  - One of these projects 
      - Ultra Barrio has ongoing projects
          - <https://www.ultrabarrio.com/greener-gulfton-shade-structures>
          - <https://www.houstonpublicmedia.org/articles/news/health-science/2023/07/20/457262/gulfton-is-the-hottest-neighborhood-in-houston-whats-being-done-about-it/> 
              - Marcus Martinez BB contact
      - Houston Land Trust 
  - 3/19
      - Metro already developing bus stops 
      - Best to not overly lean on a community group in the narrative if it ends up falling through 
      - BB evoked studies of bus stops that measure thermal comfort and felt sense of being hot by commuters
      - SP widespread interest in shade structures
          - Parse trees vs other cooling interventions 
          - Determine what communities prefer 
          - Discussed letters of collaboration 
              - Those that have agreed to sign 
              - And those that are yet to respond 
          - Nature Conservancy, SCA, 
              - Connected to Greener Gulfton Plan 
      - BB Which groups involved in Greener Gulfton 
      - SP: Gulfton Superneighborhood 
          - \_\_\_\_\_ \_\_\_\_ parkay
          - Planners at Precinct 4 very involved 
          - Commissioner attached to the project 
              - “Healthy Parks Plan” 
      - BB: Should we keep budget to keep some planting?
          - Challenge: tree planting takes years to have impact
          - Or plant a big tree and that costs money 
              - E.g. $9M tree planting costs in Louisville   
          - Big money from gov agencies (return to transcript)
              - New trail projects 
      - SP: 
          - Money set aside to communities 
          - Could frame more targeted as to community *intervention*
          - Alief example: 
              - Good deal on a water truck that brought down costs 
          - Direct money to group that’s already planting
      - BB: “Alief linear forest”
      - SP: Barbara Quattro term
          - Esplanades currently have grass–let’s put trees instead 
          - Currently sick (on hospice)
          - “The tree queen of Alief”
      - BB: Report “The Case for Cool Trees”
      - SP: that report led to Alief Planting
          - Mitsubishi funded both 
      - BB: Is idea to advance that data and prioritization?
      - SP: Data shows it’s highest heat areas
      - BB: “Heat H3E” 
      - SP: That was our heat mapping: single day community science led
      - BB: CAPA process?
      - SP: Yes
      - BB: Plans for more campaigns?
      - SP 2020, 2024, none for future planned 
          - Depends on need for data 
      - BB We know CAPA folks, cool process
          - Sensor locations for longer is more useful 
      - SP agrees longitudinal analysis more helpful 
      - BB Show what we are trying to do in narrative 
          - Show the images from SWMD 
          - Choosing a representative corridor
          - Call it "representative" and say TBD final site 
          - Rather than abstract and undefined
      - SP
          - Could use photos and infrared imagery from Alief      
      - SP
          - Focusing on precinct 4
          - Main projects are focused on esplanades 
          - Some is adding to parks 
          - Redone some community centers 
      - BB
          - Does some of grant need to go to prioritization or is this already happening 
          - Often the tree planting masterplan is crude census level 
          - Is there a need for more granular prioritization to plant trees where they have the most impact
      - SP
          - There are a number of healthy parks and healthy city plans 
          - <https://cp4.harriscountytx.gov/healthy-parks#:~:text=As%20part%20of%20the%20Healthy,park%20access>
          - 
          - Return to transcript 
      - BB
          - We worked on a cool corridors project, safe routes to schools 
              - Then get the trees along the hottest routes 
          - Vegetation maps of Harris County (SP “tree portal”) 
              - Are at census-tract level 
              - Is there a more detailed plan\>
      - SP most work at census tract level
          - Return to transcript 
              - SWA heat internships project: “cool loop”
              - HOuston “inner and outer loop” 
              - Cool corridor throughout downtown 
              - Downton Houston Plus attempting to revamp downtown
      - BB 
          - Precinct 4 gerrymandered shape
          - Promotoras model
          - What are the demographics
          - Who is working in those areas?
      - SP
          - Gulfton superneighborhood = majority Hispanic 
          - Alief slightly different
          - Need to know more 
          - Depends who the Gulfton Superneighborhood is convening 
              - Very active  
      - BB
          - Report x funded by Nature Conservancy (return to transcript)
          - Tecolotl
              - <https://www.tecolotl.org/team>
      - SP
          - Texas Energy Poverty Research Institute (TEPRI)
      - SP 
          - Trees for Houston 
          - Texas Forest Service
      - BB
          - Texas by Nature?
              - Funded by Laura Bush 
              - Based in Austin
      - SP
          - Texas Children and Nature 
      - BB 
          - Speaking engagement at Rice event 
          - Should connect 
      - SP
          - We are in woodlands, net zero buildings 45 min north 
          - Happy to show you landscape design of building
          - Letters of collab drafted 
      - MP
          - Question of site and scale 
      - BB
          - Scale to site and health data
          - Which is at meter scale 
          - Return to transcript for “local climate zones” (LCZ)
      - SP
          - Snapshot heat data can help identify those LCZs
          - <https://www.forustreehtx.org/search?groupIds=5737b46445c14cecbdabc6a123bb3e6b>
          - 5-year grant
      - BB
          - Use the LCZ data + heat data  to show the methodology in the proposal    
          - Making a compiled map
              - See if DF can layer on the higher tree resolution tree canopy data 
      - SP
          - Using that and waiting for new Landsat data  
      - BB
          - PlanITGeo released a whole new canopy map 
              - Does HARC have a high resolution tree canopy map 
      - SP
          - no , we are not data \_\_\_
      - BB
          - WE can supplement with the aerial LiDAR data and compile other data sources
              - Is the new LiDAR data currently being flown? 
          - Have DF supplement 
          - Show in narrative that this is our intervention
          - BB friend (formerly at Asakura Robinson): Luis \_\_\_ Harris County Precinct 4
              - SP has reached out 
              - He has responded  
          - Lock them in 
          - Can we direct where these trees are going to be planted by providing data?
              - Trees currently directed to specific disadvantaged communities 
          - If we want to study the impacts, are there some concentrated areas where we can demonstrate a statistical shift 
              - Pack in trees
          - Qu, tf of control, who has control of where they’re going?
              - SP: 
                  - Depends: Flood Control District only planting in x areas
                  - Other initiatives have determined where they are planted and HARC is funding 
              - BB Forest Service not asking to track where
                  - SP HARC is keeping track, however
              - BB: All street trees?
                  - City Tree Plotter \_\_\_\_
                      - Do you have access to that data?
                  - Work with Dr. Bullard
                      - SP Not a lot, but our CEO has worked in passing 
                      - ONe of his grad students connected
              - Returen to Green Schools America – Green Belts and Schools       
Action items
- [ ] 



<!-- connector commentThreads: verbatim JSON as returned by read_file_content -->
```json
[
  {
    "commentId": "AAABfSpQch0",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net, @karenthum@tamu.edu writes that \"1.\tFleischer Biosketch - It looks like the NIH format was used, please use the NSF biographical sketch format.\"",
      "modifiedTime": "2025-03-28T03:51:18.279Z",
      "postId": "AAABfSpQch0"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-03-28T03:51:18.279Z",
        "postId": "AAABfSpQcjg"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABfRhgq5g",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@max@hyphae.net",
      "modifiedTime": "2025-03-27T23:57:48.365Z",
      "postId": "AAABfRhgq5g"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-03-27T23:57:48.365Z",
        "postId": "AAABfRhgrDk"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABfRhgq5c",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net",
      "modifiedTime": "2025-03-27T22:55:59.785Z",
      "postId": "AAABfRhgq5c"
    },
    "replies": [
      {
        "authorName": "Daniel Fleischer",
        "content": "@max@hyphae.net https://docs.google.com/document/d/1sJcv08GBKqmSVZvtzGEzzHsI1yY-jNSFtk5jxxpPpQk/edit?tab=t.0",
        "modifiedTime": "2025-03-27T22:53:33.268Z",
        "postId": "AAABfRhgq_U"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-03-27T22:55:59.785Z",
        "postId": "AAABfRhgq_w"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABfRhgq48",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net Confirming ED email sent Wednesday, March 26, 2025 at 5:47 AM is sufficient",
      "modifiedTime": "2025-03-27T22:56:16.592Z",
      "postId": "AAABfRhgq48"
    },
    "replies": [
      {
        "authorName": "Daniel Fleischer",
        "content": "no here is the https://drive.google.com/drive/folders/1i1HJhw7W_DPKShvDAxL4U_XxTyKnAS_7?usp=drive_link",
        "modifiedTime": "2025-03-27T22:51:38.748Z",
        "postId": "AAABfRhgq_Q"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-03-27T22:56:16.592Z",
        "postId": "AAABfRhgq_0"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABfRhgq44",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@ericd@hyphae.net What do we submit in place of this document given that the SBIR award letter does not qualify?",
      "modifiedTime": "2025-03-27T23:57:54.007Z",
      "postId": "AAABfRhgq44"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-03-27T23:57:54.007Z",
        "postId": "AAABfRhgrDo"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABfQhKMyw",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org Here again, without a setting, @fletch@hyphae.net cannot move forward with the details of this section. Thanks!",
      "modifiedTime": "2025-03-25T21:51:06.618Z",
      "postId": "AAABfQhKMyw"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "Since we have not heard back from Gulfton supernighborhood, we could use Precinct 4 or Alief Votes as the proposed group but neither would likely be fully confirmed and Precinct 4 would not be a sub. \nIf we have a set of needs( a certain mount of open space etc) let me know, otherwise I can pick a place based off high heat as an example that may shift?",
        "modifiedTime": "2025-03-25T21:51:06.618Z",
        "postId": "AAABfQhKM1E"
      }
    ],
    "status": "OPEN"
  },
  {
    "commentId": "AAABfQhKMys",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org I'm not sure if you are working in a separate document and then adding in the material all at once but if you could provide some more info as to the main CBO contact and the setting is (the potential greening corridor that we are proposing to monitor), that would be immensely helpful. ONce he has this information @fletch@hyphae.net can pull the aerial and LiDAR data to compile the mapping layers and propose some local climate zones to add specificity to the proposal.",
      "modifiedTime": "2025-03-26T22:06:48.244Z",
      "postId": "AAABfQhKMys"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "Let me know if this is too small an area or if we need something more \"planting ready\". This is an area community members often use to highlight the typical land cover and heat in Gulfton (I can point to news stories where they are interviewed from this location)",
        "modifiedTime": "2025-03-25T22:21:30.661Z",
        "postId": "AAABfQhKM2k"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "I can support as needed but these more technical questions should be directed to @fletch@hyphae.net",
        "modifiedTime": "2025-03-26T21:54:28.722Z",
        "postId": "AAABhLQUW80"
      },
      {
        "authorName": "Daniel Fleischer",
        "content": "",
        "modifiedTime": "2025-03-26T22:06:48.244Z",
        "postId": "AAABhLQUW-U"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABe-13OZs",
    "headPost": {
      "authorName": "Andrew Dessler",
      "content": "you need to explain what this is and give references",
      "modifiedTime": "2025-03-23T21:03:46.224Z",
      "postId": "AAABe-13OZs"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "@fletch@hyphae.net",
        "modifiedTime": "2025-03-23T21:03:46.224Z",
        "postId": "AAABe-13OZ0"
      }
    ],
    "status": "OPEN"
  },
  {
    "commentId": "AAABe-13OZU",
    "headPost": {
      "authorName": "Andrew Dessler",
      "content": "you can't have URL/links in the document",
      "modifiedTime": "2025-03-23T21:04:09.738Z",
      "postId": "AAABe-13OZU"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "@fletch@hyphae.net",
        "modifiedTime": "2025-03-23T21:04:09.738Z",
        "postId": "AAABe-13OZ4"
      }
    ],
    "status": "OPEN"
  },
  {
    "commentId": "AAABe-13OZA",
    "headPost": {
      "authorName": "Andrew Dessler",
      "content": "Goal of this section: Clearly define the two or more primary research disciplines involved (Geosciences, Engineering, Computer & Information Science, Social & Behavioral Sciences).\nDiscuss how each discipline contributes uniquely and integratively to the research.",
      "modifiedTime": "2025-03-23T21:03:38.894Z",
      "postId": "AAABe-13OZA"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "@fletch@hyphae.net",
        "modifiedTime": "2025-03-23T21:03:38.894Z",
        "postId": "AAABe-13OZw"
      }
    ],
    "status": "OPEN"
  },
  {
    "commentId": "AAABeD14pxk",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net Leaving this here for you",
      "modifiedTime": "2025-02-15T00:29:49.538Z",
      "postId": "AAABeD14pxk"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-15T00:29:49.538Z",
        "postId": "AAABdbrlxNU"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABe-zAGJ4",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@karenthum@tamu.edu Is this a formal document or is the internal scope we sent you sufficient?",
      "modifiedTime": "2025-03-28T01:41:30.335Z",
      "postId": "AAABe-zAGJ4"
    },
    "replies": [
      {
        "authorName": "Deleted account",
        "content": "The Scope of Work is the Project Summary that will have the following sections: Overview, Intellectual Merit and Broader Impacts.",
        "modifiedTime": "2025-03-20T16:36:42.519Z",
        "postId": "AAABe-zAGRs"
      },
      {
        "authorName": "Deleted account",
        "content": "One page maximum.",
        "modifiedTime": "2025-03-20T16:40:15.852Z",
        "postId": "AAABe-zAGSM"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "@adessler@tamu.edu Is this what you are calling \"workplan\" in your 3/27 email from 8:40AM CT? Isn't this just the one page summary of the whole project?",
        "modifiedTime": "2025-03-28T01:09:00.588Z",
        "postId": "AAABfRhgrGY"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "@fletch@hyphae.net",
        "modifiedTime": "2025-03-28T01:09:12.053Z",
        "postId": "AAABfRhgrGg"
      },
      {
        "authorName": "Andrew Dessler",
        "content": "yes, scope of work and work plan are the same thing.  sorry for any confusion.",
        "modifiedTime": "2025-03-28T01:26:32.069Z",
        "postId": "AAABfRhgrHI"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "And also the 1-page Project description, correct?",
        "modifiedTime": "2025-03-28T01:27:28.363Z",
        "postId": "AAABfRhgrHM"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-03-28T01:41:30.335Z",
        "postId": "AAABfSpQcco"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABghG2-o4",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org",
      "modifiedTime": "2025-03-25T22:01:14.203Z",
      "postId": "AAABghG2-o4"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "",
        "modifiedTime": "2025-03-25T22:01:14.203Z",
        "postId": "AAABfQhKM1Q"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABghG2-ok",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org",
      "modifiedTime": "2025-03-25T22:01:58.488Z",
      "postId": "AAABghG2-ok"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "See TFS letter that was emailed, we can check with TAMU grants team to be sure it meets guidelines but also covers expertise",
        "modifiedTime": "2025-03-25T22:01:58.488Z",
        "postId": "AAABfQhKM1U"
      }
    ],
    "status": "OPEN"
  },
  {
    "commentId": "AAABghG2-og",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org",
      "modifiedTime": "2025-03-25T22:02:13.309Z",
      "postId": "AAABghG2-og"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "Pct 4 discussing with leadership currently",
        "modifiedTime": "2025-03-25T22:02:13.309Z",
        "postId": "AAABfQhKM1Y"
      }
    ],
    "status": "OPEN"
  },
  {
    "commentId": "AAABghG2-oc",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org",
      "modifiedTime": "2025-03-20T15:41:10.246Z",
      "postId": "AAABghG2-oc"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "",
        "modifiedTime": "2025-03-20T15:41:10.246Z",
        "postId": "AAABe-zAGFA"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABghG2-oU",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net",
      "modifiedTime": "2025-03-19T22:45:29.724Z",
      "postId": "AAABghG2-oU"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABgfANyXY",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net",
      "modifiedTime": "2025-03-19T16:19:55.475Z",
      "postId": "AAABgfANyXY"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABdrk-N9A",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net These were IH's thoughts on applicability of CFD to this project",
      "modifiedTime": "2025-03-13T23:43:47.372Z",
      "postId": "AAABdrk-N9A"
    },
    "status": "OPEN"
  },
  {
    "commentId": "AAABdrk-NkY",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org found it -- thanks!",
      "modifiedTime": "2025-03-13T22:14:13.916Z",
      "postId": "AAABdrk-NkY"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "@fletch@hyphae.net",
        "modifiedTime": "2025-03-13T20:27:51.415Z",
        "postId": "AAABdrk-Nkc"
      },
      {
        "authorName": "Stephanie Piper",
        "content": "",
        "modifiedTime": "2025-03-13T22:14:13.916Z",
        "postId": "AAABdrk-NzQ"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdrk-L_4",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@ericd@hyphae.net I will clarify this further but this gives you an idea of our question",
      "modifiedTime": "2025-03-19T15:18:09.974Z",
      "postId": "AAABdrk-L_4"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-03-19T15:18:09.974Z",
        "postId": "AAABgfANyNc"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABe110gKI",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org",
      "modifiedTime": "2025-03-19T15:18:15.228Z",
      "postId": "AAABe110gKI"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-03-19T15:18:15.228Z",
        "postId": "AAABgfANyNg"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdpj48bc",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net Check my work",
      "modifiedTime": "2025-02-13T19:17:03.662Z",
      "postId": "AAABdpj48bc"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-13T19:17:03.662Z",
        "postId": "AAABd_TOQSY"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdpj48bY",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net",
      "modifiedTime": "2025-02-18T20:47:37.836Z",
      "postId": "AAABdpj48bY"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-18T20:47:37.836Z",
        "postId": "AAABeYeUJgU"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdpj48Xc",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@adessler@tamu.edu @spiper@harcresearch.org",
      "modifiedTime": "2025-02-18T20:47:42.311Z",
      "postId": "AAABdpj48Xc"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-18T20:47:42.311Z",
        "postId": "AAABeYeUJgY"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdpj48EM",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net Here is the budget scope for the middle tier",
      "modifiedTime": "2025-02-13T19:17:08.923Z",
      "postId": "AAABdpj48EM"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-13T19:17:08.923Z",
        "postId": "AAABd_TOQSc"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABeYeTG_4",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org @adessler@tamu.edu Could we explicitly mention how findings will be shared with policymakers (e.g., policy briefs, municipal partnerships, integration into existing climate adaptation plans).",
      "modifiedTime": "2025-02-18T20:30:59.154Z",
      "postId": "AAABeYeTG_4"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "",
        "modifiedTime": "2025-02-18T20:30:59.154Z",
        "postId": "AAABeYeUJe0"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABeYeSDGU",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org @adessler@tamu.edu Can we add specificity by referencing local/state agencies (e.g., Houston’s Office of Sustainability, Texas Commission on Environmental Quality) that could adopt recommendations.",
      "modifiedTime": "2025-02-18T20:31:00.310Z",
      "postId": "AAABeYeSDGU"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "",
        "modifiedTime": "2025-02-18T20:31:00.310Z",
        "postId": "AAABeYeUJe4"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdeYYdAg",
    "headPost": {
      "authorName": "Stephanie Piper",
      "content": "@max@hyphae.net let me know if this works!",
      "modifiedTime": "2025-02-18T19:25:31.801Z",
      "postId": "AAABdeYYdAg"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-18T19:25:31.801Z",
        "postId": "AAABdeYYdA4"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdeYYc-o",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net @adessler@tamu.edu @spiper@harcresearch.org can you confirm that this is accurate. Seems like some of the graphs are zip code based. Not sure how it should be characterized in text as zip or county or census. https://publichealth.harriscountytx.gov/Portals/hcph/Documents/Reports/REPORT_Heat-2024-FINAL.pdf",
      "modifiedTime": "2025-02-18T19:23:40.286Z",
      "postId": "AAABdeYYc-o"
    },
    "replies": [
      {
        "authorName": "Daniel Fleischer",
        "content": "",
        "modifiedTime": "2025-02-18T19:23:40.286Z",
        "postId": "AAABdeYYdAY"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdeYYc9E",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@spiper@harcresearch.org Confirming if we can add this person",
      "modifiedTime": "2025-02-18T19:25:29.820Z",
      "postId": "AAABdeYYc9E"
    },
    "replies": [
      {
        "authorName": "Stephanie Piper",
        "content": "if we can edit personnel later then leave her off for now; we are still sorting through hours allocation here with the funding interruptions so schedules are in flux",
        "modifiedTime": "2025-02-18T19:24:47.725Z",
        "postId": "AAABdeYYdAk"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-18T19:25:29.820Z",
        "postId": "AAABdeYYdA0"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdbS07Ag",
    "headPost": {
      "authorName": "Andrew Dessler",
      "content": "my guess is that they are not going to be interested in this",
      "modifiedTime": "2025-02-18T19:14:42.603Z",
      "postId": "AAABdbS07Ag"
    },
    "replies": [
      {
        "authorName": "Daniel Fleischer",
        "content": "",
        "modifiedTime": "2025-02-18T19:14:42.603Z",
        "postId": "AAABdeYYc9Q"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdbS07AA",
    "headPost": {
      "authorName": "Andrew Dessler",
      "content": "we should also measure humidity",
      "modifiedTime": "2025-02-18T19:17:19.960Z",
      "postId": "AAABdbS07AA"
    },
    "replies": [
      {
        "authorName": "Daniel Fleischer",
        "content": "",
        "modifiedTime": "2025-02-18T19:17:19.960Z",
        "postId": "AAABdeYYc-I"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdbS06_8",
    "headPost": {
      "authorName": "Andrew Dessler",
      "content": "I think you need to at least mention the modeling framework you'll be using (e.g., WRF)",
      "modifiedTime": "2025-02-18T19:18:24.964Z",
      "postId": "AAABdbS06_8"
    },
    "replies": [
      {
        "authorName": "Daniel Fleischer",
        "content": "",
        "modifiedTime": "2025-02-18T19:18:24.964Z",
        "postId": "AAABdeYYc-U"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdbS06_c",
    "headPost": {
      "authorName": "Andrew Dessler",
      "content": "This looks like it contradicts what you said above, where you said that we need to get away from census tract analyses.  It might be worth really being clear about what's presently available and what we're planning to do.",
      "modifiedTime": "2025-02-18T19:06:34.828Z",
      "postId": "AAABdbS06_c"
    },
    "replies": [
      {
        "authorName": "Daniel Fleischer",
        "content": "",
        "modifiedTime": "2025-02-18T19:06:34.828Z",
        "postId": "AAABdeYYc8M"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABeD_k-Xc",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net Here I stopped editing because we got a little bit ahead of ourselves. Better to first write the more granular two-page Project *Description* before synthesizing that content into the shorter Project Summary",
      "modifiedTime": "2025-02-15T00:29:50.729Z",
      "postId": "AAABeD_k-Xc"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-15T00:29:50.729Z",
        "postId": "AAABdbrlxNY"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABeDxx4yY",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net Put some boiler plate ingredients here for you to cook up into something mouth-watering.",
      "modifiedTime": "2025-02-15T00:29:54.075Z",
      "postId": "AAABeDxx4yY"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-15T00:29:54.075Z",
        "postId": "AAABdbrlxNc"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABd_TOQS8",
    "headPost": {
      "authorName": "Maxwell Pingeon",
      "content": "@fletch@hyphae.net This is the next task for another stream of consciousness discharge",
      "modifiedTime": "2025-02-15T00:29:56.571Z",
      "postId": "AAABd_TOQS8"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-15T00:29:56.571Z",
        "postId": "AAABdbrlxNg"
      }
    ],
    "status": "RESOLVED"
  },
  {
    "commentId": "AAABdpj48vE",
    "headPost": {
      "authorName": "Daniel Fleischer",
      "content": "@max@hyphae.net this is my stream of consciousness first take, please feel free to give it a haircut or repair omissions as you see fit",
      "modifiedTime": "2025-02-13T19:24:23.860Z",
      "postId": "AAABdpj48vE"
    },
    "replies": [
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-13T19:01:53.620Z",
        "postId": "AAABdp35sfY"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "Thanks, will do",
        "modifiedTime": "2025-02-13T19:16:53.449Z",
        "postId": "AAABd_TOQSU"
      },
      {
        "authorName": "Maxwell Pingeon",
        "content": "",
        "modifiedTime": "2025-02-13T19:24:23.860Z",
        "postId": "AAABd_TOQTY"
      }
    ],
    "status": "RESOLVED"
  }
]
```
