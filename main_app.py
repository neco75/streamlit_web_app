from re import T
import streamlit as st
import os
import re

#拡張子除いたファイル取得
st.title('参考にしたURLを貼るだけのページ')
#拡張子除いたファイル取得
main_tag=[]
other=['その他']
pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
filepath='pages/'
tag=os.listdir(filepath)

for p in tag:
    name =os.path.splitext(os.path.basename(p))[0]
    if(name!='.DS_Store'):
        if(name!='creator'):
            main_tag.append(name)

main_tag.sort()
main_tag+=other

#セレクトボックス
select=st.selectbox(
'登録するサイトのカテゴリ選択',
main_tag)

if select=='その他':
	select_other=st.text_input('カテゴリーを追加')
	btn_add=st.button('追加')
	if btn_add:
		f=open('pages/' + select_other + '.py','w')
		f.close
		f=open('pages/' + select_other + '.py','w')
		f.write(f'import streamlit as st\n\nst.title(\'{select_other}\')\n')
		f.close()
		tag.append(select_other)
		st.text(f'「{select_other}」がカテゴリーに追加されました\nサイトをリロード後カテゴリ選択から選んでください')
		select=select_other
		select_other=' '
		is_file1 = os.path.isfile('pages/.py')
		is_file2 = os.path.isfile('pages/.DS_Store.py')
		if is_file1:
			os.remove('pages/.py')
		if is_file2:
			os.remove('pages/.DS_Store.py')
else:
	is_file1 = os.path.isfile('pages/.py')
	is_file2 = os.path.isfile('pages/.DS_Store.py')
	if is_file1:
		os.remove('pages/.py')
	if is_file2:
		os.remove('pages/.DS_Store.py')

with st.form(key='post_form'):

	#テキストボックス
	title=st.text_input('タイトル')
	url=st.text_input('参考にしたサイトのURL')
	text=st.text_input('サイトの簡易的な説明')

	#ボタン
	btn_post=st.form_submit_button('送信')
	if btn_post:
		if len(title)!=0 and len(url)!=0 and len(text)!=0:
			if re.match(pattern, url):
				f=open('pages/' + select + '.py','a')
				f.write(f'\nst.text(\'タイトル:{title}\\nURL:{url}\\n説明:{text}\')')
				f.close()
				st.text(f'カテゴリー「{select}」に登録されました')
			else:
				st.text('urlが正しくありません\n先頭がhttpsまたはhttpの文字列を入力してください')
		else: st.text('項目を記入してください')
