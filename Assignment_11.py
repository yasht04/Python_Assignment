import tkinter as tk
import webbrowser as wb

q = tk.Tk()
q.title("Query")
l2 = tk.Label(q, text="Enter Your course name: ", font=("Times New Roman", 25))
l2.grid()
input = tk.Entry(q, font=("Times New Roman", 25), width=30)
input.grid()


def save_input():
    query = input.get()
    f = open("save_query", "+a")
    f.writelines(["Query: ", query, "\n"])


def open_faq_page():
    selected_option = op.get()

    if selected_option == "Facebook Ads":
        wb.open("https://en-gb.facebook.com/business/help")
    elif selected_option == "Udemy Ads":
        wb.open("https://support.udemy.com/hc/en-us/articles/229232187-Learning-With-Udemy-FAQ")
    elif selected_option == "Caursera Ads":
        wb.open("https://www.coursera.support/s/article/learner-000001807-Coursera-for-Students-FAQs?language=en_US")
    elif selected_option == "Uncademy Ads":
        wb.open("https://unacademy.com/lesson/frequently-asked-questions-faqs/5NQ9GK98")


label = tk.Label(q, text="Select where you came to know about the course:")
label.grid()


op = tk.StringVar(q)
op.set("Facebook Ads")

drop = tk.OptionMenu(q,op,"Facebook Ads","Udemy Ads","Caursera Ads","Uncademy Ads")

drop.grid()

button = tk.Button(q, text="Submit", command=open_faq_page)
button.grid()

q.mainloop()
