"""Basic Video Processing methods."""
import os
import cv2


# Replace ID1 and ID2 with your IDs.
ID1 = '308339274'
ID2 = '212235246'

INPUT_VIDEO = 'atrium.avi'
GRAYSCALE_VIDEO = f'{ID1}_{ID2}_atrium_grayscale.avi'
BLACK_AND_WHITE_VIDEO = f'{ID1}_{ID2}_atrium_black_and_white.avi'
SOBEL_VIDEO = f'{ID1}_{ID2}_atrium_sobel.avi'


def get_video_parameters(capture: cv2.VideoCapture) -> dict:
    """Get an OpenCV capture object and extract its parameters.
    Args:
        capture: cv2.VideoCapture object. The input video's VideoCapture.
    Returns:
        parameters: dict. A dictionary of parameters names to their values.
    """
    fourcc = int(capture.get(cv2.CAP_PROP_FOURCC))
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    parameters = {"fourcc": fourcc, "fps": fps, "height": height, "width": width}
    return parameters


def convert_video_to_grayscale(input_video_path: str,
                               output_video_path: str) -> None:
    """Convert the video in the input path to grayscale.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, convert it to gray scale,
    and save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    # Open the input video capture
    input_video_capture = cv2.VideoCapture(input_video_path)

    # Open the input video capture and get its parameters
    parameters = get_video_parameters(input_video_capture)
    fourcc = parameters["fourcc"]
    fps = parameters["fps"]
    height = parameters["height"]
    width = parameters["width"]


    # Open the output video writer
    output_video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), False)

    # Iterate over the frames
    while True:
        retval, frame = input_video_capture.read()

        if not retval:
            break

        # Convert the frame to grayscale and write it to the output video
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output_video_writer.write(gray_frame)

    # Release the input video capture and output video writer
    input_video_capture.release()
    output_video_writer.release()

    # Destroy all windows
    cv2.destroyAllWindows()

def convert_video_to_black_and_white(input_video_path: str,
                                     output_video_path: str) -> None:
    """Convert the video in the input path to black and white.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, first convert it to gray scale,
    then use OpenCV's THRESH_OTSU to slice the gray color values to
    black (0) and white (1) and finally convert the frame format back to RGB.
    Save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    # Open the input video capture
    input_video_capture = cv2.VideoCapture(input_video_path)

    # Open the input video capture and get its parameters
    parameters = get_video_parameters(input_video_capture)
    fourcc = parameters["fourcc"]
    fps = parameters["fps"]
    height = parameters["height"]
    width = parameters["width"]


    # Open the output video writer
    output_video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), True)

    # Iterate over the frames
    while True:
        retval, frame = input_video_capture.read()
        if not retval:
            break

        # Convert the frame to grayscale, threshold it, convert it back to rgb and write it to the output video
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, black_and_white_frame = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        rgb_frame = cv2.cvtColor(black_and_white_frame, cv2.COLOR_GRAY2BGR)
        output_video_writer.write(rgb_frame)

    # Release the input video capture and output video writer
    input_video_capture.release()
    output_video_writer.release()

    # Destroy all windows
    cv2.destroyAllWindows()


def convert_video_to_sobel(input_video_path: str,
                           output_video_path: str) -> None:
    """Convert the video in the input path to sobel map.

    Use VideoCapture from OpenCV to open the video and read its
    parameters using the capture's get method.
    Open an output video using OpenCV's VideoWriter.
    Iterate over the frames. For each frame, first convert it to gray scale,
    then use OpenCV's THRESH_OTSU to slice the gray color values to
    black (0) and white (1) and finally convert the frame format back to RGB.
    Save the frame to the new video.
    Make sure to close all relevant captures and to destroy all windows.

    Args:
        input_video_path: str. Path to input video.
        output_video_path: str. Path to output video.

    Additional References:
    (1) What are fourcc parameters:
    https://docs.microsoft.com/en-us/windows/win32/medfound/video-fourccs

    """
    """INSERT YOUR CODE HERE.
        REMOVE THE pass KEYWORD AND IMPLEMENT YOUR OWN CODE.
        """
    # Open the input video capture
    input_video_capture = cv2.VideoCapture(input_video_path)

    # Open the input video capture and get its parameters
    parameters = get_video_parameters(input_video_capture)
    fourcc = parameters["fourcc"]
    fps = parameters["fps"]
    height = parameters["height"]
    width = parameters["width"]


    # Open the output video writer
    output_video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), True)

    # Iterate over the frames
    while True:
        retval, frame = input_video_capture.read()

        if not retval:
            break

        # Convert the frame to grayscale and apply the Sobel operator to it
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        sobel_frame = cv2.Sobel(gray_frame, ddepth=-1, dx=1, dy=1, ksize=5)

        # Convert the frame to RGB  and write it to the output video
        rgb_frame = cv2.cvtColor(sobel_frame, cv2.COLOR_GRAY2BGR)
        output_video_writer.write(rgb_frame)

    # Release the input video capture and output video writer
    input_video_capture.release()
    output_video_writer.release()

    # Destroy all windows
    cv2.destroyAllWindows()


def main():
    convert_video_to_grayscale(INPUT_VIDEO, GRAYSCALE_VIDEO)
    convert_video_to_black_and_white(INPUT_VIDEO, BLACK_AND_WHITE_VIDEO)
    convert_video_to_sobel(INPUT_VIDEO, SOBEL_VIDEO)


if __name__ == "__main__":
    main()
