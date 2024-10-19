/**
 * MIT License
 *
 * Copyright (c) 2024 Pablo Rodriguez Nava, @pablintino
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 *
 **/

create or replace view "Transformers" as
select c.mpn                       "Part Number",
       c.value                     "Value",
       c.manufacturer              "Manufacturer",
       c.created_on                "Created On",
       c.updated_on                "Updated On",
       c.package                   "Package",
       c.description               "Description",
       c.comment                   "Comment",
       c.operating_temperature_min "Minimum Operating Temperature",
       c.operating_temperature_max "Maximum Operating Temperature",
       l.symbol_path               "Library Path",
       l.symbol_ref                "Library Ref",
       (ftp1).footprint_path       "Footprint Path 1",
       (ftp2).footprint_path       "Footprint Path 2",
       (ftp3).footprint_path       "Footprint Path 3",
       (ftp4).footprint_path       "Footprint Path 4",
       t.number_of_windings        "Number of Windings",
       t.primary_dc_resistance     "Primary DCR",
       t.secondary_dc_resistance   "Secondary DCR",
       t.tertiary_dc_resistance    "Tertiary DCR",
       t.leakage_inductance        "Leakage Inductance",
       t.primary_inductance        "Primary Inductance",
       t.secondary_current_rating  "Secondary Current Rating",
       t.tertiary_current_rating   "Tertiary Current Rating",
       t.primary_voltage_rating    "Primary Voltage Rating",
       t.secondary_voltage_rating  "Secondary Voltage Rating",
       t.tertiary_voltage_rating   "Tertiary Voltage Rating",
       t.nps_turns_ratio           "NPS Turns Ratio",
       t.npt_turns_ratio           "NPT Turns Ratio"
from crosstab('select c.id, ROW_NUMBER() OVER (ORDER BY c.id, f.id) seq, f
    from transformer t
             inner join component c
                        on t.id = c.id
             inner join component_footprint_asc cf
                        on c.id = cf.component_id
             inner join footprint_ref f
                        on cf.footprint_ref_id = f.id'
     ) as ct(cid int, ftp1 footprint_ref, ftp2 footprint_ref, ftp3 footprint_ref, ftp4 footprint_ref)
         right outer join component c on c.id = cid
         inner join transformer t on t.id = c.id
         left outer join library_ref l on c.library_ref_id = l.id