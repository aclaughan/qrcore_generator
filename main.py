#!/usr/local/bin/python3
# ------------------------------------------------------------------------------
#        name : main.py
#      author : alan claughan
#     version : 1.0.0
#        date : 24-05-2021
# description :
#
# ==============================================================================
#

import qrcode
import qrcode.image.svg

import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def main():
    locations = \
        {
            "times_square": "https://goo.gl/maps/DzGWnHe1LBCoMHsE8",
            "big_ben": "https://goo.gl/maps/KeEWEfKTn11pUZy49",
            "tokyo_tower": "https://goo.gl/maps/rtsyB6doHHraf9Uv6"
        }

    for location in locations:
        logging.info(f'location: "{location}", link: "{locations[location]}"')
        qr_image = qrcode.make(locations[location],
                               image_factory=qrcode.image.svg.SvgImage)
        qr_image.save(location + '.svg')


if __name__ == '__main__':
    main()


