let TopicContainer = document.getElementById("TopicContainer")

let TopicData = [
    {
        id: 1,
        name: "Mathematics",
        subject_id: 1,
        poster:"math.jpg",
        description: "Mathematics is the study of numbers, shapes, and patterns."
    },
    {
        id: 2,
        name: "Physics",
        subject_id: 2,
        poster:"physics.jpg",
        description: "Physics is the natural science that involves the study of matter, its motion and behavior through space and time, and the related concepts of energy and force."
    },
    {
        id: 3,
        name: "Chemistry",
        subject_id: 3,
        poster:"chemistry.jpg",
        description: "Chemistry is the science of chemical elements and compounds, including their composition, structure, properties, and reactions."
    },
]

function DisplayData(data)
{
    TopicContainer.innerHTML = "";
    data.forEach(element => {
        
        TopicContainer.innerHTML += `
        
             <div class="SubjectCard">

                <h2>🔢 ${element.name}</h2>
                <img src="${element.poster}" class="SubjectPoster" alt="Topic">
                <p>${element.description}</p>
                <div class="Btn">
                    <a href = "/FrontEnd/Feed/Chapters/Chapter.html" >View</a>
                    <button>Test</button>
                </div>
            </div>
        `;

    });

}


DisplayData(TopicData)