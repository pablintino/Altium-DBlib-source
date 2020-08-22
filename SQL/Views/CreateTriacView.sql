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

create view [Triacs] as
select                                mpn as [Part Number],
    [Value]                         = MAX(value),
    [Manufacturer]                  = MAX(manufacturer),
    [Maximum Power]                 = MAX(power_max),
    [Vdrm]                          = MAX(vdrm),
    [Current Rating]                = MAX(current_rating),
    [Rate Rise Off-State Voltage]   = MAX(dl_dt),
    [Trigger Current]               = MAX(trigger_current),
    [Latching Current]              = MAX(latching_current),
    [Holding Current]               = MAX(holding_current),
    [Gate Trigger Voltage]          = MAX(gate_trigger_voltage),
    [Emitter Forward Current]       = MAX(emitter_forward_current),
    [Emitter Forward Voltage]       = MAX(emitter_forward_voltage),
    [Triac Type]                    = MAX(triac_type),
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
         select t.power_max                                                                     power_max,
                t.vdrm                                                                          vdrm,
                t.current_rating                                                                current_rating,
                t.dl_dt                                                                         dl_dt,
                t.trigger_current                                                               trigger_current,
                t.latching_current                                                              latching_current,
                t.holding_current                                                               holding_current,
                t.gate_trigger_voltage                                                          gate_trigger_voltage,
                t.emitter_forward_current                                                       emitter_forward_current,
                t.emitter_forward_voltage                                                       emitter_forward_voltage,
                t.triac_type                                                                    triac_type,
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
         from triac t
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
