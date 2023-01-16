import uuid,base64
from customers.models import Customer
from profiles.models import Profile
from io import BytesIO
import matplotlib.pyplot as plt
def generate_code():
    return str(uuid.uuid4()).replace('-','')[:12]

def get_customer_from_id(val):
    return Customer.objects.get(id=val)

def get_salesman_from_id(val):
    return Profile.objects.get(id=val)
def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph
def get_chart(chart_type,data,**kwargs):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,4))
    if chart_type=='#1':
        plt.bar(data['transaction_id'], data['price'])
        print('bar chart')
    elif chart_type=='#2':
        labels=kwargs.get('labels')
        plt.pie(data=data,x='price',labels=labels)
        print('pie chart')
    elif chart_type=='#3':
        print('line chart')
        plt.plot(data['transaction_id'],data['price'])
    else:
        print('chart type cannot be identified')
    plt.tight_layout()
    chart=get_graph()
    return chart