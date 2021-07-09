import cv2
import os
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def getFrame(vidcap, sec: int, output_folder: Path, count: int):
    """
    getting frames for the current video based on the time
    """
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        cv2.imwrite(str(output_folder / Path("frame{:d}.jpg".format(count))), image)
    return hasFrames


def videos2frames_time(inputdir: Path, frame_length: int):
    """
    convert video to frames based on the video length.
    """
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
        sec = 0
        count = 0
        success = getFrame(vidcap, sec, current_output, count)
        while success:
            logger.info(f'frame {count} is saved!')
            count = count + 1
            sec = sec + frame_length
            sec = round(sec, 2)
            success = getFrame(vidcap, sec, current_output, count)


def videos2frames_frame_number(inputdir: Path, frame_number: int):
    """
    convert video to frames based on the requested number of frames.
    """
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
            if count % frame_number == 0:
                cv2.imwrite(str(current_output / "frame{:d}.jpg".format(count)), image)
                save_count += 1
                logger.info(f'frame {count} is saved!')
            count += 1
