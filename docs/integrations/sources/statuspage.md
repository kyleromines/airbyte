# Statuspage.io API

## Sync overview

This source can sync data from the [Statuspage.io API](https://developer.statuspage.io). At present this connector only supports full refresh syncs meaning that each time you use the connector it will sync all available records from scratch. Please use cautiously if you expect your API to have a lot of records.

## This Source Supports the Following Streams

- pages
- subscribers
- subscribers_histogram_by_state
- incident_templates
- incidents
- components
- metrics

### Features

| Feature           | Supported?\(Yes/No\) | Notes |
| :---------------- | :------------------- | :---- |
| Full Refresh Sync | Yes                  |       |
| Incremental Sync  | No                   |       |

### Performance considerations

Mailjet APIs are under rate limits for the number of API calls allowed per API keys per second. If you reach a rate limit, API will return a 429 HTTP error code. See [here](https://developer.statuspage.io/#section/Rate-Limiting)

## Getting started

### Requirements

- Statuspage.io API KEY

## Changelog

<details>
  <summary>Expand to review</summary>

| Version | Date       | Pull Request                                              | Subject                                         |
|:--------|:-----------| :-------------------------------------------------------- | :---------------------------------------------- |
| 0.2.20 | 2025-05-04 | [58977](https://github.com/airbytehq/airbyte/pull/58977) | Update dependencies |
| 0.2.19 | 2025-04-19 | [58388](https://github.com/airbytehq/airbyte/pull/58388) | Update dependencies |
| 0.2.18 | 2025-04-12 | [57935](https://github.com/airbytehq/airbyte/pull/57935) | Update dependencies |
| 0.2.17 | 2025-04-05 | [57421](https://github.com/airbytehq/airbyte/pull/57421) | Update dependencies |
| 0.2.16 | 2025-03-29 | [56897](https://github.com/airbytehq/airbyte/pull/56897) | Update dependencies |
| 0.2.15 | 2025-03-22 | [56253](https://github.com/airbytehq/airbyte/pull/56253) | Update dependencies |
| 0.2.14 | 2025-03-08 | [55625](https://github.com/airbytehq/airbyte/pull/55625) | Update dependencies |
| 0.2.13 | 2025-03-01 | [55120](https://github.com/airbytehq/airbyte/pull/55120) | Update dependencies |
| 0.2.12 | 2025-02-22 | [54481](https://github.com/airbytehq/airbyte/pull/54481) | Update dependencies |
| 0.2.11 | 2025-02-15 | [54104](https://github.com/airbytehq/airbyte/pull/54104) | Update dependencies |
| 0.2.10 | 2025-02-08 | [53588](https://github.com/airbytehq/airbyte/pull/53588) | Update dependencies |
| 0.2.9 | 2025-02-01 | [53092](https://github.com/airbytehq/airbyte/pull/53092) | Update dependencies |
| 0.2.8 | 2025-01-25 | [52459](https://github.com/airbytehq/airbyte/pull/52459) | Update dependencies |
| 0.2.7 | 2025-01-18 | [51971](https://github.com/airbytehq/airbyte/pull/51971) | Update dependencies |
| 0.2.6 | 2025-01-11 | [51401](https://github.com/airbytehq/airbyte/pull/51401) | Update dependencies |
| 0.2.5 | 2025-01-04 | [50749](https://github.com/airbytehq/airbyte/pull/50749) | Update dependencies |
| 0.2.4 | 2024-12-21 | [50348](https://github.com/airbytehq/airbyte/pull/50348) | Update dependencies |
| 0.2.3 | 2024-12-14 | [49782](https://github.com/airbytehq/airbyte/pull/49782) | Update dependencies |
| 0.2.2 | 2024-12-12 | [49426](https://github.com/airbytehq/airbyte/pull/49426) | Update dependencies |
| 0.2.1 | 2024-08-16 | [44196](https://github.com/airbytehq/airbyte/pull/44196) | Bump source-declarative-manifest version |
| 0.2.0 | 2024-08-14 | [44061](https://github.com/airbytehq/airbyte/pull/44061) | Refactor connector to manifest-only format |
| 0.1.13 | 2024-08-12 | [43866](https://github.com/airbytehq/airbyte/pull/43866) | Update dependencies |
| 0.1.12 | 2024-08-10 | [43525](https://github.com/airbytehq/airbyte/pull/43525) | Update dependencies |
| 0.1.11 | 2024-08-03 | [43208](https://github.com/airbytehq/airbyte/pull/43208) | Update dependencies |
| 0.1.10 | 2024-07-27 | [42596](https://github.com/airbytehq/airbyte/pull/42596) | Update dependencies |
| 0.1.9 | 2024-07-20 | [42324](https://github.com/airbytehq/airbyte/pull/42324) | Update dependencies |
| 0.1.8 | 2024-07-13 | [41828](https://github.com/airbytehq/airbyte/pull/41828) | Update dependencies |
| 0.1.7 | 2024-07-10 | [41413](https://github.com/airbytehq/airbyte/pull/41413) | Update dependencies |
| 0.1.6 | 2024-07-09 | [41290](https://github.com/airbytehq/airbyte/pull/41290) | Update dependencies |
| 0.1.5 | 2024-07-06 | [40902](https://github.com/airbytehq/airbyte/pull/40902) | Update dependencies |
| 0.1.4 | 2024-06-26 | [40182](https://github.com/airbytehq/airbyte/pull/40182) | Update dependencies |
| 0.1.3   | 2024-06-20 | [#38662](https://github.com/airbytehq/airbyte/pull/38662) | Make connector compatible with Builder          |
| 0.1.2   | 2024-06-04 | [39064](https://github.com/airbytehq/airbyte/pull/39064) | [autopull] Upgrade base image to v1.2.1 |
| 0.1.1   | 2024-05-20 | [38451](https://github.com/airbytehq/airbyte/pull/38451) | [autopull] base image + poetry + up_to_date |
| 0.1.0   | 2022-10-30 | [#18664](https://github.com/airbytehq/airbyte/pull/18664) | 🎉 New Source: Statuspage.io API [low-code CDK] |

</details>
