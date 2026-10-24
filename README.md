# DataCo Supply Chain & Sales Analytics

**End-to-end analytics portfolio project | Python · MySQL · SQL · Power BI**

An exploratory analysis of the public DataCo Smart Supply Chain dataset, combining data preparation, relational storage, SQL-based analysis, and an interactive Power BI report to examine **sales performance, fulfilment reliability, and cancelled orders**.

**Dataset:** [DataCo Smart Supply Chain for Big Data Analysis — Mendeley Data](https://data.mendeley.com/datasets/8gx2fvg2k6/5)  
**Analysis period:** January 2015 – February 2018  
**Repository:** [Dataco-Supply-Chain](https://github.com/Sumed125/Dataco-Supply-Chain)

## Business questions

- How did revenue and profitability change over time, across markets and product categories?
- Which categories and customer segments contribute most to revenue?
- How reliable is order fulfilment, and how do late-delivery rates differ by shipping mode?
- How many orders were cancelled, and what potential order value was associated with those cancellations?

## Project workflow

```text
DataCo source dataset (CSV)
          ↓
Python: acquisition / cleaning / preprocessing
          ↓
MySQL: relational tables and SQL analysis
          ↓
Power BI: interactive sales, supply-chain and cancellation dashboards
```

**Tools:** Python, MySQL Community Server, SQL, Power BI Desktop. Python dependencies are listed in `Requirements.txt`.

## Executive summary

The analysis reports **$31.6M in net revenue**, **$3.8M in profit**, and approximately **173K non-cancelled orders** over the analysis period. Sales were relatively steady until October 2017, after which reported monthly revenue declined sharply and the category mix changed. Revenue was concentrated in a small number of categories, while delivery reliability remained a major concern: approximately **57%** of the analysed deliveries were classified as late. Separately, **2,855 cancelled orders** represented approximately **$1.4M in potential order value**. These are descriptive findings; the dataset alone does not establish the causes of the revenue shift, delivery delays, or cancellations.

## Key business insights

### 1. Sales performance and product mix

| Metric | Reported result |
|---|---:|
| Total sales | $35.21M |
| Net revenue | $31.6M |
| Total profit | $3.8M |
| Non-cancelled orders | ~173K |

- **Revenue trend:** Monthly revenue averaged approximately **$0.85M** before the late-2017 change. Following October 2017, the documented average was approximately **$0.42M per month**, with a downward trend. This warrants further investigation into data coverage, product assortment, and business changes; it should not automatically be treated as an anomaly to exclude.
- **Category concentration:** Fishing, Cleats, Camping & Hiking, Cardio Equipment, and Women's Apparel together contributed **more than $19M**, approximately **60% of reported net revenue**.
- **Fishing category:** Approximately **$6M** was attributed to Fishing through September 2017; the analysis notes that this category contained one listed product, *Field & Stream Sportsman 16 Gun Fire Safe*. This concentration deserves scrutiny when interpreting category performance.
- **Changing assortment:** The later period shifted toward categories including Computers, Gardening, Crafts, Children's Clothing, and Women's Clothing. The source analysis reports approximately **$0.57M** in Computers revenue during the later-period comparison.

**Business implication:** Revenue dependence on a limited group of products and a substantial late-period mix change suggest a need for category-level monitoring and validation of the underlying business/data transition.

### 2. Market and customer-segment performance

- **Overall market ranking by revenue:** Europe (**~$9.3M**), Latin America (**~$8.8M**), Pacific Asia (**~$7.1M**), USCA (**~$4.3M**), and Africa (**~$2.0M**).
- **Customer segments:** Consumer (**~$16.4M**) was the largest segment, followed by Corporate (**~$9.6M**) and Home Office (**~$5.6M**).
- The analysis notes that regional composition changed in the late-2017 period, with Computers demand concentrated in Europe. Market rankings depend on the period being compared.

**Business implication:** Break down trends by both market and category before attributing overall revenue movements to geographic demand.

### 3. Supply chain and delivery reliability

| Metric | Reported result |
|---|---:|
| Average difference between actual and scheduled shipping dates | 1.62 days |
| Average order-processing lead time | 3.5 days |
| Late deliveries | ~99K of ~173K |
| Overall late-delivery rate | ~57% |

**Late-delivery rate by shipping mode (as reported):**

| Shipping mode | Late-delivery rate |
|---|---:|
| Standard Class | 40% |
| Second Class | 79% |
| First Class | 100% |
| Same Day | 48% |

- Late delivery remained elevated across the analysed period.
- The observed rates varied substantially by shipping mode. **First Class at 100% should be rechecked against the sample size and the late-delivery calculation before drawing operational conclusions.**
- Standard Class accounted for substantial delivery volume in the analysis, so even a lower late rate may represent many delayed deliveries in absolute terms.
- No clear relationship with market or customer segment was observed in the initial descriptive analysis; this is **not** proof that no relationship exists.

**Business implication:** Prioritize a shipping-mode scorecard showing both **late-delivery rate and delayed-order count**, followed by deeper investigation of service promises, shipping timelines, and carrier performance where data is available.

### 4. Cancelled orders and potential exposure

| Metric | Reported result |
|---|---:|
| Cancelled orders | 2,855 |
| Potential order value associated with cancellations | ~$1.4M |
| Estimated unrealized profit | ~$160.5K |
| Suspected-fraud orders | 1,488 |
| Potential value of suspected-fraud orders | ~$741.5K |

- Suspected fraud represented a substantial share of cancelled orders and their potential value.
- The analysis also reports approximately **$668.2K** in value for other cancelled orders.
- **Potential order value is not the same as recognized revenue lost.** Likewise, estimated unrealized profit should not be interpreted as an accounting loss without further assumptions and validation.
- No clear market-level relationship with cancellation was identified in the initial analysis.

**Business implication:** Separate cancellation reasons/statuses, investigate suspected-fraud flags, and assess recoverable demand before estimating financial impact.

## Recommended next investigations

1. **Late-2017 revenue break:** Verify completeness of records, assortment changes, and whether any business or source-system change occurred.
2. **Delivery performance:** Validate shipping-mode denominators and definitions, then compare delayed counts alongside percentages.
3. **Order statuses:** Clarify the business meaning of *Pending*, *Pending Payment*, *Payment Review*, and *On Hold* before treating them as failed or cancelled orders.
4. **Financial measures:** Document how total sales, net revenue, profit, potential cancellation value, and estimated unrealized profit were calculated.

## Power BI report

The Power BI report contains three analytical areas:

- **Sales Performance & Insights:** Revenue, profit, time trends, categories, markets, and customer segments.
- **Supply Chain Performance:** Delivery reliability, lead times, and shipping-mode comparisons.
- **Cancelled Orders:** Cancellation counts, associated potential order value, and suspected-fraud analysis.

**Report file:** `Supply Chain and Sales Dashboard.pbix`

> Add screenshots of each report page here so visitors can review the work without installing Power BI Desktop.

## Reproducing the pipeline

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sumed125/Dataco-Supply-Chain.git
   cd Dataco-Supply-Chain
   ```
2. **Create a Python virtual environment and install dependencies** (Windows CMD):
   ```cmd
   python -m venv .venv
   .venv\Scripts\python.exe -m pip install -r Requirements.txt
   ```
3. **Obtain the source data:** Download the DataCo dataset from the [Mendeley Data page](https://data.mendeley.com/datasets/8gx2fvg2k6/5). Automated retrieval may be restricted by the host; a manual download is a valid alternative. Place source files in the location expected by the preprocessing scripts.
4. **Configure MySQL:** Start MySQL Community Server, create a local database, and execute the table definitions in `schema.txt` after checking them against your MySQL version.
5. **Configure credentials locally:** Copy `sample_credential.json` to `credential.json`, replace placeholders with your own local MySQL settings, and ensure `credential.json` remains excluded from Git.
6. **Run Python preprocessing and loading scripts:** Execute the files under `Python Files/` in their required order, adapting file paths to your local environment. **Exact script commands and expected outputs should be added after testing a clean clone.**
7. **Open and refresh the report:** Open `Supply Chain and Sales Dashboard.pbix` in Power BI Desktop. Update the MySQL connection in **Transform data → Data source settings** and authenticate with your own credentials if refreshing.
8. **Validate:** Check populated table row counts, key relationships, query results, and the report's visuals/filters.

## Data interpretation and limitations

- The source analysis is **descriptive**, not a causal study. Observed changes do not by themselves prove operational or strategic causes.
- Verify the **grain of analysis** (order vs. order line) before comparing counts or computing rates; distinct orders and order items are not interchangeable.
- Reported shipping-mode percentages, particularly the 100% First Class late rate, should be checked against their denominators.
- The reported **1.62-day** shipping difference should be interpreted according to the exact calculation used, including whether early shipments are included.
- Cancelled-order values represent **potential commercial exposure**, not necessarily recognized revenue or realized losses.
- The final reporting period ends in February 2018; verify whether partial-period coverage affects month-to-month comparisons.
- Figures are taken from the project's business-insights analysis and should be reconciled with final dashboard measures before publication.

## Data source and attribution

DataCo Smart Supply Chain for Big Data Analysis, available through [Mendeley Data](https://data.mendeley.com/datasets/8gx2fvg2k6/5). Please consult the dataset page for its attribution and reuse terms.
