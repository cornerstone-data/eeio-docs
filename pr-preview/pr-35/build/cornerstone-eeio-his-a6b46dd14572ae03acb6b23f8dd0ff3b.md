---
title: "Origins of the Cornerstone EEIO"
author: Dr. Wesley Ingwersen and Dr. Sangwon Suh
---

:::{tip} Summary
Cornerstone EEIO is a continuation of the USEEIO and CEDA EEIO models, built from the best of each model as determined by the developers through [open discussions and analysis](http://github.com/cornerstone-data/methods/discussions).
:::

## CEDA

CEDA (Comprehensive Environmental Data Archive) originated in 2000, when Sangwon Suh then at Leiden University first released it as an Excel version on the web.
Built on environmentally extended input–output analysis, CEDA was designed to support life cycle assessment (LCA) and quantify supply-chain environmental impacts across multiple indicators through an LCA software tool, SimaPRO [@suhMissingInventoryEstimation2002].
CEDA continued to evolve and its compilation method and data were published in Economic Systems Research in 2005 [@suhDevelopingSectoralEnvironmental2005].
In the same year, Suh founded VitalMetrics, which continued to develop, maintain, and commercialize CEDA for applications in industry, government, and academia.
Over the following two decades, CEDA evolved into a global multi-regional input–output (MRIO) model covering approximately 400 sectors across 148 countries and regions. Following Watershed’s acquisition of VitalMetrics in 2023, CEDA became an important data foundation for corporate Scope 3 GHG accounting.
In 2025, Watershed made a freely accessible version of CEDA available as Open CEDA 2024, which was further developed into open CEDA 2025 through Cornerstone [@openceda2025].

## USEEIO

USEEIO was a research product of the U.S. Environmental Protection Agency (USEPA), first released in early 2017 and developed as a fully open-source model [@yangUSEEIONewTransparent2017].
USEEIO built on the contributions of earlier U.S. single-region EEIO models, including the Carnegie Mellon EIO-LCA model [@hendricksonEconomicInputOutput1998;@weber20092002], openIO [@cox2011open], and CEDA. Its primary versions are v1 and v2.0 [@ingwersenUSEEIOV20US2022a].
USEEIO was initially developed for multi-indicator assessments for the USEPA's Sustainable Materials Management program.
Beginning in 2020, the Supply Chain GHG Emission Factors were created from USEEIO for Scope 3 reporting, first at the request of the USEPA Center for Corporate Climate Leadership and later at the request of the White House Office of Sustainability and the General Services Administration [@ingwersenSupplyChainGreenhouse2020;@ingwersen_supply_2024]. They became the most popular use of the model and one of the USEPA's most popular open-source datasets.
The limitations of a single-region model for estimating consumption-based impacts in the U.S. were addressed in later v2 models by coupling them with global MRIO models [@ingwersenEstimatingEmbodiedEnvironmental2024], one of which was CEDA [@ingwersenUSEEIOModelsImport2024].
The USEPA ceased updating the USEEIO models in 2025 [@stevensPopularEPADatabase2025].

## Cornerstone EEIO

A primary motivation for forming the Cornerstone Sustainability Data Initiative (Cornerstone) was to continue the USEEIO model and to bring it together with CEDA [@watershedSolidifyingFoundationsGlobal2025].
Although the [first release](../releases/index.md) of Cornerstone EEIO came in 2026, the model is "new" only in that it reconciles the methods behind USEEIO and CEDA, adds major methodological innovations such as ABSR and nowcast U.S. tables, and is assembled through a new data pipeline. Read more about these innovations in [Releases](../releases/index.md).
