%global packname  psyphy
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Functions for analyzing psychophysical data in R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-graphics 

BuildRequires:    R-devel tex(latex) R-stats R-graphics 

%description
An assortment of functions that could be useful in analyzing data from
pyschophysical experiments. It includes functions for calculating d' from
several different experimental designs, links for m-alternative
forced-choice (mafc) data to be used with the binomial family in glm (and
possibly other contexts) and self-Start functions for estimating gamma
values for CRT screen calibrations.

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
%doc %{rlibdir}/psyphy/NEWS
%doc %{rlibdir}/psyphy/html
%doc %{rlibdir}/psyphy/DESCRIPTION
%{rlibdir}/psyphy/NAMESPACE
%{rlibdir}/psyphy/R
%{rlibdir}/psyphy/INDEX
%{rlibdir}/psyphy/help
%{rlibdir}/psyphy/data
%{rlibdir}/psyphy/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora