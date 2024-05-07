# 15-minute-analysis

## Proposal

Background:  In a 15-minute city, residents have easy access to destinations that are considered to be the minimum standards of living. This includes education, healthcare, and food-related services. These communities are able to walk, ride a bike, or use public transportation to get to such urban functions within 15 minutes. According to these standards, residents are able to grow, learn, and live a content lifestyle by promoting healthy and sustainable commuting practices.

## Objective: Comparative 15 Minute City Analysis of San Diego and Washington D.C.

## Data Usage:

All data used in this project is open source and freely available for use, sharing, and modification.

**Data Considered:**
population, income, hospitals, schools, grocery stores, transporation, parks, and places of worship

### Links:

- **US Public School Data:**
[NCES](https://nces.ed.gov/programs/edge/Geographic/SchoolLocations)

- **US Hospital Data:**
[HIFLD](https://hifld-geoplatform.opendata.arcgis.com/datasets/75079bdea94743bcaca7b6e833692639/explore?location=38.883755%2C-77.045354%2C11.96)

- **DC Bus Stop Data:**
[Open Data DC](https://opendata.dc.gov/datasets/DCGIS::metro-bus-stops/explore?location=38.933986%2C-77.055527%2C10.51) 

- **DC Park Data:**
[Open Data DC](https://opendata.dc.gov/datasets/287eaa2ecbff4d699762bbc6795ffdca_9/explore?location=38.933414%2C-77.010985%2C11.04)

- **DC Places of Worship Data:**
[Open Data DC](https://opendata.dc.gov/datasets/b134de8f8eaa49499715a38ba97673c8_5/explore?location=38.894665%2C-77.006365%2C12.60)

- **DC Grocery Store Data:**
[Open Data DC](https://opendata.dc.gov/datasets/1d7c9d0e3aac49c1aa88d377a3bae430_4/explore)

- **SD Transit Stop Data:**
[Data SD](https://data.sandiego.gov/datasets/transit-stops/)

- **SD Park Data:**
[Data SD](https://data.sandiego.gov/datasets/park-locations/)

- **SD Grocery Store Data:**
[SANDAG](https://rdw.sandag.org/Account/gisdtview?dir=Business)

- **SD Places of Worship Data:**
[SANDAG](https://rdw.sandag.org/Account/gisdtview?dir=Place)

## Workflow: 
- Write and submit proposal.
- Find data.
- Import datasets in Jupyterhub.
- Clean up data and create isochrones for measuring distance from service areas
- Create buffer/spatial network using population center of SD and DC. Analyze our findings to see what areas include or lack the minimum standards of living.

## Task Distribution

**Robert:**   
- Project management
- Data Import/Clean-up for San Diego
- Spatial analysis using interpolation approach
- Notebook annotation
- Repository maintenance

**Giovanni:**  
- Data Import/Clean-up for Washington DC
- Spatial analysis using interpolation approach
- Visualize access centers & services
- Notebook annotation

**Joseph**

- Data Search/Clean-up for San Diego & Washington DC
- Spatial analysis using population center approach
- Visualize access centers/popultion distribution
- Graph final results

**Cara**

- Data search/Clean-up for San Diego
- Spatial analysis using population center approach
- Visualize population distribution
- Notebook annotation

**All:**

- Prepare presentation

## Conclusions

This project set out to evaluate the distribution of essential amenities within a 15-minute
walking or biking distance in two major U.S. cities, San Diego and Washington D.C., to assess
how well each city adheres to the 15-minute city concept. The analysis included a
comprehensive examination of access to parks, healthcare facilities, schools, transit stops, and
grocery stores, which are crucial for urban living. In San Diego, the results indicate a significant
disparity in access to amenities. Approximately 453,992 people live in areas with access to all
specified amenities within a 15-minute reach, representing a smaller portion of the population
compared to the 920,725 who reside in areas without such access. This suggests a potential for
urban planning and development efforts to focus on increasing accessibility in underserved areas,
particularly targeting regions that currently lack comprehensive access to these essential services.
Conversely, Washington D.C. shows a more favorable distribution under the 15-minute city
model, with 471,920 residents enjoying complete access to necessary amenities, against 211,234
who do not. This indicates a higher level of integration of essential services within the city's
urban fabric, which supports a sustainable urban environment that facilitates easier and quicker
access to essential services for a larger segment of the population.The per capita income
distribution within accessible areas in Washington D.C. shows a higher concentration in the
middle-income ranges, with the most common incomes between ```$50,000``` and ```$75,000```. This
suggests that the city’s accessible areas cater well to a middle-income demographic, potentially
reflecting a balanced urban planning approach that integrates residential and commercial zones
effectively. San Diego: In contrast, San Diego’s income distribution for accessible areas is
characterized by a broader spread and a significant peak in the lower to middle-income brackets,
mostly between ```$20,000``` and ```$40,000```. This indicates that while accessible amenities are
available, they are predominantly in regions with lower economic resources. The presence of
high-income ranges, though less frequent, also suggests that some affluent communities benefit
from the proximity to essential services.

## Installation Guide

### Prerequisites

Before you begin the installation of the project, you need to set up your Python environment. Anaconda is recommended since it simplifies the management of packages and virtual environments. Jupyter Lab is also recommended for data visualization & analysis. If your system already meets these prerequisite requirements, you can skip ahead to the project installation process.

#### Step 1: Install Anaconda

1. **Download Anaconda**: Visit the [Anaconda download page](https://www.anaconda.com/products/distribution) and download the installer for your operating system.

2. **Run the Installer**: Execute the downloaded file and follow the instructions on the screen.

3. **Verify Installation**: Open a terminal or command prompt and type `conda list`. This will show the installed packages if Anaconda is installed correctly.

#### Step 2: Install Required Python Packages

Use `pip` to install the required Python packages for this project:

```bash
# Update pip
pip install --upgrade pip

# Install the necessary packages
pip install geosnap geopandas pandas matplotlib seaborn shapely pandana quilt3

# Note: 'os' and 'warnings' are part of the standard library and do not need installation.
```
#### Step 3: Install and Launch JupyterLab

JupyterLab is an interactive development environment that allows users to work with notebook, markdown, and python files. Follow these steps to install and launch JupyterLab:

```bash
# Install JupyterLab
pip install jupyterlab

## Run Jupyter
jupyter lab
```

### Installation
After setting up your Python environment, you can begin the project set-up process. 

#### Clone the Repository
Clone the project repository to your local machine using the following commands:

```bash
# Clone repository 
git clone https://github.com/robertl0500/15-minute-analysis.git

# Change directory to the cloned repository
cd yourprojectdestination
```

#### Modifying & Sharing Data
Once you have cloned the repository, you can modify and share the data as needed to fit your specific analysis requirements. The repository includes a series of Jupyter notebooks that serve as examples and guides for how to use the data and the tools provided in the package.

### Known Issues

The data used in this package is very resource heavy, which can lead to longer processing times for spatial analyses. Additionally, due to the large size of some datasets, they are unable to be stored on GitHub. To manage this, smaller subsets of data were created.  

### License
This project is licensed under a Creative Commons license. For more information, refer to the License text file in the repository.
