# Input workbook format

The **timetable** and **date-sheet** generators accept the **same Excel workload file**, not a separate date-sheet input. The upload dialog and server accept **`.xlsx` and `.xlsm`**. CSV, PDF, `.xls` and `.ods` are not supported for direct upload.

A workbook may contain several sheets. The importer scans for a header row containing **Course Code** (or **Course No.**) and **Credit Hours**. It recognizes both of the formats below; column order can vary because headers are matched by name. It ignores sheets without a suitable header and filters out sections that are not recognized as Agronomy classes.

## Format A — Teacher-wise / Annexure A workload

| Name + CNIC | Course Code | Course Title | Credit Hours | Class | Semester | No. of Students |
|---|---|---|---|---|---|---|
| Dr. Sample Teacher A | AGR-503 | Crop Production Principles | 3(2-1) | BS-AGES-BWP-5TH-AGRON-M | 5th | 25 |
| *(blank — same teacher)* | AGR-505 | Crop Physiology | 3(2-1) | BS-AGES-BWP-5TH-AGRON-M | 5th | 25 |
| Dr. Sample Teacher C | AGR-701 | Advanced Agronomic Research | 3(3-0) | MSAGRO-1st-1E | 1st | 12 |

- Accepts headings **Name + CNIC**, **Name/Designation/CNIC** or equivalent `Name`, plus **Class** and **Semester**.
- A teacher's name only needs to appear on the first course row of that teacher's group; following blank teacher cells inherit that name. Ordinary (unmerged) cells also work. The app attempts to remove a CNIC-formatted value from teacher labels in generated outputs, but you should **remove personal identifiers before sharing the workbook**.
- The **Semester** field can distinguish 1st, 2nd and 3rd postgraduate cohorts.
- Download an example from this chat's release bundle or run the [template generator](examples/generate_input_templates.py) after installing dependencies.

## Format B — Legacy course-allocation workbook

| Name of Teacher | Course Code | Course Title | Credit Hours | Associated Sections | Student Strength |
|---|---|---|---|---|---|
| Dr. Sample Teacher A | AGR-503 | Crop Production Principles | 3(2-1) | BS-AGES-BWP-5TH-AGRON-M | 25 |
| *(blank — same teacher)* | AGR-505 | Crop Physiology | 3(2-1) | BS-AGES-BWP-5TH-AGRON-M | 25 |
| Dr. Sample Teacher C | AGR-701 | Advanced Agronomic Research | 3(3-0) | MSAGRO-1st-1E | 12 |

- The preferred sheet name is `Courses with MSc`, but other sheet names can be detected by their column headings.
- Supported aliases include **Course No.**, **Title of the Course**, **Course Incharge**, **Section**, and **Student Strength**.

## Fields that matter

| Field | Rules |
|---|---|
| Instructor name | A nonempty name must be available for each course (or inherited from an earlier row); teacher names are used to prevent timetable and exam clashes. |
| Course Code / Course No. | Must begin with a letter and include a hyphen followed by a three-digit course number, e.g. `AGR-503` or `SS-701`. |
| Credit Hours | `3(2-1)` = two theory sessions and one practical component; `4(3-1)` also supported; `3(3+0)` theory-only, `3(0-3)` practical-only. |
| Class / Associated Sections | Must identify the correct Agronomy cohort, e.g. `BS-AGES-BWP-5TH-AGRON-M`, `BS-AGES-BWP-6TH-AGRON-M`, `MSAGRO-1st-1E` or `MSAGRO-2nd-1E`. Other programmes can be ignored. |
| Semester (where present) | Use `5th`–`8th` for B.Sc or `1st`–`3rd` for postgraduate cohorts; its own field is especially useful for separate postgraduate semesters. |
| No. of Students / Student Strength | May be a number. Used for date-sheet reporting; the importer accepts a missing value but the produced sheet may lack accurate strength. |
| Course Title | Recommended for human-readable outputs. |

**Important:** The generator does not infer arbitrary class names. A workbook with otherwise valid-looking courses but unrecognized Agronomy section labels may produce no output; compare with the examples and/or adapt the `detect_group` function in `timetable_generator.py` for different universities.

## How to make usable sample Excel files

After running `python -m pip install -r requirements.txt` in the project folder:

```bash
python examples/generate_input_templates.py
```

The command writes two fictional, reusable workbooks into `examples/`:

- `sample_workload_annexure_a.xlsx` (the app's **Try sample workload** button uses this format)
- `sample_course_allocation.xlsx`

**Both files use synthetic teacher names and course allocations.** They are demonstrations of the accepted structure, not an actual university workload or a validated academic timetable.

## Examination date-sheet inputs

Upload the same workload file, select **Mid Term** or **Final Term**, set the exam start date, configure rooms and provide an invigilator roster in the app. The date-sheet engine derives exams from course entries; no separate examination XLSX is required. Practical-only courses are omitted from **Mid Term** date sheets. Exam schedules should be checked by a responsible academic coordinator before use.
