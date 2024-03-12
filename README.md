# Gesture-Based Presentation Control using Hand Tracking

This project enables gesture-based control of presentations using hand tracking technology. By leveraging computer vision and hand tracking modules, users can navigate through slides and interact with presentations using intuitive hand gestures.

## Features

- Navigate through slides by moving your hand left or right.
- Draw annotations on slides using hand gestures.
- Erase annotations with a specific hand gesture.
- Intuitive user interface with real-time feedback.

## Requirements

- Python 3.x
- OpenCV
- cvzone library
- HandTrackingModule from cvzone

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/garjeatharv/Gesture-Based-Presentaion.git
```

2. Install the required Python packages:

```bash
pip install opencv-python
pip install cvzone
```

## Usage

1. Run the `gesture_presentation_control.py` file:

```bash
python gesture_presentation_control.py
```

2. Ensure that your webcam is connected and positioned correctly.
3. Hold your hand in front of the webcam and use the following gestures:
   - Move your hand left or right to navigate through slides.
   - Display a closed fist to draw on the slide.
   - Extend three fingers to erase the drawing.
4. Press 'q' to quit the application.

## Troubleshooting

- If you encounter any issues, ensure that your Python environment is correctly set up and that all dependencies are installed.
- Make sure your webcam is functioning properly and positioned correctly for hand tracking.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.
