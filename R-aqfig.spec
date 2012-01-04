%global packname  aqfig
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Functions to help display air quality model output and monitoring data

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-geoR 


BuildRequires:    R-devel tex(latex) R-geoR



%description
This package contains functions to help display air quality model output
and monitoring data, such as creating color scatterplots, maps preserving
aspect ratio, and color legends.

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
%doc %{rlibdir}/aqfig/DESCRIPTION
%doc %{rlibdir}/aqfig/html
%{rlibdir}/aqfig/R
%{rlibdir}/aqfig/help
%{rlibdir}/aqfig/INDEX
%{rlibdir}/aqfig/data
%{rlibdir}/aqfig/Meta
%{rlibdir}/aqfig/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora