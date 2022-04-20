from win32com.client import Dispatch
import os

pdfRoot = "C:\\Users\PrinceCheng\Desktop\wordToPDF\pdf" # 输出pdf路径
wordRoot = "C:\\Users\PrinceCheng\Desktop\wordToPDF\word" # 输入word路径

def doc2pdf(filePath, file):
    print("正在转换:",file)
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(filePath)
    outFile = pdfRoot +"\\"+ file.split('.')[0] + ".pdf" #生成pdf文件路径名称
    doc.SaveAs(outFile, FileFormat=17)
    doc.Close()
    word.Quit()

if __name__ == "__main__":
    filelist = os.listdir(wordRoot)
    for file in filelist:
        if (file.endswith(".doc") or file.endswith(".docx")) and ("~$" not in file):
            filePath = wordRoot+"\\"+file
            doc2pdf(filePath, file)
    print ("所有word文件转PDF文件已完成！！！")