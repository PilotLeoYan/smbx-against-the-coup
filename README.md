# Against the Coup (*Contra el golpe de estado*)

**Authors:** Danyex & Sinber  
**Engine Target:** [TheXTech](https://github.com/Wohlstand/TheXTech) (SMBX 1.3 / SMBX-38A Compatible)  
**Editor Support:** [Moondust Editor (PGE)](https://wohlsoft.ru/projects/Moondust/)  
**Language:** English (translated & modernized from the original Spanish release)

---

## Story & Overview

Summoned to Princess Peach's estate (`marios_pad.lvl`) for an urgent meeting, Mario and friends walk into an ambush orchestrated by Bowser. With Princess Peach captured, Bowser declares that without a ruler, a military coup will seize control of the Mushroom Kingdom!

**Against the Coup** (*Contra el golpe de estado*) is a full-length, 6-world Super Mario Bros. X episode featuring **120 level files**, custom mechanics, boss battles, town hubs, shops, and crossover stages inspired by *Super Mario Sunshine*, *The Legend of Zelda: Majora's Mask & Ocarina of Time*, and *Undertale*.

### Key Worlds & Highlights
- **World 1 – Grassland & Royal Mines:** Classic platforming, pipe meadows, Cheep-Cheep lakes, and an expedition deep into the Royal Mines to confront Ludwig von Koopa (`castillo-1.lvl`, `castillo-1b.lvl`).
- **World 2 – Dry Dry Desert & Ancient Pyramids:** Quicksand corridors, Mouser's bomb arena, Desert Circus, and multi-trial pyramids guarding the Star of Wisdom (`piramide1.lvl`, `piramide2.lvl`, `castillo-2.lvl`).
- **World 3 – Underground Caverns & The Core:** Subterranean waterways, Toad's submarine tour (`4-3-f.lvl`), Haunted Boo Mansions (`boo.lvl`), and a showdown in the molten Core (`castillo-3b.lvl`).
- **World 4 – Sherbet Land & New Snowdin:** Icy peaks, time-attack challenges (`7a-4.lvl`), a peaceful monster town on the surface featuring Sans & Papyrus (`snowdin.lvl`), and the Ice Castle (`castillo-4.lvl`).
- **World 5 – Sunset Archipelago & Sky Tower:** Tropical beaches (`1-5-f.lvl`), F.L.U.D.D. jetpack trials (`2-5-d.lvl`), bioluminescent deep-sea trenches (`6-5-d.lvl`), Stormy Sky Tower (`torre-5.lvl`), and Larry Koopa's Beach Castle (`castillo-5.lvl`).
- **World 6 – Termina / Clock Town Hub:** A non-linear hub centered around **Clock Town** (`clock-town.lvl`) branching into four cardinal regions:
  - **South:** Poisoned swamps of **Deku Palace** (`deku-palace.lvl`) and **Woodfall** (`woodfall.lvl`).
  - **North:** Frozen village of **Icetown** (`icetown.lvl`) and the howling blizzards of **Snowpeak** (`snowpeak.lvl`).
  - **West:** **Lon Lon Ranch** (`lon-lon-ranch.lvl`) and sunset beaches (`w2-6.lvl`).
  - **East:** Giant forests (`1-6-d.lvl`), Lost Woods (`2-6-d.lvl`), and the Astral **Observatory** (`observatorio.lvl`).

---

## Controls & Custom Mechanics

| Action | Default Keyboard | Default Gamepad | Notes |
| :--- | :--- | :--- | :--- |
| **Move / Duck / Look** | Arrow Keys | D-Pad / Left Stick | Hold **DOWN** in `icetown.lvl` / `w2-6.lvl` after obtaining the Lens of Truth to reveal invisible objects. |
| **Jump** | `Z` | `A` / Cross | Standard jump; hold to jump higher. |
| **Run / Fire / Grab** | `X` | `X` / Square | Hold to sprint, pick up shells/keys, or shoot fire/ice balls. |
| **Alt-Jump (Spin-Jump)** | `A` | `B` / Circle | Spin-jump over saws/spikes; press in midair to glide slower or activate Propeller Mushroom (`6a-4.lvl`). |
| **Alt-Run / Drop Item** | `S` | `Y` / Triangle | Release reserve item or use secondary attack. |
| **Ground-Pound** | `Down` (in midair) | `Down` (in midair) | Available in select levels (even as Toad in `snowpeak.lvl`, or with Purple Yoshi in `4-2-d.lvl`). Press **UP** to cancel. |
| **Mouse / Cursor** | Left Click | Touch / Cursor | In `n1-6.lvl`, click on the screen (single-screen mode) to conjure temporary platform blocks. |

### Special Power-Ups & Mounts
- **F.L.U.D.D. & Turbo F.L.U.D.D. (`2-5-d.lvl`):** Hover or dash across water currents; touch water to refill your tank.
- **Shell Suit (`snowpeak.lvl`):** Build up running speed to tuck into a Koopa shell and bash through obstacles and bosses.
- **Propeller Box & Spring Helmets (`woodfall.lvl`, `4a-4.lvl`):** Protect against falling hazards or launch high into the air.

---

## Playing on TheXTech (Linux & Windows 10)

1. Place the `against-the-coup` directory inside your TheXTech `worlds/` folder:
   ```text
   thextech/
   └── worlds/
       └── against-the-coup/
           ├── world.wld
           ├── setting.wls
           └── *.lvl / *.ogg / *.png
   ```
2. Launch **TheXTech** (`smbx` on Linux or `thextech.exe` on Windows).
3. Select **1 Player Game** or **2 Player Game** -> **Against the Coup**.

---

## Editing with Moondust Editor (PGE) & Collaborator Guide (Windows 10 / Linux)

This repository has been fully sanitized and normalized for cross-platform collaboration between Linux and Windows 10:
- **Strict Naming Convention:** Every file and folder uses lowercase ASCII characters, digits, underscores, dots, and hyphens (`^[a-z0-9_.-]+$`), preventing case-sensitivity bugs on Linux and path issues on Windows.
- **Ogg Vorbis Audio:** All legacy `.mp3` and `.wav` files have been converted to 44.1 kHz stereo `.ogg` (Vorbis) and all `.lvl` / `world.wld` references updated accordingly.
- **Line Endings:** `.gitattributes` automatically enforces `CRLF` on `.lvl` and `.wld` files and binary treatment on `.png` and `.ogg` assets.

### Opening in Moondust Editor (Windows 10)
1. Clone the repository into your `worlds/` directory:
   ```bash
   git clone <repository-url> against-the-coup
   ```
2. Open **Moondust Editor** (`pge_editor.exe`).
3. Select the **SMBX 1.3 / TheXTech** configuration package when prompted.
4. Go to **File -> Open** and select `against-the-coup/world.wld` to edit the world map, or open any `.lvl` file directly.
5. When adding new levels, custom graphics folders, or audio tracks:
   - Keep all filenames strictly lowercase with hyphens (`^[a-z0-9_.-]+$`), no spaces or accents.
   - Match custom level asset directory names exactly to the `.lvl` filename (e.g., `my-level.lvl` -> `my-level/`).
   - Encode all custom music as `.ogg` (Vorbis) or `.mid`. Automated GitHub Actions (`lint-naming.yml` and `lint-audio.yml`) will validate every push and pull request.
