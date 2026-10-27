# Timetable & Examination Date-Sheet Generator

A **local, browser-based Python application** for generating conflict-checked class timetables and mid-term/final-term examination date sheets from departmental Excel course-allocation workbooks. The interface supports configurable rooms and invigilators, individual instructor exports, and editable generated workbooks. The primary implementation was developed for Agronomy programmes; other departments may need changes to section-matching rules.

**Status:** Source release with automated tests and synthetic examples. Inspect generated schedules before official use. No public hosting or production service is provided.

## Run

```bash
python -m pip install -r requirements.txt
python server.py
```

Then open:

```text
http://127.0.0.1:8765
```

**Requirements:** Python 3.10 or newer, a recent web browser, and dependencies in `requirements.txt`. By default the server listens only on `127.0.0.1:8765`. The app processes spreadsheets locally, so do not expose its HTTP server to public networks.

## Workflow

1. Upload the workload Excel workbook.
2. Set term, w.e.f. date, available rooms, and output file name.
3. Generate the timetable.
4. Download the Excel workbook, PDF, individual PNG images, or ZIP bundle.
5. Select an instructor after generation and print that instructor's timetable across all B.Sc and M.Sc/PhD sheets.
6. To generate exam date sheets, use the **same Excel workload**, select exam type and start date, configure invigilators, and download the date-sheet files.

## Workload Formats

**Accepted uploads:** `.xlsx` and `.xlsm` Excel workbooks. **Not supported for upload:** CSV, `.xls`, PDF and `.ods`. The timetable and date-sheet tools use the same workload input.

See **[INPUT_FORMAT.md](INPUT_FORMAT.md)** for exact columns, example rows, course/semester rules, and [a template-generation script](examples/generate_input_templates.py). Download the bundled synthetic sample workbooks, or run `python examples/generate_input_templates.py` after installing the requirements. The **Try sample workload** button uses the fictional `examples/sample_workload_annexure_a.xlsx` file.

- Existing course-allocation workbooks remain supported.
- Teacher-wise Annexure A workbooks are also supported: `Name + CNIC`, `Course Code`, `Course Title`, `Credit Hours`, `Class`, `Semester`, and `No. of Students`.
- Instructor names spanning merged rows are carried through their course rows. CNIC numbers are removed from instructor names in generated outputs.
- B.Sc Agronomy semesters 5-8 and M.Sc Agronomy courses are imported; courses for other programs and underload-summary sheets are excluded.
- The separate `Semester` column supports distinct M.Sc 1st, 2nd, and 3rd semester timetables. Older workbooks without that column retain their existing semester grouping.
- Both `3(2-1)` and `3(3+0)` credit-hour notation are supported. Practical-only courses are omitted from Mid Term date sheets.

## Scheduling Rules

- `3(2-1)` creates two one-slot theory sessions and one two-slot practical session.
- `4(3-1)` creates three one-slot theory sessions and one two-slot practical session.
- The app checks instructor availability across all generated sheets by day and real clock time.
- The app checks room availability across all generated sheets and uses only the configured rooms. B.Sc 5th/6th prefer the first classroom; 7th/8th and M.Sc prefer the second when present. Other classrooms are available as alternatives.
- When `Practicals in lab/field` is enabled, practical classes occupy their semester timetable and instructor time, but do not reserve the lecture room. This lets another semester use the room during those practical periods.
- M.Sc/PhD classes use the same one-hour periods as B.Sc classes, but are scheduled only from period 6 to period 9.
- Overflow/library rooms are used only when a placement in the normal classrooms is unavailable.
- Period 9 is treated as an overflow period. The scheduler fills periods 1-8 first and uses period 9 only when no clash-free placement is available in the first eight periods.
- Friday prayer break is blocked automatically for any slot that overlaps 1:30-2:00 PM, so no lecture is scheduled during that time.
- Saturday and Sunday rows remain visible in the timetable, but they are treated as off days and no classes are scheduled there.
- Recognized B.Sc Agronomy sections are mapped to `5th`, `6th`, `7th`, and `8th` sheets.
- Recognized M.Sc/PhD Agronomy sections are mapped to `1st` and `2nd` sheets.
- Annexure A's explicitly identified 3rd semester uses a separate `3rd` sheet.
- M.Sc exams remain at 2 PM and can use any configured room while avoiding instructor, invigilator and room clashes.

## Rooms

Add or remove rooms in the Rooms list. Each room is a classroom or an overflow/library room, and the list is saved in this browser across refreshes. Generate new timetables and date sheets to apply room changes. Removed rooms are not used for new schedules. Lab/Field remains a separate location for practicals when that option is enabled.

Class cells show their assigned room when multiple rooms are available. These room labels also carry through editor saves and individual instructor exports. Date sheets generate a sheet for each classroom and any overflow rooms used. Existing generated files are not changed when editing the room list.

## Invigilators

Add and remove names in the Invigilators list beside the date-sheet controls. The list is saved in this browser across refreshes. Generate a new date sheet to apply a changed roster.

Invigilation is randomized among available people with the fewest duties, using one shared total across both rooms. A balancing pass redistributes duties wherever availability permits, without changing exam dates or times. Room clashes, simultaneous teacher/invigilator duties, and invigilating one's own exam are prohibited. The output shows duty counts, including zero assignments. Individual date-sheet exports include both exam-teacher and invigilator duties.

## Source and data handling

- Original `.git/` history, actual faculty workload files and prior `outputs/` are intentionally excluded from this public copy.
- Uploaded workbooks are saved locally in `uploads/`, and generated files in `outputs/`. Both folders are ignored by Git.
- Sample teacher names and course data are fictitious; replace them with authorized, accurate data.
- Before processing institutional records, follow local privacy and data-governance requirements; the input parser recognizes a `Name + CNIC` header, but national identity numbers should not be included in shared samples.
- The public sample uses generic invigilator placeholders. Configure your own roster in the application before producing an official examination date sheet.
- Source license has **not** been specified; do not assume an open-source license merely because the files are visible on GitHub.

## Tests

```powershell
python -m unittest discover -s tests -v
```

JavaScript interface checks (requires Node.js):

```bash
node --test tests/*.cjs
```

**Scope:** The tests cover workload import and scheduling/room/invigilation logic; they are not a substitute for reviewing an official academic schedule.
