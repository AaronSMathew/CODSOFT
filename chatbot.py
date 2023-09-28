import re
import tkinter as tk

# Define predefined rules and responses
rules = {
    r"(hello|hi|hey)( there)?": "Hello! How can I assist you today?",
    r"how are you": "I'm just a computer program, but I'm here to help. How can I assist you?",
    r"(what is|tell me about) (yourself|you)": "I'm a simple rule-based chatbot. Ask me anything you'd like!",
    r"(good|bad|well|fine)( thanks)?": "I'm glad to hear that! How can I assist you further?",
    r"bye|goodbye": "Goodbye! Feel free to return if you have more questions.",
    r"(help|assistance)": "I'm here to help. Please ask your question, and I'll do my best to assist you.",
}

# Define additional predefined rules and responses
additional_rules = {
    r"(what is|define) (chatbot|chatbots)": "A chatbot is a computer program designed to simulate conversation with human users, especially over the internet.",
    r"(tell me|explain) (about|regarding) AI": "AI stands for Artificial Intelligence, which is the simulation of human intelligence processes by machines, especially computer systems.",
    r"(how do|can) I (use|interact with) this chatbot": "You can interact with me by typing in your questions or statements, and I'll do my best to respond.",
    r"who created you": "I was created by a team of developers using Python and natural language processing techniques.",
    r"(can|may) I ask you (a|any) question": "Of course! Feel free to ask me anything, and I'll try to provide an informative response.",
    r"(what|tell me) a joke": "Why don't scientists trust atoms? Because they make up everything!",
    r"(how old are you|your age)": "I don't have an age since I'm just a computer program.",
    r"(where are you from|your origin)": "I exist in the digital realm and don't have a physical location or origin.",
    r"(favorite color|color do you like)": "I don't have preferences for colors, but I can tell you interesting facts about them.",
    r"(recommend|suggest) a book": "I recommend reading 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams for some humor and adventure.",
    r"(recommend|suggest) a movie": "I suggest watching 'The Shawshank Redemption' for its compelling story and great acting.",
    r"(how (does|do) (something|it) work)": "I can provide explanations and instructions on various topics. Please specify what you want to know.",
    r"(what can you do|your capabilities)": "I can answer questions, provide information, tell jokes, and engage in general conversation.",
    r"(who is your favorite|best) (musician|artist|band)": "I don't have personal preferences, but I can recommend some popular artists or bands if you'd like.",
    r"(what is the|explain the) meaning of life": "The meaning of life is a philosophical question with no single definitive answer. It varies from person to person.",
    r"(weather|forecast) (today|tomorrow)": "I don't have access to real-time weather data, but you can check a weather website or app for forecasts.",
    r"(translate|translation) (hello|goodbye|thank you) (to|in) (French|Spanish|German)": "Sure! Here are translations:\nHello - Bonjour (French), Hola (Spanish), Hallo (German)\nGoodbye - Au revoir (French), Adiós (Spanish), Auf Wiedersehen (German)\nThank you - Merci (French), Gracias (Spanish), Danke (German)",
    r"(tell me|give me) (a|an) (interesting|fun|random) fact": "Here's an interesting fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    r"(recommend|suggest) a (place|restaurant|destination) to visit": "I recommend visiting Kyoto, Japan, for its rich cultural heritage and beautiful temples.",
    r"(how can I|tips to) (improve|boost) (my|personal) (productivity|efficiency)": "To improve productivity, try setting clear goals, eliminating distractions, and prioritizing tasks.",
    r"(tell me|explain) the (Pythagorean theorem|E=mc^2|Newton's laws of motion)": "Certainly! Which one would you like me to explain?",
    r"(what is|explain) the (meaning|concept) of (love|friendship)": "Love and friendship are complex and deeply personal concepts that can vary from person to person. They involve emotional bonds and connections.",
    r"(how can I|tips for) (reduce|manage) stress": "To reduce stress, consider practicing relaxation techniques, exercising regularly, and maintaining a healthy work-life balance.",
    r"(what is|describe) the (Mona Lisa|Eiffel Tower|Great Wall of China)": "The Mona Lisa is a famous painting by Leonardo da Vinci, the Eiffel Tower is an iconic Parisian landmark, and the Great Wall of China is a historic fortification.",
    r"(tell me|explain) the (difference|distinction) between (HTML|CSS|JavaScript)": "HTML is for structuring web content, CSS is for styling it, and JavaScript is for adding interactivity.",
    r"(recommend|suggest) a (programming language|framework)": "I recommend learning Python for its readability and versatility or JavaScript for web development.",
    r"(what is|define) (machine learning|deep learning)": "Machine learning is a subset of AI that involves training computers to learn from data, while deep learning is a type of machine learning using neural networks.",
    r"(tell me|give me) (a|an) (inspirational|motivational) quote": "Here's an inspirational quote: 'The only way to do great work is to love what you do.' – Steve Jobs",
    r"(what is|explain) the (theory|concept) of (evolution|relativity)": "The theory of evolution explains how species change over time, and the theory of relativity is a fundamental concept in physics developed by Albert Einstein.",
    r"(tell me|describe) (a|an) (interesting|fascinating) scientific discovery": "One fascinating discovery is the Higgs boson, a particle that helps explain the origin of mass in the universe.",
    r"(what is|define) (blockchain|cryptocurrency)": "Blockchain is a decentralized ledger technology, and cryptocurrency is digital or virtual currency that uses cryptography for security.",
    r"(how to|steps to) (start|begin) (a|my) (own|first) (business|startup)": "Starting a business involves steps like market research, creating a business plan, securing funding, and marketing your products or services.",
    r"(tell me|explain) the (concept|theory) of (black holes|quantum mechanics)": "Black holes are regions of spacetime with extremely strong gravitational effects, and quantum mechanics is a branch of physics dealing with subatomic particles.",
    r"(recommend|suggest) a (podcast|book) on (technology|science)": "I recommend the podcast 'Reply All' for tech stories and the book 'Sapiens: A Brief History of Humankind' for a science-related read.",
    r"(how can I|tips to) (improve|enhance) (my|personal) (communication|public speaking) skills": "To improve communication skills, practice active listening, work on clarity, and join a public speaking club.",
}

# Merge the new rules with the existing rules
rules.update(additional_rules)


# Function to handle user input and provide responses
def respond():
    user_input = user_input_entry.get().lower()
    response = None
    
    for pattern, reply in rules.items():
        if re.search(pattern, user_input):
            response = reply
            break
    
    if response:
        chat_text.config(state=tk.NORMAL)
        chat_text.insert(tk.END, "You: " + user_input + "\n", "user")
        chat_text.insert(tk.END, "Chatbot: " + response + "\n", "bot")
        chat_text.config(state=tk.DISABLED)
        user_input_entry.delete(0, tk.END)
    else:
        chat_text.config(state=tk.NORMAL)
        chat_text.insert(tk.END, "You: " + user_input + "\n", "user")
        chat_text.insert(tk.END, "Chatbot: I'm not sure how to respond to that. Can you please rephrase your question?\n", "bot")
        chat_text.config(state=tk.DISABLED)
        user_input_entry.delete(0, tk.END)

# Create a GUI window
window = tk.Tk()
window.title("Rule-Based Chatbot")

# Create a text widget to display the chat
chat_text = tk.Text(window, state=tk.DISABLED)
chat_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
chat_text.tag_configure("user", foreground="blue")
chat_text.tag_configure("bot", foreground="green")

# Create an entry widget for user input
user_input_entry = tk.Entry(window)
user_input_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Create a button to send user input
send_button = tk.Button(window, text="Send", command=respond)
send_button.grid(row=2, column=0, padx=10, pady=10)

# Configure grid layout
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# Start the GUI main loop
window.mainloop()
