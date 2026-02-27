# Semester Capstone — Mini SOC Investigation Pack (Fall 2025–2026)

## Goal
Combine Semester 1 evidence packs into a single HR-friendly “incident-style” narrative:
OS baseline + network observations + threat/risk thinking + compliance mindset + a small automation output.

## Start here (Top 3 Evidence)
1) ⚖️ IT Law / GRC pack: [01_Hukuk_GRC](../01_Hukuk_GRC/)
2) 🐧 Operating Systems pack: [02_Isletim_Sistemleri](../02_Isletim_Sistemleri/)
3) 🌐 Computer Networks pack: [04_Bilgisayar_Aglari](../04_Bilgisayar_Aglari/)

**Bonus:** ⌨️ Programming pack: [05_Programlama_1](../05_Programlama_1/)

![Top 3 Evidence](evidence/screenshots/capstone_top3.png)

## Mini SOC scenario (simple)
- **Signal:** suspicious login failures + unusual connections
- **Triage:** check auth/sudo evidence + services/ports baseline
- **Network:** validate DNS/TLS patterns from baseline capture
- **Controls:** map threats → risks → mitigations → evidence
- **Output:** a small script/report proves repeatability

## Pack structure
- `evidence/artifacts/capstone_case_note.md` — short investigation-style case note
- `plan.md` — scope & success criteria
- `steps.md` — how to replay the story in 5–10 minutes
- `report.md` — executive summary for HR
- `evidence/` — screenshots + artifacts
