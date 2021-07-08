import cv2
import os
import logging
from pathlib import Path
import argparse

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def frames_to_video(inputdir: Path, save_rate: int):
    assert inputdir.is_dir()
    files = list(x for x in inputdir.iterdir() if x.is_file() and x.suffix == '.mp4')
    logger.info(f'list of video files are: {files}')
    for i in range(len(files)):
        current_output = Path(inputdir) / Path(Path(files[i]).name).stem
        logger.info(f'ouputput folder for frames is: {current_output}')
        try:
            os.mkdir(current_output)
        except OSError:
            pass
        logger.info(f'saving the frames for {files[i]}')
        vidcap = cv2.VideoCapture(str(files[i]))
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        fcnt = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
        logger.info(f'framerate:, {fps}')
        logger.info(f'framecount:, {fcnt}')
        logger.info(f'video duration:, {fps/fcnt}')
        count = 0
        save_count = 0
        while True:
            success, image = vidcap.read()
            if not success:
                break
            if count % save_rate == 0:
                cv2.imwrite(str(current_output / "frame{:d}.jpg".format(count)), image)
                save_count += 1
                logger.info(f'frame {count} is saved!')
            count += 1


if __name__ == "__main__":
    logger.info(f"breaking the video to frames and save the results")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video folder")
    a.add_argument("--fsr", help="frame save rate")
    args = a.parse_args()
    args.pathIn = Path('../hockeyTrackingDataset/clips/CAR_VS_BOS_2019')
    args.fsr = 100
    frames_to_video(args.pathIn, args.fsr)

