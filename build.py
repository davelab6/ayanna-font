#! /usr/bin/env python

import os
import hindkit as kit
kit.confirm_version('0.2.1')

# - - -

family = kit.Family(
    trademark = 'Ayanna',
    script = 'Sinhala',
    hide_script_name = True,
)

family.set_masters(
    modules = [
        'kerning',
        'mark_positioning',
        'mark_to_mark_positioning',
        # 'devanagari_matra_i_variants',
    ],
)
family.masters[0]._file_name = 'Ayanna-Bold.ufo'

family.set_styles([
    ('Bold',       100, 900),
])

# - - -

#family.output_name_affix = '{} FDK'

# - - -

builder = kit.Builder(family)

builder.fontrevision = '1.000'

builder.set_options([

    'prepare_styles',   # stage i
    'prepare_features', # stage ii
    'compile',          # stage iii

    #'makeinstances', #!
    'checkoutlines', #!
    # 'autohint',      #!

    'do_style_linking',
    'use_os_2_version_4',
    'prefer_typo_metrics',
    'is_width_weight_slope_only',

])

builder.generate_designspace()
builder.generate_fmndb()

builder.build()
os.rename("build/Ayanna-Bold.otf","Ayanna-Bold.otf")

family.masters[0]._file_name = 'Ayanna-Regular.ufo'
family.masters[1]._file_name = 'Ayanna-ExtraBold.ufo'

family.set_styles([
    ('ExtraLight',     0.0, 400),
    ('Light',     13, 500),
    ('Regular',     28, 600),
    ('Medium',     47, 700),
    ('SemiBold',   71, 800),
    ('Bold1',       100, 900),
])

# - - -

#family.output_name_affix = '{} FDK'

# - - -

builder = kit.Builder(family)

builder.fontrevision = '1.000'

builder.set_options([

    'prepare_styles',   # stage i
    'prepare_features', # stage ii
    'compile',          # stage iii

    'makeinstances', #!
    'checkoutlines', #!
    # 'autohint',      #!

    'do_style_linking',
    'use_os_2_version_4',
    'prefer_typo_metrics',
    'is_width_weight_slope_only',

])

builder.generate_designspace()
builder.generate_fmndb()

builder.build()
os.remove("build/Ayanna-Bold1.otf")
os.rename("Ayanna-Bold.otf", "build/Ayanna-Bold.otf")
