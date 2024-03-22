import { useState } from 'react';
import { Box, Input, InputGroup, InputLeftElement, InputRightElement, Button } from '@chakra-ui/react'
//import './searchbar.css'
import { Search2Icon } from '@chakra-ui/icons'


export default function SearchBar({confirm, defaultValue}) {

  const [input, setInput] = useState(defaultValue);

  function handleKeyPress(e) {
    
     // This is perfectly safe in react, it correctly detect the keys
    if(e.key == 'Enter'){
        confirm(input)
    }
  }

  function confirm_clicked(e) {
    confirm(input);
  }
  
  /*
  return (
    <div id="search-bar">
      <img id="search-icon" src="/search_icon.png" />
      <input id="search-input"
        value={input}
        placeholder='Type a location' 
        onChange={(value) => setInput(value)}
        onKeyDown={handleKeyPress}
      />
      <button id="search-button" onClick={confirm} />
    </div>
  );*/

  return (
    <InputGroup size='md'>
      <InputLeftElement pointerEvents='none'>
        <Search2Icon color='gray.300' />
      </InputLeftElement>
      <Input 
        value={input}
        pr='6.5rem'
        placeholder='Type a location' 
        _placeholder={{ 'font-style': 'italic' }}
        onChange={(event) => setInput(event.target.value)}
        onKeyDown={handleKeyPress}
        borderRadius='100'
        background='white'
    />
      <InputRightElement width='6.5rem'>
        <Button  
          onClick={confirm_clicked} 
          borderRadius='100'
          backgroundColor='#b30059'
          color='white'
          fontWeight='10'
        >SEARCH</Button>
      </InputRightElement>
    </InputGroup>
  );
}
