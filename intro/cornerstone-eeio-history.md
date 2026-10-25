---
title: "Origins of the Cornerstone EEIO"
author: Dr. Wesley Ingwersen
---

## Origins of Cornerstone EEIO

Cornerstone EEIO is a continuation of the USEEIO and CEDA EEIO models, built using the both of the best of each model as determined by the developers through [open discussions and analysis](http://github.com/cornerstone-data/methods/discussions). 

CEDA dates back to the early 2000s when Sangwon Suh developed it initially at Leiden University and later at the University of Minnesota  [@suhDevelopingSectoralEnvironmental2005].
 It was initially a U.S. single-region model accompanied by environmental extensions to report many environmental indicators. 
 It was maintained and applied by VitalMetrics for private, public and academic applications. 
 CEDA was expanded to become a global MRIO model focused on GHG emissions before Watershed acquired it in 2023 and GHG emission factors for Scope 3 reporting became its primary purpose, releasing an free version of emissions factors as openCEDA in 2024.

USEEIO was a research product of the U.S. Environmental Protection Agency (USEPA) first released in early 2017 and developed as a fully open-source model [@yangUSEEIONewTransparent2017].
USEEIO built off the contributions of earlier US single-region U.S. EEIO models including the Carnegie Mellon EIO-LCA model [@hendricksonEconomicInputOutput1998;@weber20092002], openIO [@cox2011open], and CEDA, and primary versions include v1 and v2.0 [@ingwersenUSEEIOV20US2022a] were used for multi-indicator assessments.
USEEIO was initially developed for applications of the USEPA's Sustainable Materials Management program. Beginning in 2020 the Supply Chain GHG Emission Factors were created from USEEIO for Scope 3 reporting, initially at the request of the EPA Center for Corporate Climate Leadership and later continued at the request of the White House Office of Sustainability and the General Services Administration [@ingwersenSupplyChainGreenhouse2020;@ingwersen_supply_2024] and became the most popular use of the model and one of the USEPA's most popular open source datasets.
The limitations of the single-region for modeling consumption impacts in the U.S. were addressed in late v2 models by coupling them with global MRIO models [@ingwersenEstimatingEmbodiedEnvironmental2024], one of which was CEDA [@ingwersenUSEEIOModelsImport2024]. 
The USEPA ceased updating the USEEIO models in 2025.

A primary motivation for the formation of the Cornerstone Sustainability Data Initiative (Cornerstone) was to continue the USEEIO model and to bring it together with CEDA [@watershedSolidifyingFoundationsGlobal2025].  
While the [first release](../releases/index.md) of Cornerstone EEIO is in 2026, the model is only "new" in the sense of the reconciliation of the methods behind USEEIO and CEDA, major methodological innovations
including ABSR and nowcasting US tables that have been added (see a complete list under Releases), and assembly through a new data pipeline.
