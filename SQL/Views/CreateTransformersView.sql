/**
 * MIT License
 *
 * Copyright (c) 2020 Pablo Rodriguez Nava, @pablintino
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

create view [Transformers] as
select                                mpn as [Part Number],
    [Value]                         = MAX(value),
    [Manufacturer]                  = MAX(manufacturer),
    [Number of Windings]            = MAX(number_of_windings),
    [Primary DCR]                   = MAX(primary_dc_resistance),
    [Secondary DCR]                 = MAX(secondary_dc_resistance),
    [Tertiary DCR]                  = MAX(tertiary_dc_resistance),
    [Current Rating]                = MAX(leakage_inductance),
    [Primary Inductance]            = MAX(primary_inductance),
    [Secondary Current Rating]      = MAX(secondary_current_rating),
    [Tertiary Current Rating]       = MAX(tertiary_current_rating),
    [Primary Voltage Rating]        = MAX(primary_voltage_rating),
    [Secondary Voltage Rating]      = MAX(secondary_voltage_rating),
    [Tertiary Voltage Rating]       = MAX(tertiary_voltage_rating),
    [NPS Turns Ratio]               = MAX(nps_turns_ratio),
    [NPT Turns Ratio]               = MAX(npt_turns_ratio),
    [Created On]                    = MAX(created_on),
    [Updated On]                    = MAX(updated_on),
    [Type]                          = MAX(type),
    [Package]                       = MAX(package),
    [Description]                   = MAX(description),
    [Comment]                       = MAX(comment),
    [Minimum Operating Temperature] = MAX(operating_temperature_min),
    [Maximum Operating Temperature] = MAX(operating_temperature_max),
    [Through Hole]                  = MAX(CAST([is_through_hole] AS tinyint)),
    [Library Path]                  = MAX(symbol_path),
    [Library Ref]                   = MAX(symbol_ref),
    [Footprint Path 1]              = MAX([FootprintPath1]),
    [Footprint Path 2]              = MAX([FootprintPath2]),
    [Footprint Path 3]              = MAX([FootprintPath3]),
    [Footprint Ref 1]               = MAX([FootprintRef1]),
    [Footprint Ref 2]               = MAX([FootprintRef2]),
    [Footprint Ref 3]               = MAX([FootprintRef3])
from (
         select t.number_of_windings                                                            number_of_windings,
                t.primary_dc_resistance                                                         primary_dc_resistance,
                t.secondary_dc_resistance                                                       secondary_dc_resistance,
                t.tertiary_dc_resistance                                                        tertiary_dc_resistance,
                t.leakage_inductance                                                            leakage_inductance,
                t.primary_inductance                                                            primary_inductance,
                t.secondary_current_rating                                                      secondary_current_rating,
                t.tertiary_current_rating                                                       tertiary_current_rating,
                t.primary_voltage_rating                                                        primary_voltage_rating,
                t.secondary_voltage_rating                                                      secondary_voltage_rating,
                t.tertiary_voltage_rating                                                       tertiary_voltage_rating,
                t.nps_turns_ratio                                                               nps_turns_ratio,
                t.npt_turns_ratio                                                               npt_turns_ratio,
                c.manufacturer                                                                  manufacturer,
                c.mpn                                                                           mpn,
                c.value                                                                         value,
                c.created_on                                                                    created_on,
                c.updated_on                                                                    updated_on,
                c.type                                                                          type,
                c.package                                                                       package,
                c.description                                                                   description,
                c.comment                                                                       comment,
                c.operating_temperature_min                                                     operating_temperature_min,
                c.operating_temperature_max                                                     operating_temperature_max,
                c.is_through_hole                                                               is_through_hole,
                lf.symbol_path                                                                  symbol_path,
                lf.symbol_ref                                                                   symbol_ref,
                f.footprint_path                                                                footprint_path,
                f.footprint_ref                                                                 footprint_ref,
                'FootprintPath' + CAST(
                        DENSE_RANK() OVER (PARTITION BY c.id ORDER BY f.id ASC) AS NVARCHAR) AS [FootprintPathPivot],
                'FootprintRef' + CAST(
                        DENSE_RANK() OVER (PARTITION BY c.id ORDER BY f.id ASC) AS NVARCHAR) AS [FootprintRefPivot]
         from transformer t
                  inner join component c
                             on t.id = c.id
                  inner join component_footprint_asc cf
                             on c.id = cf.component_id
                  inner join footprint_ref f
                             on cf.footprint_ref_id = f.id
                  inner join library_ref lf
                             on c.library_ref_id = lf.id
     ) d
         pivot
         (
         max(footprint_path)
         FOR FootprintPathPivot IN ([FootprintPath1],[FootprintPath2],[FootprintPath3])
         ) AS Pivot1
         pivot
         (
         max(footprint_ref)
         FOR FootprintRefPivot IN ([FootprintRef1],[FootprintRef2],[FootprintRef3])
         ) AS Pivot2
GROUP BY mpn
