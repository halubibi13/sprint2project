import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


#-----Start of Set Up-----#

my_page = st.sidebar.radio('Contents',['Client: ITZY',"Exploring Spotify Data",'Part 1: Widen Listenership','Part 2: Create a Spotlight', 'Recommendations','The Team']) # creates sidebar #

st.markdown("""<style>.css-1aumxhk {background-color: #e1cfcb;background-image: none;color: #e1cfcb}</style>""", unsafe_allow_html=True) # changes background color of sidebar #

#-----End of Set Up-----#


#-----Start of Page 1 (Client: ITZY)-----#

if my_page == 'Client: ITZY':

    st.title("Making ITZY the Next Biggest K-Pop Girl Group")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
    c1, c2,c3 = st.beta_columns((1,2,1))
    c2.image('ITZY introduction.jpg',use_column_width=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
    st.markdown("Our group’s hypothetical client is ITZY’s management team. In this made up scenario, they approached us to help them with strategizing on how to make ITZY the next biggest K-Pop girl group. The ways we thought of doing that is by (1) widening their listenership and (2) creating a spotlight on ITZY.")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
    st.subheader("Who is ITZY?")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
    st.markdown('<iframe width="560" height="315" src="https://www.youtube.com/embed/wTowEKjDGkU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # for space between title and paragraph #
    st.markdown(" ITZY is a South Korean girl group formed by JYP Entertainment and they debuted on February 2019. They currently have an almost 3.5 million monthly listeners on Spotify with already 3 EPs, 1 album, and 1 single album under their belt. They’re popularly known for their own brand of spunkiness and their relentless advocacy for being true to one’s self.")
    
    
#-----End of Page 1 (Client: ITZY)-----#

#-----Start of Page 2 (Exploring Spotify Data)-----#

df1 = pd.read_csv("kpop_girlgroup_data.csv")
df2 = pd.read_csv("song characteristics.csv")

if my_page == "Exploring Spotify Data":

    st.title("Exploring Spotify Data")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    
    st.markdown('The data we used for our exploratory data analysis (EDA) were scraped through Spotify API and are the daily top 200  most streamed tracks from January 1, 2017 to January 15, 2021. We then focused our analysis on K-Pop girl groups and on ITZY.',unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("ITZY is the 5th most streamed K-Pop girl group on Spotify with 22, 997, 615 total streams for their charting songs")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    mycolors1 = ["#b88f89","#b88f89", "#b88f89", "#b88f89","#77a9b4"]
    sns.set_palette(sns.color_palette(mycolors1))
    sns.set_style("whitegrid")
    top5 = df1.groupby('artist')[['streams']].sum().sort_values(by="streams", ascending=False).head(5)
    plt.figure(figsize=(10, 7))
    fig, ax = plt.subplots()
    ax = sns.barplot(x=top5.index, y=top5.streams, data=top5)
    plt.ylabel("Streams for charting songs",fontsize=12, labelpad=20)
    plt.xlabel("K-Pop Girl Groups",fontsize=12, labelpad=20)
    plt.ticklabel_format(axis='y', style='plain')
    plt.rcParams['xtick.labelsize']=10
    plt.rcParams['ytick.labelsize']=10
    plt.ylim([0,300000000])
    a = ax
    for p in a.patches:
             a.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=10, weight="bold",color='gray', xytext=(0, 20),
                 textcoords='offset points')
    st.pyplot(fig)
    
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown("Despite being new to the game, ITZY is currently the 5th most streamed K-pop girl group on Spotify with almost 23 million total streams for their charting songs. They’re accompanied in the top 5 by BLACKPINK, TWICE, MOMOLAND, and Red Velvet.")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    
    
    st.subheader("Streams for ITZY’s charting songs increase with every EP/album release")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.image('Time Series ITZY.png',use_column_width=True)
    st.markdown("Through our further EDA, we saw that the streams for ITZY’s charting songs increase with every EP or album release. That got us wondering what is it about ITZY’s songs that made people want to listen to them? What’s their difference with the other K-Pop girl groups mentioned earlier?")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("ITZY has the most danceable charting songs")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    mycolors2 = ["#77a9b4", "#b88f89","#b88f89", "#b88f89", "#b88f89"]
    sns.set_palette(sns.color_palette(mycolors2))
    sns.set_style("whitegrid") 
    dance_data = df2[['artist','danceability']].sort_values(by="danceability", ascending=False)
    plt.figure(figsize=(11, 7))
    fig, ax = plt.subplots()
    ax = sns.barplot(x='artist', y='danceability', data=dance_data)
    plt.ylabel("Song Danceability",fontsize=11, labelpad=15)
    plt.xlabel("K-Pop Girl Group",fontsize=11, labelpad=15)
    plt.ticklabel_format(axis='y', style='plain')
    plt.rcParams['xtick.labelsize']=9
    plt.rcParams['ytick.labelsize']=9
    plt.ylim([0,1])
    a = ax
    for p in a.patches:
             a.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=10, weight="bold",color='gray', xytext=(0, 20),
                 textcoords='offset points')
    st.pyplot(fig)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown("In our exploration of the Spotify data, we saw that compared to the other K-Pop girl groups, ITZY has the most danceable charting songs. The **danceability** audio feature of Spotify tracks *describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.*")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    
    
    st.subheader("ITZY has the most energetic charting songs")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    mycolors3 = ["#77a9b4", "#b88f89","#b88f89", "#b88f89", "#b88f89"]
    sns.set_palette(sns.color_palette(mycolors3))
    sns.set_style("whitegrid")

    energy_data = df2[['artist','energy']].sort_values(by="energy", ascending=False)

    plt.figure(figsize=(11, 7))
    fig, ax = plt.subplots()
    ax = sns.barplot(x='artist', y='energy', data=energy_data)
    plt.ylabel("Song Energy",fontsize=11, labelpad=15)
    plt.xlabel("K-Pop Girl Group",fontsize=11, labelpad=15)
    plt.ticklabel_format(axis='y', style='plain')
    plt.rcParams['xtick.labelsize']=9
    plt.rcParams['ytick.labelsize']=9
    plt.ylim([0,1])
    a = ax
    for p in a.patches:
             a.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=10, weight="bold",color='gray', xytext=(0, 20),
                 textcoords='offset points')
    st.pyplot(fig)
    
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('ITZY also has the most energetic charting songs. The **energy** audio feature of Spotify tracks *represents a perceptual measure of intensity and activity. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.* A value of 0.0 means the song has low energy and 1.0  means the song has high energy.')
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("ITZY’s  charting songs tend to have a positive sound")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    mycolors4 = ["#b88f89", "#b88f89","#77a9b4", "#b88f89", "#b88f89"]
    sns.set_palette(sns.color_palette(mycolors4))
    sns.set_style("whitegrid")

    val_data = df2[['artist','valence']].sort_values(by="valence", ascending=False)

    plt.figure(figsize=(11, 7))
    fig, ax = plt.subplots()
    ax = sns.barplot(x='artist', y='valence', data=val_data)
    plt.ylabel("Song Valence",fontsize=12, labelpad=15)
    plt.xlabel("K-Pop Girl Group",fontsize=12, labelpad=15)
    plt.ticklabel_format(axis='y', style='plain')
    plt.rcParams['xtick.labelsize']=9
    plt.rcParams['ytick.labelsize']=9
    plt.ylim([0,1])
    a = ax
    for p in a.patches:
             a.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=10, weight="bold",color='gray', xytext=(0, 20),
                 textcoords='offset points')
    st.pyplot(fig)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown("In terms of how positive their tracks sound, ITZY scored a little more than halfway—still sounds a bit positive but not as cheerful as that of MOMOLAND's. The **valence** audio feature of Spotify tracks *describes the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)*.")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="text-align: left;color: #bd4b30; font-size: large;font-weight: bold;">Note</div>',unsafe_allow_html=True)
    st.markdown("Italicized parts are directly lifted from Spotify's Web API Reference for developers.")
    link = '[Access the reference through this link.](https://developer.spotify.com/documentation/web-api/reference/#endpoint-get-audio-features)'
    st.markdown(link, unsafe_allow_html=True)
