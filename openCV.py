import cv2


img = cv2.imread('d3.jpg',1)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resize = cv2.resize(img,(200,200))
cv2.imshow('dhruv',resize)
cv2.imshow('galaxy',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()