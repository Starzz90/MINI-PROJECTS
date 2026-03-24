document.addEventListener('DOMContentLoaded', () => {
        const songs = [
            {title: "One", artist: "A", src:"Kesdsoku.mp3"},
            {title: "Two", artist: "B", src:"frog.mp3"}
        ];

        const Player = document.getElementById('player');
        const playlist = document.getElementById('playlist');
        const Back = document.getElementById('Back');
        const playPause = document.getElementById('playPause');
        const Next = document.getElementById('Next');
        let currentSong = 0;

        function LoadSong(songIndex){
            currentSong = songIndex;
            const song = songs[currentSong];
            Player.src = song.src;
            Player.play();
        }

        function displayplaylist(){
            songs.forEach((_song, index) => {
                const li = document.createElement('li');
                li.textContent = `${_song.title} - ${_song.artist}`;
                li.addEventListener('click', ()=> LoadSong(index));
                playlist.appendChild(li);
            });
        }
        playPause.addEventListener('click', ()=> {
            if(Player.paused){
                Player.play();
                document.getElementById('playPause').textContent = "Pause"
            }else{
                Player.pause(); 
                document.getElementById('playPause').textContent = "Play"
            }
        });
        
        Next.addEventListener('click',() => {
            const NextIndex = (currentSong + 1)% songs.length;
            LoadSong(NextIndex);
        });

        Back.addEventListener('click', () => {
            const BackIndex = (currentSong - 1 + songs.length)% songs.length;
            LoadSong(BackIndex);
        });

        Player.addEventListener('ended',() =>{
            const nextIndex = (currentSong + 1)% songs.length;
            LoadSong(nextIndex);
        });

        displayplaylist();
        Player.src = songs[currentSong],src;
            
    });
     