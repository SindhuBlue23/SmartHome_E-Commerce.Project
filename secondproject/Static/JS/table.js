function edit_row(no)
{
 document.getElementById("edit_button"+no).style.display="none";
 document.getElementById("save_button"+no).style.display="block";
	
 var name=document.getElementById("pname_row"+no);
 var uistock=document.getElementById("uistock_row"+no);
 var price=document.getElementById("price_row"+no);
 var description=document.getElementById("description_row"+no);

 var pname_data=pname.innerHTML;
 var uistock_data=uistock.innerHTML;
 var price_data=price.innerHTML;
 var description_data=description.innerHTML;

 pname.innerHTML="<input type='text' id='pname_text"+no+"' value='"+pname_data+"'>";
 uistock.innerHTML="<input type='text' id='uistock_text"+no+"' value='"+uistock_data+"'>";
 price.innerHTML="<input type='text' id='price_text"+no+"' value='"+price_data+"'>";
 description.innerHTML="<input type='text' id='description_text"+no+"' value='"+description_data+"'>";
}

function save_row(no)
{
 var pname_val=document.getElementById("pname_text"+no).value;
 var uistock_val=document.getElementById("uistock_text"+no).value;
 var price_val=document.getElementById("price_text"+no).value;
 var description_val=document.getElementById("description_text"+no).value;

 document.getElementById("pname_row"+no).innerHTML=name_val;
 document.getElementById("uistock_row"+no).innerHTML=uistock_val;
 document.getElementById("price_row"+no).innerHTML=price_val;
 document.getElementById("description_row"+no).innerHTML=description_val;

 document.getElementById("edit_button"+no).style.display="block";
 document.getElementById("save_button"+no).style.display="none";
}

function delete_row(no)
{
 document.getElementById("row"+no+"").outerHTML="";
}

function add_row()
{
 var new_pname=document.getElementById("new_pname").value;
 var new_uistock=document.getElementById("new_uistock").value;
 var new_price=document.getElementById("new_price").value;
 var new_description=document.getElementById("new_description").value;

 var table=document.getElementById("data_table");
 var table_len=(table.rows.length)-1;
 var row = table.insertRow(table_len).outerHTML="<tr id='row"+table_len+"'><td id='pname_row"+table_len+"'>"+new_pname+"</td><td id='uistock_row"+table_len+"'>"+new_uistock+"</td><td id='price_row"+table_len+"'>"+new_price+"</td><td id='description_row"+table_len+"'>"+new_description+"</td><td><input type='button' id='edit_button"+table_len+"' value='Edit' class='edit' onclick='edit_row("+table_len+")'> <input type='button' id='save_button"+table_len+"' value='Save' class='save' onclick='save_row("+table_len+")'> <input type='button' value='Delete' class='delete' onclick='delete_row("+table_len+")'></td></tr>";

 document.getElementById("new_pname").value="";
 document.getElementById("new_uistock").value="";
 document.getElementById("new_price").value="";
 document.getElementById("new_description").value="";
}