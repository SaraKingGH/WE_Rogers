import logging
import argparse
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
from data_utils import videos2frames_time, videos2frames_frame_number


if __name__ == "__main__":
    logger.info(f"breaking the video to frames and save the results")
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video folder")
    a.add_argument("--save_method", help="saving the video frames based on the number: 0 or based on the frame length (time): 1")
    a.add_argument("--fnumber", help="frame number for saving")
    a.add_argument("--ftime", help="time length for capturing the image (seconds)")
    args = a.parse_args()
    args.pathIn = Path('../hockeyTrackingDataset/clips/CAR_VS_BOS_2019')
    args.save_method = 1
    args.fnumber = 100
    args.ftime = 20
    if args.save_method:
        videos2frames_time(args.pathIn, args.ftime)
    else:
        videos2frames_frame_number(args.pathIn, args.fnumber)
