from __future__ import unicode_literals
from icrawler.builtin import GoogleImageCrawler
import streamlit as st
from pdfminer.high_level import extract_text
from PIL import Image
from PIL import Image
import urllib.request
import streamlit as st
import shutil
import os

st.title('開発者ページ')
st.text('※pythonで勉強したもの置いとくだけです')
st.subheader('・Google画像スクレイピング')
#検索ワードと枚数指定
num=1
word=st.text_input('検索ワード')
num=st.text_input('画像の枚数')
btn=st.button('送信')
if btn:
	#100枚以下の時ディレクトリ作成＆画像取得
	if (len(word)!=0 and len(num)!=0):
		if(num.isdigit()==True):
			if int(num)<=100:
				crawler = GoogleImageCrawler(storage={"root_dir":f"{word}"})
				crawler.crawl(keyword=f"{word}",max_num=int(num))

				#ディレクトリ内の画像取得
				files=os.listdir(f"{word}")
				print(files)
				for file in files:
					image=Image.open(f'{word}/{file}')
					st.image(image,caption=file)

				#ディレクトリの削除
				#time.sleep(10)
				shutil.rmtree(f"{word}")

			#11枚以上の時再入力求める
			else:st.text("100枚以下で入力してください")
		else:st.text("枚数は整数値を入力してください")
	else: st.text("両方入力してください")


st.subheader('・YouTubeダウンロード(未完成)')
youtubeurl=st.text_input('urlを入力')
youtubebtn=st.button('URL送信')
if youtubebtn:
	if (len(youtubeurl)!=0):
		response = urllib.request.urlopen(youtubeurl)
		videos=st.video(f'{youtubeurl}')
		videos_label=st.text_input('ラベルを入力してください')
		#YouTube( youtubeurl ).streams.first().download()
		# 	if (len(videos_label)!=0):
		#with urllib.request.urlopen(response,'rb') as u:
		#st.download_button('download',response)
		# 	else:st.text('ラベルを入力してください')
	else:st.text('正しいurlを入力してください')



# st.subheader('・リアルタイム画像処理')
# def callback(frame):
#     img = frame.to_ndarray(format="bgr24")
#     img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
#     return av.VideoFrame.from_ndarray(img, format="bgr24")
# webrtc_streamer(key="example", video_frame_callback=callback)

st.subheader('・PDF文章読み取り')

# ３：PDFファイルを読み込む
filename = st.file_uploader("Choose a file",type='pdf')
if filename is not None:
    pdftext = extract_text(filename)
    st.text(pdftext)