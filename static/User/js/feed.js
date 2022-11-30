const containerBody = document.getElementById('container-body');

let blogID = 0

const firstFivePosts = axios.get('http://localhost:5000/feed/getpost')
.then((res) => {
    // let blogs = res.data;

    console.log(res)

    // counter = 1

    // while (counter <= 5){
    //     const blog = blogs[`blog ${counter}`];
        
    //     createPostCards(blog.title, blog.body, blog.userID, blog.media_src, blog.media_type);

    //     blogID = blog.fetchID

    //     counter += 1;
    // }
})
.catch((err) => {
    console.log(err)
})



// async function getPost() {
//     count = 1
//     while (count <= 5){
//         try {
//             const response = await axios.get('http://localhost:5000/feed/get_next_post', { params : {ID : blogID}});
//             let next_post = response.data;
        
//             blogID = next_post.fetchID;
        
//             createPostCards(next_post.title, next_post.body, next_post.userID, next_post.media_src, next_post.media_type);
            
//             count += 1

//           } catch (error) {
//             console.error("error");
//             blogID = 0
//             console.log(blogID)
//             break
//           }
//     }
//   }


// if (blogID !== 0){
//     $(window).scroll(function() {
//         if($(window).scrollTop() + $(window).height() == $(document).height()) {
//             getPost();
//         }
//     });
// }



// function createPostCards(title, body, userID, media_src, media_type){

//     // creates top level row div
//     const rowDiv = document.createElement('div');
//     rowDiv.classList.add('row', 'justify-content-center');

//     // creates the card div
//     const cardDiv = document.createElement('div');
//     cardDiv.classList.add('card', 'col-md-4', 'my-2', 'px-0');

//     // creates the card header
//     const cardHeaderDiv = document.createElement('div');
//     cardHeaderDiv.classList.add('card-header');

//     // creates the card title
//     const cardHeaderTitle = document.createElement('h4');
//     cardHeaderTitle.innerText = title;
    
//     // creates the userInfo header
//     const cardHeaderUserinfo = document.createElement('h6');
//     cardHeaderUserinfo.classList.add('card-subtitle', 'mb-1', 'text-muted');
//     cardHeaderUserinfo.id = 'italics';
//     cardHeaderUserinfo.innerText = `posted by ${userID}`;

//     // creates the div of the card body
//     const cardBodyDiv = document.createElement('div');
//     cardBodyDiv.classList.add('card-body', 'row');

//     // creates the paragraph for the card body
//     const cardBodyParagraph = document.createElement('p');

//     // creates the image tag for the card body
//     const cardBodyImg = document.createElement('img');

//     // creates the video tag for the card body
//     const cardBodyVid = document.createElement('vid');

//     // creates the card footer div
//     const cardFooterDiv = document.createElement('div');
//     cardFooterDiv.classList.add('card-footer', 'text-center', 'text-muted');
//     cardFooterDiv.innerText = "Comments and Likes";

//     if(media_src === null){
//         cardBodyParagraph.innerText = body;
//     }
//     else {
//         cardBodyDiv.classList.add('p-0');

//         if (media_type === 'Image'){
//             cardBodyImg.classList.add('card-img-top');
//             cardBodyImg.src = media_src;
//             cardBodyDiv.append(cardBodyImg)
//         }else {
//             cardBodyDiv.append(cardBodyVid)
//         }
//     }

//     containerBody.append(rowDiv);

//     rowDiv.append(cardDiv);

//     cardDiv.append(cardHeaderDiv);

//     cardDiv.append(cardBodyDiv);

//     cardDiv.append(cardFooterDiv);

//     cardHeaderDiv.append(cardHeaderTitle, cardHeaderUserinfo);

//     cardBodyDiv.append(cardBodyParagraph);

// }