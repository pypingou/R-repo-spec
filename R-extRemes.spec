%global packname  extRemes
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.63
Release:          1%{?dist}
Summary:          Extreme value toolkit.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk R-ismev R-Lmoments 


BuildRequires:    R-devel tex(latex) R-tcltk R-ismev R-Lmoments



%description
Uses Stuart Coles' (Coles, Stewart, "An introduction to statistical
modeling of extreme values", Springer-Verlag, London 2001) S-plus
functions as ported to the R programming language (ismev) by Alec
Stephenson (http://www.maths.lancs.ac.uk/~stephena/).  This toolkit
provides a Graphical User Interface (GUI) to ismev for pedagogical

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.63-1
- initial package for Fedora