# importing image object from PIL
import math
from PIL import Image, ImageDraw, ImageFont
import random


def mega_draw(numbers, cls, name):
    colors = {"red": "#fe0000", "yellow": "#ffcc00", "green": "#019934", "blue": "#3401cc", "violet": "#990099",
              "orange": "#ff7513"}

    cls = list(cls)
    print(numbers)
    print(cls)
    indexes = list(range(len(numbers)))
    random.shuffle(indexes)
    numbers = [numbers[i] for i in indexes]
    cls = [cls[i] for i in indexes]
    print(numbers)
    print(cls)

    w, h = 772, 772
    xw, xh = 350 - 1, 350 - 1
    border = 18 - 1

    # creating new Image object
    img = Image.new("RGB", (w, h), (255, 255, 255))

    # create rectangle image
    img1 = ImageDraw.Draw(img)

    img1.rectangle((border, border, border + xw, border + xh), fill=colors[cls[0]])
    img1.rectangle((border * 3 + xw, border, border * 3 + xw * 2, border + xh), fill=colors[cls[1]])
    img1.rectangle((border, border * 3 + xh, border + xw, border * 3 + xh * 2), fill=colors[cls[2]])
    img1.rectangle((border * 3 + xw, border * 3 + xh, border * 3 + xw * 2, border * 3 + xh * 2), fill=colors[cls[3]])

    # draw numbers
    maskw, maskh = 90, 130
    delta_t = 0

    # draw number 1
    delta_t = 0
    tstr = str(numbers[0])

    text_mask = Image.new('RGBA', (maskw + delta_t, maskh), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", 150)

    text.text((0, 0), tstr, (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)
    text_mask2 = text_mask.rotate(-90, expand=True)
    text_mask3 = text_mask.rotate(180, expand=True)

    # paste left_up
    img.paste(text_mask1, (237, 150), text_mask1)
    img.paste(text_mask2, (17, 140), text_mask2)
    img.paste(text_mask, (145, 235), text_mask)
    img.paste(text_mask3, (150, 18), text_mask3)
    # draw dot if need
    if numbers[0] == 6 or numbers[0] == "6" or numbers[0] == 9 or numbers[0] == "9":
        text_mask_dot = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        text2 = ImageDraw.Draw(text_mask_dot)
        font = ImageFont.truetype("myraidpro.ttf", 100)
        text2.text((0, 0), ".", (255, 255, 255), font=font)
        img.paste(text_mask_dot, (332, 470 - h // 2), text_mask_dot)
        img.paste(text_mask_dot, (29, 545 - h // 2), text_mask_dot)
        img.paste(text_mask_dot, (215, 660 - h // 2), text_mask_dot)
        img.paste(text_mask_dot, (150, 355 - h // 2), text_mask_dot)

    # draw number 2
    delta_t = 0
    tstr = str(numbers[1])

    text_mask = Image.new('RGBA', (maskw + delta_t, maskh), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", 150)

    text.text((0, 0), tstr, (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)
    text_mask2 = text_mask.rotate(-90, expand=True)
    text_mask3 = text_mask.rotate(180, expand=True)

    # paste right_up
    img.paste(text_mask1, (621, 150), text_mask1)
    img.paste(text_mask2, (401, 140), text_mask2)
    img.paste(text_mask, (529, 235), text_mask)
    img.paste(text_mask3, (534, 18), text_mask3)
    # draw dot if need
    if numbers[1] == 6 or numbers[1] == "6" or numbers[1] == 9 or numbers[1] == "9":
        text_mask_dot = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        text2 = ImageDraw.Draw(text_mask_dot)
        font = ImageFont.truetype("myraidpro.ttf", 100)
        text2.text((0, 0), ".", (255, 255, 255), font=font)
        img.paste(text_mask_dot, (332 + w // 2, 470 - h // 2), text_mask_dot)
        img.paste(text_mask_dot, (29 + w // 2, 545 - h // 2), text_mask_dot)
        img.paste(text_mask_dot, (215 + w // 2, 660 - h // 2), text_mask_dot)
        img.paste(text_mask_dot, (150 + w // 2, 355 - h // 2), text_mask_dot)

    # draw number 3
    delta_t = 0
    tstr = str(numbers[2])

    text_mask = Image.new('RGBA', (maskw + delta_t, maskh), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", 150)

    text.text((0, 0), tstr, (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)
    text_mask2 = text_mask.rotate(-90, expand=True)
    text_mask3 = text_mask.rotate(180, expand=True)

    # paste left_down
    img.paste(text_mask1, (237, 534), text_mask1)
    img.paste(text_mask2, (17, 524), text_mask2)
    img.paste(text_mask, (145, 619), text_mask)
    img.paste(text_mask3, (150, 402), text_mask3)

    # draw dot if need
    if numbers[2] == 6 or numbers[2] == "6" or numbers[2] == 9 or numbers[2] == "9":
        text_mask_dot = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        text2 = ImageDraw.Draw(text_mask_dot)
        font = ImageFont.truetype("myraidpro.ttf", 100)
        text2.text((0, 0), ".", (255, 255, 255), font=font)
        img.paste(text_mask_dot, (332, 470), text_mask_dot)
        img.paste(text_mask_dot, (29, 545), text_mask_dot)
        img.paste(text_mask_dot, (215, 660), text_mask_dot)
        img.paste(text_mask_dot, (150, 355), text_mask_dot)

    # draw number 4
    delta_t = 0
    tstr = str(numbers[3])

    text_mask = Image.new('RGBA', (maskw + delta_t, maskh), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", 150)
    tstr = str(numbers[3])

    text.text((0, 0), tstr, (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)
    text_mask2 = text_mask.rotate(-90, expand=True)
    text_mask3 = text_mask.rotate(180, expand=True)

    # paste right_down
    img.paste(text_mask1, (621, 534), text_mask1)
    img.paste(text_mask2, (401, 524), text_mask2)
    img.paste(text_mask, (529, 619), text_mask)
    img.paste(text_mask3, (534, 402), text_mask3)
    # draw dot if need
    if numbers[3] == 6 or numbers[3] == "6" or numbers[3] == 9 or numbers[3] == "9":
        text_mask_dot = Image.new('RGBA', (100, 100), (0, 0, 0, 0))
        text2 = ImageDraw.Draw(text_mask_dot)
        font = ImageFont.truetype("myraidpro.ttf", 100)
        text2.text((0, 0), ".", (255, 255, 255), font=font)
        img.paste(text_mask_dot, (332 + w // 2, 470), text_mask_dot)
        img.paste(text_mask_dot, (29 + w // 2, 545), text_mask_dot)
        img.paste(text_mask_dot, (215 + w // 2, 660), text_mask_dot)
        img.paste(text_mask_dot, (150 + w // 2, 355), text_mask_dot)

    # draw web
    img1.line([(0, 0), (w, h)], fill=(255, 255, 255), width=2)
    img1.line([(0 - 6, w), (h - 6, 0)], fill=(255, 255, 255), width=2)

    img1.line([(0, h / 2 - 3), (w / 2, h - 3)], fill=(255, 255, 255), width=2)
    img1.line([(w / 2 - 3, 0), (w - 3, h / 2)], fill=(255, 255, 255), width=2)

    img1.line([(0, h / 2 - 3), (w / 2, 0 - 3)], fill=(255, 255, 255), width=2)
    img1.line([(w / 2, h - 9), (w, h / 2 - 9)], fill=(255, 255, 255), width=2)

    # Обрезка
    img = img.crop((0, 0, 768, 768))
    img.save(f"draw_cards2//{name}.png")


num_ls = [[7, 4, 2, 8], [4, 6, 5, 8], [6, 1, 4, 8], [2, 9, 5, 8], [3, 7, 8, 6], [5, 7, 6, 9], [5, 6, 3, 7], [2, 1, 9, 4], [9, 4, 1, 7], [9, 4, 7, 8], [9, 6, 4, 3], [6, 9, 3, 5], [3, 8, 6, 9], [3, 6, 7, 2], [4, 9, 2, 5], [9, 4, 3, 8], [9, 7, 2, 3], [3, 6, 5, 1], [3, 5, 6, 4], [4, 2, 1, 6], [6, 2, 1, 5], [4, 1, 5, 2], [2, 3, 6, 1], [2, 5, 3, 4], [5, 3, 4, 1], [5, 3, 2, 1], [2, 4, 3, 1], [0, 3, 7, 2], [6, 5, 0, 2], [7, 0, 4, 2], [7, 5, 1, 0], [7, 2, 1, 0], [3, 4, 0, 2], [2, 6, 6, 1], [5, 1, 5, 2], [1, 3, 5, 5], [2, 5, 5, 6], [2, 5, 5, 4], [4, 5, 5, 3], [5, 4, 3, 3], [4, 2, 4, 1], [4, 4, 1, 3], [2, 6, 4, 6], [5, 2, 5, 3], [3, 3, 1, 4], [2, 2, 4, 5], [3, 2, 5, 2], [2, 1, 3, 3]]

cls_ls = [['violet', 'red', 'yellow', 'blue'], ['orange', 'violet', 'blue', 'yellow'], ['green', 'red', 'blue', 'orange'], ['yellow', 'red', 'blue', 'violet'], ['violet', 'orange', 'red', 'yellow'], ['yellow', 'green', 'red', 'violet'], ['green', 'red', 'yellow', 'orange'], ['violet', 'yellow', 'orange', 'red'], ['green', 'violet', 'red', 'blue'], ['orange', 'yellow', 'violet', 'green'], ['yellow', 'green', 'violet', 'red'], ['blue', 'green', 'violet', 'orange'], ['blue', 'yellow', 'orange', 'red'], ['blue', 'red', 'yellow', 'orange'], ['orange', 'blue', 'yellow', 'violet'], ['violet', 'red', 'orange', 'blue'], ['yellow', 'green', 'orange', 'violet'], ['blue', 'green', 'violet', 'yellow'], ['red', 'yellow', 'orange', 'green'], ['green', 'yellow', 'blue', 'red'], ['blue', 'red', 'green', 'orange'], ['blue', 'yellow', 'green', 'red'], ['blue', 'red', 'violet', 'orange'], ['blue', 'green', 'red', 'violet'], ['red', 'green', 'violet', 'blue'], ['yellow', 'orange', 'red', 'green'], ['violet', 'orange', 'yellow', 'green'], ['yellow', 'violet', 'red', 'green'], ['yellow', 'orange', 'green', 'blue'], ['yellow', 'blue', 'orange', 'green'], ['red', 'green', 'blue', 'orange'], ['blue', 'violet', 'orange', 'red'], ['green', 'orange', 'violet', 'blue'], ['green', 'orange', 'yellow', 'red'], ['green', 'orange', 'red', 'violet'], ['violet', 'yellow', 'blue', 'red'], ['orange', 'yellow', 'blue', 'violet'], ['orange', 'violet', 'red', 'yellow'], ['green', 'yellow', 'orange', 'blue'], ['orange', 'red', 'green', 'violet'], ['yellow', 'red', 'blue', 'green'], ['yellow', 'blue', 'violet', 'green'], ['red', 'blue', 'green', 'yellow'], ['blue', 'orange', 'violet', 'green'], ['blue', 'orange', 'red', 'yellow'], ['violet', 'yellow', 'green', 'red'], ['yellow', 'blue', 'violet', 'green'], ['green', 'violet', 'red', 'orange']]


for x in range(48):
    mega_draw(num_ls[x], cls_ls[x], "card_" + str(x+1))
