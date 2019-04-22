// static/js/resend.js

// 按下登入按鈕
$("#form-resend").on("click", "button#btn-resend", resendPreValidator);
function resendPreValidator(event) {

    let email = $("input#input-email");

    // email
    let email_validated = emailValidator(email.val());


    if (!email_validated) {
        $("div#login-alert").html("Email 格式有誤<button class='close close-danger-alert'>&times;</button>");
        $("div#login-alert").addClass("show");
    }
    else {
        get_ajax_validate_email(email.val())
    }
    
}


// 驗證帳號格式
function emailValidator(email) {
    let email_validated = false;
    let emailRule = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z]{3,66}$/;

    if (email.search(emailRule) != -1){
        email_validated = true;
    }

    return email_validated
}


// 最後註冊時的帳號、email重複檢查並post至註冊route
function get_ajax_validate_email(email) {
    $.ajax({type: "POST",
    async: true,   
    dataType: "json",
    url: "/ajax/validate/email/" + email,
    contentType: 'application/json; charset=UTF-8',
    success: function(msg) {
        email_pass = msg
        if (!email_pass) {
            $("div#login-alert").html("很抱歉，你輸入的電子郵件尚未註冊<button class='close close-danger-alert'>&times;</button>");
            $("div#login-alert").addClass("show");
        }
        else if (email_pass) {
            $("#form-resend").submit();
        }
    }
    })
}

// 關閉alert警告
$(".home-title").on("click", "button.close-danger-alert", closeAlert);
function closeAlert(event) {
    $(this).parent("div").removeClass("show")
}
