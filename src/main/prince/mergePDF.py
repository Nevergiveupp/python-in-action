import os

from PyPDF2 import PdfFileMerger

if __name__ == "__main__":
    pdfRoot = "C:\\Users\PrinceCheng\Desktop\wordToPDF\pdf"  # 输出合并后的pdf
    merger = PdfFileMerger()  # 调用PDF文件合并模块
    filelist = os.listdir(pdfRoot)  # 读取文件夹所有文件
    for file in filelist:
        if file.endswith(".pdf"):
            merger.append(pdfRoot + "\\" + file)  # 合并PDF文件
    merger.write("C:\\Users\PrinceCheng\Desktop\wordToPDF\pdf\\result.pdf")  # 写入PDF文件
