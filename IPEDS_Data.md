## About the data

The data is publicly available from National Center of Education Statistics ([NCES](http://nces.ed.gov/ipeds/deltacostproject/)). The Integrated Postsecondary Education Data System (IPEDS) data includes includes academic years from 19887 through 2012. The data derived from the institutional characteristics, finance, enrollment, completions, graduation rates, student financial aid, and human resources IPEDS survey components and a limited number of outside sources. The database contains one observation per institution for each year of data that is available; it includes all institutions that reported institutional characteristic data to IPEDS in the fall of each academic year. 

To allow for trends analyses that are not affected by institutions entering or leaving the dataset, the database includes variables to identify panels of institutions that report data consistently over specified time periods. These institutional panels are referred to as “matched sets.” To be included in the matched set, an institution must have data on three measures—fall full-time equivalent (FTE) student enrollment, instructional expenditures, and student completions—for every year in the panel time period. There are three different matched sets that cover different time periods: 1987-2012, 2002-2012, and 2007-2012.

## Key attributes:

**1. Institutional Characteristics**

- iclevel: Levels of Institution
- instname: Institution Name
- sector: Sector of Institution
- flagship: Flagship institution status
- hbcu: Historically Black College or University status
- hsi: Hispanic Serving Institution status
- medical: Institution grants a medical degree
- hospital: Institution has hospital
- applcn: Total number of applicants
- applcnm: Total number of applicants - male
- applcnw: Total number of applicants - female
- admssn: Total number of admissions
- admssnm: Total number of admissions - male
- admssnw: Total number of admissions - female


**2.**

- inst_grant_avg_amount: Average amount of institutional grants received by full-time first-time degree/certificate-seeking undergraduates
- inst_grant_num: Number of full-time first-time degree/certificate-seeking undergraduates receiving institutional grants
- inst_grant_pct: Percentage of full-time first-time degree/certificate-seeking undergraduates receiving institutional grants
- institutional_grant_aid: Institutional grant aid
- institutional_grant_aid_share: Share of total financial aid from institutional grants
- instname: Institution Name
- instr_sal_as_pct_instrtot: Share of total instructional expenditures for salaries and wages
- instruction_share: Instruction share of education and related expenses
- liabilities07: Total liabilities
- loan_num: Number of full-time first-time degree/certificate-seeking undergraduates receiving student loans
- loan_pct: Percentage of full-time first-time degree/certificate-seeking undergraduates receiving student loans
- net_student_tuition: Net tuition directly from students
- grant01: Pell Grants
- grant02: Other federal grants
- grant03: State grants
- grant05: Institutional grants (funded)
- grant06: Institutional grants (unfunded)
- grant07: total student aid


**3. Finance-expenditures**

- independ01: Expenditures for independent operations - current year total
- independ02: Expenditures for independent operations - salaries and wages
- instruction01: Expenditures for instruction - current year total
- instruction02: Expenditures for instruction - salaries and wages
- instr_sal_as_pct_instrtot: Share of total instructional expenditures for salaries and wages
- instruction_share: Instruction share of education and related expenses
- instsupp_sal_as_pct_instsupptot: Share of total institutional support expenditures for salaries and wages
- instsupp01: Expenditures for institutional support - current year total
- instsupp02: Expenditures for institutional support - salaries and wages
- interest01: Interest - current year total

**4. Finance-revenues**

- investment01: Revenue from investment return
- independent03: Revenue from independent operations
- tuition01: Unrestricted tuition and fees revenue
- tuition02: Restricted tuition and fees revenue
- tuition03: Gross tuition and fees revenue
- nettuition01: Net tuition and fees revenue (sum(tuition03-institutional_grant_aid))
- federal03: Revenue from federal appropriations
- state03: Revenue from state appropriations
- local03: Revenue from local appropriations
- federal07: Revenue from federal grants and contracts
- state06: Revenue from state grants and contracts
- local06: Revenue from local grants and contracts
- federal10: Revenue from federal appropriations, grants and contracts
- state09: Revenue from state and local appropriations, grants and contracts
- private03: Revenue from private gifts, grants, and contracts

**5. Finance-Balance Sheet**

- assets06: Total assets
- liabilities07: Total liabilities
- assets11: Total net assets
- assets15: Net assets end of year

**6. Enrollment**

- fte_count: Total fall FTE student enrollment
- fte12mn: Total 12-month FTE student enrollment
- ftretention_rate: Full-time retention rate
- ft_first_time_first_yr_deg_seek: Total number of full-time first-time degree/certificate-seeking undergraduates
- ftall03: Full-time Age under 18 All
- ftall04: Full-time Age 18-19 All
- ftall05: Full-time Age 20-21 All
- ftall06: Full-time Age 21-24 All
- ftall08: Full-time Age 25-29 All
- ftall09: Full-time Age 30-34 All
- ftall10: Full-time Age 35-39 All
- ftall11: Full-time Age 40-49 All
- ftall12: Full-time Age 50-64 All
- ftall13: Full-time Age 65 and over All
- ftall14: Full-time Age unknown All
- ptall03: Part-time Age under 18 All
- ptall04: Part-time Age 18-19 All
- ptall05: Part-time Age 20-21 All
- ptall06: Part-time Age 21-24 All
- ptall08: Part-time Age 25-29 All
- ptall09: Part-time Age 30-34 All
- ptall10: Part-time Age 35-39 All
- ptall11: Part-time Age 40-49 All
- ptall12: Part-time Age 50-64 All
- ptall13: Part-time Age 65 and over All
- ptall14: Part-time Age unknown All


**7. Completions**

- associatedegrees: Number of associate degrees granted
- bachelordegrees: Number of bachelor's degrees granted
- masterdegrees: Number of master's degrees granted
- doctordegrees: Number of doctoral degrees granted
- totaldegrees_100fte: Total degrees per 100 FTE students
- totalcompletions_100fte: Total completions per 100 FTE students
- totalcompletions: Number of total degrees, awards and certificates granted
- total_full_time_undergraduates: Total number of full-time undergraduate students
- total_full_time_graduates: Total number of full-time graduate students
- total_full_time: Total number of full-time students
- total_undergraduates: Total number of undergraduate students
- total_graduates: Total number of graduate students
- total_enrollment: Total enrollment
- total_enrollment_amin_tot: Total enrollment (American Indian)
- total_enrollment_asian_tot: Total enrollment (Asian)
- total_enrollment_black_tot: Total enrollment (Black)
- total_enrollment_hisp_tot: Total enrollment (Hispanic)
- total_enrollment_white_tot: Total enrollment (White)
- total_enrollment_multi_tot: Total enrollment (Multi)
- total_enrollment_unkn_tot: Total enrollment (Unknown)



**8. Graduation Rates**

- grad_rate_150_n: Number of students graduating within 150 percent of normal time
- grad_rate_150_p: Percentage of students graduating within 150 percent of normal time


**Other**

- academicyear: Academic Year
- state: State
- cpi_index: CPI index
- has_instruction: Reported instructional expenditures
- has_fte: Reported total FTE
- has_completions: Reported total completions
- has_all: Reported instructional expenditures, total FTE, and total completions

