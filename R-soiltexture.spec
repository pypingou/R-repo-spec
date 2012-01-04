%global packname  soiltexture
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.6
Release:          1%{?dist}
Summary:          Functions for soil texture plot, classification and transformation

Group:            Applications/Engineering 
License:          AGPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-sp R-MASS 


BuildRequires:    R-devel tex(latex) R-sp R-MASS



%description
"The Soil Texture Wizard" is a set of R functions designed to produce
texture triangles (also called texture plots, texture diagrams, texture
ternary plots), classify and transform soil textures data. These functions
virtually allows to plot any soil texture triangle / classification into
any triangle geometry (isosceles, right-angled triangles, etc.). This set
of function is expected to be useful to people using soil textures data
from different soil texture classification or different particle size
systems. Several texture triangles are predefined: USDA; FAO (which is
also the triangle for the soil map of Europe); Aisne (France); GEPPA
(France); German triangles "Bodenkundliche Kartieranleitung 1994", "SEA
1974" and "TGL 1985"; Soil Survey of England and Wales; Australian
triangle; Belgian triangle; Canadian triangle; ISSS triangle; Romanian
triangle; Polish triangle.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/soiltexture/DESCRIPTION
%doc %{rlibdir}/soiltexture/doc
%doc %{rlibdir}/soiltexture/html
%{rlibdir}/soiltexture/polish_triangle_ANSI.r
%{rlibdir}/soiltexture/exec
%{rlibdir}/soiltexture/polish_language.r
%{rlibdir}/soiltexture/Meta
%{rlibdir}/soiltexture/INDEX
%{rlibdir}/soiltexture/NAMESPACE
%{rlibdir}/soiltexture/help
%{rlibdir}/soiltexture/R
%{rlibdir}/soiltexture/polish_language_ANSI.r
%{rlibdir}/soiltexture/polish_triangle.r

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.6-1
- initial package for Fedora