---
title: "Origins of the Cornerstone EEIO"
author: Dr. Wesley Ingwersen
---

## Origins of Cornerstone EEIO

Cornerstone EEIO is a continuation of the USEEIO and CEDA EEIO models, built from the best of each model as determined by the developers through [open discussions and analysis](http://github.com/cornerstone-data/methods/discussions).

CEDA dates back to the early 2000s, when Sangwon Suh developed it, first at Leiden University and later at the University of Minnesota [@suhDevelopingSectoralEnvironmental2005].
It began as a U.S. single-region model with environmental extensions covering many environmental indicators.
VitalMetrics maintained it and applied it in private, public and academic work.
CEDA was expanded into a global MRIO model focused on GHG emissions before Watershed acquired it in 2023. Under Watershed, GHG emission factors for Scope 3 reporting became its primary purpose, and in 2025 Watershed released a free version of the emission factors as Open CEDA.

USEEIO was a research product of the U.S. Environmental Protection Agency (USEPA), first released in early 2017 and developed as a fully open-source model [@yangUSEEIONewTransparent2017].
USEEIO built on the contributions of earlier U.S. single-region EEIO models, including the Carnegie Mellon EIO-LCA model [@hendricksonEconomicInputOutput1998;@weber20092002], openIO [@cox2011open], and CEDA. Its primary versions are v1 and v2.0 [@ingwersenUSEEIOV20US2022a].
USEEIO was initially developed for multi-indicator assessments for the USEPA's Sustainable Materials Management program.
Beginning in 2020, the Supply Chain GHG Emission Factors were created from USEEIO for Scope 3 reporting, first at the request of the EPA Center for Corporate Climate Leadership and later at the request of the White House Office of Sustainability and the General Services Administration [@ingwersenSupplyChainGreenhouse2020;@ingwersen_supply_2024]. They became the most popular use of the model and one of the USEPA's most popular open-source datasets.
The limitations of a single-region model for estimating consumption-based impacts in the U.S. were addressed in later v2 models by coupling them with global MRIO models [@ingwersenEstimatingEmbodiedEnvironmental2024], one of which was CEDA [@ingwersenUSEEIOModelsImport2024].
The USEPA ceased updating the USEEIO models in 2025 [@stevensPopularEPADatabase2025].

A primary motivation for forming the Cornerstone Sustainability Data Initiative (Cornerstone) was to continue the USEEIO model and to bring it together with CEDA [@watershedSolidifyingFoundationsGlobal2025].
Although the [first release](../releases/index.md) of Cornerstone EEIO came in 2026, the model is "new" only in that it reconciles the methods behind USEEIO and CEDA, adds major methodological innovations such as ABSR and nowcast U.S. tables, and is assembled through a new data pipeline. Read more about these innovations in [Releases](../releases/index.md).
