---
id: cand-fresno-rfp-hyphae-2024-s8-2
status: candidate
title: Satellite and medium-resolution data for heat stratification
type: method
summary: Explains use of satellite thermal data, local climate zones, population density, and crop mapping to identify and
  stratify neighborhoods for targeted heat interventions.
words: 190
places: []
orgs: []
projects: []
facts:
- claim: Satellite data is gathered weekly or monthly at relatively high temporal resolution
  quote: it is relatively high temporal resolution, often gathered weekly or monthly
- claim: 100 meter dasymetric population density data is used to estimate where people live or work outdoors
  quote: we use 100 meter dasymetric population density data and Cropscape crop mapping to estimate where people live or are
    likely to be working outdoors
flags: []
quality_notes: Clear explanation of data limitations and applications; generic enough for reuse across heat analysis projects.
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

of the crown, might be quite hot, but that's because it's blocking the sun from the cooler and understory which is not being sensed by the satellite. But if these limitations are known, considered and not ultimately used for final intervention scale analysis, this dataset is really useful because it is relatively high temporal resolution, often gathered weekly or monthly and because it can be used to estimate unmeasured variables like air temperature which can then be fed into our higher resolution models discussed later. Other medium resolution data Local climate zones (LCZ) data is calculated at 30 meter resolution for a single time period and reflects 17 categories of local topology concerning feature types (buildings and vegetation) heights (tall, medium, short, none) and spacing (dense, medium, sparse). This can be used to stratify heat data (such as surface temperature) to prioritize where interventions are most likely to be plausible and effective. Similarly we use 100 meter dasymetric population density data and Cropscape crop mapping to estimate where people live or are likely to be working outdoors to adjust risk factors for heat stress estimates at the 30 meter scale.
