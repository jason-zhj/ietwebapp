$(document).ready(
    function(){
        // change text in the form in the 'event' page
        $("label[for='id_isNewIdea']").text("This is a new idea");

        // add styling to the form in the 'join' page
        $("input[type!='checkbox']").addClass("form-control");
        $("select").addClass("form-control");

        // form list items in the membership benefit section in 'join' page
        $items=$(".list-group").find('li');
        $items.addClass('list-group-item');
        $items.prepend("<span class='glyphicon glyphicon-forward glyphicon-align-left' aria-hidden='true'>&nbsp;</span>")

        //remove event selection box from eventDetail participation form
        //$('#participate').find('#id_event').parent().css("display","None").css("display","none");

        // onclick action for images on siderbars
        $('.media').find('a:has(img)').click(function(e){
            e.preventDefault();
            // get the img src
            $imgSrc=$(this).find('img').attr('src');
            // show a modal
            $modal=$('#imageModal_div');
            $modal.find('img').attr('src',$imgSrc);
            $modal.find('button').click(function(){
                $modal.modal('hide');
            });
            $modal.modal('show');

        });



    }

);


// this will be executed when all assets like images/js have been loaded
//
jQuery(window).load(
  function(){
              // properly resize the images with max-width attr
        $imgs=$("img[max-width]");
        for (i=0;i<$imgs.length;i++){
            currentImage=$imgs[i];
            originalHeight=currentImage.naturalHeight;
            originalWidth=currentImage.naturalWidth;
            targetWidth=Number(currentImage.getAttribute('max-width'));
            if (originalWidth>targetWidth){
                targetHeight=targetWidth*originalHeight/originalWidth;
                currentImage.style.height=targetHeight + "px";
                currentImage.style.width=targetWidth + "px";
            }
        }

      // add auto-hide to relatively big images for small devices
      $(".media-left").find("img").addClass("hidden-xs");
  }
);