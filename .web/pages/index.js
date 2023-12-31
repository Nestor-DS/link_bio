
/** @jsxImportSource @emotion/react */import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Avatar, Box, Button, Center, Flex, Heading, HStack, Image as ChakraImage, Link, Spacer, Text, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextLink from "next/link"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Box>
  <HStack sx={{"position": "sticky", "bg": "#171F26", "paddingX": "2em", "paddingY": "1em", "zIndex": "999", "top": 0}}>
  <Box sx={{"fontFamily": "Poppins", "fontWeight": "500", "fontSize": "16px"}}>
  <Text as={`span`} sx={{"color": "#14A1F0"}}>
  {`Hello`}
</Text>
  <Text as={`span`} sx={{"color": "#087ec4"}}>
  {`There!`}
</Text>
</Box>
</HStack>
  <Center>
  <VStack sx={{"maxWidth": "600px", "width": "100%", "marginY": "2em", "padding": "2em"}}>
  <VStack alignItems={`start`} spacing={`2em`}>
  <HStack spacing={`1em`} sx={{"color": "#F1F2F4"}}>
  <Avatar name={`Foto de gato`} size={`xl`} src={`image.jpeg`} sx={{"color": "#F1F2F4", "bg": "#0C151D", "padding": "2px", "border": "4px", "borderColor": "#14A1F0", "alt": "Foto de Nestor"}}/>
  <VStack alignItems={`start`}>
  <Heading sx={{"size": "lg", "color": "#F1F2F4", "fontFamily": "Poppins", "fontWeight": "500"}}>
  {`Hola, soy Nestor 👾`}
</Heading>
  <Text sx={{"marginTop": "0px !important"}}>
  {`Desarrollador de software en proceso`}
</Text>
  <HStack spacing={`1em`}>
  <Link as={NextLink} href={`https://github.com/Nestor-DS`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage alt={`Github icon`} src={`icons/github-alt.svg`} sx={{"width": "1.5em", "height": "1.5em"}}/>
</Link>
  <Link as={NextLink} href={`https://twitter.com/Nestor_DS`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage alt={`Email icon`} src={`icons/x-twitter.svg`} sx={{"width": "1.5em", "height": "1.5em"}}/>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/nestor-duhamel-sanchez`} isExternal={true} sx={{"textDecoration": "none", "_hover": {}}}>
  <ChakraImage alt={`Spotify icon`} src={`icons/linkedin.svg`} sx={{"width": "1.5em", "height": "1.5em"}}/>
</Link>
</HStack>
</VStack>
</HStack>
  <Flex sx={{"width": "100%"}}>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeight": "bold", "color": "#14A1F0"}}>
  {`+1`}
</Text>
  {` Años de experiencia`}
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeight": "bold", "color": "#14A1F0"}}>
  {`Python`}
</Text>
  {` Lenguaje favorito`}
</Box>
  <Spacer/>
  <Box sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  <Text as={`span`} sx={{"fontWeight": "bold", "color": "#14A1F0"}}>
  {`0s`}
</Text>
  {` Seguidores`}
</Box>
</Flex>
  <Text sx={{"fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Soy un desarrollador de software, mi lenguaje favorito es Python, 
            actualmente estoy aprendiendo Dart y me interesa aprender más sobre el mundo del desarrollo web y movil.`}
</Text>
</VStack>
  <VStack spacing={`1em`} sx={{"width": "100%"}}>
  <Heading size={`lg`} sx={{"width": "100%", "size": "lg", "paddingTop": "2em", "color": "#F1F2F4", "fontFamily": "Poppins", "fontWeight": "500"}}>
  {`Links`}
</Heading>
  <Link as={NextLink} href={`https://github.com/Nestor-DS`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "whiteSpace": "normal", "textAlign": "start", "backgroundColor": "#171F26", "textColor": "#F1F2F4", "_hover": {"backgroundColor": "#087ec4", "textColor": "#F1F2F4"}}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`GitHub`} src={`icons/github-alt.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Poppins", "fontWeight": "500", "color": "#F1F2F4"}}>
  {`GitHub`}
</Text>
  <Text sx={{"fontWeight": "300", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Te invito a ver mis proyectos`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.linkedin.com/in/nestor-duhamel-sanchez`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "whiteSpace": "normal", "textAlign": "start", "backgroundColor": "#171F26", "textColor": "#F1F2F4", "_hover": {"backgroundColor": "#087ec4", "textColor": "#F1F2F4"}}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Linkedin`} src={`icons/linkedin.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Poppins", "fontWeight": "500", "color": "#F1F2F4"}}>
  {`Linkedin`}
</Text>
  <Text sx={{"fontWeight": "300", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Perfil profesional`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`https://www.instagram.com/_sar_02_/`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "whiteSpace": "normal", "textAlign": "start", "backgroundColor": "#171F26", "textColor": "#F1F2F4", "_hover": {"backgroundColor": "#087ec4", "textColor": "#F1F2F4"}}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Instagram`} src={`icons/instagram.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Poppins", "fontWeight": "500", "color": "#F1F2F4"}}>
  {`Instagram`}
</Text>
  <Text sx={{"fontWeight": "300", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Un poco sobre mi`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`www.youtube.com/@nestor-d8326`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "whiteSpace": "normal", "textAlign": "start", "backgroundColor": "#171F26", "textColor": "#F1F2F4", "_hover": {"backgroundColor": "#087ec4", "textColor": "#F1F2F4"}}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Youtube`} src={`icons/youtube.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Poppins", "fontWeight": "500", "color": "#F1F2F4"}}>
  {`Youtube`}
</Text>
  <Text sx={{"fontWeight": "300", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`Videos de programación`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
  <Link as={NextLink} href={`mailto:nestorduhamel18@outlook.es`} isExternal={true} sx={{"width": "100%", "textDecoration": "none", "_hover": {}}}>
  <Button sx={{"width": "100%", "height": "100%", "padding": "0.5em", "borderRadius": "1em", "whiteSpace": "normal", "textAlign": "start", "backgroundColor": "#171F26", "textColor": "#F1F2F4", "_hover": {"backgroundColor": "#087ec4", "textColor": "#F1F2F4"}}}>
  <HStack sx={{"width": "100%"}}>
  <ChakraImage alt={`Email`} src={`icons/envelope-solid.svg`} sx={{"width": "1.5em", "height": "1.5em", "margin": "0.8em"}}/>
  <VStack alignItems={`start`} spacing={`0.5em`} sx={{"paddingY": "0.5em", "paddingRight": "0.5em"}}>
  <Text sx={{"fontSize": "1em", "fontFamily": "Poppins", "fontWeight": "500", "color": "#F1F2F4"}}>
  {`Email`}
</Text>
  <Text sx={{"fontWeight": "300", "fontSize": "0.8em", "color": "#C3C7CB"}}>
  {`nestorduhamel18@outlook.es`}
</Text>
</VStack>
</HStack>
</Button>
</Link>
</VStack>
</VStack>
</Center>
  <VStack sx={{"marginButtom": "2em", "color": "#A3ABB2", "paddingButtom": "2em", "paddingX": "2em"}}>
  <ChakraImage alt={`N's icon`} src={`favicon.ico`} sx={{"height": "4em", "borderRadius": "0.8em"}}/>
  <Link as={NextLink} href={`https://github.com/Nestor-DS`} isExternal={true} sx={{"fontSize": "0.8em", "textDecoration": "none", "_hover": {}}}>
  {`© 2023 - 2023 Nestor`}
</Link>
  <Text sx={{"fontSize": "0.8em", "marginTop": "0px !important"}}>
  {`Made with Reflex 🐍`}
</Text>
</VStack>
</Box>
  <NextHead>
  <title>
  {`Link-Bio`}
</title>
  <meta content={`Link Bio de Nestor`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
