%global packname  RXMCDA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          RXMCDA

Group:            Applications/Engineering 
License:          CeCILL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-XML 

BuildRequires:    R-devel tex(latex) R-methods R-XML 

%description
The RXMCDA library for the R statistical software allows you to read many
XMCDA tags and transform them into R variables which are then usable in
your algorithms written in R. The library also allows to write certain R
variables into XML files according to the XMCDA standard.

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
%doc %{rlibdir}/RXMCDA/COPYING
%doc %{rlibdir}/RXMCDA/DESCRIPTION
%doc %{rlibdir}/RXMCDA/html
%{rlibdir}/RXMCDA/R
%{rlibdir}/RXMCDA/NAMESPACE
%{rlibdir}/RXMCDA/help
%{rlibdir}/RXMCDA/Meta
%{rlibdir}/RXMCDA/INDEX
%{rlibdir}/RXMCDA/extdata

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora