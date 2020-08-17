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

create view [PPTC Fuses] as
select                                mpn as [Part Number],
    [Value]                         = MAX(value),
    [Manufacturer]                  = MAX(manufacturer),
    [Hold Current]                  = MAX(current_hold),
    [Trip Current]                  = MAX(current_trip),
    [Voltage Rating]                = MAX(voltage_rating),
    [Maximum Resistance]            = MAX(resistance_maximum),
    [Minimum Resistance]            = MAX(resistance_minimum),
    [Power Rating]                  = MAX(power_rating),
    [Current Rating]                = MAX(current_rating),
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
         select p.current_hold                                                                  current_hold,
                p.current_trip                                                                  current_trip,
                p.voltage_rating                                                                voltage_rating,
                p.resistance_maximum                                                            resistance_maximum,
                p.resistance_minimum                                                            resistance_minimum,
                p.power_rating                                                                  power_rating,
                p.current_rating                                                                current_rating,
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
         from fuse_pptc p
                  inner join component c
                             on p.id = c.id
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
