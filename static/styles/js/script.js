// // This is the JavaScrip for custom Audio player in Songs Page
// document.addEventListener("DOMContentLoaded", function () {
//     const audio = document.getElementById("custom-audio");
//     const progressSlider = document.getElementById("progress-slider");
//     const playButton = document.getElementById("play-button");
//     const pauseButton = document.getElementById("pause-button");
//     const stopButton = document.getElementById("stop-button");

//     playButton.addEventListener("click", () => {
//         audio.play();
//     });

//     pauseButton.addEventListener("click", () => {
//         audio.pause();
//     });

//     stopButton.addEventListener("click", () => {
//         audio.pause();
//         audio.currentTime = 0;
//     });

//     progressSlider.addEventListener("input", () => {
//         audio.currentTime = progressSlider.value;
//     });

//     audio.addEventListener("timeupdate", () => {
//         progressSlider.value = audio.currentTime;
//         progressSlider.max = audio.duration;
//     });
// });