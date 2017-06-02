
$(document).ready(function(){
	var buttonList = $('#ctrl-btn');
	var tButtons = $('table');
	var userId;

	var csrf = $('#token').data("csrf");

	$.post('/parties/json', {
					verb: 'identify',
					csrf_token: csrf,
		}).then(function(response){
			userId = response;
	});


	tButtons.on('click','button',function(e){
		csrf = $('#token').data("csrf"); // CSRF Token
		verb = $(e.target).data("verb");
		mid = $(e.target).data("mid");
		url = `/parties/${mid}/ajoin`;

		$.post(url, {
					verb: verb,
					csrf_token: csrf,
					mid: mid
		}).then(function(response){
			if (response.r.status === "success"){
				$(e.target).removeClass('btn-success');
				$(e.target).addClass('btn-danger');
				$(e.target).attr("data-verb", "leave");
				$(e.target).text("Leave");
			}
			// DO WORK!!


		});
	});

	buttonList.on('click','button',function(e){
		csrf = $('#token').data("csrf"); // CSRF Token
		url = `/parties/json`;
		verb = $(e.target).data("verb");
		console.log("verb is",verb);

		// "X-CSRFToken" =  is what would go in the header.
		$.post(url, {
					verb: verb,
					csrf_token: csrf,
					lat: "37.9126212",
					lng: "-122.2864609"
				}).then(function(response){
			$tbody = $('tbody');
			$tbody.empty();

			let plist = response.results; // Party List
			console.log("verb",verb);

			plist = plist.sort(function(a,b){return parseFloat(a.distance) > parseFloat(b.distance)})

			for (let i = 0; i < plist.length; i++){
				// create a tr
				let $tr = $('<tr>')

				let $tdButton = $('<td>')

				if (!plist[i].attendee_id && parseInt(plist[i].host_id) != parseInt(userId)){
					let $button = $('<button>').text('Join').addClass('btn').addClass('btn-success');
					$button.attr("data-mid", plist[i].id)
					$button.attr("data-verb", "join")
					$tdButton.append($button);
				}

				if ( parseInt(plist[i].attendee_id) === parseInt(userId)){
					let $button = $('<button>').text('Leave').addClass('btn').addClass('btn-danger');
					$button.attr("data-mid", plist[i].id)
					$button.attr("data-verb", "leave")
					$tdButton.append($button);
				}

				if ( parseInt(plist[i].host_id) === parseInt(userId)){
					// let $button = $('<button>').text('Edit').addClass('btn').addClass('btn-primary');
					// $button.attr("data-mid", plist[i].id)
					// $button.attr("data-verb", "edit")
					// $tdButton.append($button);
					let $aLink = $('<a>').text('Edit)').addClass('btn').addClass('btn-primary');
					$aLink.attr('href',"/parties/" + plist[i].id + "/edit")
					$tdButton.append($aLink)
				}

				let $tdHost = $('<td>');
				let $hostImage = $('<img>').addClass("list-image");
				$hostImage.attr("src", plist[i].image);
				$tdHost.text(" "+ plist[i].name);
				$tdHost.prepend($hostImage);

				let $tdDistance = $('<td>').text((plist[i].distance || "") + " km");

				let $tdDescription = $('<td>').text(plist[i].description);

				let $tdCost = $('<td>').text("$" + plist[i].cost);

				let $tdLocation = $('<td>').text(plist[i].address);

				let $tdDate = $('<td>').text(plist[i].date);

				let $tdTime = $('<td>').text(plist[i].time);
				// create td's for each property and append them
				$tr.append($tdButton)
					.append($tdHost)
					.append($tdDistance)
					.append($tdDescription)
					.append($tdCost)
					.append($tdLocation)
					.append($tdDate)
					.append($tdTime);
				// append tr to tbody.
				$tbody.append($tr)
			}
			
		});
	});

	// Now that our even listeners are established, make something happen:
	$('#default-button').trigger('click');
})

// function showPosition(position) {
//     console.log("lat: ",position.coords.latitude);
//     console.log("lng: ",position.coords.longitude); 
//     return {lat: position.coords.latitude, lng: position.coords.longitude}
// }