import logging
import argparse
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
from data_utils import frame2video_convertor


if __name__ == "__main__":
    logger.info(f"breaking the video to frames and save the results")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to the image folder")
    a.add_argument("--pathOut", help="folder for saving the output vide.")
    a.add_argument("--fps", help="frame per second")
    args = a.parse_args()
    args.pathIn = Path('../hockeyTrackingDataset/clips/CAR_VS_BOS_2019/001')
    args.pathOut = Path('../hockeyTrackingDataset/clips/CAR_VS_BOS_2019/')
    args.fps = 10
    frame2video_convertor(args.pathIn, args.pathOut, args.fps)
