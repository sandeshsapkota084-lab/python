import PyPDF2
import openai
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import pandas as pd
def gpt_response(prompt, max_tokens=300, temp=0.3):
    try:
        response = openai.Completion.create
        (
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temp
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"
pdf_summaries = {}
def extract_pdf_pages(file_path):
    pages_text = {}
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    pages_text[i+1] = text
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF:\n{e}")
    return pages_text
def summarize_pages(pages_text, chunk_size=2000):
    summaries = {}
    for page, text in pages_text.items():
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        page_summary = ""
        for chunk in chunks:
            prompt = f"Summarize the following text concisely:\n\n{chunk}\n\nSummary:"
            page_summary += gpt_response(prompt, max_tokens=150) + " "
        summaries[page] = page_summary.strip()
    return summaries
def ask_question():
    question = question_entry.get()
    if not question.strip():
        messagebox.showwarning("Warning", "Please enter a question.")
        return
    if not pdf_summaries:
        messagebox.showwarning("Warning", "Please upload a PDF first.")
        return
    combined_summary = "\n".join([f"Page {p}: {s}" for p, s in pdf_summaries.items()])
    prompt = f"Use the summarized content to answer the question. Include page numbers if relevant.\n\nSummaries:\n{combined_summary}\n\nQuestion: {question}\nAnswer:"
    answer = gpt_response(prompt)
    answer_box.config(state='normal')
    answer_box.insert(tk.END, f"Q: {question}\nA: {answer}\n\n")
    answer_box.config(state='disabled')
    history_df.loc[len(history_df)] = [question, answer]
    history_df.to_csv("pdf_qa_history.csv", index=False)
def upload_pdf():
    global pdf_summaries, history_df
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pages_text = extract_pdf_pages(file_path)
        if pages_text:
            answer_box.config(state='normal')
            answer_box.delete(1.0, tk.END)
            answer_box.insert(tk.END, "Summarizing PDF pages. Please wait...\n")
            answer_box.update()
            pdf_summaries = summarize_pages(pages_text)
            answer_box.insert(tk.END, f"PDF summarized successfully! {len(pdf_summaries)} pages processed.\nYou can now ask questions.\n\n")
            answer_box.config(state='disabled')
            history_df = pd.DataFrame(columns=["Question", "Answer"])
pdf_summaries = {}
history_df = pd.DataFrame(columns=["Question", "Answer"])
root = tk.Tk()
root.title("Ultimate PDF Q&A Assistant")
root.geometry("900x600")
upload_btn = tk.Button(root, text="Upload PDF & Summarize", command=upload_pdf, bg="#4CAF50", fg="white", padx=10, pady=5)
upload_btn.pack(pady=10)
question_entry = tk.Entry(root, width=100)
question_entry.pack(pady=5)
question_entry.insert(0, "Type your question here...")
ask_btn = tk.Button(root, text="Ask Question", command=ask_question, bg="#2196F3", fg="white", padx=10, pady=5)
ask_btn.pack(pady=5)
answer_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=30, state='disabled')
answer_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
root.mainloop()