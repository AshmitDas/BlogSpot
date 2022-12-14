const containerBody = document.getElementById('container-body');

let last_id = 0;

const get_post_id = async () => {
    return axios.get('http://localhost:5000/feed/getID')
}

const get_post = async () => {
    return axios.get('http://localhost:5000/feed/get_next_post', { params: { ID: last_id } })
}

async function makePost() {
    await get_post_id()
        .then((res) => {
            last_id = res.data.id + 1;
        })

    let counter = 1
    while (counter <= 5) {
        try {
            await get_post()
                .then((res) => {
                    let post_obj = res.data;
                    console.log(post_obj);
                    last_id = post_obj.fetchID;
                    createPostCards(post_obj.title, post_obj.body, post_obj.userID, post_obj.media_src, post_obj.media_type);
                })
            counter += 1
        } catch (err) {
            activeScrollHitsBottomRequest = false;
            console.log(err)
            break
        }
    }
}

$(document).ready(() => {
    makePost();
})


window.onscroll = function (ev) {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        let counter = 1
        while (counter <= 5) {
            try {
                get_post()
                    .then((res) => {
                        let post_obj = res.data;
                        console.log(post_obj)
                        last_id = post_obj.fetchID;
                        createPostCards(post_obj.title, post_obj.body, post_obj.userID, post_obj.media_src, post_obj.media_type);
                    })
                counter += 1
            } catch (err) {
                console.log(err)
                activeScrollHitsBottomRequest = false;
                break
            }
        }
    }
}




function createPostCards(title, body, userID, media_src, media_type) {

    // creates top level row div
    const rowDiv = document.createElement('div');
    rowDiv.classList.add('row', 'justify-content-center');

    // creates the card div
    const cardDiv = document.createElement('div');
    cardDiv.classList.add('card', 'col-md-4', 'my-2', 'px-0');

    // creates the card header
    const cardHeaderDiv = document.createElement('div');
    cardHeaderDiv.classList.add('card-header');

    // creates the card title
    const cardHeaderTitle = document.createElement('h4');
    cardHeaderTitle.innerText = title;

    // creates the userInfo header
    const cardHeaderUserinfo = document.createElement('h6');
    cardHeaderUserinfo.classList.add('card-subtitle', 'mb-1', 'text-muted');
    cardHeaderUserinfo.id = 'italics';
    cardHeaderUserinfo.innerText = `posted by ${userID}`;

    // creates the div of the card body
    const cardBodyDiv = document.createElement('div');
    cardBodyDiv.classList.add('card-body', 'row');

    // creates the paragraph for the card body
    const cardBodyParagraph = document.createElement('p');

    // creates the image tag for the card body
    const cardBodyImg = document.createElement('img');

    // creates the video tag for the card body
    const cardBodyVid = document.createElement('video');
    const videoSource = document.createElement('source');

    // creates the card footer div
    const cardFooterDiv = document.createElement('div');
    cardFooterDiv.classList.add('card-footer', 'text-center', 'text-muted');
    cardFooterDiv.innerText = "Comments and Likes";

    if (media_src === null) {
        cardBodyParagraph.innerText = body;
        appendChildToParent(rowDiv, cardDiv, cardHeaderDiv, cardHeaderTitle, cardHeaderUserinfo, cardBodyDiv, cardFooterDiv);
        cardBodyDiv.append(cardBodyParagraph);
    }
    else {
        cardBodyDiv.classList.add('p-0');

        if (media_type === 'Image') {
            cardBodyImg.classList.add('card-img-top');
            cardBodyImg.id = 'contain_img';
            cardBodyImg.src = media_src;
            appendChildToParent(rowDiv, cardDiv, cardHeaderDiv, cardHeaderTitle, cardHeaderUserinfo, cardBodyDiv, cardFooterDiv)
            cardBodyDiv.append(cardBodyImg)

        } else {
            cardBodyVid.id = 'contain_video';
            appendChildToParent(rowDiv, cardDiv, cardHeaderDiv, cardHeaderTitle, cardHeaderUserinfo, cardBodyDiv, cardFooterDiv)
            cardBodyDiv.append(cardBodyVid);
            cardBodyVid.controls = 'controls';
            cardBodyVid.append(videoSource);
            videoSource.src = media_src;
        }
    }
}


function appendChildToParent(rowDiv, cardDiv, cardHeaderDiv, cardHeaderTitle, cardHeaderUserinfo, cardBodyDiv, cardFooterDiv) {
    containerBody.append(rowDiv);

    rowDiv.append(cardDiv);

    cardDiv.append(cardHeaderDiv);

    cardDiv.append(cardBodyDiv);

    cardDiv.append(cardFooterDiv);

    cardHeaderDiv.append(cardHeaderTitle, cardHeaderUserinfo);
}