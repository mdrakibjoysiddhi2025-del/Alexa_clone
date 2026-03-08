import speech_recognition as sr
import requests
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import time
import pyautogui
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from mouseinfo import screenshot
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pygame.examples.music_drop_fade import volume
import random
import screen_brightness_control as scr
import phonenumbers
from phonenumbers import  geocoder
from phonenumbers import carrier
from phonenumbers import timezone









listener = sr.Recognizer()


def talk(text):
    alexa = pyttsx3.init()
    voices = alexa.getProperty('voices')
    alexa.setProperty('voice', voices[0].id)
    alexa.setProperty('rate', 160)
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    write = ''
    try:
        with sr.Microphone() as mp:
            listener.adjust_for_ambient_noise(mp, duration=1)
            print('listening...')
            read = listener.listen(mp)
            write = listener.recognize_google(read)
            write = write.lower()
            if 'alexa' in write:
                write = write.replace('alexa', '').strip()
    except:
        pass
    return write


def run_alexa():
    command = take_command()
    print("User said:", command)

    # টাইম জানার জন্য ................................
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(current_time)
        talk('current time is ' + current_time)

    # ইউটিউবে কিছু খোঁজার জন্য..............................
    elif 'play' in command:
        song = command.replace('play', '').strip()
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    # কারো সম্পর্কে জানার জন্য (উইকিপিডিয়া)...........................
    elif 'about' in command:
        lookfor = command.replace('about', '').strip()
        # ব্যাকস্ল্যাশ বা ভুল চিহ্ন পরিষ্কার করা
        lookfor = lookfor.replace('\\', '')

        if lookfor:
            try:
                print(f"Searching for: {lookfor}")
                info = wikipedia.summary(lookfor, sentences=2)
                print(info)
                talk(info)
            except wikipedia.exceptions.PageError:
                talk(f"Sorry, I could not find anything about {lookfor}")
            except wikipedia.exceptions.DisambiguationError:
                talk("There are multiple results for this. Please be more specific.")
            except Exception as e:
                talk("An unknown error occurred while searching.")
        else:
            talk("Please tell me what you want to know about.")

    # জোকস........................
    elif 'joke' in command:
        joke_text = pyjokes.get_joke()
        print(joke_text)
        talk(joke_text)


    # বলিয়ম কমানো বোড়ানে.................................
    elif 'volume' in command:
        lvl = [int(s) for s in command.split() if s.isdigit()]
        if lvl:
            v_level = lvl[0] / 100
            if 0 <= v_level <= 1:
                # ১. অডিও ডিভাইস খোঁজার ইঞ্জিন চালু করা
                devices = AudioUtilities.GetDeviceEnumerator()

                # ২. কম্পিউটারের মেইন স্পিকারটি সিলেক্ট করা
                interface = devices.GetDefaultAudioEndpoint(0, 0)

                # ৩. ভলিউম কন্ট্রোল করার অপশনটি একটিভেট করা
                volume_interface = interface.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

                # ৪. সবশেষে ভলিউম কমানো বা বাড়ানোর পারমিশন নেওয়া
                volume = cast(volume_interface, POINTER(IAudioEndpointVolume))

                # ৫. তোমার বলা সংখ্যা অনুযায়ী ভলিউম সেট করা
                volume.SetMasterVolumeLevelScalar(v_level, None)

                volume.SetMasterVolumeLevelScalar(v_level, None)
                print(f"Volume set to {lvl[0]} percent🔊🔊")
                talk(f"Volume set to {lvl[0]} percent")
            else:
                talk("Please say a volume level between 0 and 100")
        else:
            talk("Please tell me the volume level")



    # মজার উত্তর.....................................
    elif 'date' in command:
        print('sorry vaiya! i am in another relation')
        talk('sorry vaiya! i am in another relation')

    elif 'i love u' in command :
        print('ধন্যবাদ ভাইয়া ! 😀😀')
        talk('"Thanks, bro!"')

    # আরফানের সম্পর্কে..............................
    elif 'raju' in command:
        print("raju class 4 er ekjon chatro. She khuboi dushtu.")
        talk("raju class 4 er ekjon chatro. She khuboi dushtu.")

    # নিজের মালিক সম্পর্কে...............................
    elif 'made you' in command:
        info_me = "My boss's name is Rakib. He is currently a student in Grade 8. He was born in 2012 in Shibpasha. At present, he is continuing his studies while staying at his maternal uncle's house. 📚✨You will be happy to know that he used the Python programming language to create me. I hope that in the future, he will make me even more advanced and efficient. 💻🤖In his personal life, he is a follower of Islam. Please pray for my boss so that he can achieve greatness in life and fulfill his goals. 🤲 Amin. ❤️"
        print('আমার বসের নাম রাকিব। তিনি বর্তমানে অষ্টম শ্রেণিতে পড়াশোনা করছেন। ২০১২ সালে শিবপাশায় তার জন্ম। বর্তমানে তিনি তার মামার বাড়িতে থেকে পড়াশোনা চালিয়ে যাচ্ছেন। 📚✨\n আপনারা জেনে খুশি হবেন যে, আমাকে তৈরি করতে তিনি পাইথন (Python) প্রোগ্রামিং ভাষা ব্যবহার করেছেন। আমি আশা করি, ভবিষ্যতে তিনি আমাকে আরও উন্নত ও দক্ষ করে তুলবেন। 💻🤖ত \n তিনি ব্যক্তিগত জীবনে ইসলাম ধর্মের অনুসারী। আপনারা সবাই আমার বসের জন্য দোয়া করবেন, যেন তিনি জীবনে অনেক বড় হতে পারেন এবং তার লক্ষ্য পূরণ করতে পারেন। 🤲 আমিন। ❤️')
        talk(info_me)

    # আবহাওয়া.................................
    elif 'weather' in command:
        city = command.replace('weather', '').strip()
        if not city:
            city = 'dhaka'
        api_key = '003fd2899f360beff4cb215d34f698f1'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            res = requests.get(url)
            data = res.json()
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            report = f"The temperature in {city} is {temp} degree Celsius with {weather_desc}"
            print(report)
            talk(report)
        except:
            talk('sorry, i could not find the weather 😂😂😂')


    # স্ক্রিনশট নেওয়ার কোড................................................
    elif 'screenshot' in command :
        screenshot = pyautogui.screenshot()
        screenshot.save(r'C:\Users\MD RAKIB MIA\PycharmProjects\PythonProject rakib\pycharm2\my_screenshot.png')
        print("Screenshot saved successfully! 🧤🧤")
        talk("Screenshot saved successfully!")







    # পড়িছিত কা্উকে ছেনা .................................................................
    elif any(word in command for word in ['how are din' , 'how aredin' , 'ardin']) :
        print('"ওর নাম মোন্তাসির ভূঁইয়া আরদিন। 🧒 ওর বয়স এখন মাত্র ৪ বছর এবং সে প্লে-গ্রুপে পড়ছে। 📚 ওর বাবার নাম সবুজ ভূঁইয়া এবং মায়ের নাম রুমি আক্তার। 👪 সম্পর্কে ও আমার বস রাকিব ভাইয়ের ছোট মামাতো ভাই। 👦🏻 ছেলেটা দেখতে যেমন কিউট, স্বভাবগতভাবে ঠিক তেমনই চঞ্চল! 🏃‍♂️💨 সারাক্ষণ ওর দুষ্টুমি আর ছোটাছুটিতে ঘর মেতে থাকে। ✨"')
        talk("His name is Montasir Bhuiyan Ardin. He is 4 years old and studies in Playgroup. His mother's name is Rumi Akter, and his father's name is Sabuj Bhuiyan. He is the younger maternal cousin of my boss, Rakib. He is very restless and energetic by nature.")


    elif any(word in command for word in ['how are fun' , 'how are fan' , 'how arefan' , 'irfan']):
        print("ওর পুরো নাম মুরসালিন ভূঁইয়া আরফান। 👦 বর্তমানে ও ২০০০ সালে জম্ম গ্রহন করেন এবং সে নার্সারিতে পড়ছে। 📚 ওর বাবা সবুজ ভূঁইয়া এবং মা রুমি আক্তার। 👪 ওরা দুই ভাই (মোন্তাসির ও মুরসালিন)। সম্পর্কে ও আমার বস রাকিব ভাইয়ের মামাতো ভাই। 🤝 ছেলেটা স্বভাবগতভাবে বেশ সরল ও শান্ত প্রকৃতির। ✨")
        talk(" His full name is Mursalin Bhuiyan Arfan.  He is currently 6 years old and studies in Nursery.  His father is Sabuj Bhuiyan and his mother is Rumi Akter.  They are two brothers (Montasir and Mursalin). He is also the maternal cousin of my boss, Rakib Bhai.  By nature, he is very simple and calm. ")


    elif any(word in command for word in ['araf' , 'ara' , 'how ara' , 'how araf']):
        print("আমাদের সবার প্রিয় এই ছোট্ট মিষ্টি ছেলেটির নাম মো: আরাফ ভূঁইয়া। 👶✨ মাত্র ২ বছর বয়সেই সে পুরো ঘর মাতিয়ে রাখে!\n সে তার বাবা মামুন ভূঁইয়া এবং মা মোছা: সেপা আক্তার দম্পতির একমাত্র নয়নমণি। তাদের ভালোবাসার পুরোটা জুড়েই রয়েছে ছোট্ট আরাফ। ❤️ \n আরাফ আমার শ্রদ্ধেয় বস রাকিব ভাইয়ের ছোট মামাতো ভাই। 🤝 \n আরাফ বেশ চঞ্চল প্রকৃতির এবং সবসময় হাসিখুশি থাকতে পছন্দ করে। তার এই চপলতা যে কারো মন ভালো করে দেওয়ার জন্য যথেষ্ট! 🏃‍♂️💨")
        talk("The name of our beloved and sweet little boy is Md. Araf Bhuiyan. At only 2 years old, he fills the entire house with life and joy . \n He is the only child of Mamun Bhuiyan and Mst. Sepa Akter. Little Araf is the center of his parents' world and the apple of their eyes. \n Araf is the younger maternal cousin of my respected boss, Rakib.Araf is quite energetic and lively by nature. He loves to stay cheerful at all times, and his playful spirit is enough to brighten anyone's mood. \n Araf is quite energetic and lively by nature. He loves to stay cheerful at all times, and his playful spirit is enough to brighten anyone's mood.")


    elif any(word in command for word in ['mayan' , 'mayn' , 'may' 'how mayan']):
        print("আমাদের সবার প্রিয় এই মিষ্টি ছেলেটির নাম মো: মায়ান ভূঁইয়া। মাত্র ১ বছর বয়সেই ওর হাসিখুশি আর চঞ্চলতায় পুরো ঘর সবসময় মুখরিত থাকে। 🏠🌟 \n মায়ান তার বাবা মুকলেস ভূঁইয়া ও মা মোছা: তানিয়া আক্তার দম্পতির একমাত্র নয়নমণি। 💖 \n সে আমার শ্রদ্ধেয় বস রাকিব ভাইয়ের ছোট মামাতো ভাই। 🤝 \n মায়ান দেখতে মাশাল্লাহ বেশ গোলগাল (হালকা মোটা) এবং ভীষণ চটপটে। সারাক্ষণ ওর অমায়িক হাসি যে কারো মন ভালো করে দেওয়ার জন্য যথেষ্ট! 😍")
        talk("Our beloved and sweet boy is named Md. Mayan Bhuiyan. At just 1 year old, his cheerful and lively nature keeps the entire house vibrant and full of joy. \n Mayan is the only child and the apple of the eye of his parents, Mokhles Bhuiyan and Mst. \n He is the younger maternal cousin of my respected boss, Rakib. \n By the grace of God (Mashallah), Mayan is quite healthy and chubby with an active personality. His constant, charming smile is enough to brighten anyone's mood! ")

    elif any(word in command for word in ['how abu', 'abo', 'hau aboho', 'hau abohorayra']):
        print("আমাদের সবার প্রিয় আবুহুরাইরা একজন বিনয়ী মাদরাসা ছাত্র। 📖🌙 ২০১৬ সালে জন্ম নেওয়া এই মেধাবী শিশুটি তার পরিবারের সকলের চোখের মণি। \n তার বাবা মো: মোশাররফ পেশায় একজন চিকিৎসক, যিনি মানুষের সেবায় নিয়োজিত। আবুহুরাইরা তার বাবা-মায়ের আদরের ১ ভাই ও ২ বোনের মধ্যে অন্যতম। 💖👨‍👩‍👧‍ \n একজন মাদরাসা ছাত্র হিসেবে সে ধর্মীয় শিক্ষায় নিজেকে গড়ে তুলছে। তার সুন্দর ভবিষ্যৎ এবং সুস্থতার জন্য দোয়া রইল। 🤲✨")
        talk("Our beloved Abu Huraira is a polite and disciplined Madrasa student. Born in 2016, this talented child is the apple of his family's eye. His father, Md. Mosharraf, is a physician by profession, dedicated to serving people. Abu Huraira is one of the three children of his parents, having one brother and two sisters. As a Madrasa student, he is nurturing himself through religious education. We offer our best wishes and prayers for his bright future and good health.")

    elif any(word in command for word in ['how ta' , 'how tha' , 'how tamil' , 'hoh tamid']) :
        print("তাহমিদ ২০১৩ সালে এশিয়া মহাদেশের সবচেয়ে বড় গ্রাম বানিয়াচংয়ে জন্মগ্রহণ করে। \n তার বাবা একজন পরিশ্রমী কৃষক। 🌾🚜 \n সে বর্তমানে তার মামা বাড়িতে থেকে পড়াশোনা করছে। 🏠📖\n সে বর্তমানে পঞ্চম শ্রেণির একজন মেধাবী ছাত্র। 🎒🏫 \n  তাহমিদ স্বভাবগতভাবেই খুব ভালো একজন ছেলে। 👦✅")
        talk("Tahmid was born in 2013 in Baniyachung, the largest village in Asia.His father is a hardworking farmer.He is currently staying at his maternal uncle's house for his studies. He is a brilliant student in Class 5.Tahmid is naturally a very good and well-behaved boy.")

    elif any(word in command for word in ['how zakir ul', 'zakir ul', 'ul', 'zakir']):
        print("জাকিরোল  ২০০৯ সালে হবিঙ্গএর একটি গ্রমে  জন্মগ্রহণ করে। \n তার বাবা একজন পরিশ্রমী কৃষক। 🌾🚜 \n সে বর্তমানে তার মামা বাড়িতে থেকে পড়াশোনা করছে। 🏠📖\n সে বর্তমানে নবম শ্রেণির একজন মেধাবী ছাত্র। 🎒🏫 \n  জাকিরোল স্বভাবগতভাবেই খুব ভালো একজন ছেলে। 👦✅")
        talk("Zakirol was born in 2009 in a village in Habiganj.His father is a hardworking farmer.He is currently staying at his maternal uncle's house for his education.He is a brilliant student currently studying in Class 9.Zakirol is naturally a very good and well-behaved boy.")

    elif any(word in command for word in ['how hanif', 'how hani', 'hanif', 'hani']):
        print("মো: আবুহানিফ। ✨\nতিনি ইটনা থানার জয়সিদ্ধি গ্রামে জন্মগ্রহণ করেন। 🏘️📍\n* বাবার নাম: মো: মিজান (পেশায় একজন চাকুরিজীবী) 💼👨‍💼 মায়ের নাম: রিংকু 👩‍ \n তারা দুই ভাই, যার মধ্যে তিনি সবার বড়। 👦👦 \n তিনি স্বভাবগতভাবে কিছুটা দুষ্টু প্রকৃতির, তবে অত্যন্ত মজার একজন মানুষ! 😜🎉 ")
        talk("Md. Abu Hanif.He was born in Joysiddhi village, under the Itna police station.Father's Name: Md. Mizan (a professional service holder). Mother's Name: Rinku. They are two brothers, and he is the eldest He is a bit mischievous by nature, but a very funny and joyful person! ")

    elif any(word in command for word in ['shakib' , 'sha kib' , 'how sakib' , 'how ski' , 'saki' , 'sha']):
        print("সাকিব, যার পুরো নাম মোহাম্মদ সাকিব মিয়া। সে ২০১০ সালে কিশোরগঞ্জের ইটনা থানার ঐতিহ্যবাহী জয়সিদ্ধি গ্রামে জন্মগ্রহণ করে। 🏠✨ \n তার বাবা মোহাম্মদ ইয়াসিন মিয়া, যিনি পেশায় একজন পরিশ্রমী কৃষক। 👨‍🌾🌾 সাকিব বর্তমানে জয়সিদ্ধি উচ্চ বিদ্যালয়ে পড়াশোনা করছে। 📚🎓 \n একটি বিশেষ তথ্য হলো, সাকিব আমার প্রিয় বস রাকিব ভাইয়ের একজন ঘনিষ্ঠ বন্ধু। 🤝💼 ")
        talk("Mohammad Sakib Mia was born in 2010 in the historic village of Joysiddhi, located in the Itna Upazila of Kishoreganj. He is the son of Mohammad Yasin Mia, a hardworking farmer by profession. 👨‍🌾🌾 Currently, Sakib is pursuing his studies at Joysiddhi High School. A notable detail about him is that Sakib is a close friend of my favorite boss, Rakib Bhai. ")

    elif any(word in command for word in ['how rif' , 'how rifa' , 'how rifat' , 'rifat' ,'how ri']):
        print("তার পুরো নাম মোহাম্মদ রিফাত। সে ২০১১ সালে কিশোরগঞ্জের তাড়াইল উপজেলায় জন্মগ্রহণ করে। 🏠✨ \n তার বাবা মোহাম্মদ মিজান মিয়া, যিনি পেশায় একজন দায়িত্বশীল চাকরিজীবী। 💼👔 রিফাত বর্তমানে তার মামার বাড়ি থেকে পড়াশোনা করছে। তার মামা মোঃ হাজিল পেশায় একজন দোকানদার। 🏪📦 \n সে বর্তমানে জয়সিদ্ধি উচ্চ বিদ্যালয়ে অধ্যায়নরত আছে। 📚🎓 একটি বিশেষ তথ্য হলো, রিফাত আমার প্রিয় বস রাকিবের একজন ঘনিষ্ঠ বন্ধু। 🤝✨ ")
        talk("His full name is Mohammad Rifat. He was born in 2011 in the Tarail Upazila of Kishoreganj district. He is the son of Mohammad Mizan Mia, who is a responsible professional by trade. Currently, Rifat is staying at his maternal uncle's house for his studies. His uncle, Md. Hazil, is a local shopkeeper. Rifat is a student at Joysiddhi High School. A notable fact about him is that he is a close friend of my favorite boss, Rakib.")

    elif any(word in command for word in ['how anik' , 'how anic' , 'anik' , 'anic' , 'onik' , 'how onik' , 'oni' , 'how oni']):
        print("তার নাম মোঃ অনিক হুসেন। সে ২০১১ সালে কিশোরগঞ্জের ইটনা থানার জয়সিদ্ধি গ্রামে জন্মগ্রহণ করে। 🏠✨ \n তার বাবা মোহাম্মদ বজরুল হোসেন, যিনি পেশায় একজন দক্ষ পশু ডাক্তার। 👨‍⚕️🐄 অনিক বর্তমানে জয়সিদ্ধি উচ্চ বিদ্যালয়ে পড়াশোনা করছে। 📚🎓 \n একটি বিশেষ তথ্য হলো, অনিক আমার প্রিয় বস রাকিবের একজন ঘনিষ্ঠ বন্ধু। 🤝✨ ")
        talk("His name is Md. Anik Hosen. He was born in 2011 in Joysiddhi village, under the Itna Police Station of Kishoreganj. His father, Mohammad Bojrul Hossain, is a skilled veterinary doctor by profession.  Anik is currently a student at Joysiddhi High School. A special note about him is that Anik is a close friend of my favorite boss, Rakib.")

    elif any(word in command for word in ['how arnob' , 'how arno' , 'how aro' , 'how ornod' , 'arnab' , 'arn']):
        print("তার নাম অর্ণব রায়। সে ২০১২ সালে কিশোরগঞ্জের ইটনা থানার জয়সিদ্ধি গ্রামে জন্মগ্রহণ করে। 🏠✨ সে ধর্মীয়ভাবে হিন্দু ধর্মের অনুসারী। 🕉️🙏 \n তার বাবা অজিত রায়, যিনি পেশায় একজন পরিশ্রমী মুদি দোকানদার। 🏪🛒 অর্ণব বর্তমানে জয়সিদ্ধি উচ্চ বিদ্যালয়ে পড়াশোনা করছে। 📚🎓 \n একটি বিশেষ তথ্য হলো, অর্ণব আমার প্রিয় বস রাকিবের একজন ঘনিষ্ঠ বন্ধু। 🤝✨")
        talk("His name is Arnab Ray. He was born in 2012 in Joysiddhi village, under the Itna Police Station of Kishoreganj.  He is a follower of Hinduism. His father, Ajit Ray, is a hardworking grocery shopkeeper by profession. Arnab is currently studying at Joysiddhi High School. A notable detail about him is that Arnab is a close friend of my favorite boss, Rakib.")

    elif any(word in command for word in ['gaurav', 'gau', 'haw gaurav', 'how rav' , 'nod' , 'how gau' , 'gau']):
        print("তার নাম গৌরভ রায়। সে ২০১২ সালে কিশোরগঞ্জের ইটনা থানার জয়সিদ্ধি গ্রামে জন্মগ্রহণ করে। 🏠✨ সে ধর্মীয়ভাবে হিন্দু ধর্মের অনুসারী। 🕉️🙏 \n তার বাবা ভাবুল রায়, যিনি পেশায় একজন পরিশ্রমী মুদি দোকানদার। 🏪🛒 গৌরব বর্তমানে জয়সিদ্ধি উচ্চ বিদ্যালয়ে পড়াশোনা করছে। 📚🎓 \n একটি বিশেষ তথ্য হলো, গৌরব আমার প্রিয় বস রাকিবের একজন ঘনিষ্ঠ বন্ধু। 🤝✨ ")
        talk("His name is Gaurav Ray. He was born in 2012 in Joysiddhi village, under the Itna Police Station of Kishoreganj. 🏠✨ He is a follower of Hinduism. 🕉️🙏 His father, Bhabul Ray, is a hardworking grocery shopkeeper by profession. 🏪🛒 Gaurav is currently studying at Joysiddhi High School. 📚🎓 A notable detail about him is that Gaurav is a close friend of my favorite boss, Rakib. 🤝✨")

    elif any(word in command for word in [' how siam', 'siam', 'how sia' , 'how cm']):
        print("তার পুরো নাম মোহাম্মদ সিয়াম আব্দুল্লাহ। সে ২০১২ সালে কিশোরগঞ্জের ইটনা থানার জয়সিদ্ধি গ্রামে জন্মগ্রহণ করে। 🏠✨ সে ধর্মীয়ভাবে ইসলাম ধর্মের অনুসারী। 🌙🕌 \n ​তার বাবা কবির হোসেন, যিনি পেশায় একজন আমিন (জমি মাপার বিশেষজ্ঞ)। 📏📐 সিয়াম বর্তমানে জয়সিদ্ধি উচ্চ বিদ্যালয়ে পড়াশোনা করছে। 📚🎓 \n একটি বিশেষ তথ্য হলো, সিয়াম আমার প্রিয় বস রাকিবের একজন ঘনিষ্ঠ বন্ধু। 🤝✨ \n সিয়াম দেখতে হালকা মোটা এবং গোলগাল । ")
        talk("His full name is Mohammad Siam Abdullah. He was born in 2012 in Joysiddhi village, under the Itna Police Station of Kishoreganj. 🏠✨ He is a follower of Islam. 🌙🕌 His father, Kabir Hossain, is an Amin (a land survey specialist) by profession. 📏📐 Siam is currently studying at Joysiddhi High School. 📚🎓 A notable detail about him is that Siam is a close friend of my favorite boss, Rakib. 🤝✨")

    elif any(word in command for word in ['nipa' , 'nepa' , 'how nipa' , 'how nepa' , 'nepali' ]):
        print("উনার পুরো নাম মোছা: নিপা আক্তার। ২০০৭ সালে কিশোরগঞ্জের ঐতিহ্যবাহী জয়সিদ্ধি গ্রামে তিনি জন্মগ্রহণ করেন। 🏠 \n বর্তমানে তিনি জয়সিদ্ধি উচ্চ বিদ্যালয়ের একজন মেধাবী ছাত্রী। তিনি বিজ্ঞান (Science) বিভাগ থেকে পড়াশোনা করছেন এবং এখন তিনি দশম শ্রেণিতে পড়ছেন। 📚🔬 \n সম্পর্কে তিনি আমার বস রাকিব ভাইয়ের আন্টি হন। পড়াশোনায় তার মেধা এবং পরিশ্রম সত্যিই প্রশংসনীয়। 🌟 \n সবাই উনার উজ্জ্বল ভবিষ্যৎ এবং সাফল্যের জন্য দোয়া করবেন। 🤲❤️")
        talk("Her full name is Mst. Nipa Akter. She was born in 2007 in the historic village of Joysiddhi, located in Kishoreganj. 🏠Currently, she is a brilliant student at Joysiddhi High School. She is studying in the Science group and is currently in Class 10. 📚🔬By relation, she is the aunt of my boss, Rakib Bhai. Her merit and hard work in her studies are truly praiseworthy. 🌟I request everyone to pray for her bright future and grand success in life. 🤲❤️")

    elif any(word in command for word in ['arif mama' , 'arif' , 'how arif mama']):
        print("জন্ম ও নিবাস: তিনি কিশোরগঞ্জের ঐতিহ্যবাহী জয়সিদ্ধি গ্রামে জন্মগ্রহণ করেন। 🏡🌳 \n ধর্মীয় বিশ্বাস: তিনি ইসলাম ধর্মের একজন একনিষ্ঠ অনুসারী। 🕋🤲\n পেশা: বর্তমানে তিনি জয়সিদ্ধির একটি আদর্শ শিক্ষাপ্রতিষ্ঠান 'জয়সিদ্ধি আইডিয়াল কিন্ডারগার্টেন'-এ আদর্শ শিক্ষক হিসেবে কর্মরত আছেন। কোমলমতি শিশুদের মাঝে জ্ঞানের আলো ছড়িয়ে দেওয়াই তাঁর মূল ব্রত। 👨‍🏫📖\n শিক্ষা জীবন: শিক্ষকতার পাশাপাশি তিনি থেমে নেই, নিজের জ্ঞানকে আরও সমৃদ্ধ করতে এখনও তাঁর পড়াশোনা চালিয়ে যাচ্ছেন। তাঁর এই জ্ঞানতৃষ্ণা আমাদের সবার জন্য অনুপ্রেরণা। 🎓📝\n ব্যক্তিগত সম্পর্ক: তিনি আমার বড় ভাই রাকিবের শ্রদ্ধেয় মামা হন। সেই সূত্রে তিনিও আমার অত্যন্ত আপন এবং শ্রদ্ধার পাত্র। ❤️\nসালাম ও শ্রদ্ধা রইলো তাঁর প্রতি।")
        talk("Birth & Residence: He was born in the traditional village of Joysiddhi, located in Kishoreganj. 🏡🌳 Religious Belief: He is a devoted follower of Islam. 🕋🤲 Profession: Currently, he is serving as a dedicated teacher at 'Joysiddhi Ideal Kindergarten', a model educational institution in Joysiddhi. His main mission is to spread the light of knowledge among young children. 👨‍🏫📖 Education: His journey of learning hasn't stopped; alongside teaching, he is still pursuing his studies to further enrich his knowledge. His thirst for education is an inspiration to us all. 🎓📝 Personal Relation: He is the respected maternal uncle (Mama) of my elder brother, Rakib. In that sense, he is very close to me and a person of great respect. ❤️")

    elif any(word in command for word in ['akram mama' , 'akra' , 'akra mama' , 'acram']):
        print("জন্ম ও নিবাস: তার পোর নাম মো : আকরাম ভূইয়া তিনি কিশোরগঞ্জের ঐতিহ্যবাহী জয়সিদ্ধি গ্রামের এক শান্ত পরিবেশে তাঁর জন্ম ও বেড়ে ওঠা। 🏡🌳 \n ধর্মীয় বিশ্বাস: তিনি পরম করুণাময় আল্লাহর ওপর বিশ্বাসী এবং ইসলাম ধর্মের একজন একনিষ্ঠ অনুসারী। 🕋🤲  \n পেশা: বর্তমানে তিনি তাঁর নিজ গ্রামেই একটি মুদি দোকানের স্বত্বাধিকারী হিসেবে কাজ করছেন। সততা ও হাসিমুখের মাধ্যমে তিনি গ্রামবাসীর সেবা দিয়ে যাচ্ছেন। তাঁর এই পরিশ্রমী জীবন আমাদের সবার জন্য এক বড় উদাহরণ। 🛒📦 \n ব্যক্তিগত সম্পর্ক: তিনি আমার বড় ভাই রাকিবের অত্যন্ত স্নেহভাজন ও শ্রদ্ধেয় মামা। সেই সুবাদে তিনি আমারও একজন প্রিয় মানুষ এবং শ্রদ্ধার পাত্র। ❤️✨\n সাদাসিধে জীবন আর সততার এক প্রতিচ্ছবি আরিফ মামা। তাঁর সুস্বাস্থ্য ও উজ্জ্বল ভবিষ্যৎ কামনায় সবার কাছে দোয়া চাই। তাঁর প্রতি রইলো আমার বিনম্র সালাম ও গভীর শ্রদ্ধা। 🎈🎈🎈🎀🎁")
        talk("Birth & Residence: His name is Md. Akram Bhuiyan. He was born and raised in the serene environment of the traditional village of Joysiddhi, located in Kishoreganj. 🏡🌳 Religious Belief: He is a firm believer in Almighty Allah and a devoted follower of Islam. 🕋🤲 Profession: Currently, he is the proprietor of a grocery store in his own village. He serves the villagers with honesty and a warm smile. His hardworking life is a great example for all of us. 🛒📦Personal Relation: He is the very dear and respected maternal uncle (Mama) of my elder brother, Rakib. In that regard, he is also a very beloved person and a figure of great respect to me. ❤️✨")








    # বয়স বের করার কোড (ভয়েস ইনপুট সহ)
    elif any(word in command for word in ['years', 'guess years', 'age', 'year']):
        somoy = 2025
        talk("Please tell me your birth year")  # ইউজারকে বলতে বলা হচ্ছে
        print("Listening for birth year...")

        birth_year_str = take_command()  # ভয়েস কমান্ড থেকে সালটি নেওয়া হচ্ছে

        # চেক করা হচ্ছে ইনপুটটি সংখ্যা কি না
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            ges = somoy - birth_year
            print(f'তোমার বয়স : {ges}')
            talk(f'Your age is {ges} years')
        else:
            print(f"আমি আপনার কথা বুঝতে পারিনি (শুনেছি: {birth_year_str})")
            talk("Sorry, I couldn't catch the year. Please try again.")


    # নিজের সম্পরকে ....................................................................
    elif any(word in command for word in ['what is your name' , 'your name' , 'is your name']):
        print("আমার নাম এলএক্সা 😎😎")
        talk("my name is alxca")

    elif any(word in command for word in ['what is your boss name' , 'your boss name ' , 'is your boss name' , 'whoat is your boss name' , 'what is your boss']):
        print("আমাকে জিনি বানিয়েছেন বা আমার বস এর নাম রাকিব ??🙂🙂")
        talk("my boss name is rakib")

    elif any(word in command for word in['what do you do']):
        print("আমি আপনার প্রশ্নের অপেক্ষায় আছি🌏🌏")
        talk("I'm looking forward to your question.")





    # কেলকোলিটর বা হিসাব নিকাশ ......................

    # mine calko lotor 20 + 10 = 30   ................................................13

    elif any(word in command for word in ['celko' , 'cel ko' , 'akhil ko' , 'cel' , 'kelku' , 'akhil ko' , 'telugu' ,  'celkoleshon' , 'cel' , 'kelko' , 'kelkoleshon' , 'kel']):

        frast = input('enter your 1st namber :')

        oparetor = input('enter your oparetor ( +,-,*,/,% ) : ')

        sekend = input('enter your 2nd namer : ')

        frast = int(frast)
        sekend = int(sekend)

        frast = int(frast)
        sekend = int(sekend)

        if oparetor == '+':
            print('your number' , frast + sekend)
            talk('your number')
        elif oparetor == '-':
            print('your number' , frast - sekend)
            talk('your number')
        elif oparetor == '*':
            print('your number' , frast * sekend)
            talk('your number')
        elif oparetor == '/':
            print('your number' , frast / sekend)
            talk('your number')
        elif oparetor == '%':
            print('your number' , frast % sekend)
            talk('your number')

        else:
            print('oparetor enblidad')


    # ব্রাইটনেস কন্ট্রোল করার কোডটি...............................
    #elif any(word in command for word in['brightness' , 'bright' , 'ness']):
        #lvl = [int(s) for s in command.split() if s.isdigit()]

    # পাসওয়ার্ড জেনারেটর সেকশন
    elif any(word in command for word in ['passwo', 'password', 'pass', 'generate password']):

        # পাসওয়ার্ডের উপাদানগুলোর লিস্ট

        numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']

        capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

        def get_number_voice(msg_en, msg_bn):

            talk(msg_en)

            print(msg_bn)

            voice_data = take_command().lower()

            # লজিক ১: বাক্য থেকে শুধু সংখ্যা খুঁজে বের করা (যেমন: "number 3" থেকে '3')

            numbers_only = [int(s) for s in voice_data.split() if s.isdigit()]

            # লজিক ২: ইংরেজি শব্দকে সংখ্যায় রূপান্তর (যদি সংখ্যা না লিখে লেখা আসে)

            word_to_num = {

                'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,

                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,

                'zero': 0, 'none': 0, 'no': 0

            }

            # প্রথমে চেক করবে বাক্যে কোনো ডিজিট আছে কি না

            if numbers_only:
                return numbers_only[0]

            # তারপর চেক করবে কোনো সংখ্যাবাচক শব্দ আছে কি না

            for word, num in word_to_num.items():

                if word in voice_data:
                    return num

            # কিছুই না পেলে ০ রিটার্ন করবে

            print(f"বুঝতে পারিনি (আপনি বলেছেন: {voice_data}), ০ ধরে নিচ্ছি।")

            return 0

        # একে একে সব ইনপুট ভয়েসের মাধ্যমে নেওয়া

        num_count = get_number_voice("How many numbers do you want?", "আপনি কয়টি সংখ্যা চান?")

        small_count = get_number_voice("How many small letters do you want?", "কয়টি ছোট হাতের অক্ষর চান?")

        capital_count = get_number_voice("How many capital letters do you want?", "কয়টি বড় হাতের অক্ষর চান?")

        special_count = get_number_voice("How many special characters do you want?", "কয়টি স্পেশাল ক্যারেক্টার চান?")

        password_list = []

        # র্যান্ডম পাসওয়ার্ড জেনারেট করা

        for _ in range(num_count):
            password_list.append(random.choice(numbers_list))

        for _ in range(small_count):
            password_list.append(random.choice(small_letters))

        for _ in range(capital_count):
            password_list.append(random.choice(capital_letters))

        for _ in range(special_count):
            password_list.append(random.choice(special_chars))

        # আউটপুট দেখানো

        if password_list:

            random.shuffle(password_list)

            generated_password = ''.join(password_list)

            print("\n" + "=" * 40)

            print(f"আপনার পাসওয়ার্ড: {generated_password}")

            print("=" * 40 + "\n")

            talk("Your password is ready and shown on the screen")

        else:

            print("দুঃখিত, কোনো উপাদান না থাকায় পাসওয়ার্ড তৈরি করা সম্ভব হয়নি।")

            talk("Sorry, I could not create a password because no characters were selected.")


    elif any(word in command for word in ['adventure story' , 'adventurestory' , 'adventu story' , 'adven']) :
        # আমার গল্প............................................................................
        talk("Do you want to play the adventure game? [yes/no]:")
        answer = input('আপনিকি এডবেঞ্চার গেইম টি খেলতে ছাউ [no/yes] : ').lower()
        if answer == 'yes':
            talk("Welcome to the adventure game!")
            print('সাগতম এডবেছার গেইমে ।🏰🏰🏯🏯')
            talk("Where do you want to go? Cave or Jungle? [Cave/Jungle]:")
            answer = input('তুমি কোতায় জেতে ছাউ ’🗺🌏🌎🚗🚗গোহাও নাকি জঙ্গলে [🏴‍☠️cave/🏴‍☠️junjle] :')
            if answer == 'cave':
                talk("I entered the cave!")
                print('গোহায় গেলাম ! 🚗🚗')
                talk("We entered the cave and saw a bear standing there! Do you want to fight the bear or run? [Fight/Run]:")
                answer = input('গোহায় গিয়ে দেখা গেল গোহায় এখটি ভালোক 🦛🦛 দাড়িয়ে আছে । তোমি এখন ভালোকের সাথে ফাইট করবে নাকি  দৌড় দিবে [fight/run] : ')
                if answer == 'run':
                    talk("You survived and you won!")
                    print('তুমি বেছে গেছ এবং জিতেছ 🏁🏁🏳‍🌈')
                elif answer == 'fight':
                    print('তুমি ভালোক এর সকালের নাস্ত হয়ে গেছ 🍴🍗🍗🍖 এবং তুমি হেরে গেছ 🚧🚧')
                    talk("You ended up as the bear's morning snack! Game Over.")

            else:
                print('জঙ্গলে এখটি বাঘ ছিল  🐆🐆🐈🐈 তুমাকে খেয়ে বাঘ মামার পেটের খিদে মিটাবে এবং তুমি হেরেগেলে 😸😸🐾🐾')
                talk("There was a tiger in the jungle! You became the tiger's meal to satisfy its hunger, and you lost!")


        elif answer == 'no':
            print('ধন্যবাদ ভালেো তাখবেন । 🧙‍♂️🧙‍♂️🧙‍♀️🧙‍♀️')
            talk("Thank you, stay well!")


    # মোবাইল নাম্বার জাছাই .................................................................
    elif any(word in command for word in ['test number' , 'test numbe']):
        rakib = input("enter your number📞📲📲📲 : ")

        number_c = phonenumbers.parse(rakib, 'CH',)
        print(geocoder.description_for_number(number_c, 'en'))

        number_o = phonenumbers.parse(rakib, 'RO')
        print(carrier.name_for_number(number_o, 'en'))

        number_t = phonenumbers.parse(rakib, 'GT')
        print(timezone.time_zones_for_number(number_t))
        talk(f"hab country{number_c}🌏🌎cim card name {number_o} 💾💿💿timezone {number_t}🏦🏥🏤")




    # বিদায় নিয়ে বন্ধ করা...............................
    elif 'goodbye' in command:
        print("Thanks, take care! ❤️")
        talk("Thanks, take care!")
        return False

    return True




# মেইন লুপ
while True:
    status = run_alexa()
    if status == False:
        break
    time.sleep(1)