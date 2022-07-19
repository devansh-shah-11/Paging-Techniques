from tkinter import HORIZONTAL
from streamlit_option_menu import option_menu
import streamlit as st
from prettytable import PrettyTable
myTable1 = PrettyTable()
myTable2 = PrettyTable()
myTable3 = PrettyTable()
columns = ["Incoming page"]

st.set_page_config(layout="wide")
with open("style1.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

c1,c2,c3=st.columns(3)
with c2:
    str1=st.text_input("Enter comma-seperated list: ")
main=list(map(int,str1.split(",")))
st.text("You entered the list: "+str(main))
with c2:
    n=st.selectbox("Enter the number of frames:",["1","2","3","4","5","6"])
st.text("No of frames selected = "+str(n))
n=int(n)
def index(k,l):
    idx = []
    for i in k:
        if(i in l):
            idx.append((len(l) - (l[::-1].index(i))-1))
        else:
            idx.append(-1)
    return idx

def index1(k,l):
    if k in l:
        return l.index(k)
    else:
        return -1

my_bar = st.progress(0)

for percent_complete in range(1,n+1):
    my_bar.progress(percent_complete/n)

def FIFO():
    i1=0
    y=pf_f=0
    l_FIFO=["-"]*n
    for k in range(len(main)):
        X = l_FIFO.copy()
        st.text("\n")
        if k<n:
            st.text(str(main[k])+" not there in page frame hence adding it!")
            X[i1] = main[k]
            pf_f+=1
        else:
            if main[k] in X:
                st.text(str(main[k])+" already there in page frame hence ignoring it!")
                myTable1.add_column(str(columns[0]) +" : "+ str(main[k]),l_FIFO)
                continue
            else:
                pf_f+=1
                st.text("Index to be replaced: "+str(y))
                st.text("Incoming page: "+str(main[k]))               
                X[y]=main[k]
                y=(y+1)%n
        i1+=1
        l_FIFO = X.copy()
        myTable1.add_column(str(columns[0]) +" : "+ str(main[k]),l_FIFO)
        st.text("FIFO = "+str(l_FIFO))
        st.write(myTable1)
    st.info("\nNumber of page-faults = "+str(pf_f))

def LRU():
    pf_l=0
    i2=0
    l_LRU=["-"]*n
    for p in range(len(main)):
        Y = l_LRU.copy()
        st.text("\n")
        st.text("List of completed pages: {0}".format(main[:p]))
        st.text("Incoming page: {0}".format(main[p]))
        if p<n:
            Y[i2] = main[p]
            l_LRU.append(main[p])
            st.text(str(main[p])+" not there in page frame hence adding it!")
            pf_l+=1
        else:
            if main[p] in Y:
                st.text(str(main[p])+" already there in page frame hence ignoring it!")
                myTable2.add_column(str(columns[0]) +" : "+ str(main[p]),l_LRU)
                continue
            else:
                idx = index(l_LRU,main[:p])
                t = idx.index(min(idx))
                Y[t] = main[p]
                pf_l+=1
        i2+=1
        l_LRU=Y.copy()
        st.text("LRU = "+str(l_LRU))
        myTable2.add_column(str(columns[0]) +" : "+ str(main[p]),l_LRU)
        st.write(myTable2)
    st.info("\nNumber of page-faults = "+str(pf_l))

def optimal():
    i3=0
    pf_o=0
    l_OPTIMAL=["-"]*n
    print(l_OPTIMAL)
    for i in range(len(main)):
        Z=l_OPTIMAL.copy()
        st.text("\n")
        st.text("Incoming page = "+str(main[i]))
        l2=main[i+1:]
        st.text("Remaining list = "+str(l2))
        if i<n:
            Z[i3]=main[i]
            st.text(str(main[i])+" not there in page frame hence adding it!")
            pf_o+=1
        else:
            if main[i] in Z:
                st.text(str(main[i])+" already there in page frame hence ignoring it!")
                myTable3.add_column(str(columns[0]) +" : "+ str(main[i]),l_OPTIMAL)
                continue
            else:
                pf_o+=1
                l3=[]
                for j in l_OPTIMAL:
                    t=index1(j,l2) 
                    l3.append(t)
                st.text("Remaining list ma current list no index: "+str(l3))
                x=index1(-1,l3)
                if x==-1:
                    t2=max(l3)
                    t1=index1(t2,l3)
                else:
                    t1=x
                st.text("Index to be replaced = "+str(t1))
                Z[t1]=main[i]
        i3+=1
        l_OPTIMAL=Z.copy()
        st.text("Optimal = "+str(l_OPTIMAL))
        myTable3.add_column(str(columns[0]) +" : "+ str(main[i]),l_OPTIMAL)
        st.write(myTable3)
        st.text("\n")
    st.info("Number of page-faults = "+str(pf_o))

choice = option_menu("",["FIFO", "LRU", "OPTIMAL"],orientation=HORIZONTAL)
if choice=="FIFO":
    FIFO()

elif choice=="LRU":
    LRU()
else:
    optimal()