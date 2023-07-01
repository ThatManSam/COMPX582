import argparse
import cv2 as cv

from camera import Camera


def _save_image(camera, filename, num=0):
    if args.wait:
        input(f'Take image{f" {num}" if num !=0 else ""}? <Press ANY Key>')

    for attempt in range(3):
        try:
            img = camera.get_image()
            filename = f'{filename}{num if num != 0 else ""}.jpg'
            c_img = cv.cvtColor(img, cv.COLOR_BayerRG2RGB)
            cv.imwrite(filename, c_img)
            print(f'Saved image {filename}')
            break
        except AssertionError:
            if attempt == 3:
                print(f'Error getting image {f" {num}" if num != 0 else ""} from camera')
            else:
                continue




if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='save_photo',
                                     description='Takes one or more photos from the Basler GibE Camera and saves them '
                                                 'to the specified filename',
                                     epilog='If a count is specified, images will have a number suffix')
    parser.add_argument('filename', help='The filename to save the photo to, without a suffix')
    parser.add_argument('-c', '--count', required=False,
                        help='The number of photos to take')
    parser.add_argument('-w', '--wait', required=False, action='store_true',
                        help='The program will wait for user input before taking each image')

    args = parser.parse_args()

    cam = Camera(color=True)

    if args.count is not None:
        count = int(args.count)

        for i in range(1, count+1):
            _save_image(cam, args.filename, i)
    else:
        _save_image(cam, args.filename)
