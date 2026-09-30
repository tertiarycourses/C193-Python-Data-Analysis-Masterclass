# Learner Guide: Python Data Analysis Masterclass

Course Code: C193
Version: v1.0

The slide deck is concept-led. Detailed lab procedures are provided here.

## Topic 01: Data Preparation

pandas foundations · import/export · selection · filtering · cleaning

### Concept deep-dives

#### Analytics, reporting, BI and data science (Slide 21)

These disciplines overlap but answer different needs. Reporting tells stakeholders what happened using agreed definitions; BI enables repeated exploration; analytics investigates drivers and uncertainty; data science may automate predictions or decisions. The useful boundary is the decision and evidence standard, not the job title or tool.

- **Reporting:** Describes agreed metrics from known data.
- **Business intelligence:** Explores patterns through governed dashboards.
- **Analytics:** Tests questions and explains decision-relevant variation.
- **Data science:** Builds and evaluates models or data products.

**Evidence:** Labs 1, 2.

#### Decision-first analytical framing (Slide 22)

Begin with the decision rather than the available columns. State the decision owner, analytical question, population, time window, measure, comparison and guardrail. This framing prevents technically correct analysis that cannot change an action and exposes missing data before work begins.

- **Decision:** What action could change?
- **Question:** What must be learned?
- **Evidence:** Which measure and comparison answer it?
- **Guardrail:** What must not worsen?

**Evidence:** Labs 1, 2.

#### Observational unit and data grain (Slide 23)

The observational unit explains what one row means; grain adds the time and dimensional detail. An order-line table and an order table are not interchangeable even when both contain order_id. Declare grain before deduplication, joins or aggregation because every later denominator and reconciliation depends on it.

- **Unit:** The entity or event represented by one observation.
- **Grain:** The exact level of detail in each row.
- **Key:** Fields expected to identify one row at that grain.
- **Measure:** A value meaningful at the declared grain.

**Evidence:** Labs 1, 2, 3.

#### Data quality dimensions (Slide 24)

Quality is fitness for a stated analytical purpose. Completeness, validity, uniqueness and consistency are separate tests: a value can be present but invalid, unique but inconsistent, or valid yet too old. Profile each dimension against explicit rules and retain exception counts so cleaning remains reviewable.

- **Completeness:** Required values are present.
- **Validity:** Values follow type, range and format rules.
- **Uniqueness:** Declared entities are not duplicated.
- **Consistency:** Values agree across fields and sources.

**Evidence:** Labs 1.

#### Missing data is an analytical signal (Slide 25)

A blank value is not automatically an error and deletion is not automatically neutral. Introductory MCAR, MAR and MNAR language helps explain why missingness may bias results. Compare missing rates by meaningful segments, preserve a missingness flag when useful, and state how the chosen treatment could change totals or distributions.

- **MCAR:** Missingness is unrelated to observed or unobserved values.
- **MAR:** Missingness can be explained by observed variables.
- **MNAR:** Missingness relates to the unseen value itself.
- **Response:** Drop, impute, flag or redesign with documented impact.

**Evidence:** Labs 1, 10.

#### Duplicate records and business keys (Slide 26)

Duplicates are defined relative to grain and a business key. Two identical rows may be an ingestion fault, while repeated customer_id values can be valid transactions. Test the declared key, investigate competing records, document the survivorship rule and reconcile how many rows were retained, removed or aggregated.

- **Exact duplicate:** Every field repeats.
- **Key duplicate:** Declared identifier repeats.
- **Legitimate repeat:** Same entity, different event or time.
- **Resolution:** Keep, aggregate or reject by rule.

**Evidence:** Labs 1, 3.

#### Types, categories and encoding (Slide 27)

A storage type is not the same as a measurement meaning. A customer code made of digits is still categorical; an ordered satisfaction label needs an explicit category order; a date string must become datetime before time arithmetic. Correct dtypes reduce silent sorting, joining and modelling errors.

- **Numeric:** Supports meaningful arithmetic.
- **Categorical:** Represents a controlled set of labels.
- **Datetime:** Preserves calendar and interval semantics.
- **Boolean:** Stores explicit true or false states.

**Evidence:** Labs 1, 2, 8.

#### Reconciliation and an audit trail (Slide 28)

Reconciliation proves that transformation did what was intended. Capture before-and-after row counts, distinct keys, monetary totals and exception counts; then explain each difference through a named rule. A reproducible script, exclusion table and control totals are stronger evidence than a cleaned spreadsheet alone.

- **Before:** Record row count, key count and control totals.
- **Change:** Name the rule and affected records.
- **After:** Recalculate the same controls.
- **Explain:** Account for every difference and exception.

