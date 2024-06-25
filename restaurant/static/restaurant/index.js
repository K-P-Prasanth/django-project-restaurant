
document.addEventListener('DOMContentLoaded', function() {
    
    allorder()
    recommendation()
    allitems()
    menu()
})


function allorder(){
    fetch('/orders')
    .then(response => response.json())
    .then(orders => {
        orders.forEach(order => {
            if (!order.quantity.every(item => item === 0) && order.quantity.length != 0 ) {
                let ordercontent = document.createElement('div');
                ordercontent.className = 'd-flex justify-content-between border text-light pt-2 pl-2 pr-3 pb-1';
                ordercontent.innerHTML = `
                <h5>Order ID: ${order.id} </h5>
                <p> | Customer Name: ${order.user}</p>
                <p> | Total : ${order.total}</p>
                `
                let buttons = document.createElement('div');
                buttons.className="d-flex";
                let viewbutton = document.createElement('button');
                viewbutton.type = "button";
                viewbutton.className = 'btn btn-outline-warning';
                viewbutton.innerHTML = "View";
                viewbutton.onclick = function(){
                    vieworder(order.id)
                }

                let clearform = document.createElement('form');
                clearform.action = `orders/${order.id}`;
                clearform.method = "post";

                let order_id = document.createElement('input');
                order_id.type = "hidden";
                order_id.name = "order_id";
                order_id.value = order.id;
                clearform.appendChild(order_id);

                let clearbutton = document.createElement('button');
                clearbutton.type = "submit";
                clearbutton.className = 'btn btn-outline-danger ml-2';
                clearbutton.innerHTML = "Clear";
                clearform.appendChild(clearbutton);

                buttons.appendChild(viewbutton);
                
                buttons.appendChild(clearform);
                ordercontent.appendChild(buttons);
                document.querySelector("#orders-display").appendChild(ordercontent);
            }
            
        })
    })
}


function vieworder(order_id){
    document.querySelector("#orders-display").style.display = "none";
    document.querySelector("#order-display").style.display = "block";
    let parent = document.querySelector("#order-display")
    fetch(`orders/${order_id}`)
    .then(response => response.json())
    .then(orderset =>{
        orderset.forEach(order =>{
            items = order.items;
            quantity = order.quantity;
            let len = items.length;
            parent.innerHTML = `
                        <h3>Order ID: ${order.id}</h3>
                        <p>Customer Name: ${order.user}</p>
                        <p>Total: ${order.total}</p>
                        <h5>Items</h5>`
            let ul = document.createElement('ul');
            for(let i=0;i<len;i++){
                if(quantity[i]>0){
                    let li = document.createElement('li');
                    li.innerHTML = `Item Name : ${items[i]} | Quantity : ${quantity[i]}`;
                    ul.appendChild(li);
                }
            }
            parent.appendChild(ul);
        })
    })
}

function menu(){
    let select = document.querySelector("#select-category")
    select.onchange = () =>{
        let parent = document.querySelector("#menudiv")
        parent.innerHTML = ""
        fetch(`/allitems/${select.value}`)
            .then(response => response.json())
            .then(items => {
                items.forEach(item => {

                    displayItem(item, parent)

                });
            })
    }   
}

function recommendation(){
    let parent = document.querySelector("#recommendations");
    user_id = document.querySelector("#user").innerHTML;
    fetch(`/orders/${user_id}`)
    .then(response => response.json())
    .then(orders => {
        orders.forEach(order => {
            items = order.item_ids;
            rec = document.querySelector("#rec")
            if(items.length === 0){
                rec.innerHTML= ""
                rec.style.display="none"
            }else{
                rec.style.display="block"
                rec.innerHTML = "You Previously Ordered...."
            }
            items.forEach(item_id => {
                fetch(`/allitems/${item_id}`)
                    .then(response=>response.json())
                    .then(itemlst => {
                        itemlst.forEach(item => {
                            displayItem(item,parent)
                        })
                    })
                
            })           
        });
    })
}

