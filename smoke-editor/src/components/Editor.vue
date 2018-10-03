<template>
  <div id = "editor">
    <div class="dropdown">
      <button @click = "myFunction()" class = "dropbtn">Dropdown</button>
      <div id='myDropdown' class="dropdown-content">
        <a href="#">testing</a>
        <a href="#">testing2</a>
        <a href="#">testing3</a>
      </div>
    </div>
  <div>
    <brace style="height: 500px"
      :fontsize="'12px'"
      :theme="'github'"
      :mode="'python'"
      :codefolding="'markbegin'"
      :softwrap="'free'"
      :selectionstyle="'text'"
      :highlightline="true">
    </brace>
  </div>
  </div>
</template>

// ************************************************************************
<style>
  /* Dropdown button */
  .dropbtn {
    background-color: #333;
    color: white;
    padding: 3px;
    font-size: 14px;
    border: none;
    cursor: pointer;
  }

  /* Dropdown button on hover & focus */
  .dropbtn:hover, .dropbtn:focus {
    background-color: #2980B9;
  }

  /* The container <div> - needed to position the dropdown content */
  .dropdown {
    position: relative;
    top: 0px;
    left: 40px;
    display: inline-block;
  }

  /* Dropdown Content (Hidden by Default) */
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
  }

  /* Links inside the dropdown */
  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }

  /* Change color of dropdown links on hover */
  .dropdown-content a:hover {background-color: #ddd}

  /* Show the dropdown menu (use JS to add this class to the .dropdown-content container when the user clicks on the dropdown button) */
  .show {display:block;}
</style>
// ****************************************************************
<script>
import Brace from 'vue-bulma-brace'

export default {
  components: {
    Brace
  },
  methods: {
    myFunction: function () {
      document.getElementById('myDropdown').classList.toggle('show')
    }
  }
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName('dropdown-content')
    var i
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i]
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show')
      }
    }
  }
}
</script>