**Evidence:** Labs 1, 3, 9.

#### Population, sample and selection bias (Slide 29)

A precise calculation can still support the wrong population. Define who could appear in the data, who actually appears and who is systematically absent. Convenience samples, voluntary responses and operational filters can distort estimates; describe the target population and limit claims to the represented sample.

- **Population:** All units the claim is intended to cover.
- **Sample:** Observed units used in the analysis.
- **Sampling frame:** Operational list from which units can enter.
- **Selection bias:** Inclusion relates to the outcome or exposure.

**Evidence:** Labs 7, 10.

### Lab 01: Profile and Clean Retail Transactions

**Alignment:** LO1

Audit a synthetic omnichannel retail extract, repair missing and invalid values, remove duplicate records and preserve an exception log.

#### Detailed procedure

1. Open the lab folder and inspect the CSV and data dictionary before running code.
   - `Review README.md and retail_transactions.csv`
2. Create a virtual environment or use Google Colab, then install the required libraries.
   - `python3 -m pip install pandas matplotlib seaborn scikit-learn`
3. Load the CSV, parse order_date and inspect shape, dtypes, head and missing-value counts.
   - `pd.read_csv('retail_transactions.csv', parse_dates=['order_date'])`
4. Flag missing keys, duplicate order_id values, non-positive units and implausible unit prices.
   - `Build Boolean masks and an exceptions DataFrame`
5. Apply the documented cleaning rules without altering the source CSV.
   - `drop_duplicates, fillna, clip and astype`
6. Create revenue and compare revenue by channel before and after cleaning.
   - `assign(revenue=lambda d: d.units*d.unit_price)`
7. Save clean_data.csv, quality_report.csv and the comparison chart.
   - `python3 lab.py`
8. Write a two-sentence interpretation that distinguishes corrected records from business findings.
   - `Complete the Evidence section in README.md`

**Acceptance:** The script runs without error, clean_data.csv has unique order IDs, critical fields are complete and the quality report reconciles every change.

### Lab 02: Select, Filter and Segment Customer Orders

**Alignment:** LO1

Use label-based and position-based selection, Boolean filters and slicing to answer a realistic customer-retention question.

#### Detailed procedure

1. Load customer_orders.csv and set customer_id as the stable index.
   - `df = pd.read_csv(...).set_index('customer_id')`
2. Use loc to select named customers and columns, then use iloc for a positional audit sample.
   - `df.loc[...] and df.iloc[...]`
3. Filter recent high-value customers and at-risk customers using explicit Boolean conditions.
   - `mask = (df['days_since_last_order'] > 90) & ...`
4. Use between and isin to create transparent business segments.
   - `Series.between and Series.isin`
5. Aggregate segment size and average order value.
   - `groupby('segment').agg(...)`
6. Create a labelled bar chart and save the segment extracts.
   - `python3 lab.py`
7. Verify the segment totals do not exceed the source population.
   - `Compare unique customer counts`

**Acceptance:** The loc and iloc samples are saved, every segment rule is reproducible and the chart uses an honest zero baseline.

## Topic 02: Data Transformation

concat · merge · sort · groupby · aggregation · pivot tables

### Concept deep-dives

#### Tidy data and long-form structure (Slide 46)

Tidy data gives pandas operations predictable semantics. Long form is especially useful for grouping, faceting and statistical graphics because variable names and values remain explicit. Wide form can be convenient for presentation, but reshaping must preserve keys, grain and aggregation rules.

- **Variable:** Each measured attribute has its own column.
- **Observation:** Each unit at the declared grain has one row.
- **Value:** Each cell contains one value.
- **Table:** Each observational unit has a coherent table.

**Evidence:** Labs 3, 4.

#### Choose a join from the business question (Slide 47)

A join is a population decision, not merely syntax. Use a left join when the analytical base must be preserved, an inner join only when excluding unmatched records is defensible, and an outer join to diagnose coverage. Validate key types and cardinality before interpreting the result.

- **Base:** Which table defines the required population?
- **Match:** Which key expresses the relationship?
- **Join:** Left, inner or outer based on the decision.
- **Audit:** Inspect matched and unmatched records.

**Evidence:** Labs 3.

#### Join cardinality and row multiplication (Slide 48)

Suppose three order rows and two promotion rows share the same product key: a many-to-many join can create six rows. That multiplication may be valid, but it can also double-count revenue. Use pandas validate=, test key uniqueness and compare row counts and control totals before and after the merge.

- **1 × 1:** One key on each side produces at most one row.
- **n × 1:** Many transactions map to one reference record.
- **1 × n:** One entity expands into several valid events.
- **n × n:** Repeated keys on both sides can multiply rows.

**Evidence:** Labs 3.

#### Unmatched-record audit (Slide 49)

The pandas merge indicator turns join coverage into evidence. Count left_only, right_only and both; inspect rates by source, period or category; and decide whether exceptions indicate stale master data, invalid keys or legitimate new entities. Never silently discard unmatched records.

- **Left only:** Base records with no reference match.
- **Right only:** Reference records never used by the base.
- **Both:** Successfully matched records.
- **Disposition:** Correct, enrich, exclude or escalate by rule.

**Evidence:** Labs 3.

#### Aggregation grain and denominator (Slide 50)

An aggregation changes grain. A monthly-region summary contains one row per month and region, so transaction-level attributes no longer have the same meaning. Name metrics explicitly, retain counts beside means and rates, and reconcile grouped totals to the eligible base population.

- **Group:** Dimensions defining each result row.
- **Measure:** Count, sum, mean, median or rate.
- **Denominator:** Eligible observations behind a rate or mean.
- **Reconcile:** Group results must explain the base population.

**Evidence:** Labs 4, 5.

#### Weighted and unweighted averages (Slide 51)

A mean of group means is valid only when groups should contribute equally. When the overall result represents individuals or transactions, weight each group value by its population or exposure. Always state the weight because revenue-weighted, customer-weighted and time-weighted averages answer different questions.

**Formula:** `x̄w = Σ(wᵢxᵢ) / Σwᵢ`

- **Unweighted:** Every group mean receives equal influence.
- **Weighted:** Influence follows an exposure such as students or sales.
- **Weight:** Must reflect the decision and be non-negative.
- **Check:** Report total weight and compare both results.

**Evidence:** Labs 4, 7.

#### Rates, proportions and explicit bases (Slide 52)

A rate is interpretable only when its base is visible. A 90% SLA rate could mean 9 of 10 cases or 900 of 1,000, which have different stability and operational importance. Report count and rate together, align periods and specify exclusions.

- **Numerator:** Events meeting the stated condition.
- **Denominator:** Eligible opportunities for that event.
- **Period:** Time window shared by numerator and base.
- **Exclusions:** Missing or ineligible records disclosed.

**Evidence:** Labs 4, 5.

#### GroupBy, pivot table and crosstab (Slide 53)

Choose the operation from the output grain. GroupBy is ideal for named metrics, pivot_table for a comparison matrix with repeated values, and crosstab for categorical frequencies. Confirm that fill values and aggregation functions do not hide missing combinations or create false zeros.

- **GroupBy:** Flexible split-apply-combine calculations.
- **Pivot table:** Matrix summary with explicit aggregation.
- **Crosstab:** Counts or proportions for categorical combinations.
- **Reshape:** melt and pivot change layout, not meaning.

**Evidence:** Labs 4.

#### Transformation pipeline controls (Slide 54)

A transformation pipeline should fail visibly when its assumptions are violated. Encode required columns, key uniqueness, allowed ranges and reconciliation tolerances as assertions; use named functions that return new tables; and write an audit summary alongside the analytical output.

- **Contract:** Assert required columns and types.
- **Transform:** Use named, pure stages.
- **Validate:** Check grain, ranges and reconciliations.
- **Publish:** Save outputs with provenance and limitations.

**Evidence:** Labs 3, 4, 9.

### Lab 03: Integrate Orders, Products and Targets

**Alignment:** LO2

Join transaction, product and monthly-target tables with validated keys, cardinality checks and unmatched-record evidence.

#### Detailed procedure

1. Inspect the grain and key uniqueness of each source file.
   - `nunique, duplicated and value_counts`
2. Validate the products key as many-to-one before merging.
   - `merge(..., validate='many_to_one', indicator=True)`
3. Create a month key and merge monthly regional targets.
   - `df['month'] = df.order_date.dt.to_period('M').astype(str)`
4. Review unmatched and duplicated records instead of silently dropping them.
   - `Filter _merge != 'both'`
5. Concatenate an approved late-arriving order batch.
   - `pd.concat([...], ignore_index=True)`
6. Calculate revenue, attainment and category contribution.
   - `assign and groupby`
7. Save the enriched data, join audit and chart.
   - `python3 lab.py`

**Acceptance:** Row counts reconcile, the many-to-one validations pass, unmatched keys are reported and totals before/after integration are explained.

### Lab 04: Summarise Service Operations with GroupBy and Pivot

**Alignment:** LO2

Transform service-ticket data into SLA and workload summaries using named aggregations and pivot tables.

#### Detailed procedure

1. Load ticket data and create resolution_hours and sla_met fields.
   - `pd.to_datetime and vectorised comparison`
2. Group by support_team with named aggregations for volume, median resolution and SLA rate.
   - `groupby(...).agg(ticket_count=..., median_hours=..., sla_rate=...)`
3. Create a multi-index summary by team and priority.
   - `groupby(['support_team','priority'])`
4. Build a pivot table of ticket counts and fill only structurally missing combinations with zero.
   - `pivot_table(..., fill_value=0)`
5. Sort the scorecard by SLA rate and volume to focus management attention.
   - `sort_values`
6. Create a stacked bar chart and save all summaries.
   - `python3 lab.py`
7. Validate the pivot total equals the source ticket count.
   - `assert pivot.to_numpy().sum() == len(df)`

**Acceptance:** The pivot total reconciles, each metric has an explicit denominator and the SLA result is not confused with ticket volume.

## Topic 03: Data Visualization

pandas plots · Matplotlib · Seaborn · chart choice · visual integrity

### Concept deep-dives

#### Pre-attentive attributes guide attention (Slide 72)

Viewers detect position, length, colour and size before consciously reading labels. Use the strongest channel for the decision-critical comparison and reserve saturated colour for emphasis. Decorative variation competes with the evidence and makes patterns harder to verify.

- **Position:** Supports precise comparison along a common scale.
- **Length:** Makes magnitude easy to compare.
- **Colour:** Highlights category or exception when used sparingly.
- **Size:** Attracts attention but is less precise than length.

**Evidence:** Labs 5, 6.

#### Chart selection decision tree (Slide 73)

Chart choice follows the analytical question and data types. A line implies ordered continuity, a bar compares magnitudes, a histogram aggregates a continuous distribution into bins and a scatter plot shows paired observations. Select the simplest encoding that makes the required comparison accurate.

- **Trend:** Line for values across ordered time.
- **Compare:** Bar or dot plot for category magnitude.
- **Distribution:** Histogram, density or box plot.
- **Relationship:** Scatter plot for two numeric variables.

**Evidence:** Labs 5, 6, 7.

#### Visual encoding accuracy (Slide 74)

Humans compare aligned position and length more accurately than angles, areas or colour intensity. Use bars or dots when precise magnitude matters and pies only for a few clear part-to-whole categories. Labels do not fully repair a weak encoding because the visual pattern still guides interpretation.

- **Position:** Most accurately compared on a common scale.
- **Length:** Strong for bars sharing a baseline.
- **Angle and area:** Harder to compare precisely.
- **Colour intensity:** Best for ordered patterns, not exact values.

**Evidence:** Labs 5.

#### Zero baselines and honest axes (Slide 75)

A truncated bar axis exaggerates small differences because bar length carries the claim. Line charts can use a non-zero baseline when change, not total magnitude, is the question, but the range must be visible and context preserved. Never use uneven category spacing to imply a continuous time interval.

- **Bars:** Start at zero because length encodes magnitude.
- **Lines:** May use a focused range when disclosed and justified.
- **Intervals:** Use truthful spacing and consistent time units.
- **Breaks:** Mark discontinuities instead of hiding them.

**Evidence:** Labs 5.

#### Colour accessibility and semantics (Slide 76)

Colour should encode a defined variable or direct attention, not decorate. Use a sequential palette for low-to-high values and a diverging palette only when a meaningful centre such as zero exists. Add labels, shape or position cues so meaning survives colour-vision differences and greyscale printing.

- **Categorical:** Use distinct hues for a small set of groups.
- **Sequential:** Use ordered light-to-dark for magnitude.
- **Diverging:** Centre two directions on a meaningful midpoint.
- **Accessible:** Check contrast and avoid colour-only meaning.

**Evidence:** Labs 5, 6.

#### Histogram bins change the story (Slide 77)

A histogram is a model of a distribution created by binning continuous values. Compare several defensible bin widths and use common bins when groups are overlaid or faceted. Interpret shape, skew, modes and tails together with the sample size rather than treating one bin configuration as the truth.

- **Too few:** Important modes and gaps disappear.
- **Too many:** Random noise appears as structure.
- **Comparison:** Use shared boundaries across groups.
- **Disclosure:** State bin width or count and sample size.

**Evidence:** Labs 7.

#### Box plot anatomy and limitations (Slide 78)

A box plot compresses a distribution into robust summaries and is useful for comparing groups. It does not show every shape, mode or sample size, and its plotted fliers depend on a convention rather than a business rule. Pair it with counts or raw points when those details matter.

- **Median:** Line at the 50th percentile.
- **Box:** Q1 to Q3, the middle 50 percent.
- **Whiskers:** Often extend to 1.5 IQR from the quartiles.
- **Fliers:** Candidates for investigation, not automatic errors.

**Evidence:** Labs 7.

#### Scatter plots, overplotting and trend (Slide 79)

A scatter plot reveals form, direction, strength, clusters and unusual observations between two numerical variables. Dense overlap can hide frequency, so adjust transparency or use hexbin/aggregation. A regression line summarises an association; it does not control confounding or establish time order.

- **Pair:** Each point must represent one matched observation.
- **Overlap:** Use transparency, jitter or aggregation when dense.
- **Trend:** Show a fitted line only with a clear descriptive purpose.
- **Causality:** Association alone cannot identify an intervention effect.

**Evidence:** Labs 6, 10.

#### Decision-ready annotation and context (Slide 80)

A decision-ready chart makes its scope verifiable. Use a message title that stays within the data, label units and time period, show the denominator for rates, cite the source and annotate only material evidence. Include limitations where they affect the decision rather than burying them elsewhere.

- **Message:** State the supported finding in the title.
- **Evidence:** Show units, period, base and comparison.
- **Annotation:** Label the turning point or exception.
- **Caveat:** Disclose uncertainty, exclusions and source.

**Evidence:** Labs 5, 6, 10.

### Lab 05: Visualise Monthly Retail Performance

**Alignment:** LO3

Select chart types for time trend, category comparison and target variance, then annotate the decision signal.

#### Detailed procedure

1. Load monthly_retail.csv, parse month and validate one row per month-region.
   - `read_csv, to_datetime, duplicated`
2. Pivot revenue by region and create a line chart with shared units and restrained colours.
   - `pivot(...).plot.line`
3. Aggregate annual revenue and create a sorted horizontal bar chart.
   - `groupby and barh`
4. Calculate revenue minus target and colour positive/negative variances consistently.
   - `np.where(variance >= 0, ...)`
5. Add titles, units, source period and a concise annotation for the strongest signal.
   - `Axes.set_title, set_ylabel and annotate`
6. Remove non-data ink, use honest axes and export at 160 dpi.
   - `plt.savefig(..., dpi=160, bbox_inches='tight')`
7. Record why each chart matches its analytical question.
   - `Complete chart_rationale.md`

**Acceptance:** All three charts render, labels and units are complete, bars use a zero baseline and the rationale connects chart choice to the question.

### Lab 06: Explore Marketing Relationships and Correlation

**Alignment:** LO3

Use scatter, regression, pair plots and a correlation heatmap to explore marketing performance without causal overclaim.

#### Detailed procedure

1. Load campaign data and classify channel as categorical.
   - `read_csv and astype('category')`
2. Inspect distributions and extreme values before plotting relationships.
   - `describe and quantile`
3. Create a scatter plot of spend versus conversions coloured by channel.
   - `sns.scatterplot`
4. Overlay a regression line for descriptive guidance only.
   - `sns.regplot(scatter=False)`
5. Create a pair plot for numerical fields and a correlation heatmap with annotations.
   - `sns.pairplot and sns.heatmap`
6. Identify the strongest linear association and state why it does not prove causation.
   - `corr().abs() and an interpretation note`
7. Save the correlation table and all graphics.
   - `python3 lab.py`

**Acceptance:** The graphics render, correlation values are reproducible and the interpretation explicitly separates association from causation.

## Topic 04: Data Analysis

data types · descriptive statistics · covariance · correlation · time series

### Concept deep-dives

#### Population, sample, parameter and statistic (Slide 98)

Descriptive statistics summarise observed data, while inferential reasoning uses a sample to learn about a population. A sample mean is not the population mean; its usefulness depends on sampling design, size and variability. Always separate the calculated statistic from the broader claim.

- **Population:** Full group about which a claim is intended.
- **Sample:** Observed subset used for calculation.
- **Parameter:** Unknown population quantity such as μ or σ.
- **Statistic:** Sample estimate such as x̄ or s.

**Evidence:** Labs 7, 10.

#### Measurement scales determine valid analysis (Slide 99)

Measurement scale determines which summaries and operations are meaningful. A mean of unordered category codes is meaningless; a median can suit ordinal ratings; ratios require a true zero. Do not confuse how a value is stored with what its scale permits you to claim.

- **Nominal:** Labels with no inherent order.
- **Ordinal:** Ordered labels with unknown spacing.
- **Interval:** Equal differences without a true zero.
- **Ratio:** Equal differences and a meaningful zero.

**Evidence:** Labs 7.

#### Mean, median and mode under an outlier (Slide 100)

For 12, 13, 13, 14 and 48, the mean is 20 while the median and mode are 13. None is universally best: the mean uses every value, the median resists extremes and the mode identifies the most common value. Choose the statistic that matches the distribution and decision.

**Formula:** `x̄ = Σxᵢ / n`

- **Data:** 12, 13, 13, 14, 48
- **Mean:** 20; pulled upward by 48.
- **Median:** 13; robust midpoint.
- **Mode:** 13; most frequent observed value.

**Evidence:** Labs 7.

#### Quartiles, IQR and the five-number summary (Slide 101)

The five-number summary describes position and spread without assuming a symmetric distribution. IQR measures the middle 50 percent and is robust to extreme values. Percentile algorithms can differ slightly across software, so retain the method when exact boundary decisions matter.

**Formula:** `IQR = Q3 − Q1`

- **Minimum:** Smallest observed value.
- **Q1:** 25th percentile.
- **Median:** 50th percentile.
- **Q3 / maximum:** 75th percentile and largest value.

**Evidence:** Labs 7.

#### Variance and standard deviation (Slide 102)

Sample variance divides the sum of squared deviations by n−1 to estimate population variability. Standard deviation is easier to interpret because it returns to the original unit, but both are sensitive to extreme values. Compare them only for measures with compatible units and meaning.

**Formula:** `s² = Σ(xᵢ − x̄)² / (n − 1)   ·   s = √s²`

- **Deviation:** Distance of each value from the mean.
- **Square:** Prevents positive and negative distances cancelling.
- **Variance:** Average squared deviation using n−1 for a sample.
- **SD:** Square root returns to the original unit.

**Evidence:** Labs 7.

#### Coefficient of variation (Slide 103)

The coefficient of variation expresses standard deviation relative to the mean, making it useful for ratio-scale measures with different magnitudes. It is inappropriate when zero is arbitrary, the mean is near zero or values can cross zero. Report the original-unit mean and SD beside it.

**Formula:** `CV = s / x̄ × 100%`

- **Purpose:** Compares relative spread across different scales.
- **Numerator:** Standard deviation.
- **Denominator:** Mean of the same measure.
- **Caution:** Unstable when the mean is near zero or can be negative.

**Evidence:** Labs 7.

#### Z-scores and unusual observations (Slide 104)

A z-score standardises a value relative to a chosen reference distribution. It supports comparisons across compatible measures and can flag unusual observations, but thresholds assume context and often approximate normality. Investigate provenance before correcting or deleting a flagged record.

**Formula:** `z = (x − x̄) / s`

- **Centre:** Subtract the reference mean.
- **Scale:** Divide by the reference standard deviation.
- **Meaning:** Number of standard deviations from the mean.
- **Caution:** A large z-score is unusual, not automatically wrong.

**Evidence:** Labs 7.

#### Covariance and correlation (Slide 105)

Covariance depends on measurement scale, making magnitudes difficult to compare. Pearson correlation standardises covariance by the variables' standard deviations. Both describe co-movement; neither controls confounding, proves time order or identifies a causal mechanism.

**Formula:** `r = cov(X,Y) / (sX sY)`

- **Covariance:** Direction of joint movement in product units.
- **Correlation:** Standardised association from −1 to +1.
- **Sign:** Shows direction, not importance or causality.
- **Magnitude:** Shows linear strength and is sensitive to outliers.

**Evidence:** Labs 6, 10.

#### Pearson or Spearman correlation (Slide 106)

Pearson correlation suits an approximately linear relationship without dominating outliers. Spearman correlation uses ranks and can capture a monotonic but curved relationship, while handling ordinal data more naturally. Neither coefficient replaces a scatter plot or a careful check for subgroup effects.

- **Pearson:** Linear association between numerical variables.
- **Spearman:** Monotonic association based on ranks.
- **Inspect:** Plot form, outliers, ties and subgroup patterns.
- **Report:** Method, coefficient, sample size and limitation.

**Evidence:** Labs 6, 10.

#### Time-series components (Slide 107)

Time-series observations are ordered and often dependent, so ordinary random comparisons can mislead. Separate level, trend, repeating seasonality and irregular variation conceptually before selecting a baseline. Calendar effects and operational changes should be documented rather than treated as unexplained noise.

- **Level:** Typical magnitude around which a series varies.
- **Trend:** Persistent long-run movement.
- **Seasonality:** Pattern repeating at a known calendar frequency.
- **Irregular:** Residual shocks, noise and anomalies.

**Evidence:** Labs 8.

#### Resampling, rolling windows and leakage (Slide 108)

Resampling changes frequency with an explicit aggregation such as daily maximum or weekly sum. Rolling calculations create trailing features across observations or time offsets. Operational features must never include future values; define whether the current period is included and test boundary behaviour.

- **Parse:** Create valid, timezone-aware timestamps.
- **Order:** Sort and resolve duplicate intervals.
- **Resample:** Aggregate to the decision frequency.
- **Roll:** Use only information available at prediction time.

