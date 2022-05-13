import boto3
import os
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor

def ProcessFoo(photodir):
  photo = os.path.basename(photodir)
  bucket = 'mybucket677'
  s3 = boto3.client('s3')
  s3.upload_file(photodir, bucket,photo )

  client=boto3.client('rekognition')

  s3_connection = boto3.resource('s3')
  s3_object = s3_connection.Object(bucket,photo)
  s3_response = s3_object.get()

  stream = io.BytesIO(s3_response['Body'].read())

  response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
      Attributes=['ALL'])

  res_arr = []
  for faceDetail in response['FaceDetails']:
      item = {}
      image = Image.open(stream)
      imgWidth, imgHeight = image.size
      draw = ImageDraw.Draw(image)
      box = faceDetail['BoundingBox']
      left = imgWidth * box['Left']
      top = imgHeight * box['Top']
      width = imgWidth * box['Width']
      height = imgHeight * box['Height']

      points = (
          (left,top),
          (left + width, top),
          (left + width, top + height),
          (left , top + height),
          (left, top)

      )
      draw.line(points, fill='#00d400', width=2)
      item['image'] = image 
      item['labels'] = []
      for emotion in faceDetail['Emotions']:
          if emotion["Confidence"] > 0:
              disstr = f'{emotion["Type"]}: {emotion["Confidence"]}' 
              item['labels'].append(disstr)
      res_arr.append(item)
  return res_arr
