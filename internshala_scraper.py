from bs4 import BeautifulSoup
import requests
import time

url="https://internshala.com/internships/android%20app%20development-internship/page-3"
html = requests.get(url).text



def find_Internships():
    with open('C:/Users/91889/OneDrive/Desktop/InternshipUpdate.txt','w') as Info_txt:
        Info_txt.truncate(0)
        soup = BeautifulSoup(html,'lxml')
        internships = soup.find_all('div',class_ ='internship_meta') # first did coding for 1 internship section
        for internship in internships: # and now applied for loop on lists of internships by changing above methode frm find -> find_all
            Role = internship.find('a',class_ ='view_detail_button').text.strip()
            if ('Android' in Role or 'Mobile' in Role ) and 'Flutter' not in Role: 
                Company = internship.find('a',class_ ="link_display_like_text view_detail_button").text.strip()
                timeline = internship.find_all('div',class_ ="item_body")
                duration = timeline[1].text.strip()
                apply_by = timeline[3].text.strip()
                apply_Link = internship.div.a['href']
                apply_Link = "https://internshala.com/"+apply_Link
                Info  = f"Role: {Role}\n" 
                Info += f"Company: {Company}\n" 
                Info += f"Inernship Duration: {duration}\n" 
                Info += f"Apply Before: {apply_by}\n"
                Info += f"Apply Link: {apply_Link}\n\n"
                if int(duration[0]) <= 3:
                    print(Info)
                    Info_txt.writelines(Info)

if __name__=="__main__":
        # while True:
            find_Internships()
            print("File Information Updated")
            # url = "https://internshala.com/internships/android%20app%20development-internship/page-2"
            # waiting_min = 15
            # time.sleep(waiting_min*60)