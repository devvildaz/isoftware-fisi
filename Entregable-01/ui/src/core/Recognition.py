import boto3
from botocore import UNSIGNED
from botocore.client import Config
import os
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor
from kivy.core.image import Image as CoreImage


def ProcessFoo(photodir):
  photo = os.path.basename(photodir)
  bucket = 'mybucket677'
  s3 = boto3.client('s3',
    aws_access_key_id = "AKIA3FHVZEYFTTL5QK4E",
    aws_secret_access_key = "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",
    region_name = "us-east-2",
  )
  s3.upload_file(photodir, bucket,photo )

  client=boto3.client('rekognition',
    aws_access_key_id = "AKIA3FHVZEYFTTL5QK4E",
    aws_secret_access_key = "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",
    region_name = "us-east-2",
  )

  s3_connection = boto3.resource('s3',
    aws_access_key_id = "AKIA3FHVZEYFTTL5QK4E",
    aws_secret_access_key = "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",
    region_name = "us-east-2",
  )
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
      file_extension = os.path.splitext(photo)[1][1:]
      if file_extension.upper() == 'JPG': 
          file_extension = 'jpeg'
      item['image'] = io.BytesIO()
      image.save(item['image'], format=file_extension)
      item['image'].seek(0)
      item['image'] = CoreImage(item['image'], ext=file_extension)
      item['labels'] = []
      for emotion in faceDetail['Emotions']:
          if emotion["Confidence"] > 0:
              disstr = f'{emotion["Type"]}: {emotion["Confidence"]}' 
              item['labels'].append(disstr)
      res_arr.append(item)
  return res_arr
