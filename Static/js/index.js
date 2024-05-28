 $( document ).ready(function() {

        $("#regbutton").click(function(){
            $("#initform").hide()
            $("#registerform").slideDown();
            $("#registerform").show()
        })
        $("#logbutton").click(function(){
            $("#initform").hide()
            $("#loginform").slideDown();
            $("#loginform").show()
        })
        $("#reglink").click(function(){
            $("#loginform").hide()
            $("#registerform").slideDown();
            $("#registerform").show()
        })
        $("#loglink").click(function(){
            $("#registerform").hide()
            $("#loginform").slideDown();
            $("#loginform").show()
        })

        $("#registerbtn").click(function(){
            var uname    = $("#runame").val()
            var email    = $("#remail").val()
            var phone    = $("#rphone").val()
            var password = $("#rpassword").val()

            if (uname == '' || email == '' || phone == '' || password == ''){
                $(".error").html("* Please fill all the fields")
                $(".error").show()
            }else{
                $.ajax({
                    url:"/registeruser", 
                    type: "post", 
                    dataType: 'json',
                    data: {"uname":uname, "email":email, "phone":phone, "password":password},
                    beforeSend: function(){
                        $(".loader").show();
                    },
                    success: function(output){
                        $(".success").html("Registeration Completed. Please login.")
                        $(".success").show()
                    }
                });
            }
        });


         $("#logbtn").click(function(){
            var phone    = $("#sphone").val()
            var password = $("#spassword").val()

            if (phone == '' || password == ''){
                $(".error").html("* Please fill all the fields")
                $(".error").show()
            }else{
                $.ajax({
                    url:"/login", 
                    type: "post", 
                    dataType: 'json',
                    data: {"phone":phone, "password":password},
                    beforeSend: function(){
                        $(".loader").show();
                    },
                    success: function(output){
                        if (output == 0){
                            $(".error").html("Invalid username and password")
                            $(".error").show()
                        }else{
                            
                            location.href = 'http://localhost:5000/tweetpage';

                        }
                    }
                });
            }
        });


        $("#newsupdate").click(function(){
            $.ajax({
                    url:"/updatenews", 
                    type: "post", 
                    dataType: 'json',
                    data: {},
                    beforeSend: function(){
                        $("#newsupdate").attr('disabled', true)
                        $("#statustext").html("Process InProgress.......")
                        $("#statustext").show()
                    },
                    success: function(output){
                        $("#newsupdate").removeAttr('disabled')
                        $("#statustext").hide()
                    }
                });
        });

        

        $("#searchbtn").click(function(){
            filter();
        })

        $("#type").change(function(){
            filter();
        })
        $("#category").change(function(){
            filter();
        })
        $("#fromdate").change(function(){
            filter();
        })
        $("#todate").change(function(){
            filter();
        })

        function filter(){
            var type = $("#type").val()
            var category = $("#category").val()
            var fromdate = $("#fromdate").val()
            var todate = $("#todate").val()
            var searchdata = $("#search").val()
            $.ajax({
                url:"/filternews", 
                type: "post", 
                dataType: 'json',
                data: {"type":type, "category":category, "fromdate":fromdate, "todate":todate, "search":searchdata},
                beforeSend: function(){
                
                },
                success: function(output){
                    if (output.length > 0){
                        createtable(output)
                         $("#nonews").hide()
                         $("#newssection").show()
                    }else{
                        $("#nonews").show()
                        $("#newssection").hide()
                    }
                   
                }
            });
        }

        function createtable(data){
            var appenddata = ''
            $("#totalnews").html(data.length)
            for(var i=0; i<=data.length-1; i++){
                 var author = data[i]["author"]
                  if (author == null || author == undefined || author == 'null'){
                    author = 'Unknown'
                  }
                appenddata += `<li class="list-group-item" onclick='navpage(`+data[i]["news_id"]+`)'>
                <p class="list-group-item-heading" style='font-size:18px;overflow-wrap: break-word;'>`+data[i]["title"]+`</p>
                <p class="list-group-item-text" style='font-size:13px; color:gray'>`+author+" | "+data[i]["publishedAt"]+" | "+data[i]["type"]+" | "+data[i]["category"]+`</p>
              </li>`
            }
            $("#newsfeed").html(appenddata)
        }



});

