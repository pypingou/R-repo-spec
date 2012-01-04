%global packname  gamesNws
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5
Release:          1%{?dist}
Summary:          Playing games using a NWS Server

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nws 

BuildRequires:    R-devel tex(latex) R-nws 

%description
This is a package with different card games (e.g. uno, poker, ...) and
using a NWS Server as card table. You can play the games with your friends
in the whole world. Just install a NWS Server at one machine, send the
login data to your friends and start the game.

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
%doc %{rlibdir}/gamesNws/DESCRIPTION
%doc %{rlibdir}/gamesNws/NEWS
%doc %{rlibdir}/gamesNws/html
%{rlibdir}/gamesNws/Meta
%{rlibdir}/gamesNws/INDEX
%{rlibdir}/gamesNws/R
%{rlibdir}/gamesNws/NAMESPACE
%{rlibdir}/gamesNws/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5-1
- initial package for Fedora