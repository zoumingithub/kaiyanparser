import data
data.load_data()
for vlst in data.categorized_data:
    for video in vlst:
        print 'wget \"{}\" -O {}.mp4'.format(video['playUrl'],video['id'])
        print 'aws s3 cp {}.mp4 s3://feednews-video-id/videos/{}.mp4'.format(video['id'],video['id'])
        print 'rm -f {}.mp4'.format(video['id'])
