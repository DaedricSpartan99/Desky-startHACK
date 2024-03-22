import { Image, Text, Box, Button } from '@chakra-ui/react'

export default function Description() {
  return (
    <>
      <Image src='https://www.fucinead.it/wp-content/uploads/2021/05/office-design-idee-come-arredare-ufficio-studio-architettura-interior-design-roma1.jpg' alt='Ufficio' />

      <Box p='5' pb='2'>
        <Text fontSize='3xl'> Casamia bureau </Text>
      </Box>

      <Box >
        <Text pl='8' fontSize='1xl'> Services </Text>
        <Box p='2'>
        </Box>
      </Box>

      <Box p='1'>
        <Button colorScheme='messenger'> Book </Button> 
      </Box>
    </>
  );
}
