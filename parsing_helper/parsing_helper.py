from bs4 import BeautifulSoup
import requests
from fpdf import FPDF
import pypdf
from pathlib import Path

def get_links(url:str, vis:set)->list:
    """input url and already visited url set, return list of unvisited url

    Args:
        url (str): input url
        vis (set): visited set

    Returns:
        res (list): url string list
    """
    response = requests.get(url)

    html_texts = response.content
    soup = BeautifulSoup(html_texts,'html.parser')
    
    res  = []



    # Find all the links in the page
    links = soup.find_all('a')
    for link in links:
        link = link.get('href')
        if link not in vis:
            res.append(link)
            vis.add(link)
    return res

def convert_url_to_pdf(url:str, output_file:str, tag:str="p", language:str='ch'):
    """input url and output_file path name(.pdf), create a
    pdf file with the web page content

    Args:
        url (str): input url
        output_file (str): file path name
        tag (str): the tag in the html that you want to parse
        language (str): text language, default is chinese, else en
    Returns:
        (bool): True if success create pdf file
    """
    try:
        response = requests.get(url)
        html_texts = response.content
        soup = BeautifulSoup(html_texts,'html.parser')
        elements = soup.findAll(tag)
        #elements = soup.select(".YS-WeaponBrief")
        _convert_string_to_pdf(elements, output_file, language)
    except Exception as e:
        print("creating "+ output_file, "has error:\n"+str(e))
        return False
    return True




def _convert_string_to_pdf(elements, output_file:str, language:str = 'ch'):
    """ convert Resultset into pdf file

    Args:
        elements (ResultSet): resultset from bs4
        output_file (str): file path name
        language (str): text language, default is chinese, else en
    """
    #text_file = open(output_file, "w+",encoding='utf-8')
    #n = text_file.write(text)
    #text_file.close()

    pdf = FPDF()
    pdf.add_page()
    if language == 'ch':
        pdf.add_font('SIMYOU','','SIMYOU.ttf',True)
        pdf.set_font("SIMYOU",size=10)
    else:
        pdf.set_font("Arial", size=10)
    
    effective_page_width = pdf.w - 2*pdf.l_margin

    for element in elements:
        if element:
            element=element.text.strip()
            pdf.multi_cell(effective_page_width, 0.15, element)
            #pdf.cell(0,5, txt=element,ln=2,align='C')
    pdf.output(output_file)


def remove_pdfs_redun(source_dir:str="bwiki/",res_dir:str="bwiki/", skip_head_line:int=1, skip_tail_line:int=1):

    dir = Path(source_dir)
    pdf_files = dir.glob("*.pdf")
    loaders = [file.name for file in pdf_files]
    fail_count = 0
    for file in loaders:
        print(file)
        try:
            remove_lines_from_pdf(source_dir+file, res_dir+file, skip_head_line, skip_tail_line)
        except:
            print(file,"remove lines failed.\n")
            fail_count +=1
    print("failed number: ", fail_count)
    return fail_count


def remove_lines_from_pdf(input_file:str, output_file:str, skip_head_line:int=1, skip_tail_line:int=1):
    """if the begining and end of the pdf file have redundent words, removes

    Args:
        input_file (str): input file path name
        output_file (str): output file path name
        skip_head_line (int, optional): number of lines in the begining need to be removed. Defaults to 1.
        skip_tail_line (int, optional): number of lines in the end need to be removed. Defaults to 1.
    """
    
    pdf = FPDF()
    pdf.add_font('SIMYOU','','SIMYOU.ttf',True)
    # Open the input PDF file and iterate through its pages
    pdf_reader = pypdf.PdfReader(input_file)
    num_pages = len(pdf_reader.pages)

    flag = True
    #if pdf_reader.pages[0].extract_text().split('\n')[0]=="":
    #    flag = False

    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        
        if page_num == 0  and num_pages == 1 and flag:
            lines = text.split('\n')[skip_head_line:skip_tail_line] 
            
        elif page_num == 0 and flag:
            
            lines = text.split('\n')[skip_head_line:]
        elif num_pages-1 == page_num and flag:
            lines = text.split('\n')[:skip_tail_line] 
        else :
            lines = text.split('\n')
        
        if len(lines) <= 0:   ## prevent empty page
            continue
       #lines[0] = title + lines[0]
        modified_text = '\n'.join(lines)
        

        # Add the modified text to the new PDF page
        pdf.add_page()
        pdf.set_font("SIMYOU",size=10)
        pdf.multi_cell(0, 10, modified_text)

    # Save the modified PDF to the output file
    pdf.output(output_file)