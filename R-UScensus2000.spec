%global packname  UScensus2000
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          US Census 2000 Suite of R Packages

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-maptools R-sp R-foreign R-methods R-grDevices R-base R-stats R-utils R-UScensus2000tract R-UScensus2000blkgrp R-UScensus2000cdp R-gpclib 


BuildRequires:    R-devel tex(latex) R-maptools R-sp R-foreign R-methods R-grDevices R-base R-stats R-utils R-UScensus2000tract R-UScensus2000blkgrp R-UScensus2000cdp R-gpclib



%description
US Census 2000 shape files and additional demographic data from the SF1
100 percent files. This package contains a number of helper functions for
the UScensus2000blk, UScensus2000blkgrp, UScensus2000tract,
UScensus2000cdp packages.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora