<h1 align="center" style="margin-top: 10px;margin-bottom:10px;text-decoration:underline">Data Science Project</h1>
<p align="center" style="margin-bottom: 0px !important;">
  <img width="200" src="https://gis-bucket-aswinvk28.s3.eu-west-2.amazonaws.com/adp/buildings-and-earthquakes.jpg" alt="Earthquake and Data Science" title="Earthquake and Data Science" align="center">
</p>

# Understand building and land characteristics associated with earthquakes, by getting insights into data.

*A Practical Project undertaken by students at Kingston University for Group 5*

## Introduction

In 1970, a group of architects prepared seismic codes to prevent deaths that occur when buildings collapse (
Guevara-Perez, 2012). Their rigorous building regulations were hugely beneficial in 2011 when a magnitude 9 earthquake
hit the region, one of the largest earthquakes ever recorded. There are many factors that influence the strength of
earthquakes including the magnitude of earthquake, the site's proximity to the fault, the local geology, and the soil
type.

In this project, the field of **Data Science** uses scientific algorithms, methods, and processes to collect, refine and
represent the data in a way that it can describe patterns and observations related to building destruction due to
earthquakes. The obtained patterns and observations can be further analysed, and appropriate actions can be taken by
business or organizations to improve the quality of buildings and land (Dhar, 2013).

<h3 align="center" style="margin-top: 10px;margin-bottom:10px">Data Science Process</h3>

![./images/DS-Process.png](./images/DS-Process.png)

### Problem Statement

This study will address the possible factors behind the major destruction of buildings during the earthquake. The
information on earthquake events and quality of buildings are highly critical for an effective government. An effective
government could implement governance plans and reduce post-earthquake reconstruction. To support this problem statement
various research questions are formed and studied in this report.

### Proposed Approach

(Hoffinann and Schubert, 1994) confirms the compressibility measurements of concrete, and calcium silicate (in N/mm2)
which is used as Building Stone that proves to be a highly durable component in construction. (
Guevara-Perez, 2012) illustrates that the degree of irregularity in the configuration of a building is one of the most
important factors supporting the earthquake-resistant buildings. The dataset given for this project (explained later)
provides count of floors, ground floor type and other floor type attributes which indicate, according to the paper, a
soft-storey and weak-storey irregularity pattern may be explored from a given row of data (a building).

![./images/floor-irregularity.jpg](./images/floor-irregularity.jpg)
<p align="right" style="margin-bottom: 0px !important;font-weight: bold; font-size:11px">
Lateral forces and shear forces generated in buildings due to ground motion, <br/>
Source: (Guevara-Perez, 2012)
</p>

Recognizing the importance of: number of floors; component durability due to cement, mud and stone; roof type;
foundation type; and plan configuration (also attributes in the dataset), urges patterns to be revealed from this
dataset. Data sampling, Exploratory data analysis, data pre-processing, data visualization, and finding real-world
relationships between data attributes and damage grade will uncover seismic vulnerability to buildings.

## Dataset (Attribute Classification)

### :globe_with_meridians: Geographical Attributes

- **1.INT.1** ***geo_level_1_id:*** Level 1 Geographical Region of a building, Ranges from 0-30
- **2.INT.2** ***geo_level_2_id:*** Level 2 Geographical Region of a building, Ranges from 0-1427
- **3.INT.3** ***geo_level_3_id:*** Level 3 Geographical Region of a building, Ranges from 0-12567

### :chart_with_upwards_trend: Numerical Measures

- **4.INT.1** ***count_floors_pre_eq:*** Number of floors of a building before the earthquake
- **5.INT.2** ***age:*** The building age (in years)
- **6.INT.3** ***area_percentage:*** Normalized area of building footprint
- **7.INT.4** ***height_percentage:*** Normalized height of building footprint
- **8.INT.5** ***count_families:*** Number of families that live in a building

### :house_with_garden: Main Building/Land Characteristics

- **9.CATEGORICAL.1** ***ground_floor_type:*** type of the ground floor (GFT), Discrete: f,m,v,x,z
- **10.CATEGORICAL.2** ***other_floor_type:*** type of construction used in higher than the ground floors (except for
  the roof) (OFT), Discrete: j,q,s,x
- **11.CATEGORICAL.3** ***legal_ownership_status:*** legal ownership status of the land where the building was built,
  Discrete: a,r,v,w
- **12.CATEGORICAL.4** ***plan_configuration:*** building plan configuration, Discrete: a,c,d,f,m,n,o,q,s,u

### :office: Sub Building/Land Characteristics

- **13.CATEGORICAL.1** ***land_surface_condition:*** Surface condition of the land where the building was built,
  Discrete: n,o,t
- **14.CATEGORICAL.2** ***foundation_type:*** type of foundation used while building, Discrete: h,i,r,u,w
- **15.CATEGORICAL.3** ***roof_type:*** type of roof used while building, Discrete: n,q,x
- **16.CATEGORICAL.4** ***position:*** Position of the building, Discrete: n,o,t

### :construction: Superstructure Construction Attributes

- **17.BINARY.1** ***has_superstructure_adobe_mud:*** flag variable that indicates if the superstructure was made of
  Adobe/Mud
- **18.BINARY.2** ***has_superstructure_mud_mortar_stone:*** flag variable that indicates if the superstructure was made
  of Mud Mortar - Stone
- **19.BINARY.3** ***has_superstructure_stone_flag:*** flag variable that indicates if the superstructure was made of
  Stone
- **20.BINARY.4** ***has_superstructure_cement_mortar_stone:*** flag variable that indicates if the superstructure was
  made of Cement Mortar - Stone
- **21.BINARY.5** ***has_superstructure_mud_mortar_brick:*** flag variable that indicates if the superstructure was made
  of Mud Mortar - Brick
- **22.BINARY.6** ***has_superstructure_cement_mortar_brick:*** flag variable that indicates if the superstructure was
  made of Cement Mortar - Brick
- **23.BINARY.7** ***has_superstructure_timber:*** flag variable that indicates if the superstructure was made of Timber
- **24.BINARY.8** ***has_superstructure_bamboo:*** flag variable that indicates if the superstructure was made of Bamboo
- **25.BINARY.9** ***has_superstructure_rc_non_engineered:*** flag variable that indicates if the superstructure was
  made of non-engineered reinforced concrete
- **26.BINARY.10** ***has_superstructure_rc_engineered:*** flag variable that indicates if the superstructure was made
  of engineered reinforced concrete
- **27.BINARY.11** ***has_superstructure_rc_engineered:*** flag variable that indicates if the superstructure was made
  of any other material

### :hospital: Secondary Usage Attributes

- **28.BINARY.12** ***has_secondary_use:*** flag variable that indicates if the building was used
  for any secondary purpose
- **29.BINARY.13** ***has_secondary_use_agriculture:*** flag variable that indicates if the
  building was used for agricultural purposes
- **30.BINARY.14** ***has_secondary_use_hotel:*** flag variable that indicates if the building
  was used as a hotel
- **31.BINARY.15** ***has_secondary_use_rental:*** flag variable that indicates if the building
  was used for rental purposes
- **32.BINARY.16** ***has_secondary_use_institution:*** flag variable that indicates if the
  building was used as a location of any institution
- **33.BINARY.17** ***has_secondary_use_school:*** flag variable that indicates if the building
  was used as a school
- **34.BINARY.18** ***has_secondary_use_industry:*** flag variable that indicates if the building
  was used for industrial purposes
- **35.BINARY.19** ***has_secondary_use_health_post:*** flag variable that indicates if the
  building was used as a health post
- **36.BINARY.20** ***has_secondary_use_gov_office:*** flag variable that indicates if the
  building was used fas a government office
- **37.BINARY.21** ***has_secondary_use_use_police:*** flag variable that indicates if the
  building was used as a police station
- **38.BINARY.22** ***has_secondary_use_other:*** flag variable that indicates if the building
  was secondarily used for other purposes

### :x: Damage Impact Attributes

- **39.BINARY.22** ***building_id:*** unique random identifier of a building
- **40.BINARY.22** ***damage_grade:*** represents a level of damage to a building that was hit by earthquake,
    - 1 represents low damage
    - 2 represents a medium amount of damage
    - 3 represents almost complete destruction

The dataset is a structured dataset containing information on geographical attributes and different building and land
attributes/characteristics. The geo levels (geographical) attributes, designate a hierarchy of values increasing from 0
onwards at each level.

