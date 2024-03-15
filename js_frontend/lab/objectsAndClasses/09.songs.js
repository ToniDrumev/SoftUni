function solve(array) {
    class Song {
        constructor(typeList, songName, time) {
            this.typeList = typeList;
            this.name = songName;
            this.time = time;
        }
    }

    let n = array.shift();
    let type = array.pop();
    let songs = [];

    for (const element of array) {
        let [typeList, name, time] = element.split('_');
        let song = new Song(typeList, name, time);
        
        songs.push(song);
    }

    if (type === 'all') {
        songs.forEach(song => console.log(song.name));
    } else {
        const filteredSongs = songs.filter(song => song.typeList === type);
        filteredSongs.forEach(song => console.log(song.name));
    }
}
