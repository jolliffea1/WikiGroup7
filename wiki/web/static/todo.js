var todoListItems = document.getElementsByClassName("todo-li");
for (var i = 0; i < todoListItems.length; i++) {
  var span = document.createElement("span");
  var txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  todoListItems[i].appendChild(span);
}

var close = document.getElementsByClassName("close");
for (var i = 0; i < close.length; i++) {
  close[i].onclick = function() {
    var div = this.parentElement;
    div.style.display = "none";
  }
}

function newTodoItem() {
  var item = document.createElement("li");
  item.className = "todo-li";
  var inputValue = document.getElementById("todo-input").value;
  var textNode = document.createTextNode(inputValue);
  item.appendChild(textNode);
  if (inputValue !== '') {
    document.getElementById("todo-ul").appendChild(item);
  }
  document.getElementById("todo-input").value = "";

  var closeSpan = document.createElement("span");
  var x = document.createTextNode("\u00D7");
  closeSpan.className = "close";
  closeSpan.appendChild(x);
  item.appendChild(closeSpan);

  for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      var div = this.parentElement;
      div.style.display = "none";
    }
  }
}