#-----End of Page 2 (Exploring ITZY's Spotify Data)-----#


#-----Start of Page 3 (Part 1: Widen Listenership)-----#

elif my_page == 'Part 1: Widen Listenership':
    st.title("Widen listenership: Collaborate with other artists")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.image('Solution 1.png',use_column_width=True)
    st.markdown("Our first suggestion to ITZY’s management team is to widen the group's listenership by collaborating with other artists. According to a study by Ordanini et. al entitled *\"The featuring phenomenon in music: how combining artists of different genres increases a song’s popularity\"* (2018), the average likelihood of entering in Billboards’ Top 10 Hit by a song with a featured artist is 18.4%, significantly greater than the 13.9% likelihood for songs that do not include a featured artist.")
    st.markdown("")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("Who Should ITZY Collaborate With?")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown("To look for possible music collaborators for ITZY, we’ve built a recommendation engine with the following technical details and resulting metrics:",unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    c1,c2 = st.beta_columns((1,2))
    c1.markdown('<div style="text-align: left;color: #77a9b4; font-weight: bold;">Classification algorithm used </div>',unsafe_allow_html=True)
    c2.markdown("k Nearest Neighbors",unsafe_allow_html=True)
    
    c3,c4 = st.beta_columns((1,2))
    c3.markdown('<div style="text-align: left;color: #77a9b4; font-weight: bold;">Optimal k</div>',unsafe_allow_html=True)
    c4.markdown("19",unsafe_allow_html=True)
    
    c5,c6 = st.beta_columns((1,2))
    c5.markdown('<div style="text-align: left;color: #77a9b4; font-weight: bold;">Genres used for training</div>',unsafe_allow_html=True)
    c6.markdown("Pop, R&B, Rap",unsafe_allow_html=True)
    
    c7,c8 = st.beta_columns((1,2))
    c7.markdown('<div style="text-align: left;color: #77a9b4; font-weight: bold;">Features used to train model</div>',unsafe_allow_html=True)
    c8.markdown("danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo",unsafe_allow_html=True)
    
    c9,c10 = st.beta_columns((1,2))
    c9.markdown('<div style="text-align: left;color: #77a9b4; font-weight: bold;">Target variable</div>',unsafe_allow_html=True)
    c10.markdown("Genre",unsafe_allow_html=True)
    
    c11,c12 = st.beta_columns((1,2))
    c11.markdown('<div style="text-align: left;color: #77a9b4; font-weight: bold;">Metrics</div>',unsafe_allow_html=True)
    c12.markdown("*Accuracy:* 65%", unsafe_allow_html=True)
    c12.markdown("*Multiclass ROC AUC:* 80% ", unsafe_allow_html=True)
    c12.markdown("*Multiclass F1:* 64%", unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown("The data we used to train the model were scraped from the Spotify API and are tracks from playlists with titles explicitly stating the genre (Pop, R&B, Rap). We took the playlist with the most number of followers with the assumption that since lots of people follow those playlists, it means they agree that the tracks on those playlists belong on the genres stated on their titles.", unsafe_allow_html=True)
    st.markdown("After training the model to classify the genres, a representative track was made by aggregating the audio features of ITZY’s charting songs. Its similarity was then computed against other songs based on the cosine distance of the audio features and the predicted genre probabilities. A playlist with similar audio features as that of ITZY’s representative track is deployed on Spotify. You may listen to those songs through the link below:", unsafe_allow_html=True)
    link = '[Spotify Playlist Link](https://open.spotify.com/playlist/3iwKMiQ0EVEFooxMwGDHjb)'
    st.markdown(link, unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    
    st.subheader("List of Recommended Artists per Genre")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown("For each genre, we picked five songs with the greatest similarity to ITZY's representative track. We interpreted that those artists whose songs have great similarity with the representative track are possible collaborators.", unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('We also wanted to know how the recommended artists fare when it comes to the number of streams of their charting songs. ITZY’s team might also consider going for an artist with high number of streams when deciding who to collaborate with.',unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    option = st.selectbox('Choose genre', ['Pop', 'R&B', 'Rap'])
    
    if option == 'Pop':
        
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Recommended Pop Artists</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        #Pop reco
        a1,a2,a3,a4,a5 = st.beta_columns(5)
        a1.image('Pop-Sigma.jpg',use_column_width=True)
        a1.markdown('<div style="text-align: center;color: #c6793a; font-weight: bold;">Sigma</div>',unsafe_allow_html=True)
        a1.markdown('<div style="text-align: center;color: #666666; font-style: italic">3.2*</div>',unsafe_allow_html=True)
        a2.image('Pop-Lady Gaga.jpg',use_column_width=True)
        a2.markdown('<div style="text-align: center;color: #c6793a; font-weight: bold;">Lady Gaga</div>',unsafe_allow_html=True)
        a2.markdown('<div style="text-align: center;color: #666666; font-style: italic">3.26*</div>',unsafe_allow_html=True)
        a3.image('Pop-Flo Rida.jpg',use_column_width=True)
        a3.markdown('<div style="text-align: center;color: #c6793a; font-weight: bold;">Flo Rida</div>',unsafe_allow_html=True)
        a3.markdown('<div style="text-align: center;color: #666666; font-style: italic">4.5*</div>',unsafe_allow_html=True)
        a4.image('Pop-Nevada.jpg',use_column_width=True)
        a4.markdown('<div style="text-align: center;color: #c6793a; font-weight: bold;">Nevada</div>',unsafe_allow_html=True)
        a4.markdown('<div style="text-align: center;color: #666666; font-style: italic">4.6*</div>',unsafe_allow_html=True)
        a5.image('Pop-Camila.jpg',use_column_width=True)
        a5.markdown('<div style="text-align: center;color: #c6793a; font-weight: bold;">Camila Cabello</div>',unsafe_allow_html=True)
        a5.markdown('<div style="text-align: center;color: #666666; font-style: italic">4.67*</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown("*\* Cosine distance value (×10^-3). Lower value indicates closeness of the audio features of the recommended artist's song to ITZY's representative track.*",unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Camila Cabello is the most streamed recommended Pop artist based on her charting songs for the period of January 2017 to January 2021</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        df3 = pd.read_csv("popreco_streams.csv")

        
        mycolors5 = ["#c6793a", "#c6793a","#c6793a", "#c6793a", "#c6793a"]
        sns.set_palette(sns.color_palette(mycolors5))
        sns.set_style("whitegrid")
        plt.figure(figsize=(12, 7))
        fig, ax = plt.subplots()
        ax = sns.barplot(x=df3.artist, y=df3.streams, data=df3)
        plt.ylabel("Streams for charting songs",fontsize=11, labelpad=15)
        plt.xlabel("Recommended pop artists",fontsize=11, labelpad=15)
        plt.ticklabel_format(axis='y', style='plain')
        plt.rcParams['xtick.labelsize']=9
        plt.rcParams['ytick.labelsize']=9
        plt.ylim([0,120000000])
        a = ax
        for p in a.patches:
             a.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=9, weight="bold",color='#c6793a', xytext=(0, 20),
                 textcoords='offset points')
        st.pyplot(fig)
                
    elif option == 'R&B':
        
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Recommended R&B Artists</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        #R&B Reco
        b1,b2,b3,b4,b5 = st.beta_columns(5)
        b1.image('R&B-Drake.jpg',use_column_width=True)
        b1.markdown('<div style="text-align: center;color: #77a9b4; font-weight: bold;">Drake</div>',unsafe_allow_html=True)
        b1.markdown('<div style="text-align: center;color: #666666; font-style: italic">86.39*</div>',unsafe_allow_html=True)
        b2.image('R&B-Charlie.jpg',use_column_width=True)
        b2.markdown('<div style="text-align: center;color: #77a9b4; font-weight: bold;">Charlie Puth</div>',unsafe_allow_html=True)
        b2.markdown('<div style="text-align: center;color: #666666; font-style: italic">89.57*</div>',unsafe_allow_html=True)
        b3.image('R&B-Why.jpg',use_column_width=True)
        b3.markdown('<div style="text-align: center;color: #77a9b4; font-weight: bold;">Why Don’t We</div>',unsafe_allow_html=True)
        b3.markdown('<div style="text-align: center;color: #666666; font-style: italic">91.11*</div>',unsafe_allow_html=True)
        b4.image('R&B-Kygo.jpg',use_column_width=True)
        b4.markdown('<div style="text-align: center;color: #77a9b4; font-weight: bold;">Kygo</div>',unsafe_allow_html=True)
        b4.markdown('<div style="text-align: center;color: #666666; font-style: italic">91.67*</div>',unsafe_allow_html=True)
        b5.image('R&B-David.jpg',use_column_width=True)
        b5.markdown('<div style="text-align: center;color: #77a9b4; font-weight: bold;">David Guetta</div>',unsafe_allow_html=True)
        b5.markdown('<div style="text-align: center;color: #666666; font-style: italic">93.02*</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown("*\* Cosine distance value (×10^-3). Lower value indicates closeness of the audio features of the recommended artist's song to ITZY's representative track.*",unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Drake is the most streamed recommended R&B artist based on his charting songs for the period of January 2017 to January 2021</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        
        df4 = pd.read_csv("rnbreco_streams.csv")

        mycolors6 = ["#77a9b4", "#77a9b4","#77a9b4", "#77a9b4", "#77a9b4"]
        sns.set_palette(sns.color_palette(mycolors6))
        sns.set_style("whitegrid")
        plt.figure(figsize=(12, 7))
        fig, ax = plt.subplots()
        ax = sns.barplot(x=df4.artist, y=df4.streams, data=df4)
        plt.ylabel("Streams for charting songs",fontsize=11, labelpad=15)
        plt.xlabel("Recommended R&B artists",fontsize=11, labelpad=15)
        plt.ticklabel_format(axis='y', style='plain')
        plt.rcParams['xtick.labelsize']=9
        plt.rcParams['ytick.labelsize']=9
        plt.ylim([0,120000000])
        a = ax
        for p in a.patches:
             a.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=9, weight="bold",color="#77a9b4", xytext=(0, 20),
                 textcoords='offset points')
        st.pyplot(fig)
                    
    else:
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Recommended Rap Artists</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        #Rap Reco
        d1,d2,d3,d4,d5 = st.beta_columns(5)
        d1.image('Rap-Lost Kings.jpg',use_column_width=True)
        d1.markdown('<div style="text-align: center;color: #565b7b; font-weight: bold;">Lost Kings</div>',unsafe_allow_html=True)
        d1.markdown('<div style="text-align: center;color: #666666; font-style: italic">85.18*</div>',unsafe_allow_html=True)
        d2.image('Rap-Charlie Puth.jpg',use_column_width=True)
        d2.markdown('<div style="text-align: center;color: #565b7b; font-weight: bold;">Charlie Puth</div>',unsafe_allow_html=True)
        d2.markdown('<div style="text-align: center;color: #666666; font-style: italic">91.89*</div>',unsafe_allow_html=True)
        d3.image('Rap-Lil Nas X.jpg',use_column_width=True)
        d3.markdown('<div style="text-align: center;color: #565b7b; font-weight: bold;">Lil Nas X</div>',unsafe_allow_html=True)
        d3.markdown('<div style="text-align: center;color: #666666; font-style: italic">93.54*</div>',unsafe_allow_html=True)
        d4.image('Rap-Tyga.jpg',use_column_width=True)
        d4.markdown('<div style="text-align: center;color: #565b7b; font-weight: bold;">Tyga</div>',unsafe_allow_html=True)
        d4.markdown('<div style="text-align: center;color: #666666; font-style: italic">93.65*</div>',unsafe_allow_html=True)
        d5.image('Rap-Demi.jpg',use_column_width=True)
        d5.markdown('<div style="text-align: center;color: #565b7b; font-weight: bold;">Demi Lovato</div>',unsafe_allow_html=True)
        d5.markdown('<div style="text-align: center;color: #666666; font-style: italic">97.21*</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown("*\* Cosine distance value (×10^-3). Lower value indicates closeness of the audio features of the recommended artist's song to ITZY's representative track.*",unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Charlie Puth is the most streamed recommended Rap artist based on his charting songs for the period of January 2017 to January 2021</div>',unsafe_allow_html=True)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        df5 = pd.read_csv("rapreco_streams.csv")
        mycolors7 = ["#565b7b", "#565b7b","#565b7b", "#565b7b", "#565b7b"]
        sns.set_palette(sns.color_palette(mycolors7))
        sns.set_style("whitegrid")
        plt.figure(figsize=(12, 7))
        fig, ax = plt.subplots()
        ax = sns.barplot(x=df5.artist, y=df5.streams, data=df5)
        plt.ylabel("Streams for charting songs",fontsize=11, labelpad=15)
        plt.xlabel("Recommended rap artists",fontsize=11, labelpad=15)
        plt.ticklabel_format(axis='y', style='plain')
        plt.rcParams['xtick.labelsize']=9
        plt.rcParams['ytick.labelsize']=9
        plt.ylim([0,120000000])
        a = ax
        for p in a.patches:
            a.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=9, weight="bold",color="#565b7b", xytext=(0, 20),
                textcoords='offset points')
        st.pyplot(fig)
        
        
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("Audio Features Comparison")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    df6 = pd.read_csv("itzyfeatures_vs_reco.csv")
    mycolors = ["#b88f89", "#c6793a","#77a9b4","#565b7b"]
    sns.set_palette(sns.color_palette(mycolors))
    sns.set_style("whitegrid")
    plt.figure(figsize=(8, 6))
    fig, ax = plt.subplots()
    ax = sns.barplot(x=df6.variable, y=df6.value, hue = df6.category, data=df6)
    plt.ylabel("Value",fontsize=11, labelpad=15)
    plt.xlabel("Features",fontsize=11, labelpad=15)
    plt.ticklabel_format(axis='y', style='plain')
    plt.rcParams['xtick.labelsize']=9
    plt.rcParams['ytick.labelsize']=9
    plt.ylim([0,1])
    a = ax
    for p in a.patches:
                 a.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center', fontsize=9, weight='bold',color='gray', xytext=(0, 20),
                     textcoords='offset points')
    st.pyplot(fig)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('When compared to the aggregated audio features of the recommended songs per genre, ITZY’s representative track is the most danceable, most energetic, and most positive sounding. It is followed by Rap in danceability (how danceable a track is), Pop in energy (measure of a track’s intensity), and R&B for valence (measure of a track’s “cheerfulness”).',unsafe_allow_html=True)

#-----End of Page 3 (Part 1: Widen Listenership)-----#


#-----Start of Page 4 (Part 2: Create a Spotlight)-----#

elif my_page == 'Part 2: Create a Spotlight':
    st.title("Create a spotlight on ITZY")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.image('Solution 2.png',use_column_width=True)
    st.markdown("Another suggestion that we have for ITZY’s management team is to create a spotlight for ITZY. That means releasing songs on months with least activity from other K-Pop girl groups in order to focus the audience attention on ITZY.")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("Other most streamed K-Pop girl groups tend to release their songs on Spotify during April onwards")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.image('Timeline Top4.png',use_column_width=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown("According to our data, the other most streamed K-Pop girl groups tend to release their songs on Spotify during April onwards (with the exception of MOMOLAND). Upon seeing this pattern we wanted to see how this  contrast that with ITZY’s past releases. ")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("ITZY’s previous release dates do not coincide with other K-Pop girl groups aside from the ‘Not Shy’ release")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.image('Timeline ITZY.png',use_column_width=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown("We saw that ITZY released their debut album on February 2019 and another EP on March 2020, which are outside the April to December period mentioned earlier—however two of their releases were within that period.")
    
#-----End of Page 4 (Part 2: Create a Spotlight)-----#


#-----Start of Page 5 (Recommendations)-----#

elif my_page == 'Recommendations':
    st.title("Recommendations")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("Artists to collaborate with based on the number of streams of his/her charting songs")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    h1,h2,h3,h4,h5 = st.beta_columns(5)
    h1.image('Pop-Camila.jpg',use_column_width=True)
    h1.markdown('<div style="text-align: center;color: #c6793a; font-weight: bold;">Camila Cabello</div>',unsafe_allow_html=True)
    h1.markdown('<div style="text-align: center;color: #666666; font-style: italic">96.9M Streams</div>',unsafe_allow_html=True)
    h1.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    h3.image('R&B-Drake.jpg',use_column_width=True)
    h3.markdown('<div style="text-align: center;color: #77a9b4; font-weight: bold;">Drake</div>',unsafe_allow_html=True)
    h3.markdown('<div style="text-align: center;color: #666666; font-style: italic">82.7M Streams</div>',unsafe_allow_html=True)
    h5.image('Rap-Charlie Puth.jpg',use_column_width=True)
    h5.markdown('<div style="text-align: center;color: #565b7b; font-weight: bold;">Charlie Puth</div>',unsafe_allow_html=True)
    h5.markdown('<div style="text-align: center;color: #666666; font-style: italic">69.8M Streams</div>',unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("Artists to collaborate with based on song similarity (cosine distance)")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    i1,i2,i3,i4,i5 = st.beta_columns(5)
    i1.image('Pop-Sigma.jpg',use_column_width=True)
    i1.markdown('<div style="text-align: center;color: #c6793a; font-weight: bold;">Sigma</div>',unsafe_allow_html=True)
    i1.markdown('<div style="text-align: center;color: #666666; font-style: italic">3.2×10^-3</div>',unsafe_allow_html=True)
    i3.image('R&B-Drake.jpg',use_column_width=True)
    i3.markdown('<div style="text-align: center;color: #77a9b4; font-weight: bold;">Drake</div>',unsafe_allow_html=True)
    i3.markdown('<div style="text-align: center;color: #666666; font-style: italic">86.39×10^-3</div>',unsafe_allow_html=True)
    i5.image('Rap-Lost Kings.jpg',use_column_width=True)
    i5.markdown('<div style="text-align: center;color: #565b7b; font-weight: bold;">Lost Kings</div>',unsafe_allow_html=True)
    i5.markdown('<div style="text-align: center;color: #666666; font-style: italic">85.18×10^-3</div>',unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("What musical direction to pursue")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('ITZY can also base their collaboration decision on genres since each of them exhibit high values on different audio features.',unsafe_allow_html=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    option = st.selectbox('Choose genre', ['Pop', 'R&B', 'Rap'])
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    df7 = pd.read_csv("itzyfeatures_vs_reco.csv")
    df7 = df7[~df7.category.str.contains('ITZY')]
    if option == 'Rap':
    
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Recommended Rap songs are the most danceable</div>',unsafe_allow_html=True)
        dance = df7[df7["variable"]=="danceability"]
        mycolors = ["#c6793a","#77a9b4","#565b7b"]
        sns.set_palette(sns.color_palette(mycolors))
        sns.set_style("whitegrid")
        plt.figure(figsize=(8, 6))
        fig, ax = plt.subplots()
        ax = sns.barplot(x=dance.category, y=dance.value, ci = None, data=dance)
        plt.ylabel("Danceability Value",fontsize=11, labelpad=15)
        plt.xlabel("Genre",fontsize=11, labelpad=15)
        plt.ticklabel_format(axis='y', style='plain')
        plt.rcParams['xtick.labelsize']=9
        plt.rcParams['ytick.labelsize']=9
        plt.ylim([0,1])
        a = ax
        for p in a.patches:
                     a.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', fontsize=9, weight='bold',color='gray', xytext=(0, 20),
                         textcoords='offset points')
        st.pyplot(fig)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('If ITZY wants to create a danceable song, they can consider collaborating with someone under the Rap genre.',unsafe_allow_html=True)
        
    elif option == 'Pop':
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Recommended Pop songs are the most energetic</div>',unsafe_allow_html=True)
        
        energy = df7[df7["variable"]=="energy"]
        mycolors = ["#c6793a","#77a9b4","#565b7b"]
        sns.set_palette(sns.color_palette(mycolors))
        sns.set_style("whitegrid")
        plt.figure(figsize=(8, 6))
        fig, ax = plt.subplots()
        ax = sns.barplot(x=energy.category, y=energy.value, ci = None, data=energy)
        plt.ylabel("Energy Value",fontsize=11, labelpad=15)
        plt.xlabel("Genre",fontsize=11, labelpad=15)
        plt.ticklabel_format(axis='y', style='plain')
        plt.rcParams['xtick.labelsize']=9
        plt.rcParams['ytick.labelsize']=9
        plt.ylim([0,1])
        a = ax
        for p in a.patches:
                     a.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', fontsize=9, weight='bold',color='gray', xytext=(0, 20),
                         textcoords='offset points')
        st.pyplot(fig)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('If ITZY wants to create an energetic song, they can consider collaborating with someone under the Pop genre.',unsafe_allow_html=True)
       
    else :
        
        st.markdown('<div style="text-align: left; font-weight: bold;font-size: large;">Recommended R&B songs are the most positive sounding</div>',unsafe_allow_html=True)
        
        valence = df7[df7["variable"]=="valence"]
        mycolors = ["#c6793a","#77a9b4","#565b7b"]
        sns.set_palette(sns.color_palette(mycolors))
        sns.set_style("whitegrid")
        plt.figure(figsize=(8, 6))
        fig, ax = plt.subplots()
        ax = sns.barplot(x=valence.category, y=valence.value, ci = None, data=valence)
        plt.ylabel("Valence Value",fontsize=11, labelpad=15)
        plt.xlabel("Genre",fontsize=11, labelpad=15)
        plt.ticklabel_format(axis='y', style='plain')
        plt.rcParams['xtick.labelsize']=9
        plt.rcParams['ytick.labelsize']=9
        plt.ylim([0,1])
        a = ax
        for p in a.patches:
                     a.annotate("%.2f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', fontsize=9, weight='bold',color='gray', xytext=(0, 20),
                         textcoords='offset points')
        st.pyplot(fig)
        st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
        st.markdown('If ITZY wants to create a cheerful song, they can consider collaborating with someone under the R&B genre.',unsafe_allow_html=True)
        
    
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.subheader("Song release activities on months of January to March are few to none, desirable for future ITZY releases")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.image('Timeline Empty.png',use_column_width=True)
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('ITZY’s management team can consider doing future releases on the months of January to March, as data from previous years show that release activities from other most streamed K-Pop girl groups tend to be few to none.',unsafe_allow_html=True)
    
#-----End of Page 5 (Recommendation)-----#


#-----Start of Page 6 (The Team)-----#
elif my_page == 'The Team':
    st.title("The Team")
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    g1,g2,g3 = st.beta_columns(3)
    g1.markdown('<div style="text-align: left;font-size: large;font-weight: bold;">Mikee Jazmines</div>',unsafe_allow_html=True)
    g1.markdown('<div style="text-align: left;font-style: italic;color: gray;">Mentor</div>',unsafe_allow_html=True)
    g1.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    link = '[LinkedIn](https://www.linkedin.com/in/mikee-jazmines-059b48bb/)'
    g1.markdown(link, unsafe_allow_html=True)
    link = '[GitHub](https://github.com/mikeejazmines)'
    g1.markdown(link, unsafe_allow_html=True)
    
    g2.markdown('<div style="text-align: left;font-size: large;font-weight: bold;">Andrei Labayan</div>',unsafe_allow_html=True)
    g2.markdown('<div style="text-align: left;font-style: italic;color: gray;">Member</div>',unsafe_allow_html=True)
    g2.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    link = '[LinkedIn](https://www.linkedin.com/in/andrei-gabriel-labayan-48a8ba1a4/)'
    g2.markdown(link, unsafe_allow_html=True)
    link = '[GitHub](https://github.com/aalabayan)'
    g2.markdown(link, unsafe_allow_html=True)
    
    
    g3.markdown('<div style="text-align: left;font-size: large;font-weight: bold;">Patrick Nuguid</div>',unsafe_allow_html=True)
    g3.markdown('<div style="text-align: left;font-style: italic;color: gray;">Member</div>',unsafe_allow_html=True)
    g3.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    link = '[LinkedIn](https://www.linkedin.com/in/patricknuguid/)'
    g3.markdown(link, unsafe_allow_html=True)
    link = '[GitHub](https://github.com/halubibi13)'
    g3.markdown(link, unsafe_allow_html=True)
    
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    st.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    
    
    g4,g5,g6 = st.beta_columns(3)
    g4.markdown('<div style="text-align: left;font-size: large;font-weight: bold;">Phoemela Ballaran</div>',unsafe_allow_html=True)
    g4.markdown('<div style="text-align: left;font-style: italic;color: gray;">Member</div>',unsafe_allow_html=True)
    g4.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    link = '[LinkedIn](https://www.linkedin.com/in/phoemela-ballaran/)'
    g4.markdown(link, unsafe_allow_html=True)
    link = '[GitHub](https://github.com/phoemelaballaran)'
    g4.markdown(link, unsafe_allow_html=True)
    
    g5.markdown('<div style="text-align: left;font-size: large;font-weight: bold;">Razel Manapat</div>',unsafe_allow_html=True)
    g5.markdown('<div style="text-align: left;font-style: italic;color: gray;">Member</div>',unsafe_allow_html=True)
    g5.markdown('<div style="color: #FFFFFF;">.</div>',unsafe_allow_html=True) # space #
    link = '[LinkedIn](https://www.linkedin.com/in/razel-manapat-745650166/)'
    g5.markdown(link, unsafe_allow_html=True)
#-----End of Page 6 (The Team)-----#