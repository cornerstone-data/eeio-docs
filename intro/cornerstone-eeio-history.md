---
title: "History of the Cornerstone EEIO"
author: Dr. Wesley Ingwersen
---

## Origins of Cornerstone EEIO

Cornerstone EEIO is a continuation of the USEEIO and CEDA EEIO models, built using the both of the best of each model as determined by the developers through [open discussions and analysis](http://github.com/cornerstone-data/methods/discussions). 
CEDA dates back to the early 2000s when Sangwon Suh developed it at the University of Minnesota  [@suhDevelopingSectoralEnvironmental2005]. It was initially a US single-region model accompanying by environmental extensions for many release types. It was later expanded by Suh's company, VitalMetrics, into a global MRIO model, CEDA Global, which by the time Watershed acquired VitalMetrics in 2023 covered 148 countries. Under Watershed, the model focused on GHG emissions, GHG emission factors for Scope 3 reporting became its primary purpose, and starting with CEDA 2024 all versions were global.
USEEIO was a research product of the U.S. Environmental Protection Agency (USEPA) first released in early 2017 [@yangUSEEIONewTransparent2017]. USEEIO built off the contributions of earlier US single-region EEIO models including the Carnegie Mellon EIO-LCA model, openIO, and CEDA, and primary versions include v1 and v2.0 [@ingwersenUSEEIOV20US2022a] were used for multi-indicator assessments.
Initially developed primarily for applications of the USEPA's Sustainable Materials Management program, the Supply Chain Emission Factors were developed for Scope 3 reporting initially at the request of the EPA Center for Corporate Climate Leadership and later continued at the request of the White House Office of Sustainability and the General Services Administration [@ingwersenSupplyChainGreenhouse2020;@ingwersen_supply_2024] and became the most popular use of the model and one of the USEPA's most popular open source datasets.
The limitations of the single-region for modeling consumption impacts in the U.S. were addressed in late v2 models by coupling them with global MRIO models [@ingwersenEstimatingEmbodiedEnvironmental2024], one of which was CEDA [@ingwersenUSEEIOModelsImport2024]. 
The USEPA ceased updating the USEEIO model in 2025.

A primary motivation for the formation of the Cornerstone Sustainability Data Initiative (Cornerstone) was to continue maintaining the USEEIO model and to bring it together with CEDA.  
While the [first release](../releases/index.md) of Cornerstone EEIO is in 2026, the model is only "new" in the sense of the reconciliation of the methods behind USEEIO and CEDA, major methodological innovations
including ABSR and nowcasting US tables that have been added (see a complete list under Releases), and assembly through a new data pipeline.
