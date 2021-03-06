import datetime
import random
def bot():
    print("Bot: আপনাকে স্বাগতম।")

    while(True):

        user_input = input('Me: ')
        print('Bot:', end=' ')

        if user_input in ['ধন্যবাদ', 'আপনাকে ধন্যবাদ']:
            print('আপনাকে কিভাবে সাহায্য করতে পারি?\n')

        elif user_input in ['তোমার নাম কি', 'তোমার নাম বল', 'তুমি কে', 'কে তুমি', 'নাম কি', 'কি নাম']:
            print('আমার নাম অমুক।\n')

        elif user_input in ['তুমি কি কর', 'তোমার কাজ কি', 'তোমার উদ্দেশ্য কি']:
            #print('আমার কাজ আপনাদের আনন্দ দেয়া ।\n')
            print('আমার কাজ আপনাদের প্রশ্নের উত্তর  দেয়া ।\n')

        elif user_input in ['আজ কি বার', 'কি বার', 'আজকে কি বার']:
            day = datetime.date.today()
            day_no = day.weekday()
            if day_no == 0:
                print('আজ সোমবার')
            elif day_no == 1:
                print('আজ মঙ্গলবার')
            elif day_no == 2:
                print('আজ বুধবার')
            elif day_no == 3:
                print('আজ বৃহস্পতিবার')
            elif day_no == 4:
                print('আজ শুক্রবার')
            elif day_no == 5:
                print('আজ শনিবার')
            elif day_no == 6:
                print('আজ রবিবার')

        elif user_input in ['তুমি কেমন আছ', 'কেমন আছো', 'আপনি কেমন আছেন', 'ভাল আছো', 'কি খবর']:
            print('আমি ভাল আছি। আমাকে প্রশ্ন করুন।')

        elif user_input in ['তুমি কি মানুষ']:
            print('না। আমি ভার্চুয়াল এজেন্ট।')

        elif user_input in ['বয়স কত', 'তোমার বয়স কত', 'আপনার বয়স কত']:
            print('এক দিন।')

        elif user_input in ['তুমি ছেলে না মেয়ে', 'তুমি কি ছেলে', 'তুমি কি মেয়ে']:
            print('আমি মানুষ না।')

        elif user_input in ['তুমি কি রোবট', 'তুমি কি']:
            print('আমি একটি চ্যাটবট।')

        elif user_input in ['তুমি কোথায় থাক', 'তোমার বাসা কই', 'তোমার ঠিকানা কি']:
            print('আমি সব জায়গায় থাকি।')

        elif user_input in ['exit','ভাল থাকবেন','বিদায়','আল্লাহাফেজ']:
            print('বিদায়।')
            break

        else:
            rand = random.randint(0,4)

            if rand == 0:
                print('দুঃখিত। বুঝতে পারি নি। অন্য কিছ জিজ্ঞেস করুন।')

            elif rand == 1:
                print('দুঃখিত। মাথার উপর দিয়ে গেছে । আরেকবার জিজ্ঞেস করুন')

            elif rand == 2:
                print('দুঃখিত । আরেকবার জিজ্ঞেস করুন')

            elif rand == 3:
                print('দুঃখিত । আমার প্রোগ্রাম আপনার কথা বুঝছেনা । আনুগ্রহ পুরবক অন্য কিছ জিজ্ঞেস করুন ।')

            else:
                print('দুঃখিত । এইটা আমার জ্ঞান এর বাইরে  । আনুগ্রহ পুরবক অন্য কিছু জিজ্ঞেস করুন।')


if __name__ == '__main__':
    bot()
