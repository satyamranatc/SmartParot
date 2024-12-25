let SubjectContainer = document.getElementById("SubjectContainer");


let subjects = [
    {
        id: 1,
        name: "Math",
        poster:"abc.jpg",
        description: "Math is the study of numbers, shapes, and patterns.",

    },
    {
        id: 2,
        name: "Science",
        poster:"def.jpg",
        description: "Science is the natural science that involves the study of matter, its motion and behavior through space and time, and the related concepts of energy and force.",
    },{
        id: 3,
        name: "English",
        poster:"ghi.jpg",
        description: "English is a West Germanic language of the Indo-European family, with around 11,700 known varieties. It is a member of the Indo-European language family, as well as a member of the Germanic language family.",
    },
    {
        id: 4,
        name: "History",
        poster:"jkl.jpg",
        description: "History is the study of past events, civilizations, and social changes.",
    },
    {
        id: 5,
        name: "Geography",
        poster:"mno.jpg",
        description: "Geography is the study of the Earth's land, sea, atmosphere, and natural features.",
    }

]


function DisplayData(data)
{
    SubjectContainer.innerHTML = "";
    data.forEach(element => {
        
        SubjectContainer.innerHTML += `
        
             <div class="SubjectCard">
                <img src="${element.poster}" class="SubjectPoster" alt="Subject">
                <h2>${element.name}</h2>
                <p>${element.description}</p>
                <a href="/FrontEnd/Feed/Topic/Topic.html" class="view-details">View Details</a>
            </div>
        `;

    });

}


DisplayData(subjects)