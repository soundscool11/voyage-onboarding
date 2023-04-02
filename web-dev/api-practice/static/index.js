const REST_API_KEY = "ecccae707771b94f694293f812986c2c";

function search_book() {
	const title = $(".input").val();
	$.ajax({
		method: "GET",
		url: "https://dapi.kakao.com/v3/search/book?target=title",
		data: { query: title },
		headers: { Authorization: `KakaoAK ${REST_API_KEY}` },
	}).done(function (msg) {
		try {
			const title = msg["documents"][0]["title"];
			const author = msg["documents"][0]["authors"][0];
			const publisher = msg["documents"][0]["publisher"];
			const price = msg["documents"][0]["price"];
			const thumbnail = msg["documents"][0]["thumbnail"];
			const url = msg["documents"][0]["url"];
			const status = msg["documents"][0]["status"];
			let contents = [];
			msg["documents"].forEach((e) => {
				contents.push(e["contents"]);
			});
			const book = {
				title: title,
				author: author,
				publisher: publisher,
				price: price,
				thumbnail: thumbnail,
				contents: contents,
				url: url,
				status: status,
			};
			const temp_html = `<div class="tile is-ancestor">
                                    <div class="tile is-4 is-vertical is-parent">
                                        <div class="tile is-child box">
                                            <p class="title">${book["title"]}</p>
                                            <img src="${book["thumbnail"]}">
                                        </div>
                                        <div class="tile is-child box">
                                            <p class="title">Published by ${book["publisher"]}</p>
                                            <p>판매 가격: ${book["price"]}원</p>
                                            <p>현재 상태: ${book["status"]}</p>
                                            <a href="${book["url"]}">책 자세히 구경하기</a>
                                        </div>
                                        </div>
                                        <div class="tile is-parent">
                                        <div class="tile is-child box">
                                            <p class="title">Written by ${book["author"]}</p>
                                            <p>${book["contents"]}</p>
                                        </div>
                                    </div>
                                </div>`;
			$(".book").append(temp_html);
		} catch {
			alert("책을 찾을 수 없습니다.");
		}
	});
}
