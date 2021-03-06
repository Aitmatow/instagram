const baseUrl = 'http://localhost:8000/api/v1/';

let addBtn, editBtn, delBtn, dislike, like;

function setUpGlobalVars() {
    addBtn = $('#comment-add');
    editBtn = $('#editBtn');
    delBtn = $('#delBtn');
    dislike = $('#dislike');
    like = $('#like');
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

function disLike() {
    let user = dislike.attr('data-author');
    let cur_image = dislike.attr('data-image_id');
    let cur_token = getCookie('csrftoken');
    console.log(user);
    $.ajax({
      type: "POST",
      url: baseUrl + 'likes/'+ cur_image + '/',
      data: JSON.stringify({'oper':'dislike', 'user' : user}),
      dataType: 'json',
      contentType: 'application/json',
      headers: {
         'X-CSRFToken': cur_token
      },
      success: function (response) {
          dislike.replaceWith(like);
          $('#likes').text(response.like);
      }
    });
}

function Like() {

    let user = like.attr('data-author');
    let cur_image = like.attr('data-image_id');
    let cur_token = getCookie('csrftoken');
    $.ajax({
      type: "POST",
      url: baseUrl + 'likes/'+ cur_image + '/',
      data: JSON.stringify({'oper':'like', 'user' : user}),
      dataType: 'json',
      contentType: 'application/json',
      headers: {
         'X-CSRFToken': cur_token
      },
      success: function (response) {
        like.replaceWith(dislike);
        $('#likes').text(response.like);
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

function checkLiked()
{
    if($('#liked'));

}


$(document).ready(function() {
    setUpGlobalVars();
    checkLiked()
});
