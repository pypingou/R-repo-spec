%global packname  UScensus2010
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.10
Release:          1%{?dist}
Summary:          US Census 2010 Suite of R Packages: Installers and helperfunctions for UScensus2010blk, UScensus2010blkgrp, UScensus2010tract, UScensus2010county, UScensus2010cdp packages.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-maptools R-sp R-foreign R-methods R-grDevices R-base R-stats R-utils 


BuildRequires:    R-devel tex(latex) R-maptools R-sp R-foreign R-methods R-grDevices R-base R-stats R-utils



%description
US Census 2010 shape files and additional demographic data from the SF1
100 percent files. This package contains a number of helper functions for
the UScensus2010blk, UScensus2010blkgrp, UScensus2010tract,
UScensus2010county, UScensus2010cdp packages.

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
%doc %{rlibdir}/UScensus2010/html
%doc %{rlibdir}/UScensus2010/DESCRIPTION
%doc %{rlibdir}/UScensus2010/CITATION
%{rlibdir}/UScensus2010/data
%{rlibdir}/UScensus2010/NAMESPACE
%{rlibdir}/UScensus2010/help
%{rlibdir}/UScensus2010/INDEX
%{rlibdir}/UScensus2010/R
%{rlibdir}/UScensus2010/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.10-1
- initial package for Fedora