**Evidence:** Labs 8.

### Lab 07: Analyse Service Quality Distributions

**Alignment:** LO4

Compare centre and spread across service channels and identify candidate outliers without deleting them automatically.

#### Detailed procedure

1. Load service_quality.csv and distinguish categorical from continuous fields.
   - `select_dtypes and astype`
2. Calculate count, mean, median, standard deviation, quartiles and range by channel.
   - `groupby.describe and named agg`
3. Create histograms with common bins and scales.
   - `sns.histplot(..., hue='channel', common_bins=True)`
4. Create a box plot and calculate IQR candidate-outlier thresholds.
   - `quantile and sns.boxplot`
5. Compare the mean and median to diagnose skew.
   - `summary.assign(mean_median_gap=...)`
6. Investigate candidate outliers and retain a review file rather than dropping rows.
   - `Save outlier_review.csv`
7. Write a decision note for the operations manager.
   - `python3 lab.py`

**Acceptance:** Statistics reconcile to the source, candidate outliers remain traceable and the interpretation uses median when the distribution is skewed.

### Lab 08: Resample and Monitor Energy Demand

**Alignment:** LO4

Parse an hourly time series, resample it to daily and weekly frequency, calculate rolling demand and detect peaks without future leakage.

#### Detailed procedure

1. Load the hourly readings, parse timestamp and set a sorted DatetimeIndex.
   - `read_csv(..., parse_dates=['timestamp']).set_index('timestamp').sort_index()`
2. Check frequency, duplicates and missing hourly intervals.
   - `index.to_series().diff and asfreq('h')`
3. Resample demand to daily mean/max and weekly total.
   - `resample('D').agg(...) and resample('W').sum()`
4. Calculate a trailing seven-day rolling mean using only current and past values.
   - `rolling(7, min_periods=3).mean()`
5. Detect peak days above the 95th percentile.
   - `daily['max_kw'] > daily['max_kw'].quantile(.95)`
6. Plot daily maximum with the rolling baseline and peak markers.
   - `Matplotlib line and scatter`
7. Save summaries, exceptions and the chart.
   - `python3 lab.py`

**Acceptance:** The index is complete and sorted, resampled totals are explainable, rolling calculations use no future values and peak days are retained as evidence.

## Topic 05: Advanced Data Analytics

pipe · apply · custom functions · linear regression · credibility review

### Concept deep-dives

#### Four levels of analytics (Slide 126)

The four levels describe increasing decision ambition, not an automatic maturity ladder. A reliable descriptive measure can be more valuable than a weak prediction. Each level requires additional assumptions, validation and governance, especially when moving from association to recommended action.

- **Descriptive:** What happened?
- **Diagnostic:** What factors are associated with it?
- **Predictive:** What may happen under similar conditions?
- **Prescriptive:** Which action best meets an objective and constraints?

**Evidence:** Labs 9, 10.

#### Correlation, regression and causality (Slide 127)

Correlation and regression can describe patterns and support prediction, but a causal claim requires a credible counterfactual design. Confounding, reverse causality, selection and measurement error can create associations. Use causal language only when study design and assumptions support it.

- **Correlation:** Symmetric description of association.
- **Regression:** Conditional outcome estimate given predictors.
- **Prediction:** Performance on unseen cases under similar conditions.
- **Causal effect:** Change attributable to an intervention under a design.

**Evidence:** Labs 6, 10.

#### Simple linear regression model (Slide 128)

Simple linear regression fits the line that minimises squared residuals. The slope is an estimated conditional change, not automatically a causal effect, and the intercept may have little practical meaning when zero is outside the observed range. Interpret coefficients with units, range and uncertainty.

**Formula:** `ŷ = β₀ + β₁x   ·   e = y − ŷ`

- **ŷ:** Predicted outcome for a given x.
- **β₀:** Predicted outcome when x equals zero.
- **β₁:** Estimated change in outcome for one-unit increase in x.
- **e:** Observed minus predicted outcome.

**Evidence:** Labs 10.

#### Interpreting coefficients responsibly (Slide 129)

A coefficient must be translated with both predictor and outcome units. In multiple regression it is conditional on other included predictors, not a standalone relationship. Avoid extrapolation beyond the observed range and acknowledge omitted variables, uncertainty and measurement quality.

- **Direction:** Positive or negative conditional association.
- **Magnitude:** Outcome-unit change per predictor unit.
- **Reference:** Baseline or omitted category for categorical inputs.
- **Scope:** Applies to the fitted population and observed range.

**Evidence:** Labs 10.

#### Train, test and overfitting (Slide 130)

