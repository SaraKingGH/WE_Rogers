import logging
import argparse
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
from data_utils import videos2frames_frame_number


if __name__ == "__main__":
    logger.info(f"breaking the video to frames and save the results")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video folder")
    a.add_argument("--fnumber", help="frame gap number for saving")
    args = a.parse_args()
    args.pathIn = Path('../RogersDataset')
    args.fnumber = 100
    videos2frames_frame_number(args.pathIn, args.fnumber)
