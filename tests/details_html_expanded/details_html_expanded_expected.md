# Details Blocks HTML with open attribute

/// details | with a summary
    open: True
some more text with a summary
///

/// details
    open: True
Breaking News! The Earth is round. ;-)
///

<!--- since open is a boolean, with it present at all the details block is open! --->
/// details | Secret
    open: True
Well it isn't a secret anymore with this open...
///
