import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
  ret, frame = cap.read()

  #print(cap.get(cv2.CAP_PROP_FPS))
  #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # grayscale
  canny = cv2.Canny(frame, 100, 200) # noise reduction, gradient calculation, non maximum suppression, double threshold, edge tracking by hysteresis
  cv2.imshow('LIVE', canny)

  if ret == True:
    out.write(canny) # write video.avi

  if cv2.waitKey(1) & 0xFF == ord('q'):  # q to close
    break

# manage memory
cap.release()
out.release()

cv2.destroyAllWindows()