Overfitting occurs when a model learns sample-specific noise that does not generalise. A reproducible train/test split estimates unseen performance, provided leakage and dependence are controlled. Compare train and test metrics, use a baseline and avoid repeatedly tuning against the test set.

- **Split:** Reserve unseen observations before fitting.
- **Train:** Estimate parameters and tune choices.
- **Test:** Evaluate once on held-out data.
- **Compare:** Check generalisation against a simple baseline.

**Evidence:** Labs 10.

#### Residual diagnostics (Slide 131)

Residuals are the part of the outcome not explained by the fitted model. Random scatter around zero is desirable; curves, funnels, runs or group differences signal specification, variance or dependence problems. Diagnostics guide model revision and limitation statements rather than proving the model correct.

- **Residual versus fitted:** Reveals curvature or changing spread.
- **Distribution:** Shows skew and extreme errors.
- **Time order:** Reveals dependence or drift.
- **Segments:** Checks whether errors concentrate in groups.

**Evidence:** Labs 10.

#### MSE, RMSE, MAE and R-squared (Slide 132)

No single metric defines a good model. RMSE and MAE express typical error differently, while R-squared is relative to outcome variation and can be negative on test data. Select metrics from the decision cost, compare against a baseline and evaluate relevant segments.

**Formula:** `MSE = Σe²/n   ·   RMSE = √MSE   ·   MAE = Σ|e|/n`

- **MSE:** Average squared error; strongly penalises large misses.
- **RMSE:** Square root of MSE in outcome units.
- **MAE:** Average absolute error; more robust to large misses.
- **R²:** Variation explained relative to a mean baseline.

**Evidence:** Labs 10.

#### Model credibility and communication (Slide 133)

Credibility comes from a chain of evidence rather than a high headline metric. Review provenance, representativeness, leakage, assumptions, diagnostics, subgroup performance and reproducibility. Communicate what the model can support, what it cannot establish, and what monitoring or further evidence is required before action.

- **Data:** Representative, valid and decision-time available.
- **Method:** Assumptions match design and grain.
- **Evidence:** Held-out metrics, diagnostics and sensitivity checks.
- **Claim:** Action, guardrail and limitation stay within support.

**Evidence:** Labs 9, 10.

### Lab 09: Build a Reusable pandas Analytics Pipeline

**Alignment:** LO5

Refactor a fulfilment analysis into small testable functions connected with pipe, assign and vectorised transformations.

#### Detailed procedure

1. Load fulfilment data and define the expected schema and allowed categories.
   - `EXPECTED_COLUMNS and validation function`
2. Write a validate_input function that raises clear errors before analysis.
   - `def validate_input(df): ...`
3. Write pure functions for cleaning, feature engineering and summarisation.
   - `def clean(df), add_features(df), summarise(df)`
4. Chain the functions with pipe and assign.
   - `df.pipe(validate_input).pipe(clean).pipe(add_features)`
5. Use vectorised np.select for risk bands; reserve apply for a justified custom label.
   - `np.select and DataFrame.apply`
6. Add assertions for row count, non-negative duration and valid risk categories.
   - `assert ...`
7. Save outputs and a late-rate chart by warehouse.
   - `python3 lab.py`

**Acceptance:** The pipeline can be re-run from raw input, validation fails loudly on broken schema, assertions pass and every output is derived without manual edits.

### Lab 10: Capstone: Public Health Insight and Regression Review

**Alignment:** LO1–LO5

Prepare, visualise and model synthetic student-health indicators, then review the credibility of the evidence for a programme decision.

#### Detailed procedure

1. Frame the decision: which modifiable indicators are associated with wellbeing score?
   - `Write the analytical question before opening results`
2. Load and profile the synthetic student-health data; document missingness and ranges.
   - `read_csv, info, describe and isna`
3. Clean data using explicit rules and retain excluded records in an audit file.
   - `Boolean validity mask`
4. Create group summaries and truthful charts for activity, nutrition and wellbeing.
   - `groupby, bar, scatter and heatmap`
5. Split data into train/test sets and fit a linear regression model.
   - `train_test_split and LinearRegression`
6. Evaluate R-squared, MSE and residual patterns on held-out data.
   - `r2_score, mean_squared_error and residual plot`
7. Interpret coefficients as model associations, not causal effects.
   - `Create model_summary.csv and stakeholder_brief.md`
8. Run the credibility checklist for sampling, confounding, measurement and reproducibility.
   - `Complete credibility_review.csv`
9. Package all outputs and confirm another learner can reproduce them with one command.
   - `python3 lab.py`

**Acceptance:** The script reproduces every output, test-set metrics and residuals are reported, causal claims are avoided and limitations are explicit in the stakeholder brief.
