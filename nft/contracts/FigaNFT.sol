pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";


contract FigaNFT is ERC721 {
    uint256 public tokenCounter;
    enum Car{SPORT_CAR, HATCHBACK, SUV}
    // add other things
    mapping(uint256 => Car) public tokenIdToCar;
    event requestedCollectible(uint256 tokenId); 


    
    
    constructor()
    public 
    ERC721("FigaNFT", "FIGA")
    {
        tokenCounter = 0;
   
    }

    function createCollectible(string memory tokenURI, int256 carModel) 
        public returns (bytes32){
            uint256 newItemId = tokenCounter;
            _safeMint(msg.sender, newItemId);
            _setTokenURI(newItemId, tokenURI);
            Car car = Car(carModel);
            tokenIdToCar[newItemId] = car;
            tokenCounter = tokenCounter+1;
            emit requestedCollectible(newItemId);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