function allitems(){
    let parent = document.querySelector("#items-holder")
    fetch(`/allitems`)
    .then(response => response.json())
    .then(items => {
        items.forEach(item => {
            displayItem(item,parent)
        });
    })
}

function displayItem(item,parent){
    let div1 = document.createElement('div');
            div1.className = "col d-flex p-2 border border-dark rounded opacity-25 text-light";
            let veg ;
            if(item.vegBool){
                veg = "success";
            }else{
                veg = "danger";
            }
            div1.innerHTML = `
            <div class="w-50">
                <img src="${item.imageURL}" alt="${item.name}" class="w-100" style="height: 250px;border-radius:10%">
            </div>`

            let div2 = document.createElement('div');
            div2.className = "w-50 d-flex flex-column ";
            div2.innerHTML = `
                    <div class="mb-1">
                        <p class="lead"><b class="d-inline">Name :</b>${item.name}</p>
                    </div>
                    <div class="mb-3">
                        <div class="border rounded border-${veg} text-${veg} d-inline p-2">
                            <div class="rounded-circle border-${veg}  h-25 bg-${veg} d-inline pl-1">O</div>
                        </div>
                        &nbsp; &nbsp; &nbsp;
                        <p class="d-inline">Price : ${ item.prices }</p>
                    </div>
            `
            div1.appendChild(div2);

            let form = document.createElement('form');
            form.method = "POST"
            form.action = `/additem`
            form.className = "forms"

            let div3 = document.createElement("div");
            div3.className = "mb-1 d-flex flex-row";

                

                //increment button
                let btn1 = document.createElement('button');
                btn1.className= "btn d-inline inc w-25 border text-light ml-2 "
                btn1.type = "button"
                btn1.innerHTML = "+";
                btn1.onclick = () =>{
                    increment(input,div5,item,input3)
                }

                let input = document.createElement('input');
                input.type = "text"
                input.value = 0
                input.className="form-control w-50 text-center"
                input.name = "quantity"

                let input2 = document.createElement('input');
                input2.type = "hidden"
                input2.value = item.id
                input2.name = "item_id"

                
                
                //decrement button
                let btn2 = document.createElement('button');
                btn2.className= "btn d-inline inc w-25 border text-light"
                btn2.type = "button"
                btn2.innerHTML = "-";
                btn2.onclick = () =>{
                    decrement(input,div5,item,input3)
                }

                div3.appendChild(btn1);
                div3.appendChild(input);
                div3.appendChild(input2);
                div3.appendChild(btn2);
                form.appendChild(div3);

            

            let div5 = document.createElement('div');
            div5.className=" mb-1"
            div5.style.display = "none";
            form.appendChild(div5)

            let input3 = document.createElement('input');
                input3.type = "hidden"
                input3.value = 0
                input3.name = "amt"
                
                form.appendChild(input3)

            let div4 = document.createElement('div')
                let btn = document.createElement('button')
                btn.className = "btn btn-outline-warning"
                btn.innerHTML = "Add to Cart"
                btn.type="submit"
                div4.appendChild(btn)
            form.appendChild(div4)
            div2.appendChild(form);
            
        
        // let parent = document.querySelector("#items-holder")
        parent.appendChild(div1)
}

function increment(input,div5,item,input3){
    div5.style.display = "block";
    count = parseInt(input.value);
    if (count === 10) {
        alert("Cannot order more than 10 same items")
    } else {
        count++;
        input.value = count;
        input3.value = count * item.prices;
        div5.innerHTML = `Value : Rs.${count * item.prices}`
    }
}

function decrement(input,div5,item,input3){
    count = parseInt(input.value);
    if(count===0){
        alert("Cannot order -ve number of items")

    }else{
        count--; 
        input.value = count;
        input3.value = count * item.prices;
        div5.innerHTML = `Value : Rs.${count * item.prices}`
    }
}
