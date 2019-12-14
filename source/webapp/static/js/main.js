const baseUrl = 'http://localhost:8000/api/v1/';

let addBtn, editBtn, delBtn;


function setUpGlobalVars() {
    addBtn = $('#comment-add');
    editBtn = $('#editBtn');
    delBtn = $('#delBtn');
}

function commentDel(id){
    let cur_token = getCookie('csrftoken');
    $.ajax({
      type: "DELETE",
      url: baseUrl + 'comment/'+ id,
      data: null,
      headers: {
         'X-CSRFToken': cur_token
      },
      success: function () {
          let cur_el = '.body' + id;
        $(cur_el).remove();
      }
    });
}
function commentAdd(){
    console.log(addBtn.attr('data-image_id'));
    let cur_token = getCookie('csrftoken');
    $.ajax({
      type: "POST",
      url: baseUrl + 'comment/',
      data: JSON.stringify(
          {
              image : addBtn.attr('data-image_id'),
              author : addBtn.attr('data-author_id'),
              text: $('#user_text').val()
          }
      ),
      dataType: 'json',
      contentType: 'application/json',
      headers: {
         'X-CSRFToken': cur_token
      },
      success: function (response) {
          let new_el = `<div class="body${response.comment_id}">
                            <p>Автор : ${addBtn.attr('data-author_id')}</p>
                            <p>Текст : ${$('#user_text').val()}</p>  
                            <p>Дата : ${response.created}</p>  
                            <p>
                              <a  class="btn btn-success text-white" id="editBtn">Редактирование</a>
                              <a onclick="commentDel(${response.comment_id})" class="btn btn-danger text-white" id="delBtn">Удаление</a>
                          </p>             
                        </div>`;
        $('.cardcomment').append(new_el);
      }
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function() {
    setUpGlobalVars();
});
