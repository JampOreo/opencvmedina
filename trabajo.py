import cv2
import numpy as np

def draw_python_logo(img, x, y, scale=1.0):
    """Draws a simplified Python logo."""

    # Define colors
    blue = (0, 255, 255)  # Yellow for the top snake
    yellow = (255, 255, 0) # Blue for the bottom snake
    black = (0, 0, 0)

    # Scale coordinates
    def scaled(val):
        return int(val * scale)

    # Top snake (yellow)
    cv2.ellipse(img, (x + scaled(50), y + scaled(50)), (scaled(40), scaled(20)), 0, 0, 360, yellow, -1)
    cv2.ellipse(img, (x + scaled(50), y + scaled(50)), (scaled(40), scaled(20)), 0, 0, 360, black, 2)
    cv2.ellipse(img, (x + scaled(80), y + scaled(80)), (scaled(20), scaled(40)), 0, 0, 360, yellow, -1)
    cv2.ellipse(img, (x + scaled(80), y + scaled(80)), (scaled(20), scaled(40)), 0, 0, 360, black, 2)

    # Bottom snake (blue)
    cv2.ellipse(img, (x + scaled(50), y + scaled(150)), (scaled(40), scaled(20)), 0, 0, 360, blue, -1)
    cv2.ellipse(img, (x + scaled(50), y + scaled(150)), (scaled(40), scaled(20)), 0, 0, 360, black, 2)
    cv2.ellipse(img, (x + scaled(20), y + scaled(120)), (scaled(20), scaled(40)), 0, 0, 360, blue, -1)
    cv2.ellipse(img, (x + scaled(20), y + scaled(120)), (scaled(20), scaled(40)), 0, 0, 360, black, 2)

    #eyes
    cv2.circle(img, (x + scaled(90), y + scaled(60)), scaled(5), black, -1)
    cv2.circle(img, (x + scaled(10), y + scaled(110)), scaled(5), black, -1)

# Main code
img = np.zeros((300, 300, 3), np.uint8)

draw_python_logo(img, 50, 50, scale=1.0)

# Add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'ola sebas', (80, 250), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('omega medina workis', img)
cv2.waitKey(0)
cv2.destroyAllWindows()