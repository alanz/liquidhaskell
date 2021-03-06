module spec GHC.Base where

import GHC.CString
import GHC.Prim
import GHC.Classes
import GHC.Types

embed GHC.Types.Int      as int
embed GHC.Types.Bool     as bool

measure autolen :: forall a. a -> GHC.Types.Int
class measure len :: forall f a. f a -> GHC.Types.Int
instance measure len :: forall a. [a] -> GHC.Types.Int
len []     = 0
len (y:ys) = 1 + len ys


// measure null :: [a] -> Bool
// null []     = true 
// null (y:ys) = false

measure fst :: (a,b) -> a
fst (a,b) = a

measure snd :: (a,b) -> b
snd (a,b) = b


qualif Fst(__v:a, __y:b): (__v = (fst __y))
qualif Snd(__v:a, __y:b): (__v = (snd __y))


invariant {v: [a] | len v >= 0 }
map       :: (a -> b) -> xs:[a] -> {v: [b] | len v == len xs}
(++)      :: xs:[a] -> ys:[a] -> {v:[a] | len v == len xs + len ys}

($)       :: (a -> b) -> a -> b
id        :: x:a -> {v:a | v = x}

data variance Text.ParserCombinators.ReadPrec.ReadPrec contravariant

