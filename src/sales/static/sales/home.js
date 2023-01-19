console.log('hello world')
const reportBtn=document.getElementById('report-btn')
const img=document.getElementById('img')
const modalBody=document.getElementById('modal-body')
const reportForm=document.getElementsById('report-form')
const reportName=document.getElementsById('id_name')
const reportRemarks=document.getElementsById('id_remarks')
const csrf=coudment.getElementByName('csrfmiddlewaretoken')[0].value
console.log(csrf)
if(img){
    reportBtn.classList.remove('invisible')
}


reportBtn.addEventListener('click',()=>{
    console.log('click')
    img.setAttribute('class','w-100') //set img same width as modalbody
    modalBody.prepend(img)
    reportForm.addEventListener('submit',e=>{

        e.preventDefault()
        const formData=new FormData()
        formData.append('csrfmiddlewaretoken',csrf)
        formData.append('name',reportName.value)
        formData.append('remark',reportRemarks.value)
        formData.append('image',img.src)
        $.ajax({
            type:'POST',
            url:'/reports/save/',
            data:formData,
            success:function(response){
                console.log(response)

            },
            error:function(error){
                console.log(error)

            },
            processData:false,
            contenttype:false,
        })
    })
})